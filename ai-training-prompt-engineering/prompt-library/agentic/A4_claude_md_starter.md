# A4 · CLAUDE.md / Project-Instructions Starter

**Type:** Agentic infrastructure · **Version:** 1.0 · **Use when:** setting up a repo or project folder that agents (Claude Code, Cowork, other coding/work agents) will operate in repeatedly. The same content works as ChatGPT Project instructions or a Copilot agent description, minus the file-path specifics.

> A CLAUDE.md (or AGENTS.md) is the **standing memory of a workspace**: every agent session
> reads it automatically before doing anything. It's where you put what you're tired of
> repeating — and what an agent must never do. Keep it short; every line spends context
> in every session. Link out to detail files instead of inlining them.

---

## The template (save as `CLAUDE.md` in the repo/folder root)

```markdown
# {{Project / initiative name}}

## What this workspace is
{{Two sentences: the initiative, who runs it, what "good" means here.}}
Owner: {{name}} · Started: {{date}} · Status log: CHANGES.md

## Layout
- `{{inputs/}}` — source files. READ-ONLY: never modify, overwrite, or "fix" anything here.
- `{{work/}}` — scratch and intermediates; anything here may be regenerated.
- `{{deliverables/}}` — what humans open. Versioned with `_MMDDYY` suffix; never overwrite,
  write a new version.
- `{{prompt-library/ | briefs/}}` — standing mission briefs; the {{job}} cycle runs from
  `{{briefs/xyz.md}}`.

## Conventions
- Dates {{ISO in files, MM/DD/YY on slides}} · Units {{...}} · Language {{...}}.
- Glossary and metric definitions live in `{{GLOSSARY.md}}` — use those terms exactly;
  if a needed definition is missing, add a PROPOSED entry and flag it, don't improvise.
- Logs: append to CHANGES.md (what/when/why), FINDINGS.md (claims + evidence),
  OPEN_ITEMS.md (assumptions & questions, each with owner + status).

## Standing rules
- Never invent, estimate, or back-fill numbers. Missing is missing.
- Prefer scripts over manual edits; anything computed twice gets a script in `{{work/scripts/}}`.
- No network calls / external sharing beyond: {{allowed list, e.g., "the linked Notion page —
  summaries only, never raw data"}}.
- Ask before: deleting anything, sending anything, changing a previously published number,
  or adding a new dependency/tool.

## Known quirks (read before touching data)
- {{quirk → rule, e.g., "Site B sheets record part {{PN-X}} under a legacy code — map it to {{PN-Y}}"}}
- {{quirk → rule}}

## Common commands / recurring jobs
- {{job name}}: run per `{{briefs/job.md}}`; typical trigger "run the {{job}} cycle for {{period}}".
```

---

## What belongs here vs. in a mission brief

| CLAUDE.md (standing, every session) | Mission brief (per job) |
|---|---|
| Folder layout & read/write boundaries | This job's inputs and outputs |
| House conventions, units, date formats | This job's metric definitions |
| Permanent rules & ask-first list | This job's process, phases, gates |
| Known data quirks | This cycle's dates and deltas |
| Where the briefs live | The deliverables of this run |

## Pitfalls
- Novels: a 400-line CLAUDE.md gets skimmed by humans and dilutes agent attention. Target ≤ 60 lines; link the rest.
- Stale quirks: when a quirk is fixed at the source, delete the rule — obsolete instructions cause new errors.
- Secrets: never put credentials, tokens, or personal data here — it's read into every session and lives in git history.
- Writing it once and never updating: end sessions that changed conventions with "update CLAUDE.md to reflect what we decided."
