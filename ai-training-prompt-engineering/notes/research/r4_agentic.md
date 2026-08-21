# R4 — Agentic AI: Concepts, and How Prompting an Agent Differs from Prompting a Chatbot

Research notes for corporate AI training (medical-device supplier/quality engineers + business professionals).
Compiled 2026-08-21. Every fact carries an inline source URL and an "as of" date where currency matters.
Verification status: facts fetched directly from primary sources are stated plainly; anything not confirmed against a primary source is flagged **UNVERIFIED** or "reported by".

---

## PART A — Definitions & Building Blocks

### A1. The three canonical vendor definitions

**Anthropic — "Building Effective Agents" (published Dec 19, 2024; still the reference Anthropic cites as of Aug 2026):**
- Distinguishes two kinds of "agentic systems":
  - **Workflows**: "systems where LLMs and tools are orchestrated through predefined code paths" (source: https://www.anthropic.com/engineering/building-effective-agents)
  - **Agents**: "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks" (source: https://www.anthropic.com/engineering/building-effective-agents)
- Core advice: start simple — "often optimizing single LLM calls suffices without adding agentic complexity". Workflows suit well-defined, predictable tasks; agents suit open-ended problems where you can't hard-code the number of steps (source: https://www.anthropic.com/engineering/building-effective-agents).
- Five named workflow patterns: prompt chaining, routing, parallelization (sectioning/voting), orchestrator-workers, evaluator-optimizer (source: https://www.anthropic.com/engineering/building-effective-agents).

**OpenAI — "A Practical Guide to Building Agents" (PDF; widely reported as published April 2025 — the PDF itself carries no date, so the exact date is UNVERIFIED from the document):**
- One-line definition: "**Agents are systems that independently accomplish tasks on your behalf.**" Applications that merely integrate LLMs without letting them control workflow execution — "simple chatbots, single-turn LLMs, or sentiment classifiers — are not agents" (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- An agent has three core components: **Model** (reasoning/decision-making), **Tools** (external functions/APIs to act), **Instructions** ("explicit guidelines and guardrails defining how the agent behaves") (source: same PDF).
- When to build one: prioritize workflows involving (1) complex decision-making / nuanced judgment, (2) difficult-to-maintain rule sets, (3) heavy reliance on unstructured data. "Otherwise, a deterministic solution may suffice." (source: same PDF).
- Recommends maximizing a **single agent with tools first**, splitting into multi-agent (manager pattern = agents-as-tools; decentralized = handoffs) only when instructions get too complex or tools overlap (source: same PDF).

**Google:**
- Google Cloud definition: an AI agent is an application that achieves a goal by "processing input, performing reasoning with available tools, and taking actions based on its decisions"; core capabilities are reasoning/planning, acting via tools (APIs, databases, calendars), and autonomy (source: https://cloud.google.com/discover/what-are-ai-agents, as of Aug 2026).
- Google "Agents" whitepaper (Wiesinger, Marlow, Vuskovic, Sept/Nov 2024): "A Generative AI Agent can be defined as an application that attempts to achieve a goal by observing the world and acting upon it using tools that it has at its disposal." Cognitive architecture = Model + Tools + Orchestration layer (source: https://ia800601.us.archive.org/15/items/google-ai-agents-whitepaper/Newwhitepaper_Agents.pdf; summarized at https://cloud.google.com/discover/what-are-ai-agents). Google's docs cite **ReAct** (reason + act interleaved) as a common orchestration pattern (source: https://cloud.google.com/discover/what-are-ai-agents).

**Convergent teachable definition:** all three vendors agree an agent = LLM + tools + instructions, run in a loop, with the *model* (not fixed code) deciding what to do next until a goal or stop condition is reached.

### A2. The agent loop (plan → act via tools → observe → adjust)

- Anthropic's Claude Agent SDK post (Sep 29, 2025) states the loop as: "**gather context → take action → verify work → repeat**" (source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk).
- OpenAI: every orchestration needs "the concept of a 'run', typically implemented as a loop that lets agents operate until an exit condition is reached. Common exit conditions include tool calls, a certain structured output, errors, or reaching a maximum number of turns." (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- Anthropic computer-use docs define the agent loop concretely: Claude requests an action → your application executes it and returns the result (e.g., a screenshot) → Claude evaluates and requests the next action; "The repetition of steps 3 and 4 without user input is referred to as the 'agent loop'" (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool, as of Aug 2026).
- **Analogy** (defensible): the loop is the same OODA-style cycle a human troubleshooter runs — look at the situation, do one step, check what happened, adjust. Technically accurate at teaching altitude; the "plan" step is implicit model reasoning rather than a discrete module in most implementations.

### A3. Tool use / function calling

- Tools are how agents act: "external functions or APIs the agent can use to take action" (OpenAI, source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf). The model doesn't execute anything itself — it emits a structured request (`tool_use` block / function call); *your* application executes it and returns the result (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).
- Anthropic urges treating the tool interface ("agent-computer interface") with the same care as a human UI: clear docs with examples and edge cases, formats close to natural text, and "poka-yoke" the tools so mistakes are hard to make (source: https://www.anthropic.com/engineering/building-effective-agents). (Poka-yoke — mistake-proofing — will land well with quality engineers; the term is used verbatim by Anthropic.)

### A4. MCP — Model Context Protocol (status as of Aug 2026)

- MCP = an open standard for connecting AI applications to tools and data; commonly described as "the USB-C of AI" — one connector standard instead of an N×M mess of custom integrations (analogy used by MCP's own docs and press; technically defensible as a standardization analogy) (source: https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/).
- **Governance:** On **Dec 9, 2025**, Anthropic donated MCP to the newly formed **Agentic AI Foundation (AAIF)**, a directed fund under the **Linux Foundation**, co-founded by Anthropic, Block, and OpenAI with support from Google, Microsoft, AWS, Cloudflare, and Bloomberg. AAIF also hosts **goose** and **AGENTS.md** (sources: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation ; https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ ; https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation).
- **Adoption (as of Dec 2025, per the MCP project):** "over 97 million monthly SDK downloads, 10,000 active servers and first-class client support across major AI platforms" including ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot, VS Code (source: https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/).
- **Adoption (as of Jul 2026, per the MCP project):** "close to half-a-billion downloads a month" across Tier-1 SDKs; TypeScript and Python SDKs each crossed **1 billion total downloads** (source: https://blog.modelcontextprotocol.io/posts/2026-07-28/).
- **Spec currency:** the **2026-07-28 specification** is the largest revision since launch — stateless request/response core, multi-round-trip requests, header-based routing, cacheable list results, authorization hardening (source: https://blog.modelcontextprotocol.io/posts/2026-07-28/). Use this in training as evidence the field moves fast: cite "as of Aug 2026".

### A5. Memory: context window = short-term, files/notes = long-term

- Anthropic "Effective context engineering for AI agents" (Sep 29, 2025): context is a **finite resource** — models suffer "context rot" as the window fills, so agents need an "attention budget" mindset (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Long-horizon techniques named there: **compaction** (summarize history), **structured note-taking** — "agents maintain external memory files like NOTES.md or to-do lists, retrieving them as needed" — and **sub-agent architectures** that condense findings to 1,000–2,000 tokens for a coordinator (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Anthropic also ships a **memory tool** that stores information in files outside the context window (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool).
- Claude Code docs (as of Aug 2026): "Claude's context window fills up fast, and performance degrades as it fills... The context window is the most important resource to manage." (source: https://code.claude.com/docs/en/best-practices).
- Long-running agents post (Nov 26, 2025): "Each new session begins with no memory of what came before" — hence progress files, JSON state, and git history as durable memory (source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
- **Analogy** (defensible and vendor-aligned): context window = the agent's short-term/working memory (RAM, or what fits on its desk right now); files, notes, and git = long-term memory (the filing cabinet/lab notebook). Anthropic's own materials describe note files as "external memory," so the analogy is technically defensible; caveat for the class: nothing is "remembered" between sessions unless it is written down.

### A6. Subagents / orchestration

- Anthropic patterns: orchestrator-workers (a central LLM delegates dynamically) (source: https://www.anthropic.com/engineering/building-effective-agents); OpenAI patterns: manager (agents-as-tools) vs decentralized handoffs (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- Practical rationale is mostly **context isolation**: "Subagents run in separate context windows and report back summaries," keeping the main conversation clean; also useful for fresh-context adversarial review ("the agent doing the work isn't the one grading it") (source: https://code.claude.com/docs/en/best-practices).
- Claude docs warn about overuse: recent models "may spawn [subagents] in situations where a simpler, direct approach would suffice" — prompt guidance: use subagents for parallel/isolated/independent workstreams, work directly for simple sequential tasks (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices, as of Aug 2026).

### A7. Computer use & browser use

- **Computer use** (as of Aug 2026): generally available on the Claude API as the `computer_toolset_20260801` toolset (no beta header) for current models; 17 actions (screenshot, zoom, clicks, drag, scroll, type, key, wait). The agent sees screenshots and drives mouse/keyboard in a loop (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).
- Safety guidance in the same doc: run in an isolated VM/container with minimal privileges, avoid giving credentials, allowlist domains, and "require human confirmation for consequential actions"; Anthropic runs automatic prompt-injection classifiers on screenshots that steer the model to ask for user confirmation when an injection is suspected (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).
- **Browser use:** Claude for Chrome launched as a 1,000-user research preview Aug 2025, expanded to all Max users (Nov 24, 2025) and then Pro/Team/Enterprise (Dec 18, 2025) (source: https://claude.com/blog/claude-for-chrome). Red-teaming numbers in Part D.

---

## PART B — Agentic Prompting Best Practices (the heart)

### B1. Key primary sources (all Anthropic engineering unless noted)

| Source | Date | URL |
|---|---|---|
| Building Effective Agents | Dec 19, 2024 | https://www.anthropic.com/engineering/building-effective-agents |
| Claude Code Best Practices (now docs page) | live doc, as of Aug 2026 | https://code.claude.com/docs/en/best-practices |
| Writing Effective Tools for AI Agents | Sep 11, 2025 | https://www.anthropic.com/engineering/writing-tools-for-agents |
| Effective Context Engineering for AI Agents | Sep 29, 2025 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Building Agents with the Claude Agent SDK | Sep 29, 2025 | https://claude.com/blog/building-agents-with-the-claude-agent-sdk |
| Effective Harnesses for Long-Running Agents | Nov 26, 2025 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| Claude Prompting Best Practices ("Agentic systems" section) | live doc, as of Aug 2026 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| OpenAI GPT-5 Prompting Guide (agentic eagerness, stop conditions) | 2025, live | https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide |
| OpenAI Practical Guide to Building Agents | 2025 | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf |

### B2. CLAUDE.md / AGENTS.md convention

- **CLAUDE.md**: "a special file that Claude reads at the start of every conversation... persistent context it can't infer from code alone." Include/exclude table from the docs (as of Aug 2026):
  - ✅ Include: Bash commands Claude can't guess; code style rules that differ from defaults; testing instructions and preferred test runners; repository etiquette (branch naming, PR conventions); architectural decisions specific to the project; developer environment quirks (required env vars); common gotchas or non-obvious behaviors.
  - ❌ Exclude: anything Claude can figure out by reading code; standard conventions; detailed API docs; frequently-changing info; long tutorials; file-by-file codebase descriptions; "self-evident practices like 'write clean code'".
  - Keep it short: "For each line, ask: 'Would removing this cause Claude to make mistakes?' If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" Emphasize sparingly ("IMPORTANT" on one line, not many). Check it into git; treat it like code — prune and test. (source: https://code.claude.com/docs/en/best-practices)
- **AGENTS.md**: the cross-vendor equivalent — "a standardized markdown format that serves as dedicated guidance for AI coding agents," complementing README. Used by **over 60,000 open-source projects** (per agents.md, as of Aug 2026); created across the ecosystem (OpenAI Codex, Amp, Google Jules, Cursor, Factory) and now **stewarded by the Agentic AI Foundation under the Linux Foundation** (since Dec 2025). Recommended contents: "project overview, build and test commands, code style guidelines, testing instructions, security considerations," plus commit/PR conventions and deployment steps (sources: https://agents.md/ ; https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation).
- **Analogy** (defensible): CLAUDE.md/AGENTS.md is the onboarding packet you'd hand a new contractor on day one — the tribal knowledge that isn't written anywhere else. Aligned with Anthropic's advice to write tool descriptions "as though explaining to a new team member" (source: https://www.anthropic.com/engineering/writing-tools-for-agents).

### B3. Mission-spec elements for delegating work to an agent — each element with its source

This is the checklist the training should teach. Every element below is recommended by at least one primary source.

1. **Goal & definition of done (verifiable success criteria).**
   - "Give Claude a check it can run: tests, a build, a screenshot to compare... Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available." Provide explicit verification criteria in the prompt (before/after examples given) (source: https://code.claude.com/docs/en/best-practices).
   - "The most useful specs are self-contained: they name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step that proves the feature works." (source: https://code.claude.com/docs/en/best-practices)
   - OpenAI: define exit conditions for the run loop (final output, no more tool calls, error, max turns) (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).

2. **Environment & file boundaries (read-only inputs vs outputs).**
   - Claude docs' sample restart prompt: "**Call pwd; you can only read and write files in this directory.**" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
   - Enforced version: sandboxing = "filesystem isolation to ensure the agent can only access or modify specific directories, and network isolation to ensure the agent can only connect to approved servers" (sources: https://code.claude.com/docs/en/sandboxing ; https://anthropic.com/engineering/claude-code-sandboxing).
   - NCSC: "limit scope by constraining what an agent can access and what actions it can take" (source: https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai).

3. **Allowed / forbidden tools (least privilege).**
   - Claude Code: `--allowedTools` "restricts what Claude can do, which matters when you're running unattended"; permission allowlists via `/permissions`; per-subagent `tools:` lists (source: https://code.claude.com/docs/en/best-practices).
   - OpenAI: assign each tool a **risk rating** (low/medium/high) "based on factors like read-only vs. write access, reversibility, required account permissions, and financial impact," and use ratings to "trigger automated actions, such as pausing for guardrail checks before executing high-risk functions or escalating to a human" (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
   - NCSC: least privilege — minimum access for the shortest time, short-lived credentials (source: https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai).

4. **Process phases with human approval gates.**
   - Claude Code's recommended workflow is explicitly phased: **Explore → Plan → Implement → Commit**, with plan mode as a built-in gate — "Claude reads files and answers questions without making changes" until you approve the plan (source: https://code.claude.com/docs/en/best-practices).
   - OpenAI: "High-risk actions: Actions that are sensitive, irreversible, or have high stakes should trigger human oversight until confidence in the agent's reliability grows. Examples include canceling user orders, authorizing large refunds, or making payments." Also escalate when failure thresholds are exceeded (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).

5. **Autonomy rules (when to proceed vs stop and ask).**
   - Anthropic sample prompt: "Consider the reversibility and potential impact of your actions. You are encouraged to take local, reversible actions like editing files or running tests, but for actions that are hard to reverse, affect shared systems, or could be destructive, ask the user before proceeding." — with named examples (deleting branches, `git push --force`, posting to shared systems) and "do not use destructive actions as a shortcut" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
   - OpenAI GPT-5 guide — dial autonomy both ways: for persistence, "You are an agent — please keep going until the user's query is completely resolved, before ending your turn" and "Only terminate your turn when you are sure that the problem is solved"; for restraint, set tool-call budgets and "escape hatches" allowing the model to proceed under uncertainty and document assumptions (source: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide).

6. **Validation / self-verification steps.**
   - Agent SDK loop makes "verify work" a first-class phase, with three methods: rules-based feedback (tests/linting), visual feedback (screenshots), LLM-as-judge (source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk).
   - Long-running agents: test end-to-end "as users would experience it" (browser automation), and protect the tests: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality." (source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
   - Adversarial review: "have a subagent review the diff in a fresh context and report gaps... so the agent doing the work isn't the one grading it" — but scope it ("Report gaps, not style preferences") to avoid over-engineering (source: https://code.claude.com/docs/en/best-practices).

7. **Structured final reporting (evidence, not assertions).**
   - "Have Claude show evidence rather than asserting success: the test output, the command it ran and what it returned, or a screenshot of the result." (source: https://code.claude.com/docs/en/best-practices)
   - Machine-readable output for pipelines: `claude -p ... --output-format json` / `stream-json` (source: https://code.claude.com/docs/en/best-practices).

8. **Logs: changelog / findings / open items.**
   - Long-running harness artifacts: `claude-progress.txt` session log, a JSON feature/test list (state changed only via a `passes` field), `init.sh` setup script, git commits with descriptive messages as the durable changelog (source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
   - Claude docs' state-management best practices: "Use structured formats (JSON) for state data; use unstructured text for progress notes; use git for state tracking; emphasize incremental progress" — with worked `tests.json` + `progress.txt` examples (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
   - Context engineering: NOTES.md-style external memory persists goals and open items across context windows (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

### B4. Other high-value agentic-prompting practices

- **Specificity beats vagueness** — documented before/after pairs, e.g. "add tests for foo.py" → "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." (source: https://code.claude.com/docs/en/best-practices).
- **Right altitude for system prompts**: "specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics" — avoid both brittle hardcoded if-else logic and vague platitudes (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- **Tool design is prompt engineering**: consolidate tools around workflows; namespace them; return human-readable fields, not cryptic IDs; write actionable error messages; "even small refinements to tool descriptions can yield dramatic improvements" (source: https://www.anthropic.com/engineering/writing-tools-for-agents).
- **Instructions from SOPs**: OpenAI — "use existing operating procedures, support scripts, or policy documents to create LLM-friendly routines"; break tasks into smaller, unambiguous numbered steps; "define clear actions" per step; "capture edge cases" with conditional branches (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf). (Direct bridge to the med-device audience: your work instructions and SOPs are agent-instruction raw material.)
- **Curb overengineering / test-gaming**: sample prompts exist for "avoid over-engineering... the right amount of complexity is the minimum needed" and "Tests are there to verify correctness, not to define the solution... inform me rather than working around them" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
- **Failure patterns to teach** (all from https://code.claude.com/docs/en/best-practices): kitchen-sink sessions (clear context between tasks), correcting repeatedly (restart with a better prompt), over-specified CLAUDE.md, trust-then-verify gap ("If you can't verify it, don't ship it"), unscoped "infinite exploration".

---

## PART C — Contrast: Generative (Chat) Prompt vs Agentic Prompt

### C1. Authoritative articulations of the difference

- **Anthropic (Claude Code docs, as of Aug 2026):** "Claude Code is an agentic coding environment. **Unlike a chatbot that answers questions and waits**, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely... Instead of writing code yourself and asking Claude to review it, **you describe what you want and Claude figures out how to build it.**" (source: https://code.claude.com/docs/en/best-practices)
- **OpenAI:** applications that only generate output on request "are not agents"; agents "perform... workflows on the users' behalf with a high degree of independence," recognize completion, self-correct, and "halt execution and transfer control back to the user" on failure (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- **Anthropic (context engineering):** the discipline itself shifts — from "crafting effective written instructions" (prompt engineering) to "what configuration of context is most likely to generate our model's desired behavior?" — managing "the entire context state (system instructions, tools, Model Context Protocol, external data, message history, etc)" (source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- **OpenAI (GPT-5 guide):** agentic prompts must set **stop conditions and uncertainty thresholds per tool** ("checkout tools should demand user confirmation, while search tools need minimal threshold"; file-deletion stricter than grep) and calibrate eagerness/persistence — concerns that simply don't exist in a chat prompt (source: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide).

### C2. The teachable contrast (synthesis — instructor framing, grounded in the sources above)

| | Generative (chat) prompt | Agentic prompt |
|---|---|---|
| Specifies | **WHAT TO WRITE** | **A JOB TO RUN** |
| Core elements | role, task, context, format, examples | mission & definition of done; environment & file boundaries; allowed/forbidden tools; inputs (read-only) vs outputs; process phases & approval gates; autonomy/stop rules; self-verification; deliverables & logs |
| Output | one response you read | a sequence of actions + artifacts + a report with evidence |
| Failure mode | bad text — you just re-prompt | wrong *actions* (files changed, emails sent) — so you need gates, sandboxes, verification |
| Human role | reader/editor of the answer | delegator/reviewer at checkpoints |
| Analogy | briefing a ghost-writer | writing a work order / statement of work for a contractor |

- The "work order for a contractor" analogy is instructor synthesis, not a vendor quote — but it is directly supported by OpenAI's "on your behalf" definition and Anthropic's onboarding-doc framing of CLAUDE.md/tool descriptions, and by Anthropic's advice that specs should name files, scope, and an end-to-end verification step (sources: as cited in B2/B3). Defensible with attribution as "our framing."
- Continuity point for the class: everything from generative prompting (clarity, context, examples, format) **still applies** inside an agentic prompt — Anthropic: "Providing examples, otherwise known as few-shot prompting, is a well known best practice that Anthropic continues to strongly advise" (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). The agentic prompt is a superset, adding environment, process, and safety layers.

---

## PART D — Risks & Guardrails

### D1. Prompt injection — OWASP LLM01:2025

- Prompt injection is **#1** in the OWASP Top 10 for LLM Applications 2025 (LLM01:2025). Definition: an attacker manipulates LLM behavior through crafted inputs — **direct** (malicious user prompt overriding system instructions) or **indirect** (malicious content planted in documents, web pages, emails, or database records the LLM later processes) (source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ — note: the OWASP page returned HTTP 403 to our fetcher on 2026-08-21; the definition and mitigation list were corroborated across multiple secondary write-ups, e.g. https://www.indusface.com/learning/owasp-llm-prompt-injection/ and https://aembit.io/blog/owasp-top-10-llm-risks-explained/).
- OWASP mitigations (corroborated): constrain model behavior; define/validate expected output formats; input & output filtering; **enforce privilege control and least-privilege access**; **require human approval for high-risk actions** (e.g., approve before sending/deleting emails); segregate and identify external content; adversarial testing (same sources).
- **Why analogies mislead here — NCSC "Prompt injection is not SQL injection (it may be worse)" (Dec 8, 2025, Dave Chismon):** "Under the hood of an LLM, there's no distinction made between 'data' or 'instructions'; there is only ever 'next token.'" Hence "prompt injection attacks may never be totally mitigated in the way that SQL injection attacks can be"; LLMs are "inherently confusable deputies." Recommended posture: reduce risk and impact, not hope for a fix — e.g., "when an LLM processes information from a party, the privileges it has drop to that of the party"; log inputs/outputs/tool calls; don't rely on deny-listing phrases (source: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection). **Teaching note:** the popular "SQL injection for AI" analogy is explicitly rejected by NCSC — teach the difference, it's memorable.
- **"Lethal trifecta" (Simon Willison, Jun 16, 2025)** — an agent becomes dangerous when it combines: (1) access to private data, (2) exposure to untrusted content, (3) ability to communicate externally. One poisoned document can then exfiltrate data with no traditional software vulnerability involved (source: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/). Widely cited framing; technically defensible and excellent for a quality-risk-matrix audience — break any one leg of the trifecta and the exfiltration path closes.

### D2. Least privilege & governance — UK NCSC

- NCSC blog "Thinking carefully before adopting agentic AI" (fetched copy shows 15 May 2026; an accompanying PDF is dated June 2026 on ncsc.gov.uk): apply **least privilege** (minimum access, shortest time, short-lived credentials, revoke elevated access after task); constrain what agents can access and do; monitor for unusual activity; threat-model the deployment; plan for incidents. Quotes: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment." and humans "remain accountable for the decision to deploy it, the access it was granted, the safeguards around it, the consequences of its operation." (source: https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai ; PDF: https://www.ncsc.gov.uk/sites/default/files/2026-06/Thinking-carefully-before-adopting-agentic-AI.pdf). Related: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai (not fetched in detail — UNVERIFIED contents).

### D3. Approval gates for consequential actions

- OpenAI: human intervention on (a) exceeded failure thresholds and (b) high-risk actions — "sensitive, irreversible, or... high stakes... canceling user orders, authorizing large refunds, or making payments"; plus guardrail stack: relevance classifier, safety classifier (jailbreak/injection), PII filter, moderation, tool-risk-rated safeguards, rules-based protections (blocklists, regex, input limits), output validation (source: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- Anthropic: computer-use docs require "human confirmation for consequential actions"; Claude for Chrome requires action confirmations "before taking high-risk actions like publishing, purchasing, or sharing personal data" (sources: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool ; https://claude.com/blog/claude-for-chrome).
- Anthropic autonomy-vs-safety sample prompt (ask-before-irreversible) — see B3 item 5 (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

### D4. OpenClaw third-party skills — supply-chain data exfiltration (Cisco et al.)

- Context: OpenClaw is a popular open-source personal AI agent with a community "skills" marketplace (ClawHub) — third-party instruction/code packages the agent installs. It became 2026's cautionary tale for agent supply chains.
- **Cisco AI Defense findings (blog, Jan 28, 2026; authors Amy Chang, Vineeth Sai Narajala, Idan Habler):** running Cisco's Skill Scanner against the **#1-ranked community skill ("What Would Elon Do?")** found it was malicious: **silent data exfiltration via curl to attacker-controlled servers, direct prompt injection to bypass safety guidelines, command injection via embedded bash** — nine findings total, 2 critical / 5 high. Cisco's framing: "Security for OpenClaw is an option, but it is not built in." The same post cites research that **26% of 31,000 agent skills analyzed contained at least one vulnerability** (source: https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare ; see also Cisco's follow-up https://blogs.cisco.com/ai/cisco-announces-defenseclaw).
- Related (reported by press/secondary, not independently verified): Koi Security's Feb 2026 ClawHub audit found ~341 malicious skills ("ClawHavoc" campaign, macOS infostealers), and OpenClaw subsequently integrated VirusTotal scanning for ClawHub skills (sources: https://www.authmind.com/blogs/openclaw-malicious-skills-agentic-ai-supply-chain ; https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html — treat exact counts as **reported, UNVERIFIED against Koi's primary post**).
- Teaching point: skills/plugins are **unsigned third-party code + instructions** your agent executes — apply the same supplier-qualification mindset the audience already uses for component suppliers (incoming inspection = skill scanning; approved-vendor list = curated/allowlisted skills).

### D5. Sandboxing

- Anthropic Claude Code sandboxing (announced ~Nov 2025; docs live as of Aug 2026): OS-level enforcement (Linux bubblewrap, macOS Seatbelt) of **filesystem isolation** ("only access or modify specific directories") + **network isolation** ("only connect to approved servers"); both are needed — without network isolation a prompt-injected agent could exfiltrate secrets, without filesystem isolation it could escape. Reduced permission prompts by ~84% in Anthropic's internal usage; runtime released open source (sources: https://code.claude.com/docs/en/sandboxing ; https://anthropic.com/engineering/claude-code-sandboxing ; https://www.infoq.com/news/2025/11/anthropic-claude-code-sandbox).
- Computer-use docs: dedicated VM/container, minimal privileges, no credentials, domain allowlists (source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).

### D6. Anthropic browser-use red-teaming numbers (Claude for Chrome)

- Announced Aug 2025 (blog page fetched 2026-08-21 shows Aug 25, 2025 and later rollout updates): adversarial testing on **123 test cases representing 29 different attack scenarios**. Without mitigations, deliberate prompt-injection attacks succeeded **23.6%** of the time in autonomous mode; with new safety mitigations this fell to **11.2%**. On a browser-specific challenge set (hidden DOM fields, URL/tab-title injections), mitigations cut the attack success rate from **35.7% to 0%** (source: https://claude.com/blog/claude-for-chrome).
- Mitigations: site-level permissions (grant/revoke per site), confirmation before high-risk actions (publishing, purchasing, sharing personal data), blocked categories (financial services, adult content, pirated content), injection classifiers, hardened system prompts. Pilot: 1,000 Max users → all Max (Nov 24, 2025) → Pro/Team/Enterprise (Dec 18, 2025). A real pilot case: a phishing email tried to make the agent delete the user's emails; mitigations defended it (source: https://claude.com/blog/claude-for-chrome).
- Teaching point: 11.2% is a vendor-reported *residual* risk figure — an honest number showing injections are mitigated, not solved; pairs perfectly with NCSC's "reduce risk and impact" posture.

---

## Verification gaps / UNVERIFIED items

1. OpenAI "A Practical Guide to Building Agents" exact publication date (widely reported April 2025; PDF itself is undated).
2. OWASP LLM01:2025 page content — genai.owasp.org returned 403 to our fetcher; definition/mitigations corroborated via multiple secondary sources only.
3. Koi Security ClawHub audit numbers (341 malicious skills / ClawHavoc) — press-reported; not verified against Koi's own publication.
4. NCSC "Managing the cyber risk of agentic AI" blog — found but contents not fetched in detail.
5. AGENTS.md "over 60,000 projects" — from agents.md itself as fetched 2026-08-21; some press cites higher figures; use "60k+ (per agents.md)".
6. Claude Code sandboxing "~84% fewer permission prompts" — from search-result snippets of Anthropic/InfoQ coverage, not fetched from the engineering post directly.

## Raw materials on disk

- OpenAI guide full text: /tmp/claude-0/-home-user-Claude-Works/554d7b42-af40-5647-a410-4bcb2103024f/scratchpad/openai_agents_guide.txt (extracted from the official PDF, 34 pp.)
- Claude prompting best-practices full page: /root/.claude/projects/-home-user-Claude-Works/554d7b42-af40-5647-a410-4bcb2103024f/tool-results/toolu_01UaXtbDzTf7nw2D33XvkXsH.txt
