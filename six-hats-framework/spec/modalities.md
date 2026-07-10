# Modalities — Adapting the Hats to the Task

The same hat means different things depending on what you're thinking *about*.
Black-hat on a business decision hunts for financial and execution risk;
Black-hat on a code change hunts for security holes and race conditions;
Black-hat on a short story hunts for plot holes and flat characters. The
framework keeps the *discipline* of each hat constant while rewriting its
*focus* per modality.

This repo ships four modalities. Each has a prompt file in
[`../prompts/modalities/`](../prompts/modalities/) that gets prepended to every
hat's prompt during a run, and a default sequence in
[`sequences.md`](sequences.md). Use `auto` to have the model classify the topic
into one of these first.

---

## `decisions` — Decisions & Strategy

Evaluating options, go/no-go calls, prioritization, strategic and personal
choices.

| Hat | Focus for this modality |
|-----|-------------------------|
| ⚪ White | Known facts, constraints, costs, timelines; what data would de-risk the call. |
| 🟢 Green | Options beyond the obvious two — reframes, hybrids, "do nothing," staged bets. |
| 🟡 Yellow | Value of each option, upside cases, strategic optionality created. |
| ⚫ Black | Execution risk, cost of being wrong, reversibility, second-order effects. |
| 🔴 Red | Gut read on each option and on the decision-maker's real appetite. |

Emphasis: surface the *full option set* before judging, and weigh reversibility
heavily.

---

## `research` — Research & Learning

Investigating a topic, understanding something deeply, mapping known vs unknown.

| Hat | Focus for this modality |
|-----|-------------------------|
| ⚪ White | The state of knowledge: established facts, contested claims, confidence, and the sharpest open questions. |
| 🟢 Green | New angles, hypotheses, analogies, cross-disciplinary connections, questions worth asking. |
| ⚫ Black | Weak evidence, methodological holes, where consensus is thinner than it looks, failure of the sources. |
| 🟡 Yellow | What's genuinely well-established and useful; the strongest findings to build on. |
| 🔴 Red | Which parts feel solid vs hand-wavy; where curiosity or suspicion is pulling. |

Emphasis: White does the heavy lifting; Black stress-tests the evidence rather
than the idea. Great for "help me understand X."

---

## `creative` — Creative & Writing

Drafting, ideation, and critique of creative or written work.

| Hat | Focus for this modality |
|-----|-------------------------|
| 🟢 Green | Fresh directions, premises, voices, structures, "what if we did the opposite." |
| 🟡 Yellow | What already sings; the strongest images, lines, or beats to amplify. |
| 🔴 Red | Emotional truth — does it *land*? Where does it move you or leave you cold? |
| ⚪ White | What the piece actually says vs intends; audience, constraints, form. |
| ⚫ Black | Plot holes, flat characters, clichés, structural sag, where a reader checks out. |

Emphasis: Green leads (creative work wants divergence first), and Red matters
more here than anywhere — art is judged by how it feels.

---

## `technical` — Technical / Code

Architecture, debugging, code review, technical design tradeoffs.

| Hat | Focus for this modality |
|-----|-------------------------|
| ⚪ White | What the system does, the actual constraints (scale, latency, deps), what's measured vs assumed. |
| ⚫ Black | Bugs, security holes, race conditions, failure modes, ops burden, tech debt, edge cases. |
| 🟢 Green | Alternative designs, simpler approaches, different tools, ways to sidestep the hard part. |
| 🟡 Yellow | Where the approach is genuinely strong: maintainability, performance, fit to team/stack. |
| 🔴 Red | Smell test — what feels fragile, over-engineered, or "you'll regret this in six months." |

Emphasis: White pins down real constraints before anyone judges, and Black runs
early and thorough because the cost of missed failure modes is high.

---

## Adding your own modality

1. Create `prompts/modalities/<name>.md` with a short framing paragraph and the
   per-hat focus (mirror the tables above).
2. Add a default sequence to [`sequences.md`](sequences.md).
3. Register it in the CLI's `MODALITIES` list (see `cli/six_hats.py`).

The hat *disciplines* never change — only the focus. That invariance is what
keeps results comparable across task types.
