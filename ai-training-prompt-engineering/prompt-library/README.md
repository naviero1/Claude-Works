# Prompt Library

Reusable, versioned prompt templates for the "From Prompts to Agents" training.
**Owner:** Oscar Penny · **Version:** 1.0 (Aug 2026) · **Status:** approved for team use

A good prompt takes an hour of iteration to earn. This library is where that hour is banked:
copy a template, fill the `{{placeholders}}`, run it, and commit improvements back.

---

## What's here

### Generative templates (`generative/`) — run in any chat assistant

| File | Use for |
|---|---|
| `G1_writing_editing.md` | Emails, summaries, reports — drafting, editing, voice matching |
| `G2_data_analysis.md` | Trustworthy analysis of an attached dataset, with charts |
| `G3_evaluation_rubric.md` | Rubric grading, proposal comparison, anti-sycophancy critique |
| `G4_spreadsheet_builder.md` | Building workbooks, cleaning messy sheets, formula help |
| `G5_presentation_builder.md` | Content → outline → approval → deck, message titles |
| `G6_html_interactive.md` | Single-file dashboards, calculators, trackers |
| `G7_research_brief.md` | Cited web research; claim verification |
| `G8_summarize_compare.md` | Long-document summaries, version diffs, meeting actions |

### Agentic templates (`agentic/`) — for Claude Code / Cowork-class tools

| File | Use for |
|---|---|
| `A1_mission_brief_template.md` | The general 12-block mission brief for delegating any job |
| `A2_etl_to_presentation.md` | The full worked template: data → validated analysis → slide (v1.0) |
| `A3_recurring_cycle.md` | Ten-line cycle kickoff against a standing brief ("reuse by diff") |
| `A4_claude_md_starter.md` | CLAUDE.md / project-instructions starter for a workspace |
| `A5_document_pipeline.md` | Folder of documents → extracted, flagged tracker |

**Which kind do I need?** A *generative* prompt describes **what to write** — you read the
answer and act on it. An *agentic* prompt describes **a job to run** — environment, inputs,
process, checks, and when the agent must stop and ask. If the task involves files, tools,
multiple steps, or a deliverable produced without you watching, use an A-template.

---

## Conventions (used by every template here)

- **`{{placeholder}}`** — yours to fill; think mail-merge fields. Search for `{{` before you
  run: if any remain, you're not done.
- **`[optional]`** — delete the block if it doesn't apply.
- **Everything else is scaffold** — the blocks marked "keep" are what make outputs reliable
  and runs auditable; don't trim them to save space.
- **Version header** — each file carries `Version` and an owner. Bump the version and add a
  one-line change note when you materially change a template. Note which model you tested on:
  prompts behave differently per model.
- **Filled examples** — most files include one. Keep them: a gold-standard filled prompt +
  output teaches faster than any instruction.

## Managing this library (the rules we teach)

1. **Promotion trigger** — explained the same task more than once? Package it: add it here,
   or make it a Claude Skill / Project instruction / Copilot saved prompt. (This is
   Anthropic's own guidance for when a prompt becomes a skill.)
2. **Test before approving** — run a new/changed template on 3–5 representative real cases,
   including one edge case. Re-test after major model updates; record the date.
3. **One owner per template** — a person, not a team. Owners review on a cadence (quarterly
   is fine) and after model changes.
4. **Reuse by diff** — for recurring jobs, don't re-fill the whole template each cycle;
   keep the filled version alongside and change only dates/paths (see `A3`).
5. **Where things live per tool** — this repo is the source of truth. Mirror what you use
   often into your tools: Claude Projects/Skills, ChatGPT Projects, Gemini Gems, Copilot
   Prompt Gallery (team tab). The repo copy is the versioned master.

## Governance — prompts contain data

- A stored prompt often carries supplier names, pricing, findings, draft language.
  **Classify and share this library like the documents it quotes.**
- **Never store credentials, personal data, or patient-adjacent examples in a template.**
  `{{placeholders}}` exist so sensitive values are supplied at run time, never saved.
- Filled examples in this repo must use generic or already-internal data consistent with the
  repo's classification — when in doubt, genericize.
- Treat third-party skills/plugins like installing software: audit before adopting.
- Your organization's AI policy and approved-tool list outrank anything in this library.

## Contributing

Improve a template → bump its version, note the change and the model you tested on, commit
with a message like `G2 v1.1: added reconciliation example (tested Sonnet 5)`. New template →
follow the house format: header (type/version/owner/use-when), template in a code block,
filled example, "what makes this work," pitfalls.
