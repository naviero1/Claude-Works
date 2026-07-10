# Six Thinking Hats — a reusable thinking framework

Run **any topic** through Edward de Bono's Six Thinking Hats and get a
structured, multi-mode analysis back — as a script, as a Claude Code command, or
as a portable spec you can wire into your own agents.

The framework's one commitment: **think in one mode at a time, and keep the
modes from contaminating each other.** A model asked to "analyze this" mushes
facts, feelings, risks, and ideas into one hedged blur. Forcing it through one
hat per pass — ideally as separate calls that can't see each other's output —
produces sharper thinking in each mode, and makes the modes people usually skip
(a *pure* optimism pass, a *pure* idea-generation pass) actually happen.

## The six hats

| Hat | Mode | Question | Discipline |
|-----|------|----------|------------|
| 🔵 Blue | Process / meta | How should we think about this? | Frames (open) & synthesizes (close). Bookends the run. |
| ⚪ White | Facts | What's known, what's missing? | Neutral. Data & gaps only — shared with every other hat. |
| 🔴 Red | Emotion | What's my gut say? | Feelings, stated with **no** justification. |
| ⚫ Black | Caution | Why might this fail? | Critique — every risk backed by a reason. |
| 🟡 Yellow | Optimism | Why might this work? | Value — every benefit backed by a reason. |
| 🟢 Green | Creativity | What else could we do? | Options & provocations; judgment suspended. |

## Three layers, one repo

This repo is deliberately layered so you can use it at whatever altitude you
need:

```
spec/        The portable, model-agnostic framework — the source of truth.
prompts/     A prompt library: one file per hat, one per modality, + orchestrator.
cli/         six_hats.py — a standalone runner (one model call per hat).
.claude/     A Claude Code layer: /six-hats command, one sub-agent per hat, a skill.
examples/    A sample rendered report.
```

- **Just want to run it?** Use the [CLI](cli/README.md).
- **Working inside Claude Code?** Clone the repo and use `/six-hats` (see below).
- **Building your own agents / processes?** Read [`spec/framework.md`](spec/framework.md)
  — it *is* the orchestration contract, and each hat maps onto one
  single-purpose agent.

## Modalities

The same hat means different things for different tasks — Black-hat is "security
holes" for code but "plot holes" for a story. The framework keeps each hat's
*discipline* fixed while re-tuning its *focus* per task type. Four ship in the
box: **decisions**, **research**, **creative**, **technical** (see
[`spec/modalities.md`](spec/modalities.md)). `auto` classifies the topic for you.

## Quickstart — CLI

```bash
cd cli
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# auto-detect the task type and run all hats
python six_hats.py "Should we rewrite the billing service in Go?"

# force a modality, save the report
python six_hats.py "Is now a good time to switch careers?" \
    --modality decisions -o career.md

# see the exact prompts with no key and no network call
python six_hats.py "any topic" --modality research --dry-run
```

Full CLI docs: [`cli/README.md`](cli/README.md).

## Quickstart — Claude Code

The `.claude/` directory makes this a project-scoped Claude Code setup. Clone
the repo and, from inside it:

```
/six-hats Should we adopt a four-day work week? --modality decisions
```

The command frames the session, gathers facts, then dispatches **one sub-agent
per hat** (`hat-green`, `hat-yellow`, `hat-black`, `hat-red`) so each thinks in
isolation, and finishes with a Blue synthesis. The `six-hats` **skill** also
lets Claude reach for the framework on its own whenever a topic wants
structured, full-spectrum thinking.

> To use the hats *anywhere* (not just inside this repo), copy `.claude/commands`,
> `.claude/agents`, and `.claude/skills` into your project's `.claude/`, or into
> `~/.claude/` for global use.

## How a run works

```
Blue (open)   → frame the session; pick the modality & hat order
White         → shared facts + gaps        ─┐ (fed forward to every later hat)
Green / Yellow / Black / Red  → each runs BLIND, one isolated pass per hat
Blue (close)  → reads everything; synthesizes bottom line, tensions, next actions
```

The rules — hats stay isolated, White is shared, Blue bookends, Red goes
unjustified — are spelled out in [`spec/framework.md`](spec/framework.md).
There's a sample output in [`examples/`](examples/sample-output.md).

## Extending it

- **New modality:** add `prompts/modalities/<name>.md` + a sequence in
  `spec/sequences.md`, and register it in `cli/six_hats.py`.
- **New hat** (e.g. a stakeholder-empathy "Purple"): add
  `prompts/hats/<name>.md` and a `.claude/agents/hat-<name>.md`, then slot it
  into a sequence.
- **Different fidelity:** multi-pass (default, faithful) vs `--single-pass`
  (one call, cheaper).

## Credit & caveats

The framework is Edward de Bono's *Six Thinking Hats* (1985). It's a widely-used
practical thinking tool; treat it as a useful scaffold for structured
deliberation rather than an empirically-validated algorithm. This repo is an
independent implementation, not affiliated with de Bono or his estate.

## License

[MIT](LICENSE).
