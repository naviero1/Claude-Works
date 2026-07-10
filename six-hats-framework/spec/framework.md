# The Six Thinking Hats — Portable Framework Spec

This is the model-agnostic core of the framework. Everything else in this repo
(the CLI, the Claude Code plugin, the prompt library) is a rendering of the
rules described here. If you want to port this to another tool, another model,
or your own agent system, this file plus [`hats.md`](hats.md),
[`modalities.md`](modalities.md), and [`sequences.md`](sequences.md) is all you
need.

## What the framework is

Edward de Bono's Six Thinking Hats (1985) is a protocol for **parallel
thinking**. Instead of participants arguing from fixed positions — one attacking,
one defending — everyone adopts the *same mode of thinking at the same time*,
then switches together. Each "hat" is a distinct mode. The point is to
deliberately separate kinds of thinking that normally get tangled up: emotion
contaminating logic, criticism killing ideas before they're formed, optimism
papering over real risk.

Applied to a single agent or model, the payoff is the same but the mechanism is
different: rather than de-conflicting *people*, you de-conflict *reasoning
modes* inside one process. A model asked to "analyze this" collapses facts,
feelings, risks, and ideas into one muddy pass. Forcing it through one hat at a
time — ideally as **separate calls that cannot see each other's hedging** —
produces sharper, less self-censoring output in each mode.

## The design commitment

The single most important implementation choice: **run each hat as its own
focused pass, and give each pass only the context it should see.** A Black-hat
pass that can see the Yellow-hat pass will soften its criticism to stay
consistent. A Green-hat pass that can see the Black-hat pass will pre-censor
wild ideas. Isolation is the feature.

This is also what makes the framework *agent-ready*: each hat maps cleanly onto
a single-purpose sub-agent. The orchestration below is exactly the contract a
multi-agent system would implement.

## The six modes (summary)

Full definitions in [`hats.md`](hats.md).

| Hat | Mode | Core question | Discipline |
|-----|------|---------------|------------|
| 🔵 Blue | Process / meta | How should we think about this? | Manages the other hats; bookends the session. |
| ⚪ White | Facts & information | What do we know, and what's missing? | Neutral. Data and gaps only — no interpretation. |
| 🔴 Red | Emotion & intuition | What's my gut say? | Feelings stated openly, **no** justification required. |
| ⚫ Black | Caution & critique | Why might this fail? | Logical negativity — every risk backed by a reason. |
| 🟡 Yellow | Optimism & value | Why might this work? | Logical positivity — every benefit backed by a reason. |
| 🟢 Green | Creativity | What else could we do? | New options and provocations; judgment suspended. |

Two asymmetries worth remembering: Yellow is *harder* than Black for most
people/models (we're wired to spot threats first), so it deserves an explicit,
protected pass. And Red is the only hat that is deliberately **un**justified —
its value is flushing feelings into the open so they stop distorting the
"logical" hats.

## Orchestration contract

A run is defined by three inputs:

1. **`topic`** — the subject to think about (a decision, a question, a draft, a
   codebase, anything).
2. **`modality`** — the task type. This selects the hat *sequence* and rewrites
   each hat's prompt so its discipline lands correctly for the task. See
   [`modalities.md`](modalities.md). Supported: `decisions`, `research`,
   `creative`, `technical`. (`auto` asks the model to classify first.)
3. **`sequence`** — the order of hats. Defaults per modality live in
   [`sequences.md`](sequences.md); override freely.

Execution rules:

- **Blue always opens and closes.** The opening Blue pass sets the agenda and
  (in `auto` mode) fixes the modality. The closing Blue pass synthesizes — it is
  the *only* pass that reads every other pass.
- **White is shared context.** Its factual output (and *only* its factual
  output) is passed to every subsequent hat, because facts are legitimately
  common ground. Nothing else is shared laterally.
- **Every other hat runs blind** to its siblings. Feed it: the topic, the
  modality instructions, its own hat prompt, and White's facts. Nothing else.
- **Red carries no reasons.** Do not ask it to justify. Do not penalize it for
  not justifying.
- **The closing Blue pass** receives all passes and produces the synthesis:
  the decision/answer/plan, the key tensions between hats, and next actions.

### Reference pseudocode

```
run(topic, modality, sequence):
    ctx = {}
    ctx.agenda = blue_open(topic, modality)          # sets frame; may set modality if auto
    ctx.white  = white(topic, modality, ctx.agenda)  # facts + gaps — the only shared pass
    for hat in sequence without blue/white:
        ctx[hat] = think(hat, topic, modality, facts=ctx.white)   # runs blind
    ctx.synthesis = blue_close(topic, modality, all_passes=ctx)   # sees everything
    return report(ctx)
```

## Why this over "just ask the model to analyze it"

- **No mode bleeds into another.** Isolation prevents the optimism-tax on
  criticism and the criticism-tax on creativity.
- **The skipped modes actually happen.** Left to themselves, people and models
  rarely run a pure Yellow or pure Green pass. The protocol forces them.
- **It's inspectable.** You get six labeled artifacts, not one blob, so you can
  see *where* a conclusion came from and re-run a single hat.
- **It's composable.** Each hat is a drop-in agent. Swap models per hat, add a
  seventh custom lens, or run the whole thing as one prompt for a cheap version.

## Two ways to run it

- **Multi-pass (faithful).** One call per hat, isolation enforced by the
  orchestrator. This is what the CLI does by default and what the Claude Code
  sub-agents implement. Best fidelity, higher cost.
- **Single-pass (cheap).** One prompt that walks the model through the hats in
  order. Faster and cheaper, but isolation is only as good as the model's
  discipline. Good for quick passes; use `--single-pass` in the CLI.

## Adapting it

- Add a modality by writing a new file in `prompts/modalities/` and a sequence
  in [`sequences.md`](sequences.md).
- Add a hat (e.g. a "Purple" stakeholder-empathy hat) by writing
  `prompts/hats/<name>.md` and inserting it into a sequence.
- Change fidelity by toggling multi-pass vs single-pass.

The rules above are the whole contract. Keep hats isolated, keep White shared,
let Blue bookend, and let Red go unjustified — everything else is taste.
