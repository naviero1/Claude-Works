# The Elements of Prompting — Field Guide

**Version:** 1.0 (Aug 2026) · **Owner:** Oscar Penny · **Companion to:** the G/A templates in this library and the Prompt Anatomy Cheat Sheet.

Every template in this library is assembled from a small set of recurring **elements**. This
file defines each one precisely: what it is, what it mechanically does to the model, what a
weak vs. strong fill looks like, and which failure it exists to prevent. Learn the elements
and you can diagnose any bad output — and build templates of your own instead of collecting
other people's.

**Why elements instead of "good prompts":** output quality swings up to 76 accuracy points
from formatting alone (Sclar et al., ICLR 2024). You cannot inspect your way to a reliable
prompt by rewording; you get there by knowing which element failed and fixing that one. The
elements are also the *diagnosis grid*:

| The output is… | The element that failed |
|---|---|
| the wrong altitude, tone, or posture | **Role** |
| an answer to a different (or vaguer) question | **Task** |
| generically right, specifically wrong for us | **Context** |
| right content, unusable shape or length | **Format** |
| not matching the standard in your head | **Examples** |
| confidently invented | **The Out** (missing) |
| sprawling past what you asked | **The Stop** (missing) |

---

# Part 1 — Generative elements

A generative prompt commissions **one piece of text** you will read and act on. Its five
elements plus two safety valves:

## 1. ROLE — who is answering

**Definition.** The identity, expertise posture, and — critically — the *behavioral
commitments* you assign to the model before the task begins.

**Mechanism.** An LLM completes documents by predicting what plausibly comes next. The role
determines *which region of everything it has read* the completion is drawn from: the
vocabulary, the caution level, what gets foregrounded. "You are a careful analyst" makes
analyst-document continuations more probable; it does not add analyst knowledge.

**What goes in it:** the posture (analyst / editor / skeptical reviewer), the audience
relationship (writes for busy executives), and 2–4 explicit behaviors stated as rules the
output can be checked against.

**Weak → strong:**
- Weak: `You are a senior data scientist.` (a credential — produces nothing checkable)
- Strong: `You are a careful analyst. You compute every number by running code, you state n
  for every proportion, you never drop data silently, and you say "the data can't answer
  that" when it can't.` (four behaviors, each auditable in the output)

**Failure it prevents:** the generic-assistant voice — mid-distribution, hedge-everything
output. Average prompts return average responses.

**Evidence & nuance.** Personas do **not** improve factual accuracy (162-persona study,
Zheng et al., EMNLP 2024): "you are a genius mathematician" doesn't fix arithmetic. They
**do** reliably shift tone, framing, and which knowledge gets foregrounded (Salewski et al.,
NeurIPS 2023). So: use Role for *how it answers*, never as a substitute for *checking what
it answers*. Behaviors beat titles because behaviors are testable.

**In the templates:** every G-template opens with a behavioral role; compare G2's analyst
vs. G3's "demanding but fair reviewer" vs. G5's "titles state findings" presentation writer —
same element, different behavior sets.

## 2. TASK — what, for whom, to what end

**Definition.** The single clear ask: a **verb + object + audience + success criterion**.

**Mechanism.** The task is the most load-bearing text in the prompt — it defines the target
the completion optimizes toward. Vendors agree to the point of redundancy: Google calls the
task "the most important component"; for Microsoft the Goal is the *only* required part.

**What goes in it:** one action verb (draft / compare / grade / extract — not "help me
with"); the object, precisely; the audience and what they already know; and the success
criterion phrased as an outcome: *"the reader should be able to decide X after reading."*

**Weak → strong:**
- Weak: `Analyze the returns data.` (a topic — topics generate exploration)
- Strong: `Answer: what is the return rate by site for Q2 versus the 2.0% target, and which
  three reason codes drive 80% of returns?` (questions generate answers)

**Failure it prevents:** wandering output — ten observations and no answer; a summary of
everything instead of the thing the meeting needs.

**Nuance.** One task per prompt. If there are genuinely several, number them in priority
order and add the Stop (below). A question is a stronger task than an instruction, because
it carries its own completion test: either it got answered or it didn't.

## 3. CONTEXT — what the model cannot know

**Definition.** Everything true in *your* world that isn't in the model's training data:
raw material, definitions, constraints, history, quirks — and the *reasons* behind your rules.

**Mechanism.** The model fills every information gap with the most statistically plausible
filler from its training. Context replaces plausible-in-general with true-for-you. This is
the anti-hallucination element: most "lies" are really unsupplied context.

**What goes in it:**
- The **raw material** itself (paste or attach — never assume it knows your documents)
- A **glossary** for terms with local meaning ("FPY means *this* here, computed *this* way")
- **Constraints and sensitivities** (what not to promise, what's confidential)
- **Known quirks** with the rule to apply — every quirk you don't write down becomes a
  silent "fix" the model invents
- **The why** behind non-obvious rules: "this will be read aloud, so no ellipses" measurably
  outperforms "no ellipses" — models generalize from reasons (Anthropic guidance)

**Weak → strong:**
- Weak: `Use our standard definitions.` (the model's "standard" is the internet's average)
- Strong: `Glossary — use exactly: Return rate = returned units ÷ shipped units (shipped
  from shipped_q2.csv). Known quirk: the export has a totals row at the bottom — exclude it
  and say so.`

**Failure it prevents:** generically-correct, specifically-wrong output — the plausible
number with your company's name on it.

**Discipline.** Delimit context from instructions (tags, fences, headers) so the model never
confuses *material to work on* with *orders to follow* — this is also your first line of
defense when the material itself contains text that looks like instructions.

## 4. FORMAT — the output contract

**Definition.** The required shape of the response: structure, length, tone, medium, what to
include and what to omit.

**Mechanism.** Models imitate structure more readily than they obey descriptions of it —
which is why Format works best stated positively ("respond in flowing prose paragraphs"
beats "don't use markdown") and best of all *demonstrated* (see Examples).

**What goes in it:** the skeleton (sections, table columns, bullet limits); a **numeric
length cap** with a priority rule ("≤120 words — cut content before quality"); tone; and
output hygiene ("headline answer first, support after", "end with the assumptions").

**Weak → strong:**
- Weak: `Keep it short and professional.` (unenforceable adjectives)
- Strong: `Max 120 words. Structure: the ask in sentence one; two supporting facts with
  numbers; the deadline. Nothing else.`

**Failure it prevents:** the 3×-too-long draft; the buried answer; output you must
re-shape by hand before anyone can use it.

**Nuance.** Heavy format constraints can tax reasoning on hard problems ("Let Me Speak
Freely?", 2024): for genuinely difficult analysis, let the model reason free-form first and
format the *answer* in a second step. For routine work, format up front.

## 5. EXAMPLES — show, don't describe

**Definition.** 3–5 realistic demonstrations of the task done right, placed in the prompt.

**Mechanism.** In-context learning (Brown et al., 2020 — the discovery that founded prompt
engineering): the model infers the pattern from demonstrations without retraining. Examples
are the strongest steering signal that exists for format, tone, and edge-case handling —
stronger than any description of the same.

**What goes in them:** *diverse* cases, not five clones — include the awkward one (the
missing field, the borderline grade, the angry customer email) because the model handles
edge cases exactly as your examples do. Wrap them in tags so they can't be mistaken for the
live input. Real beats invented; lightly-genericized real beats both.

**Weak → strong:**
- Weak: three examples that are the same happy case reworded
- Strong: one typical case, one edge case, one "reject/escalate" case — now the model knows
  the boundaries, not just the center

**Failure it prevents:** the model guessing your standard from the internet's average, and
format drift across runs.

**2026 nuance.** On reasoning/thinking models, start **zero-shot** — examples constrain
more than they help on hard reasoning, and few-shot measurably degrades some reasoning
models (DeepSeek-R1's own paper). Add examples only when the *format* drifts. On everyday
drafting/formatting tasks, examples remain the highest-leverage element there is.

## The two safety valves

These are single sentences, not sections — but they appear in every template in this library
because each shuts off a signature failure.

**THE OUT — permission to not know.** `If the document doesn't say, say so. If you are not
sure, say you are not sure.` Models are trained on benchmarks that reward guessing over
abstaining (OpenAI, 2025); the Out re-opens the abstain option and drastically cuts invented
answers. Without it you have implicitly ordered the model to always produce something.

**THE STOP — the scope boundary.** `Answer these three questions, then stop — do not go
exploring.` The Stop converts open-ended capability into bounded work. It is the difference
between an answer and a wander; in agentic prompts it grows up to become gates and autonomy
rules.

---

# Part 2 — Agentic elements

An agentic prompt commissions **a job, not a text**: the agent plans, acts through tools,
checks results, and iterates — mostly while you are not watching. Every generative element
still applies (an agentic prompt *contains* role, task-like mission, context, format-like
outputs, and often worked examples). The seven additional elements exist for one reason:

> **Text that fails costs you a re-prompt. Actions that fail change the world** — files
> overwritten, emails sent, wrong numbers published. So the agentic elements govern
> *conduct*: where the agent may act, how it must verify itself, when it must stop and ask,
> and how it proves what it did.

The twelve blocks of the mission brief (template A1), defined:

## `<role>` — the standing behavioral contract

Same element as generative Role, but with higher stakes: in chat, the role shapes one answer
you're about to read; in an agent, it biases **hundreds of unsupervised decisions**. Write it
as the behaviors you'd want if you couldn't check any single step: *"never invents numbers,
logs every transformation with a row count, prefers reproducible scripts over manual edits."*
Failure prevented: an agent that improvises its professional standards mid-run.

## `<mission>` — the goal and the definition of done

The agentic Task: one goal, the decision it feeds, the audience, the deadline — plus the one
line chat prompts never need: **"done looks like: …"**. An agent runs a loop; the mission is
its exit condition. Vendor grounding: give the agent "a check it can run… without a check,
'looks done' is the only signal available" (Anthropic). A mission without a verifiable done
state produces the agent equivalent of wandering: plausible activity, indefinitely.
Failure prevented: the agent deciding for itself what finished means.

## `<context>` — tribal knowledge, written down

Same element as generative Context; the agentic difference is *coverage pressure*. A chat
answer touches your domain once; an agent touches it at every step, so every unstated quirk
gets stepped on. The glossary becomes a **controlled vocabulary** (the agent will otherwise
happily compute three subtly different "yields"), and each known quirk carries its rule
("Parks records PN 668518; it means 666518 — map it"). Failure prevented: silent invented
fixes — the most expensive class of agent error because they look like diligence.

## `<environment>` — the workspace contract

**New in kind.** Where the agent may read, where it must write, what tools exist, what is
forbidden. The load-bearing distinctions: **inputs are read-only** (never modify a source),
**outputs are versioned** (never overwrite what a human already opened), **scratch is
regenerable**. Name the forbidden actions explicitly (no network calls, no emails sent, no
writes outside the folder). This is least-privilege written as prose — and where available,
enforce it with sandboxing too; the prompt is policy, the sandbox is physics.
Failure prevented: the agent "helpfully" editing your master workbook.

## `<inputs>` — the source register

**New in kind.** One block per source: location, exact format, **grain** ("one row = one
inspected unit" vs "one lot with counts" — the line that determines every denominator
downstream), primary key, coverage, owner, **trust level** (authoritative / derived / manual
entry), and known issues. The register's cardinal rule: a fact you can't establish is written
`UNKNOWN` and raised as an open item — **never guessed**. Failure prevented: the agent
inferring your schema, which is where most wrong numbers are born.

## `<plan>` — bounded method

The steps in order, plus two lists chat prompts don't carry: **methods allowed** (boring,
reproducible ones) and **methods not allowed without asking** (dropping data, causal claims,
fancy models, new dependencies). This is the "right altitude" element: specific enough to
prevent improvised rigor, open enough that the agent can adapt to what it finds.
Failure prevented: creative methodology at step 14 of 20, discovered only at review.

## `<checks>` — machine-evaluable verification

**New in kind, and the honesty engine of the whole brief.** Verification the agent can
actually *run*, split by consequence: **HARD** checks stop the run when violated (totals
reconcile to a trusted number; pass + fail = inspected; no duplicate keys; every citation
resolves); **SOFT** checks flag and continue (null-rate spikes, small samples, metric moved
>X vs last cycle). Two disciplines make checks real: write them as equalities and
set-memberships, not aspirations ("check data quality" is not a check); and always include
**one reconciliation anchor** — a number you already trust from outside the run. Without an
anchor, every other check can pass on the wrong data.
Failure prevented: plausible-but-wrong deliverables — the agent's version of hallucination.

## `<outputs>` — the deliverable contract and the audit trail

The agentic Format: exact filenames (with date suffixes), exact locations, and the **three
logs** that make a run auditable after the fact — `CHANGES.md` (what changed, when, why),
`FINDINGS.md` (claims → evidence → confidence), `OPEN_ITEMS.md` (assumptions and questions,
each with owner and status). A colleague should be able to find, understand, and regenerate
everything from the folder alone. Failure prevented: results you can't locate, and
conclusions you can't trace to evidence six weeks later.

## `<process>` — phases and human gates

**New in kind.** The job cut into phases with **human checkpoints at the cheap-error
points**: Gate 1 confirms *definitions* before any data is touched (cheapest possible
catch); Gate 2 reviews *reconciliation* before analysis builds on the numbers; Gate 3
approves *headlines as plain text* before anything renders or ships. The ordering principle:
a definition error caught at Gate 1 costs a sentence; the same error caught after the deck
circulated costs a retraction. Failure prevented: compounding — hours of competent work on
top of a wrong foundation.

## Autonomy rules — when to proceed, when to stop *(inside `<process>`)*

The agentic Stop, matured. Between gates the agent proceeds **without asking**; it must stop
and ask immediately when: a HARD check fails · an input isn't as described · a definition is
ambiguous · an action is hard to reverse (delete, send, publish, overwrite) · a previously
published number would change. Both halves matter: without the "proceed" half the agent asks
about everything (you've built a slow chatbot); without the "stop" half it asks about
nothing (you've built a liability). The reversibility line is the general principle:
**reversible → act; irreversible → ask.**

## `<rules>` — the invariants

The non-negotiables, kept short and absolute so they survive a long context: never invent or
back-fill a number; sources are immutable; every transformation is logged with a row count;
assumptions are stated as assumptions; house conventions (units, date formats, language).
Rules differ from checks: checks are *evaluated* at defined points; rules *hold everywhere*.
Failure prevented: standards drift in hour three of a long run.

## `<quality_bar>` — done, as a checklist

The definition of done made auditable: every placeholder resolved or logged · all HARD
checks pass, every SOFT flag noted · every deliverable re-opened and verified after creation ·
logs written · every presented number traceable to a source cell. The agent must satisfy it
before reporting done — and *you* can audit it in sixty seconds. Distinct from `<checks>`:
checks verify the **work** mid-run; the quality bar verifies **completeness** at the end.
Failure prevented: "done" meaning "I stopped."

## `<reporting>` — the interface back to you

The agentic Format for the *message*, fixed in shape: **status** (done / stopped at gate n /
blocked) · **headline answer with the number** · deliverable paths · checks summary ·
open items needing a human · risks. Under 25 lines; evidence, not assertions — the test it
ran and what it returned, not "everything went well." Details live in the files.
Failure prevented: a narrative essay where a status should be — and claims of success you
can't distinguish from hope.

---

# Part 3 — The mapping

The agentic brief is the generative anatomy **grown up to survive autonomy**:

| Generative element | Agentic descendant(s) | What was added, and why |
|---|---|---|
| Role | `<role>` | persists across unsupervised decisions → behaviors only |
| Task | `<mission>` | + definition of done — the loop needs an exit condition |
| Context | `<context>` + `<inputs>` | + a per-source register with grain & trust — agents touch every source repeatedly |
| Format | `<outputs>` + `<reporting>` | + audit logs and a fixed status shape — actions must be traceable |
| Examples | the filled brief (A2) | a worked run is the agentic few-shot |
| The Out | `UNKNOWN` → open items | not-knowing becomes a logged, owned item |
| The Stop | gates + autonomy rules | scope control becomes checkpointed process |
| *(none)* | `<environment>` `<plan>` `<checks>` `<rules>` `<quality_bar>` | **new in kind** — they govern conduct, method, verification, invariants, and completeness, which text-only prompts never needed |

**When to switch modes:** if the work involves files, tools, multiple steps, or a
deliverable produced while you're not watching — write the brief. If you'll read the output
and act on it yourself — the five elements and two valves are enough.

# Part 4 — Building your own templates

The meta-skill this library teaches: a template is *elements + reasons*, assembled against a
task's failure modes.

1. Name the task's three most expensive failure modes (wrong denominator? invented facts?
   unusable format? irreversible action?).
2. Pick the element that owns each failure (diagnosis grid, top of this file; reversibility →
   autonomy rules).
3. Write those elements strong; keep the rest light. A template where every element is
   maximal is a template nobody fills in.
4. Add one filled example — the gold standard teaches faster than the instructions do.
5. Test on 3–5 real cases (one edge case), version it, name an owner, add it to the library.
