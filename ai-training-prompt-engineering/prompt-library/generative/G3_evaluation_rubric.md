# G3 · Evaluations & Reviews (rubric grading, comparison, critique)

**Type:** Generative · **Version:** 1.0 · **Use when:** grading or comparing documents against criteria — supplier proposals, SOP drafts, reports, training materials, vendor responses — or stress-testing your own work/decisions.
**Works in:** any chat assistant. **Caution:** AI evaluation supports human judgment; for consequential calls (people, money, compliance) a human owns the final grade.

---

## Template A — Rubric grading (one document)

```text
<role>
You are a demanding but fair reviewer. You grade strictly against the rubric below — nothing
else. You justify every score with verbatim quotes from the document. Where the document is
silent on a criterion, score it 1 and say "not addressed" — do not give credit for what you
assume the author meant.
</role>

<rubric>
Score each criterion 1-5. Anchors: 1 = absent/wrong · 3 = adequate with gaps · 5 = complete,
specific, evidence-backed. (Adjust anchors per criterion if needed.)
1. {{criterion — e.g., "Technical capability: addresses our spec point by point"}}
2. {{criterion — e.g., "Risk handling: names failure modes and mitigations, not platitudes"}}
3. {{criterion}}
4. {{criterion}}
Weights: {{equal | list weights}}.
</rubric>

<task>
Grade the attached {{document type}} against the rubric.
</task>

<format>
Table: criterion | score | 1-2 verbatim quotes as evidence | what a 5 would have contained.
Then: weighted total, the 3 biggest gaps, and the 3 questions I should ask the author.
Do NOT soften. If the document is weak, say so plainly.
</format>
```

## Template B — Pairwise comparison (two or more options)

```text
Compare the attached {{proposals | drafts | options}} against the criteria below.

<criteria>{{list, with weights}}</criteria>

<method>
- Evaluate each independently first (short scorecard each, with quotes as evidence).
- Then compare head-to-head per criterion — name a winner per criterion, with the evidence.
- Do NOT let length, polish, or confident tone influence scores; substance only.
- If the order I attached them could bias you, state your conclusion, then re-check it
  imagining you had read them in reverse order.
</method>

<format>Scorecards → head-to-head table → recommendation with the 2 decisive factors →
what would change your mind.</format>
```

## Template C — Critique my work / decision (anti-sycophancy)

```text
I'm going to show you {{a draft | a plan | a decision I'm leaning toward}}. Do not tell me
whether you agree, and do not compliment it.

Your job:
1. Steelman the OPPOSITE position — the strongest honest case against this.
2. List the 3 weakest points, each with why it fails and how a critic would attack it.
3. What evidence, if it existed, would prove this wrong? Which of it should I check first?
4. Only after all that: your overall read, hedges included.

"""
{{the work / the decision and its context — do NOT say which option you prefer}}
"""
```

---

## What makes this work
- **Rubric before judgment.** Without criteria, an LLM grades on fluency and agrees with your framing. With anchored scales + "quotes as evidence," scores become checkable.
- **"Not addressed = 1"** blocks the model's habit of charitably filling gaps.
- **Independent-then-comparative** in Template B reduces position bias (models favor the first/last option read); the reverse-order recheck is a cheap debias.
- **Never reveal your preference.** Models measurably affirm the user's stated position (sycophancy); Template C withholds it and demands the counter-case first.
- **Known judge biases** to design around: verbosity bias (longer ≠ better), position bias, self-preference. Say explicitly that substance beats polish.

## Pitfalls
- Grading people (resumes, performance) — bias risk and often policy/regulatory territory. Don't, without HR/legal sign-off.
- One-pass evals of consequential choices: run twice (fresh chats), compare; disagreement = look closer yourself.
- Letting the AI write the rubric AND grade against it unsupervised — you've delegated the judgment twice. Own the rubric.
