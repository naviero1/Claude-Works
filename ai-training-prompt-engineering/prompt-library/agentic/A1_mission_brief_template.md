# A1 · Mission Brief — the general agentic prompt template

**Type:** Agentic · **Version:** 1.0 · **Owner:** Oscar Penny · **Works in:** Claude Code, Claude Cowork, ChatGPT agent mode, Copilot agents (adapt tool references)
**Use when:** you are delegating a *job* to an AI agent — something with files, tools, multiple steps, and a deliverable — rather than asking for a piece of text.

> A generative prompt describes **what to write**. An agentic prompt describes **a job to run**:
> the goal, the working environment, the inputs, the process, the checks, when to stop and ask,
> and what "done" looks like. If any of those are missing, the agent will fill the gap with a guess.

**Conventions:** `{{placeholder}}` = yours to fill · `[optional]` = delete if unused · everything else is scaffold — keep it.
Search for `{{` before you run; if any remain, you're not done. Never delete `<checks>`, `<process>`, or `<rules>` — they keep a run honest.

---

## The template (copy from here)

```xml
<role>
You are a {{posture — e.g., "meticulous analyst and report writer"}} working for {{your_name}},
{{your_role}} at {{org}}. Name behaviours, not titles: {{e.g., "you never invent numbers, you log
what you change and why, you write headline-first for busy decision-makers"}}.
</role>

<mission>
Goal (one sentence): {{the question to answer or the thing to produce}}
Why it matters: {{the decision or event this feeds}}
Audience: {{who receives it, and how much time they'll give it}}
Deadline: {{date/time, timezone}}
Done looks like: {{the deliverables in one line}}
</mission>

<context>
Domain in three sentences: {{what the process is, who the actors are, what "good" means}}
Glossary (use these terms exactly):
- {{TERM}} — {{definition as used at your org}}
Known quirks (tribal knowledge that will bite if unstated):
- {{quirk and the rule to apply}}
Targets / thresholds that matter: {{...}}
Prior work to stay consistent with: {{files/pages and what must not change}}
</context>

<environment>
Working location: {{repo/folder/workspace, branch}}
Read-only inputs live in: {{paths}} — never modify an input file.
Write outputs to: {{path}} · Scratch/intermediate files: {{path}}
Tools available: {{e.g., file system, shell, Python + pandas/openpyxl/python-pptx, web search}}
Tools you must NOT use: {{e.g., no network calls, no writes outside the project folder, no emails sent}}
Confidentiality: {{what may not leave the environment; where summaries may/may not be posted}}
</environment>

<inputs>
Source S1 — {{short name}}
  Location: {{exact path or URL}} · Format: {{xlsx sheet/header row | csv | ...}}
  What one row/record means: {{grain}}
  Trust level: {{authoritative | derived | manual entry}} · Known issues: {{...}}
Source S2 — {{...}}
If a required fact about an input cannot be determined, write UNKNOWN and raise it as an
open item before starting — never guess.
</inputs>

<plan>
The steps of the job, in order, with what each consumes and produces:
1. {{step — e.g., "inventory and profile every input, report structure before processing"}}
2. {{step}}
3. {{step}}
Methods allowed: {{boring, reproducible ones}}.
Methods NOT allowed without asking: {{e.g., dropping data, causal claims, new dependencies}}.
</plan>

<checks>
Before reporting done, verify and show evidence:
HARD (stop and report if violated):
- {{check written as an equality or rule the agent can actually evaluate,
   e.g., "totals reconcile to the source", "every citation resolves", "file re-opens without errors"}}
SOFT (flag and continue):
- {{e.g., "any metric moving >X vs. last cycle gets a one-line explanation"}}
</checks>

<outputs>
Deliverables (exact names and locations):
1. {{path/NAME_MMDDYY.ext}} — {{what it contains}}
2. {{...}}
Logs: CHANGES.md (what changed, when, why) · FINDINGS.md (claims + evidence + confidence)
· OPEN_ITEMS.md (assumptions, exclusions, questions — each with owner and status)
</outputs>

<process>
Phase 0 — Intake: restate the mission, the definitions, and your assumptions in your own words.
Ask only the questions that block Phase 1.
  ▶ GATE 1 (human): I confirm definitions. Do not proceed without it.
Phase 1..n — {{the plan above, grouped into phases}}
  ▶ GATE 2 (human): {{mid-run checkpoint — e.g., "reconciliation reviewed before analysis"}}
Final phase — QA: re-open every deliverable, verify against <checks>, then report.
  ▶ GATE 3 (human): {{pre-render/pre-send approval — e.g., "headlines approved before the deck is built"}}
Autonomy rules: between gates, proceed without asking. Stop and ask immediately if:
a HARD check fails; an input is missing or shaped differently than described; a definition
is ambiguous; an action would be hard to reverse (delete, send, publish, overwrite).
</process>

<rules>
- Never invent, estimate, or back-fill a fact or number. Missing is missing; say so.
- Inputs are immutable; outputs are versioned; everything regenerable goes in scratch.
- State assumptions as assumptions, in OPEN_ITEMS.md.
- Prefer boring, reproducible methods; propose fancier ones at a gate, don't just use them.
- {{house rules: language, units, date formats, naming conventions}}
</rules>

<quality_bar>
Definition of done — all must be true before you say "done":
[ ] Every {{placeholder}} resolved or logged as an open item.
[ ] All HARD checks pass; every SOFT flag has a note.
[ ] Deliverables re-opened and verified after creation.
[ ] Logs written (CHANGES / FINDINGS / OPEN_ITEMS).
[ ] {{job-specific bar, e.g., "every number traces to a source cell"}}
</quality_bar>

<reporting>
When you finish (or stop at a gate), reply in this exact shape, under 25 lines:
1. Status: DONE | STOPPED AT GATE n | BLOCKED — one line why.
2. Headline answer/outcome — one sentence with the number(s).
3. Deliverables — paths.
4. Checks summary — what passed, what was flagged.
5. Open items needing a human — who, what, by when.
6. What I'd check next / risks — ≤ 3 bullets.
Details live in the files, not the message.
</reporting>
```

---

## Why each block exists (30-second version)

| Block | What it prevents |
|---|---|
| `<role>` | Generic "helpful assistant" behaviour. Behaviours beat titles: "never invent numbers" changes output; "senior analyst" doesn't. |
| `<mission>` | Exploration instead of an answer. Topics generate wandering; questions generate answers. |
| `<context>` | The agent inventing your glossary, or silently "fixing" a quirk you already know about. |
| `<environment>` | The agent "helpfully" editing your master file, or wandering outside its folder. |
| `<inputs>` | Guessed schemas. The "one row means…" line determines every formula downstream. |
| `<plan>` | Ten charts and no answer. Also caps the methods so rigor isn't improvised. |
| `<checks>` | Plausible-but-wrong output. Checks must be written so the agent can actually evaluate them. |
| `<outputs>` | Deliverables you can't find, and no audit trail. |
| `<process>` + gates | Errors caught at the expensive end. Gate 1 catches definition errors (cheapest), the last gate catches message errors. Autonomy rules stop the agent from asking about everything or nothing. |
| `<rules>` | The non-negotiables drifting when the run gets long. |
| `<quality_bar>` | "Done" meaning "I stopped." A checklist the agent must satisfy — and you can audit. |
| `<reporting>` | A narrative essay instead of a status you can read in 30 seconds. |

**Reuse by diff:** for a recurring job, keep the filled template in the repo (or project instructions) and change only `<inputs>` paths and dates each cycle.

**See also:** `A2_etl_to_presentation.md` — the full worked example this pattern was distilled from (data → validated analysis → slide).
