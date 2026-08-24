# T6 — Attribute-and-option decomposition for AGENTIC prompt blocks
Research date: 2026-08-23. All facts cite source URLs inline. Primary sources fetched directly (vendor docs, arXiv, official PDF). Verbatim lists preserved wherever possible.

---

## 1. AUTONOMY LEVELS — published gradations of agent autonomy / human oversight

### 1.1 Feng, McDonald & Zhang — "Levels of Autonomy for AI Agents" (five user-role levels)
Source: https://arxiv.org/abs/2506.12469 (submitted 2025-06-14, rev. 2025-07-28); table detail from https://arxiv.org/html/2506.12469v2
Framing: autonomy is "a deliberate design decision, separate from capability and operational environment." Levels are named by **the role the USER takes**:

| Level | User role | User does | Agent does | Control mechanisms |
|---|---|---|---|---|
| L1 | **Operator** | Maintains control of long-term planning; invokes agent for specific subtasks; approves actions before execution | On-demand assistance; contextual suggestions; avoids preference-based decisions | "User-managed planning"; "Invocation or approval before actions" |
| L2 | **Collaborator** | Jointly plans and delegates; freely modifies agent output; can take control at any point | Independently works on assigned tasks; communicates transparently about progress and blockers | "Control transfer from agent to user, and vice versa"; "Shared representation of progress" |
| L3 | **Consultant** | Provides feedback, preferences, higher-level directional guidance | Plans and executes most tasks; proactively consults user for expertise/preferences | "Rich user feedback elicitation interfaces (in addition to simple approvals)" |
| L4 | **Approver** | Passively engaged; approves consequential actions or provides credentials at blockers | Autonomous on lower-stakes matters; requests involvement only for high-risk situations | "Approval elicitation for consequential actions"; "Customizable conditions for seeking approval" |
| L5 | **Observer** | Monitors via activity logs; can activate emergency shutdown but cannot provide input | Plans and executes all tasks independently; iterates without user involvement | "Emergency off switch" only |

### 1.2 Mitchell, Ghosh, Luccioni, Pistilli (Hugging Face) — "Fully Autonomous AI Agents Should Not Be Developed" (five code-pattern levels)
Source: https://arxiv.org/abs/2502.02649 ; table from https://arxiv.org/html/2502.02649v2
Levels named by **how much program flow the model controls** (risk "increases with the autonomy of a system"):

| Level | Description (verbatim) | Who controls | Example code pattern |
|---|---|---|---|
| Simple Processor (✩✩✩✩) | "Model has no impact on program flow" | Human | `print_llm_output(llm_response)` |
| Router (★✩✩✩) | "Model determines basic program flow" | Human: how functions done; system: when | `if llm_decision(): path_a() else: path_b()` |
| Tool Call (★★✩✩) | "Model determines how functions are executed" | Human: what functions; system: how | `run_function(llm_chosen_tool, llm_chosen_args)` |
| Multi-step Agent (★★★✩) | "Model controls iteration and program continuation" | Human: what functions exist; system: which/when/how | `while should_continue(): execute_next_step()` |
| Fully Autonomous Agent (★★★★) | "Model creates & executes new code" | System | `create_code(user_request); execute()` |

### 1.3 Morris et al. (Google DeepMind) — "Levels of AGI", Table 2 "Levels of Autonomy" (six levels)
Source: https://arxiv.org/html/2311.02462v4

- **Level 0 — No AI**: human does everything.
- **Level 1 — AI as a Tool**: "AI takes on mundane sub-tasks while humans retain full task control" (e.g., grammar checkers, search engines).
- **Level 2 — AI as a Consultant**: invoked by humans for substantive support (code generators, summarizers).
- **Level 3 — AI as a Collaborator**: "Co-equal human-AI collaboration; interactive coordination of goals & tasks."
- **Level 4 — AI as an Expert**: "AI drives interaction; human provides guidance & feedback."
- **Level 5 — AI as an Agent**: "Fully autonomous AI."
Key claim: "lower levels of autonomy may be desirable for particular tasks and contexts" — autonomy is a deliberate choice, not a capability ceiling.

### 1.4 Human-in/on-the-loop framing
- "Automation Level is characterized by two dimensions: Human-on-the-loop and Human-in-the-loop, with Human-on-the-loop providing humans with appropriate oversight" — Building Symbiotic AI (AI Act review), https://arxiv.org/pdf/2501.08046
- SOC trusted-autonomy framework: "five levels of AI autonomy from manual to fully autonomous, mapped to Human-in-the-Loop (HITL) roles and task-specific trust thresholds" — https://arxiv.org/abs/2505.23397
- Common three-way enumeration usable as options: **human-in-the-loop (approve each action) → human-on-the-loop (monitor, can intervene) → human-out-of-the-loop / full auto** (supported by the frameworks above; no single canonical vendor source uses these exact three labels).

### 1.5 OpenAI — tool risk ratings (autonomy modulator)
Source: "A practical guide to building agents" PDF, https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf (extracted via pdftotext), "Tool safeguards" entry, verbatim:
> "Assess the risk of each tool available to your agent by assigning a rating—**low, medium, or high**—based on factors like **read-only vs. write access, reversibility, required account permissions, and financial impact**. Use these risk ratings to trigger automated actions, such as pausing for guardrail checks before executing high-risk functions or escalating to a human if needed."

### 1.6 Anthropic — reversible vs. irreversible action guidance (operationalized)
- Claude Code auto-mode classifier blocks by default: "Irreversibly destroying files that existed before the session"; `git reset --hard`, `git clean -fd`, etc. "which the classifier presumes would discard uncommitted changes"; `terraform destroy` / `pulumi destroy` / `cdk destroy` — https://code.claude.com/docs/en/permission-modes ("What the classifier blocks by default").
- Long-running-agents harness: use git so agents can "revert bad code changes and recover working states" (reversibility engineered in) — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Microsoft Magentic-UI operationalizes the same axis as a 3-way action classification: **"always irreversible"** (explicit human approval), **"maybe irreversible"** (LLM judge assesses), **"never irreversible"** (auto-execute) — https://arxiv.org/html/2507.22358v1

### 1.7 NIST
No NIST levels-of-autonomy framework for AI agents was found as of Aug 2026 (NIST AISI work covers agent hijacking evaluations, not autonomy gradations). NOT RETRIEVED — note for taxonomy: cite academic/vendor frameworks above instead.

**Taxonomy suggestion — attribute "autonomy_level", options:** operator/L1 · collaborator/L2 · consultant/L3 · approver/L4 · observer/L5 (Feng et al.); or the 3-way HITL/HOTL/full-auto simplification; modifiers: per-tool risk rating (low/medium/high, OpenAI) and action reversibility class (never/maybe/always irreversible, Magentic-UI).

---

## 2. TOOL PERMISSIONS — Claude Code parameterization + OpenAI guardrail categories

### 2.1 Claude Code permission modes (complete, exact names)
Source: https://code.claude.com/docs/en/permissions and https://code.claude.com/docs/en/permission-modes

| Mode (config value) | What runs without asking | Best for |
|---|---|---|
| `default` (labeled **Manual**; alias `manual`) | Reads only | "Reviewing every action yourself, sensitive work" |
| `acceptEdits` | Reads, file edits, and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.) | "Iterating on code you're reviewing" |
| `plan` | Reads, plus classifier-approved commands when auto mode is available | "Exploring a codebase before changing it" |
| `auto` | "Everything, with background safety checks" (a classifier model reviews actions) | "Long tasks, reducing prompt fatigue" |
| `dontAsk` | Only pre-approved tools (auto-denies everything else) | "Locked-down CI and scripts" |
| `bypassPermissions` | Everything (skips prompts incl. protected paths) — "Only use this mode in isolated environments like containers or VMs" | "Isolated containers and VMs only" |

Set via `--permission-mode <mode>` (CLI), `permissions.defaultMode` (settings). Org locks: `permissions.disableBypassPermissionsMode` and `permissions.disableAutoMode` set to `"disable"`.

### 2.2 Permission rules (allow / ask / deny)
Source: https://code.claude.com/docs/en/permissions — verbatim:
- "**Allow** rules let Claude Code use the specified tool without manual approval."
- "**Ask** rules prompt for confirmation whenever Claude Code tries to use the specified tool."
- "**Deny** rules prevent Claude Code from using the specified tool."
- "Rules are evaluated in order: deny, then ask, then allow."
- CLI flags: `--allowedTools`, `--disallowedTools`; settings keys `permissions.allow`, `permissions.ask`, `permissions.deny`, `permissions.additionalDirectories`, `permissions.defaultMode`.

Rule syntax `Tool` or `Tool(specifier)`:
- `Bash(npm run build)` exact; `Bash(npm run test *)` prefix wildcard; wildcards at any position (`Bash(* install)`, `Bash(git * main)`); `:*` suffix ≡ trailing ` *`.
- `Read(./.env)`, `Edit(docs/**)` — gitignore-style path patterns with 4 anchor shapes: `//path` (absolute), `~/path` (home), `/path` (relative to settings source), `path`/`./path` (cwd-relative).
- `WebFetch(domain:example.com)`, `WebFetch(domain:*.example.com)`.
- MCP: `mcp__server`, `mcp__server__tool`, `mcp__server__*`.
- Subagents: `Agent(Explore)`, `Agent(Plan)`, `Agent(my-custom-agent)`.
- Parameter matching (deny/ask only): `Agent(model:opus)`, `Agent(isolation:worktree)`, `Bash(run_in_background:true)`, `Bash(dangerouslyDisableSandbox:true)`.
- Compound commands: recognized separators `&&`, `||`, `;`, `|`, `|&`, `&`, newlines — "A rule must match each subcommand independently."
- Built-in read-only Bash set runs promptless in every mode: `ls, cat, echo, pwd, head, tail, grep, find, wc, which, diff, stat, du, cd` + read-only `git` forms.
- Precedence: "If a tool is denied at any level, no other level can allow it" (managed > CLI > local > project > user).
- Hooks: PreToolUse hooks "can deny the tool call, force a prompt, or skip the prompt"; a blocking hook (exit code 2) overrides allow rules.

### 2.3 Claude Code sandbox settings (actual option names)
Source: https://code.claude.com/docs/en/sandboxing
- Enable: `sandbox.enabled: true`; hard-fail option `sandbox.failIfUnavailable: true`.
- **Sandbox modes** (verbatim): "**Auto-allow mode**" — "When a command can be sandboxed, Claude Code runs it inside the sandbox and approves it automatically"; "**Regular permissions mode**" — "All Bash commands go through the regular permission flow, even when sandboxed."
- Escape hatch: model may retry with `dangerouslyDisableSandbox` parameter → goes through regular permission flow; disable via `"allowUnsandboxedCommands": false` (**Strict sandbox mode**); `excludedCommands` lists commands that never run sandboxed.
- Filesystem: `sandbox.filesystem.allowWrite`, `denyWrite`, `denyRead`, `allowRead` (re-allow within denied region; "the more specific path wins"), `sandbox.filesystem.disabled`.
- Network: `sandbox.network.allowedDomains`, `deniedDomains`, `allowUnixSockets`/`allowAllUnixSockets`, `strictAllowlist` (deny instead of prompt), managed `allowManagedDomainsOnly`.
- Credentials: `sandbox.credentials` entries (file paths or env vars) with `"mode": "deny"`; credential masking via proxy with `injectHosts` and `extract` regex.
- Interaction: `autoAllowBashIfSandboxed` (default `true`) — sandboxed commands run without prompting. Defense-in-depth framing (verbatim, https://code.claude.com/docs/en/permissions): "Permissions control which tools Claude Code can use... Sandboxing provides OS-level enforcement that restricts the Bash tool's filesystem and network access."

### 2.4 OpenAI guardrail categories (complete list)
Source: "A practical guide to building agents," https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf — "Types of guardrails," verbatim:
1. **Relevance classifier** — "Ensures agent responses stay within the intended scope by flagging off-topic queries."
2. **Safety classifier** — "Detects unsafe inputs (jailbreaks or prompt injections) that attempt to exploit system vulnerabilities."
3. **PII filter** — "Prevents unnecessary exposure of personally identifiable information (PII) by vetting model output for any potential PII."
4. **Moderation** — "Flags harmful or inappropriate inputs (hate speech, harassment, violence)."
5. **Tool safeguards** — the low/medium/high risk rating (see §1.5).
6. **Rules-based protections** — "Simple deterministic measures (blocklists, input length limits, regex filters) to prevent known threats like prohibited terms or SQL injections."
7. **Output validation** — "Ensures responses align with brand values via prompt engineering and content checks."
Mechanics: "Guardrails can be implemented as functions or agents that enforce policies such as jailbreak prevention, relevance validation, keyword filtering, blocklist enforcement, or safety classification"; Agents SDK uses "optimistic execution" with tripwires (`GuardrailFunctionOutput`, `InputGuardrailTripwireTriggered`).
Agent Builder (2026): guardrails node "redact personally identifiable information (PII) and detect jailbreak attempts"; separate **human approval node** — https://developers.openai.com/api/docs/guides/agent-builder-safety

---

## 3. CHECK TYPES — taxonomy of verification methods for agent work

### 3.1 Anthropic Agent SDK — "Verify work" (canonical 3-type list)
Source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk (agent loop: "gather context → take action → verify work → repeat"):
1. **Rules-based feedback** — "The best form of feedback is providing clearly defined rules for an output, then explaining which rules failed and why." Example: code linting/type-checking (TypeScript vs raw JS); tests.
2. **Visual feedback** — screenshots or renders to assess visual output: "layout positioning, styling accuracy, content hierarchy, and responsive design appearance."
3. **LLM as judge** — "have another language model 'judge' the output of your agent based on fuzzy rules"; "less robust with latency tradeoffs."

### 3.2 Anthropic long-running-agents harness — session-level checks
Source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Smoke tests** before new work: run "basic end-to-end functionality" tests first, so agent doesn't build on a broken state (checks whether "the app had been left in a broken state").
- **Browser automation end-to-end verification**: "Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools."
- **Re-read state check**: "Read the git logs and progress files to get up to speed on what was recently worked on."
- **Careful-testing gate for done-marking**: mark features "passes": true only "after careful testing"; "It is unacceptable to remove or edit tests."
- Corroborated by memory-tool docs: "Mark a feature complete only after end-to-end verification confirms it works, not when the code is written" — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (Multisession pattern, "Key principle").

### 3.3 Deterministic recalculation / reconciliation checks (Anthropic skills repo)
Source: https://github.com/anthropics/skills/blob/main/document-skills/xlsx/SKILL.md (Anthropic's public agent-skills repo)
- xlsx skill mandates LibreOffice headless **recalculation** of all formulas before delivery, scanning for Excel errors (`#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`); recalc script "outputs JSON with status (success or errors_found), total_errors count, total_formulas count, and an error_summary" — i.e., a re-open-the-file + machine-check pattern. (Exact SKILL.md text summarized from search results; full file not fetched — note.)

### 3.4 Claude Code auto mode — classifier-as-check
Source: https://code.claude.com/docs/en/permission-modes — "a second model, the classifier, reviews actions instead of you," "blocking anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile content Claude read." (A per-action LLM-judge check built into the harness.)

**Taxonomy suggestion — attribute "check_type", options:** rules-based test (lint/typecheck/unit test) · deterministic recalculation & error scan · reconciliation to known totals (xlsx recalc JSON status) · visual/screenshot check · end-to-end run (browser automation / smoke test) · re-open-the-file / re-read state check · LLM-as-judge · per-action safety classifier.

---

## 4. GATE PLACEMENTS — where vendor guidance puts human approval

Distinct gate types found, each with source:

1. **Plan approval gate (before any edits).** Claude Code plan mode: "Plan mode tells Claude to research and propose changes without making them... edits stay blocked until you approve the plan." Approval options verbatim: "Yes, and use auto mode" / "Yes, manually approve edits" / "No, keep planning"; user can edit the plan (Ctrl+G) before approving. — https://code.claude.com/docs/en/permission-modes. Magentic-UI co-planning: "press 'Accept Plan' to start execution" — https://arxiv.org/html/2507.22358v1
2. **Pre-irreversible / high-risk-action gate.** OpenAI verbatim: "High-risk actions: Actions that are sensitive, irreversible, or have high stakes should trigger human oversight until confidence in the agent's reliability grows. Examples include canceling user orders, authorizing large refunds, or making payments." — OpenAI practical guide PDF. Magentic-UI action guards: "Any irreversible or potentially harmful agent actions are reviewed by the human user before being executed" (always/maybe/never-irreversible triage) — https://arxiv.org/html/2507.22358v1. Claude Code equivalents: `ask` rules ("Tools matched by an explicit ask rule" are never auto-approved in any mode), protected paths (prompted in default/acceptEdits; ".claude, .git..." list), critical-path `rm` circuit breaker ("never lets a permissions.allow rule or a PreToolUse hook that returns 'allow' approve an rm... that targets a critical path") — https://code.claude.com/docs/en/permission-modes
3. **Failure-threshold escalation gate.** OpenAI verbatim: "Exceeding failure thresholds: Set limits on agent retries or actions. If the agent exceeds these limits (e.g., fails to understand customer intent after multiple attempts), escalate to human intervention." — OpenAI practical guide PDF. Mechanized as `max_turns` → `MaxTurnsExceeded` in Agents SDK (https://openai.github.io/openai-agents-python/running_agents/) and `maxTurns` → result subtype `error_max_turns` in Claude Agent SDK (https://code.claude.com/docs/en/agent-sdk/typescript).
4. **Blocker / checkpoint gate (mid-task).** Anthropic "Building effective agents": agents can "pause for human feedback at checkpoints or when encountering blockers"; include "stopping conditions (such as a maximum number of iterations)." — https://www.anthropic.com/engineering/building-effective-agents. Feng et al. L4: "Approval elicitation for consequential actions" + "Customizable conditions for seeking approval" — https://arxiv.org/html/2506.12469v2
5. **Final-review / answer-verification gate.** Magentic-UI: "After task completion, the user can verify the answer by either going through the agent actions for each step or by asking the agent follow-up questions." — https://arxiv.org/html/2507.22358v1. Claude Code classifier enforces a human merge gate: blocks "Merging a pull request no human has approved, approving Claude's own pull request, or disabling CI checks." — https://code.claude.com/docs/en/permission-modes
6. **Credential/blocker handoff gate.** Feng et al. L4 user "approves consequential actions or provides credentials when agent reaches blockers" — https://arxiv.org/html/2506.12469v2
7. **Tool-level interactive gate.** Claude Code: "Tools that require user interaction: the built-in `AskUserQuestion` tool and MCP tools marked `requiresUserInteraction`" are in the "Actions no mode auto-approves" list (with ask-rule matches, org connector `ask` tools, critical-path rm, cross-session messaging safeguards) — https://code.claude.com/docs/en/permission-modes. OpenAI Agent Builder: dedicated "human approval node" so "users can review and confirm operations" — https://developers.openai.com/api/docs/guides/agent-builder-safety

**Taxonomy suggestion — attribute "gate_placement", options:** plan-approval · pre-irreversible-action · per-tool ask rule · failure-threshold escalation · mid-task checkpoint/blocker · credential handoff · final review/answer verification · human PR/merge approval.

---

## 5. MEMORY / STATE options — enumerated state-management patterns (Anthropic)

### 5.1 Long-running-agents harness artifacts (exact file names)
Source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **`claude-progress.txt`** — "a log of what agents have done" kept alongside git history.
- **`feature_list.json`** — comprehensive JSON of structured feature descriptions each with `"passes": false` status; "a comprehensive file of feature requirements expanding on the user's initial prompt" (prevents premature completion).
- **Git commits** with "descriptive commit messages" — enables "revert bad code changes and recover working states."
- **`init.sh`** — environment startup script for reproducible sessions.
- Two-agent structure: **initializer agent** ("the very first agent session uses a specialized prompt that asks the model to set up the initial environment") + **coding agent** ("every subsequent session asks the model to make incremental progress, then leave structured updates").
- Per-session ritual: (1) `pwd`; (2) "Read the git logs and progress files"; (3) "Read the features list file and choose the highest-priority feature that's not yet done"; (4) run init.sh / dev server; (5) basic end-to-end tests; (6) work on ONE feature; (7) commit + update claude-progress.txt. "Leave the environment in a clean state" = "code that would be appropriate for merging to a main branch."

### 5.2 Context-engineering techniques (long-horizon)
Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Compaction** — "taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary"; preserves "architectural decisions, unresolved bugs, and implementation details"; Claude Code continues "with this compressed context plus the five most recently accessed files"; lightest-touch form = "tool result clearing."
- **Structured note-taking / agentic memory** — "the agent regularly writes notes persisted to memory outside of the context window... pulled back into the context window at later times"; examples: "creating a to-do list", "maintaining a NOTES.md file"; Pokémon agent kept "precise tallies across thousands of game steps," maps, achievements, "strategic notes"; "after context resets, the agent reads its own notes and continues."
- **Sub-agent architectures** — "specialized sub-agents can handle focused tasks with clean context windows," each returning "only a condensed, distilled summary of its work (often 1,000-2,000 tokens)."

### 5.3 Memory tool (API-level option)
Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- Client-side `/memories` directory of files; tool type `memory_20250818`. Commands (complete): **view** (with `view_range`), **create**, **str_replace**, **insert**, **delete**, **rename**.
- Auto-injected system prompt (verbatim): "IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE... ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory."
- **Multisession software development pattern** (enumerated): 1. Initializer session (sets up "a progress log..., a feature checklist..., a reference to any startup or initialization script"); 2. Subsequent sessions ("opens by reading those memory files"); 3. End-of-session update ("updates the progress log with what was completed and what remains").
- Pairing guidance (verbatim): "compaction keeps the active context small without client-side bookkeeping, and memory preserves the information that must survive summarization." Related server features: context editing (clears tool results client-side) and compaction (server-side summarization) — https://platform.claude.com/docs/en/build-with-claude/context-editing, https://platform.claude.com/docs/en/build-with-claude/compaction

**Taxonomy suggestion — attribute "state_mechanism", options:** progress log file (claude-progress.txt) · structured JSON state (feature_list.json with passes flags) · git commit log · NOTES.md / to-do notes · memory tool /memories files · compaction summary · tool-result clearing · sub-agent summaries · init.sh environment script.

---

## 6. REPORTING shapes — structured completion-report formats

### 6.1 Claude Code / Agent SDK output formats
Source: https://code.claude.com/docs/en/headless
- `--output-format` values (complete): **`text`** (default), **`json`** ("structured JSON with result, session ID, and metadata"), **`stream-json`** ("newline-delimited JSON for real-time streaming"; last line is a `result` message with "final response text, cost, and session metadata").
- Schema-constrained output: `--output-format json --json-schema '<JSON Schema>'` → structured payload in `structured_output` field; invalid schema → hard error.
- JSON result payload fields include `result`, `session_id`, `total_cost_usd` (+ per-model breakdown), `structured_output`.
- Exit codes: "exits with code 0 on success and a non-zero code when the run fails"; SIGTERM → 143.

### 6.2 Result status enum (Agent SDK)
Source: https://code.claude.com/docs/en/agent-sdk/typescript — `SDKResultMessage`:
- **subtype values**: `success`, `error_max_turns`, `error_during_execution`.
- **fields**: `duration_ms`, `is_error`, `num_turns`, `result`, `total_cost_usd`, `permission_denials`, `usage`, `structured_output`.

### 6.3 API-level status enum
Source: https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons — `stop_reason` values (complete): `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn` ("server-tool loop reached its iteration limit — send content back to continue"), `refusal`, `model_context_window_exceeded`.

### 6.4 Evidence requirements in completion reports (harness guidance)
- Long-running agents: sessions must "leave structured updates" (progress file + descriptive commit messages) and may mark work done only "after careful testing" — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Memory tool pattern: end-of-session update records "what was completed and what remains" — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- xlsx skill recalc report shape: JSON `{status: success|errors_found, total_errors, total_formulas, error_summary}` — https://github.com/anthropics/skills/blob/main/document-skills/xlsx/SKILL.md (via search; full file not fetched)
- OpenAI Agent Builder: "Structured outputs to constrain data flow" listed as a safety practice — https://developers.openai.com/api/docs/guides/agent-builder-safety

**Taxonomy suggestion — attribute "report_shape", options:** plain text · JSON envelope (result+metadata+cost) · schema-constrained structured_output · stream-json events · status enum (success / error_max_turns / error_during_execution; or stop_reason set) · progress-file update + commit message · evidence block (tests run, recalc status, what remains).

---

## 7. ERROR / ESCALATION policies — published enumerations

### 7.1 OpenAI — escalation triggers & graceful handoff
Source: OpenAI practical guide PDF (verbatim): "Implementing a human intervention mechanism allows the agent to gracefully transfer control when it can't complete a task. In customer service, this means escalating the issue to a human agent. For a coding agent, this means handing control back to the user." Two triggers: **exceeding failure thresholds** (retry/action limits) and **high-risk actions** (see §4.2–4.3).

### 7.2 OpenAI Agents SDK — exception/abort enumeration
Source: https://openai.github.io/openai-agents-python/running_agents/ (complete): `AgentsException` (base) · `MaxTurnsExceeded` · `ModelBehaviorError` ("unexpected or invalid outputs... malformed JSON") · `ModelTimeoutError` · `ToolTimeoutError` · `UserError` · `InputGuardrailTripwireTriggered` · `OutputGuardrailTripwireTriggered`. `max_turns` limits loop iterations; `max_turns=None` disables.

### 7.3 Claude Code — retry event + error categories
Source: https://code.claude.com/docs/en/headless — `system/api_retry` event fields: `attempt`, `max_retries`, `retry_delay_ms`, `error_status`; **error category enum (complete, verbatim)**: `authentication_failed`, `oauth_org_not_allowed`, `billing_error`, `rate_limit`, `overloaded`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `unknown`.

### 7.4 Claude Code — deny-with-reason / continue vs stop-turn semantics
Source: https://code.claude.com/docs/en/permissions — on a permission prompt: "**No**: Claude Code sends your comment to Claude as the reason for the denial, and Claude continues working. If you select No without a comment... Claude Code stops the turn." (log-reason-and-continue vs abort as user-side options). PreToolUse hook outcomes: "deny the tool call, force a prompt, or skip the prompt"; SDK `canUseTool` returns `{behavior:'allow', updatedInput}` or `{behavior:'deny', message, interrupt}` — https://code.claude.com/docs/en/agent-sdk/typescript
- dontAsk mode = auto-deny-and-continue policy: "Auto-denies tools unless pre-approved" — https://code.claude.com/docs/en/permissions
- Sandbox failure policy options: escape-hatch retry unsandboxed (`dangerouslyDisableSandbox`) vs `allowUnsandboxedCommands:false` (strict abort) vs `failIfUnavailable` (hard failure at startup) — https://code.claude.com/docs/en/sandboxing

### 7.5 Long-running agents — recover-don't-abandon policy
Source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents — on entering a broken state: use git to "revert bad code changes and recover working states"; "It is unacceptable to remove or edit tests"; leave clean state each session.

### 7.6 Anthropic building-effective-agents — stopping conditions
Source: https://www.anthropic.com/engineering/building-effective-agents — "stopping conditions (such as a maximum number of iterations) to maintain control"; pause "at checkpoints or when encountering blockers."

**Taxonomy suggestion — attribute "error_policy", options per failure class:** retry (bounded: max_retries/max_turns) · retry-with-modified-approach (unsandboxed retry) · ask/escalate to human (threshold or high-risk trigger) · abort/interrupt (exception, strict mode) · deny-and-continue with logged reason · revert-and-recover (git) · hand-back control gracefully.

---

## Retrieval notes / gaps
- OpenAI PDF fetched as binary; text extracted locally with pdftotext (saved: /root/.claude/projects/.../tool-results/openai-agents-guide.txt) — guardrail and human-intervention sections captured verbatim.
- anthropics/skills xlsx SKILL.md content taken from search-result synthesis of the GitHub file, not a direct fetch — exact wording should be re-verified if quoted verbatim.
- NIST: no levels-of-autonomy framework for AI agents found (only agent-hijacking eval guidance); nothing to enumerate.
- Mitchell et al. (2502.02649) star-ratings table retrieved from arXiv HTML v2; abstract page alone did not include it.
- Claude Code full docs pages cached locally: permissions (toolu_01NMpe...txt), sandboxing (toolu_011ArH...txt), permission-modes (toolu_01XFYL...txt) under /root/.claude/projects/-home-user-Claude-Works/554d7b42-af40-5647-a410-4bcb2103024f/tool-results/ — contain complete protected-paths and classifier block/allow lists if more verbatim detail is needed.
