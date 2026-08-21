# A3 · Recurring Cycle Kickoff ("reuse by diff")

**Type:** Agentic · **Version:** 1.0 · **Use when:** re-running a job you've already specified once — the weekly report, the monthly KPI refresh, the quarterly review — where a full mission brief (A1/A2) already lives in the repo or project.
**Works in:** Claude Code / Cowork (best with the filled brief in the repo or project instructions), ChatGPT Projects, Copilot agents.

> The economics of agentic prompting: write the full brief **once**, then each cycle is a
> 10-line diff. If you're re-writing the whole prompt every cycle, you're storing it in the
> wrong place — put it in the repo/project so every session inherits it.

---

## The template

```text
Run the {{job name}} cycle per the standing brief in {{path/to/brief.md — or "this project's
instructions"}}. Everything in the brief holds unless changed below.

<this_cycle>
Cycle: {{e.g., "QDR August 2026" | "week of 2026-08-17"}}
New/changed inputs only:
- {{S1: new files at path/..., covering {{dates}}}}
- {{S2: unchanged}}
As-of date for outputs: {{MMDDYY}}
Changes to scope this cycle: {{none | "include site C for the first time — flag its small n"}}
</this_cycle>

<deltas_to_watch>
- Compare every headline metric to last cycle ({{path to last deliverable}}); any move
  > {{threshold}} gets a one-line explanation or a flag in FINDINGS.md.
- New failure modes / categories not seen before: list them explicitly.
</deltas_to_watch>

<gates>
Standing gates apply. This cycle I additionally want a stop before {{e.g., "anything that
changes a previously published figure"}}.
</gates>

Report in the standing <reporting> shape. Start with Phase 0 restatement — include
what changed vs. last cycle as you understand it, so I can catch drift early.
```

---

## What makes this work
- **The standing brief carries the definitions.** Metric definitions, schemas, checks, and formats live in one versioned file; the cycle prompt only points and diffs. No drift, no re-explaining.
- **Delta reporting** turns each cycle into "what changed and why" — which is what your audience actually asks.
- **Phase-0 restatement including the diff** catches the classic recurring-job failure: the agent silently using last cycle's paths and dates.
- **Publish-figure protection:** numbers that already went to leadership deserve their own gate.

## Pitfalls
- Letting the standing brief rot: when a definition changes at a gate, update the brief file *in the same session* and log it in CHANGES.md.
- Accumulating "just this once" exceptions in cycle prompts — after two repeats, fold the exception into the brief.
- Reusing a chat thread across cycles instead of a fresh session + standing brief: old context leaks old numbers.
