# T5 — How CODE formalizes prompts: validation for an OOP decomposition

Research date: 2026-08-23. All facts cite the source URL fetched. This document validates the "prompt template creator" ontology (Elements → Attributes → Options) against how programmatic systems already decompose prompts.

---

## 1. DSPy (dspy.ai): Signatures = WHAT, Modules = HOW

### 1.1 Signatures — the declarative I/O contract

Source: https://dspy.ai/getting-started/expanding-signatures/ and https://dspy.ai/diving-deeper/signatures-in-depth/

> A signature is "the declarative contract between your program and the language model: the input fields it accepts, the output fields it produces, and the instructions describing the task." (signatures-in-depth)

**Inline signature syntax** (expanding-signatures):
- `"question -> answer"`
- `"location, mood -> haiku"`
- `"location, mood, contains_pun: bool -> haiku"`
- Multiple fields comma-separated on either side of `->`.

**Field naming is load-bearing**: field names are read by the LM to infer meaning — "naming is the cheapest optimization in DSPy"; a field called `research_request` outperforms `request` with no other changes; `"a, b -> c"` leaves the model confused. (expanding-signatures)

**Type annotations**: `name: type` — `bool` flags, `list[str]`, Literal, Pydantic models, TypedDicts, dataclasses. Typed outputs let DSPy coerce LM responses into the requested format and "surface clear warnings when they can't." (expanding-signatures)

**Class-based signatures** (https://dspy.ai/getting-started/class-based-signatures/):
- The class **docstring becomes the task instructions** in the prompt ("Write a classical haiku given the provided inputs." appears in the system instructions sent to the LM).
- Fields are declared with `dspy.InputField()` / `dspy.OutputField()`; `desc=` adds clarifying context rendered into the prompt.

```python
class HaikuBot(dspy.Signature):
    """Write a classical haiku given the provided inputs."""
    location: str = dspy.InputField(desc="The setting of the poem")
    mood: str = dspy.InputField()
    haiku: str = dspy.OutputField()
```

- **Enumerable options via Literal**: `Season = Literal["spring", "summer", "autumn", "winter"]` constrains both callers and the LM to defined values, with type-mismatch warnings.
- Design guidance: don't restate obvious information in `desc`; choose field names carefully because "optimizers cannot adjust them later."

**Signature internals** (https://dspy.ai/diving-deeper/signatures-in-depth/):
- Signatures extend `pydantic.BaseModel`; each field is a `FieldInfo` object → type validation, JSON-schema generation, constraints (`gt`, `lt`, `min_length`, …).
- String and class forms both produce identical `Signature` subclasses (metaclass `SignatureMeta` parses the string form).
- Missing docstring → auto-generated instructions: "Given the fields X, produce the fields Y."
- **Field metadata attributes**: `desc` (description rendered into the prompt), `prefix` (custom label override; auto-inferred from attribute name if omitted), plus pydantic constraints. Declared as `dspy.InputField(desc="...", prefix="...", **pydantic_constraints)`. (Verified against API stub at https://dspy.ai/api/signatures/InputField/ — `InputField(**kwargs)` wraps `pydantic.Field(**move_kwargs(**kwargs, __dspy_field_type="input"))`.)
- **Programmatic manipulation methods** (all return new immutable classes): `with_instructions()`, `append_instructions()`, `with_updated_fields(name, type_, **metadata)`, `prepend/append/insert(name, field, type_)`, `delete(name)`.
- **Introspection**: `Signature.input_fields` / `output_fields` / `fields`, `.instructions`, `.signature` (string form), `.equals(other)`.
- **Optimizer-resistant design**: "Field names, descriptions, and prefixes are 'inert to optimizers' — only docstrings (instructions) get rewritten."
- **Persistence**: `dump_state()` / `load_state()` serialize instructions + field metadata.

### 1.2 Modules — the inference strategy (technique)

Source: https://dspy.ai/getting-started/changing-modules/ and https://dspy.ai/diving-deeper/built-in-module-variants/

> "Other modules define different strategies for executing a task, and trying them out is very simple." The same `HaikuBot` signature works identically with `Predict` and `ChainOfThought`; the latter **automatically adds a `reasoning` output field**. (changing-modules)

Built-in modules (changing-modules + built-in-module-variants):

| Module | Role | Key parameters |
|---|---|---|
| `Predict` | Single LM call, basic inference | signature |
| `ChainOfThought` | Adds reasoning before the answer (injects a `reasoning` output field) | signature |
| `ReAct` / `ReActV2` | Agent loop with tool use | `tools=` |
| `ProgramOfThought` | Generates & executes Python code | `signature, max_iters=3, interpreter_factory` |
| `CodeAct` | "ReAct plus a code sandbox" | `signature, tools, max_iters=5, interpreter_factory` |
| `RLM` | Experimental REPL agent, large-context exploration | `signature, max_iters=20, max_llm_calls=50, interpreter_factory, tools, sub_lm` |
| `MultiChainComparison` | Synthesizes comparison of pre-generated completions | `signature, M=3, temperature=0.7` |
| `BestOfN` | "Samples several, then pick or combine" via reward function | `module, N, reward_fn, threshold, fail_count` |
| `Refine` | Like BestOfN but "generates feedback between attempts" | `module, N, reward_fn, threshold, fail_count` |
| `majority` | "No-LM aggregator" returning most-common normalized value | `prediction_or_completions, normalize, field` |
| `Parallel` | "A runner, not a Module" — batch concurrency | `num_threads, max_errors, timeout, straggler_limit` |
| `Flex` | Optimizable module code | — |

### 1.3 Adapters — where each element LIVES in the rendered prompt

Source: https://dspy.ai/api/adapters/ChatAdapter/

The **ChatAdapter** renders a Signature into chat messages:
- **System message** = field descriptions (inputs & outputs with their purposes) + field structure (delimiter pattern) + task description (the signature's instructions).
- Fields are delimited with markers `[[ ## field_name ## ]]`; an arbitrary `[[ ## completed ## ]]` marker ends output fields.
- **User messages** = input field values in their markers (+ output-requirements reminder in multi-turn).
- **Assistant messages** = output field values in markers + completion marker.
- **Few-shot examples** are rendered as alternating user/assistant turns in the same marker format; conversation history is formatted sequentially before the current input.
- Fallback: on formatting failure it "will retry using JSONAdapter" (unless `use_json_adapter_fallback` disabled).

**OOP takeaway (DSPy):** Signature = class (typed interface). InputField/OutputField = attributes with metadata slots (`desc`, `prefix`, type, constraints). Instructions (docstring) = a class-level attribute that optimizers may rewrite. Module = strategy object (method choice) parameterized by the signature. Adapter = serializer deciding which API role each element lands in.

---

## 2. LangChain: PromptTemplate / ChatPromptTemplate

### 2.1 ChatPromptTemplate

Source: https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate

Constructed from `(role, template)` tuples:

```python
template = ChatPromptTemplate([
    ("system", "You are a helpful AI bot. Your name is {name}."),
    ("human", "Hello, how are you doing?"),
    ("ai", "I'm doing well, thanks!"),
    ("human", "{user_input}"),
])
```

**Supported role strings**: `system` (system instructions), `human`/`user`, `ai`/`assistant`, `placeholder` (substitutable message sequences via `MessagesPlaceholder`):

```python
template = ChatPromptTemplate([
    ("system", "You are a helpful AI bot."),
    ("placeholder", "{conversation}"),   # expands to a list of messages
])
```

**Key parameters** (reference page):

| Parameter | Purpose |
|---|---|
| `input_variables` | Required variable names |
| `optional_variables` | Auto-inferred optional placeholders |
| `partial_variables` | Pre-filled values reducing invocation requirements |
| `template_format` | Defaults to `'f-string'`; also `mustache`, `jinja2` |

**Methods**: `from_messages()` / `from_template()` (factories), `partial()` (pre-populate variables — partial application, exactly like currying), `invoke()` / `format_messages()` / `aformat_messages()` (render). Single-variable shorthand: `template.invoke("value")`.

### 2.2 Template formats

Source: https://docs.langchain.com/langsmith/prompt-template-format

- **f-string**: `{variable}`, single braces; no nesting, no expressions, no loops/conditionals.
- **mustache**: `{{variable}}`; "logic-less" but with structured control flow — nested access `{{user.profile.email}}`, loops `{{#items}}...{{/items}}`, conditionals via sections/inverted sections, index access `{{items.0}}`, comments `{{!-- --}}`.
- F-string converts to mustache losslessly; reverse fails for advanced features. (LangSmith supports these two; jinja2 exists in the OSS `template_format` enum per the ChatPromptTemplate reference.)
- LangSmith special thread variables for evaluators: `{{all_messages}}`, `{{human_ai_pairs}}`, `{{first_human_last_ai}}`.

### 2.3 Few-shot examples as first-class objects

Source: https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate

`FewShotChatMessagePromptTemplate` generates "a list of messages consisting of prefix message(s), example message(s), and suffix message(s)". Attributes: `examples` (fixed list) **or** `example_selector` (dynamic selection based on the input), plus `example_prompt` (the per-example template) and `input_variables`.

**Example selector taxonomy** (search: [reference.langchain.com SemanticSimilarityExampleSelector](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/SemanticSimilarityExampleSelector), [LangChain example selectors overview](https://pub.aimind.so/langchain-in-chains-6-example-selectors-310f47b4cdf3)):
1. `SemanticSimilarityExampleSelector` — greatest cosine similarity of embeddings with the input.
2. `MaxMarginalRelevanceExampleSelector` — similarity + diversity (MMR).
3. `LengthBasedExampleSelector` — fits examples to a length budget.
4. `NGramOverlapExampleSelector` — n-gram overlap with the input.

**OOP takeaway (LangChain):** the template is a class; `input_variables` are its typed-ish attributes; `partial()` is partial application (a method producing a subclass-like specialized instance); message roles are an enum attribute per message; Examples are a composed sub-object whose "selection strategy" is a pluggable strategy class — i.e., LangChain treats *example selection* as a technique/method, exactly parallel to DSPy treating *reasoning strategy* as a module.

---

## 3. API-level anatomy (as of Aug 2026)

### 3.1 OpenAI: roles + instruction hierarchy

Source: https://developers.openai.com/api/docs/guides/text (fetched 2026-08-23)

- Roles in the Responses API: **developer**, **user**, **assistant**.
  - "`developer` messages are instructions provided by the application developer, prioritized ahead of user messages."
  - "`user` messages are instructions provided by an end user, prioritized behind developer messages."
  - "Messages generated by the model have the `assistant` role."
- **Function analogy (verbatim)**: "`developer` messages provide the system's rules and business logic, like a function definition"; "`user` messages provide inputs and configuration to which the `developer` message instructions are applied, like arguments to a function." ← *OpenAI itself frames the prompt as code: developer = function definition, user = arguments.*
- `instructions` parameter (Responses API): high-level guidance on behavior, tone, goals, response examples; "will take priority over a prompt in the `input` parameter"; applies only to the current request (does not persist across `previous_response_id` chains); roughly equivalent to a developer-role message in the input array.

**Model Spec chain of command** — source: https://model-spec.openai.com/2025-09-12.html
Ordered authority levels: **Root → System → Developer → User → Guideline → (Assistant/tool = No Authority)**.
- Root: "Fundamental root rules that cannot be overridden by system messages, developers or users."
- System: "Rules set by OpenAI… cannot be overridden by developers or users."
- Developer: "Models should obey developer instructions unless overridden by root or system instructions."
- User: "Models should honor user requests unless they conflict with developer-, system-, or root-level instructions."
- Guideline: "Instructions that can be implicitly overridden."
- Assistant & tool messages: "No Authority" — their content cannot serve as instructions.

(Note: in OpenAI's Chat Completions the legacy `system` role is treated as the developer message for newer models; the current Responses guide documents developer/user/assistant as the working set.)

### 3.2 Anthropic: system parameter + structured outputs

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (the retired standalone "system prompts" page 301-redirects here; fetched 2026-08-23)

- **Role lives in the `system` parameter**: "Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference" — example: `system: "You are a helpful coding assistant specializing in Python."` with the task in the `user` message.
- **XML tags as element separators**: "Wrapping each type of content in its own tag (for example, `<instructions>`, `<context>`, `<input>`) reduces misinterpretation." Use consistent, descriptive tag names; nest when hierarchical (`<documents>` > `<document index="n">`).
- **Examples element**: 3–5 examples; make them Relevant / Diverse / Structured; "Wrap examples in `<example>` tags (multiple examples in `<examples>` tags)."
- **Ordering rule (long context)**: "Place your long documents and inputs near the top of your prompt, above your query, instructions, and examples… Queries at the end can improve response quality by up to 30 percent." Documents wrapped in `<document>` with `<document_content>` and `<source>` subtags. Ask for `<quotes>` extraction first for grounding.
- **Motivation attribute**: "Providing context or motivation behind your instructions… can help Claude better understand your goals" (the TTS/ellipses example).
- **Output control**: tell what to do, not what not to do; XML format indicators ("Write… in `<smoothly_flowing_prose_paragraphs>` tags"); match prompt style to desired output; sample `<avoid_excessive_markdown_and_bullet_points>` block.
- **Prefill deprecation**: "Starting with Claude 4.6 models…, prefilled responses… on the last assistant turn are no longer supported" — migrate to Structured Outputs, direct instructions, or user-turn continuations. (The prompt element "prefill" is now replaced by API-level constraints.)
- **Agentic prompt blocks documented as named XML sections**: `<default_to_action>`, `<do_not_act_before_instructions>`, `<use_parallel_tool_calls>`, `<investigate_before_answering>`, `<frontend_aesthetics>` — i.e., vendor-canonical named behavior modules injected into the system prompt.
- Manual CoT fallback: "Use structured tags like `<thinking>` and `<answer>` to cleanly separate reasoning from the final output"; self-check: "Before you finish, verify your answer against [test criteria]."

**Structured outputs** — source: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- Two capabilities: **JSON outputs** via `output_config.format` = `{type: "json_schema", schema: {...}}`, and **strict tool use** (`strict: true`) guaranteeing schema validation of tool inputs.
- Guaranteed compliance via **constrained decoding**: "Always valid… Type safe… No retries needed for schema violations." Grammar compiled on first use, cached 24h.
- Supported on claude-fable-5, claude-mythos-5, claude-opus-5, claude-opus-4-8/4-7/4-6, claude-sonnet-5/4-6/4-5, claude-haiku-4-5, etc.
- → The "Format" element has *migrated from prompt text into an API parameter* for strict cases; prompt-level format instructions remain for soft cases.

### 3.3 Where each element canonically lives (vendor guidance, Aug 2026)

| Element | OpenAI | Anthropic |
|---|---|---|
| Role/persona | `developer` message (or `instructions` param) | `system` parameter |
| Business rules / process | `developer` ("function definition") | `system` prompt, often named XML blocks |
| Task + inputs/data | `user` ("arguments to a function") | `user` turn; long docs at TOP of turn, query at end |
| Examples | `instructions` may include "response examples"; else developer msg | `<examples>` in system or user prompt |
| Output format (strict) | Responses API structured outputs / json_schema | `output_config.format` json_schema (constrained decoding) |
| Output format (soft) | developer message | prompt text + XML format indicators |
| Reasoning control | reasoning effort params | `thinking: adaptive` + `effort` param (prompt-level `<thinking>` tags only as fallback) |
| Prior turns / few-shot dialogues | alternating user/assistant messages | alternating user/assistant messages (prefill on last turn now banned on 4.6+) |
| Priority order | Root > System > Developer > User > Guideline; assistant/tool = no authority (Model Spec) | system parameter vs user turn (no formal published hierarchy levels beyond that) |

---

## 4. Anthropic Console prompt improver / generator — the emitted structure

### 4.1 Prompt improver

Sources: retired docs page (content recovered via search snippet of https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver — the live URL now 301s to the consolidated best-practices page) and the announcement https://claude.com/blog/prompt-improver.

**4-step process** (docs, verbatim from search extract):
1. **Example identification** — "locates and extracts examples from your prompt template"
2. **Initial draft** — "creates a structured template with clear sections and XML tags"
3. **Chain of thought refinement** — "adds and refines detailed reasoning instructions"
4. **Example enhancement** — "updates examples to demonstrate the new reasoning process"

**What the improved prompt contains** (docs, verbatim): "templates with detailed chain-of-thought instructions that guide Claude's reasoning process…, clear organization using XML tags to separate different components, standardized example formatting that demonstrates step-by-step reasoning from input to output, and strategic prefills that guide Claude's initial responses."

**Blog's five improvement methods** (https://claude.com/blog/prompt-improver, verbatim):
1. Chain-of-thought reasoning: "Adds a dedicated section for Claude to think through problems systematically before responding."
2. Example standardization: converts examples into consistent XML formatting.
3. Example enrichment: "Augments existing examples with chain-of-thought reasoning that aligns with the newly structured prompt."
4. Rewriting: "Rewrites the prompt to clarify structure and correct any minor grammatical or spelling issues."
5. Prefill addition: "Prefills the Assistant message to direct Claude's actions and enforce output formats."

Reported results: +30% accuracy on a multilabel classification test; 100% word-count adherence on a summarization task. Examples are managed as structured input/output pairs; Claude can generate synthetic examples.

**Implication for the ontology**: Anthropic's own tooling decomposes any prompt into {structured sections in XML tags, CoT/reasoning section, standardized `<example>` blocks with embedded reasoning, prefill/format enforcement, template variables} — a direct machine-produced instance of Elements-with-Attributes.

### 4.2 Prompt generator

The standalone generator docs page (formerly `/prompt-generator`, "guided by a metaprompt" with a companion Google Colab notebook) also now redirects to the consolidated best-practices page; **could not retrieve the archived page** (web.archive.org blocked in this environment; mintlify mirror 404). What is retrievable: the generator produced a best-practice prompt template from a task description, with `{{VARIABLE}}` placeholders, and the underlying metaprompt was published as a Colab/cookbook notebook. Treat the section list above (improver) as the authoritative recovered output shape.

**Gap noted**: exact verbatim text of the retired prompt-generator docs page and the metaprompt notebook was not retrieved; the Anthropic interactive tutorial's "complex prompt from scratch" 10-element ordering (task context, tone, background data, rules, examples, history, immediate task, step-by-step thinking, output formatting, prefill) is in `anthropics/courses` notebook 09 but the notebook content could not be extracted via GitHub HTML fetch in this session.

---

## 5. Agentic "class definitions" in the wild

### 5.1 Claude Skills — SKILL.md schema

Sources: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview , https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices , https://code.claude.com/docs/en/skills

**Portable (Agent Skills spec, agentskills.io) frontmatter fields** — the only fields accepted by claude.ai uploads, the Skills API, and `package_skill.py` (code.claude.com/docs/en/skills): `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Including any other field "fails with a hard error": *"Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name."*

**Validation rules** (overview + best-practices):
- `name`: required (platform docs), ≤64 chars, lowercase letters/numbers/hyphens only, no XML tags, no reserved words "anthropic"/"claude".
- `description`: required, non-empty, ≤1,024 chars, no XML tags, "must include both what the Skill does and when Claude should use it"; **written in third person** ("The description is injected into the system prompt").

**Claude Code full frontmatter field table** (code.claude.com/docs/en/skills, all optional; verbatim summaries):

| Field | Purpose |
|---|---|
| `name` | Display name; defaults to directory name (plugin skills: last command segment) |
| `description` | What + when; if omitted uses first paragraph of body; description + when_to_use truncated at 1,536 chars in listing |
| `when_to_use` | Extra triggering context appended to description |
| `argument-hint` | Autocomplete hint, e.g. `[issue-number]` |
| `arguments` | Named positional args for `$name` substitution |
| `disable-model-invocation` | `true` = only human can invoke (side-effect workflows: /commit, /deploy) |
| `user-invocable` | `false` = only Claude invokes (background knowledge) |
| `allowed-tools` | Pre-approved tools for the invoking turn |
| `disallowed-tools` | Tools removed while skill active |
| `model` | Model override while active |
| `effort` | Effort-level override (`low`–`max`) |
| `context` | `fork` = run in subagent |
| `agent` | Subagent type when forked |
| `background` | Wait vs background for forked run |
| `hooks` | Hooks registered on invocation |
| `paths` | Glob patterns gating auto-activation |
| `shell` | `bash`/`powershell` for inline `!` commands |
| `metadata` | Free-form YAML map for own tooling |
| `license` | Spec field, not acted on |
| `compatibility` | Env requirements, ≤500 chars, spec field |

String substitutions in the body: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N`, `$name`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`.

**Body conventions & progressive disclosure** (overview):
- Canonical body skeleton: `# Skill Name` → `## Instructions` ("Clear, step-by-step guidance") → `## Examples` ("Concrete examples").
- **Level 1 Metadata** — always loaded, ~100 tokens/skill (name + description in system prompt).
- **Level 2 Instructions** — SKILL.md body, loaded on trigger, "Under 5k tokens" (best practices: body <500 lines).
- **Level 3+ Resources** — bundled files/scripts, "None until accessed"; scripts run through bash so only output enters context.
- Best-practice body patterns (best-practices page): high-level guide with references (one level deep only), domain-split reference dirs, conditional details, **workflow checklists** ("Copy this checklist and track your progress"), **feedback/validation loops** ("Run validator → fix errors → repeat"), template pattern (strict "ALWAYS use this exact template" vs flexible "sensible default"), examples pattern (input/output pairs), conditional workflow pattern (decision points), **degrees of freedom** (high = text heuristics / medium = pseudocode with params / low = "Run exactly this script… Do not modify"), no time-sensitive info, consistent terminology, MCP tools referenced as `ServerName:tool_name`.

### 5.2 AGENTS.md

Source: https://agents.md/

- "A **README for agents**: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project." 60k+ open-source projects use it.
- **No required fields — "just standard Markdown"; any headings work.** Popular section categories: **Project overview; Setup commands; Build and test commands; Code style guidelines; Testing instructions; PR/commit guidelines; Security considerations.**
- Example content: setup (`pnpm install`, `pnpm dev`, `pnpm test`) and style rules ("TypeScript strict mode; single quotes, no semicolons; use functional patterns where possible").
- **Precedence**: nested AGENTS.md files in monorepos; "agents automatically read the nearest file in the directory tree"; closest file wins; "explicit user prompts override all." (OpenAI's own repo has 88 nested AGENTS.md files.)
- Agents "attempt to run listed commands and fix failures" — checks are executable, not descriptive.
- Supported by Codex, Jules, Factory, Aider, goose, VS Code, Cursor, Zed, Copilot coding agent, Devin, Windsurf, Junie, and ~20+ others.

---

## 6. KEY QUESTION — the cross-system OOP mapping

**Verdict:** every system studied independently converges on the same three-way split the ontology proposes: a typed interface (CLASS) whose slots are configurable metadata (ATTRIBUTES), with reasoning/selection strategies factored out as pluggable operations (METHODS/techniques), and a serialization layer that decides which API role each element lands in.

### 6.1 What each system treats as class / attribute / method

| System | CLASS / type | ATTRIBUTE / field | METHOD / operation (technique) |
|---|---|---|---|
| **DSPy** | `Signature` (pydantic BaseModel subclass); custom `dspy.Type`s | `InputField`/`OutputField` with slots `desc`, `prefix`, type annotation, pydantic constraints; `instructions` (docstring) as class-level attribute | `Module` strategies: Predict, ChainOfThought, ReAct, ProgramOfThought, CodeAct, BestOfN, Refine, MultiChainComparison, majority; signature manipulation methods (`with_instructions`, `append`, `delete`); `Adapter.format()` |
| **LangChain** | `PromptTemplate` / `ChatPromptTemplate` / `FewShotChatMessagePromptTemplate` classes | `input_variables`, `optional_variables`, `partial_variables`, `template_format`, per-message `role`, `examples`, `example_prompt` | `partial()` (specialization), `invoke()/format_messages()` (render), `ExampleSelector.select_examples()` — 4 pluggable selection strategies |
| **OpenAI API** | Message (typed by `role` enum: developer/user/assistant); Response request object | `role`, `content`, `instructions` param; authority level per role (Model Spec) | The chain-of-command resolution itself; reasoning-effort params; structured-output enforcement |
| **Anthropic API** | Request with `system` + `messages`; named XML blocks as reusable pseudo-classes (`<default_to_action>`, `<use_parallel_tool_calls>`…) | `system` string, XML-tagged sections (`<instructions>`, `<context>`, `<examples>`, `<document index>` with `<source>`/`<document_content>` subtags), `output_config.format` json_schema | `thinking: adaptive` + `effort`; constrained decoding; prompt improver's 4 transformation steps (example identification → structured draft → CoT refinement → example enhancement) |
| **SKILL.md** | The skill directory + SKILL.md (a literal class file: interface in frontmatter, implementation in body, private helpers in `scripts/`) | Frontmatter fields: name, description, when_to_use, allowed-tools, model, effort, context, paths, … (typed, validated, hard error on unknown keys) | Body workflows/checklists, validation feedback loops, utility scripts (executed not read); progressive disclosure = lazy loading |
| **AGENTS.md** | The file itself as an environment/base-class contract (nearest-wins inheritance) | Conventional sections: overview, setup, build/test, code style, testing, PR rules, security | Executable commands agents run and iterate on ("run listed commands and fix failures") |

### 6.2 Ontology elements → how each system models the same concept

| Our candidate element/attribute | DSPy | LangChain | OpenAI API | Anthropic | SKILL.md / AGENTS.md |
|---|---|---|---|---|---|
| **Role/persona** | (folded into instructions docstring) | `("system", ...)` message | developer message / `instructions` | `system` parameter — "even a single sentence makes a difference" | skill `description` third-person identity; AGENTS.md project overview |
| **Task** | signature `instructions` (docstring; auto-generated fallback) | human message template | user message ("arguments to a function") | user turn, query at END after long data | body `## Instructions`; `$ARGUMENTS` parameterizes it |
| **Inputs / variables** | `InputField` (name, type, desc, prefix) | `{var}` / `{{var}}` + input_variables/partials | user content | `{{VARIABLE}}` in Console templates; `<input>`/`<document>` tags | `$ARGUMENTS`, `$name`, `${CLAUDE_*}` substitutions |
| **Context/background** | additional InputFields (e.g. `History`) | MessagesPlaceholder / extra messages | developer or user content | `<context>` / `<documents>` at top of turn | Level-3 reference files, loaded lazily; AGENTS.md itself |
| **Output spec / Format** | `OutputField` + type annotation (Literal = enumerated options!) | output parsers (separate layer) | structured outputs | `output_config.format` json_schema; XML format-indicator tags; template pattern (strict vs flexible) | template pattern in body |
| **Examples** | rendered by adapter as alternating user/assistant turns | `FewShotChatMessagePromptTemplate` + selector strategy | example turns / instructions | `<examples>`→`<example>` tags, 3–5, relevant/diverse/structured; improver standardizes + enriches them | Examples pattern (input/output pairs) |
| **Reasoning directive (CoT)** | `ChainOfThought` module — injects `reasoning` field; NOT part of signature | not modeled (user writes it) | reasoning effort param | adaptive thinking + effort; `<thinking>` tags as fallback; improver step 3 | workflow checklists play this role |
| **Tools/environment** | `ReAct(tools=…)`, `CodeAct` | tool-binding layer | tools param | tools param + `<use_parallel_tool_calls>` etc. | `allowed-tools`/`disallowed-tools`; AGENTS.md setup/build commands |
| **Checks/verification** | `BestOfN`/`Refine` reward_fn; assertions | — | — | "verify your answer against [test criteria]"; plan-validate-execute | validation feedback loops + validator scripts; AGENTS.md test commands |
| **Precedence/hierarchy** | system msg (adapter) vs user msg | message order | Root>System>Developer>User>Guideline; assistant/tool = no authority | system vs user turns | nearest AGENTS.md wins; user prompt overrides file |
| **Trigger/when-to-use** | — | — | — | — | `description` "when to use", `when_to_use`, `paths` globs — a dedicated attribute class our ontology should include |

### 6.3 Three load-bearing design lessons for the taxonomy

1. **WHAT/HOW separation is universal and should be structural**: DSPy proves the same signature runs under Predict/CoT/ReAct unchanged; LangChain proves the same example set runs under 4 selection strategies; Anthropic moved format enforcement (prefill→structured outputs) and reasoning (CoT text→thinking/effort params) *out of prompt text into API config*. → In the ontology, techniques (CoT, self-check, best-of-N, example-selection) must be modeled as METHODS applied to elements, not as elements themselves — and each should carry a "realization" option: {prompt-text | API-parameter | harness-scaffold}.
2. **Attributes carry enumerable options natively**: DSPy `Literal["spring","summer",...]`, structured-output JSON-schema `enum`s, skill frontmatter's closed vocabularies (`context: fork`, effort levels, boolean forms) all validate the Element→Attribute→Options shape, including hard validation errors on out-of-vocabulary values (SKILL.md's "Unexpected key(s)" error).
3. **Placement (which role/section an element renders into) is an attribute of the element, decided by a serializer**: DSPy Adapters, LangChain role tuples, and the OpenAI/Anthropic vendor tables (§3.3) all treat "lives in system vs user vs assistant vs API-param" as configurable metadata — the ontology needs a `placement` attribute on every element with options {system/developer, user-turn-top, user-turn-end, assistant-history, api-parameter, lazy-file}.

---

## Retrieval gaps
- Retired standalone Anthropic docs pages (`/prompt-improver`, `/prompt-generator`, `/system-prompts`) all 301 to the consolidated best-practices page; improver content recovered via search snippet of the old docs + the claude.com/blog/prompt-improver post. The prompt-generator metaprompt notebook text was NOT retrieved (web.archive.org blocked; mintlify mirror 404).
- `anthropics/courses` notebook 09 (10-element complex-prompt anatomy) not extractable via GitHub HTML fetch this session.
- DSPy InputField full kwargs list only via signatures-in-depth prose (`desc`, `prefix`, pydantic constraints); the API page shows only the wrapper stub.
- LangSmith template-format page documents f-string/mustache only; jinja2 confirmed only in the OSS ChatPromptTemplate reference.
