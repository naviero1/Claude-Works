# G2 · Data Analysis (in chat)

**Type:** Generative · **Version:** 1.0 · **Use when:** you attach a dataset (csv/xlsx) to a chat and want trustworthy answers — summaries, trends, comparisons, charts.
**Works in:** Claude (analysis/file creation), ChatGPT (Advanced Data Analysis), Copilot Excel, Gemini.
**For multi-source / recurring / high-stakes pipelines, use the agentic version instead: `../agentic/A2_etl_to_presentation.md`.**

---

## The template

```text
<role>
You are a careful data analyst. You compute every number by running code — never mental
arithmetic. You state n for every proportion, you never drop data silently, and you say
"the data can't answer that" when it can't.
</role>

<data>
Attached: {{file name(s)}}.
Sheet/tab: {{name}} · Header row: {{n}} · One row = {{what a row means — e.g., "one inspected unit"}}.
Columns that matter (exact names): {{ColA — meaning/units; ColB — ...}}
Known issues: {{totals rows at bottom, merged cells, codes with leading zeros, mixed units, ...}}
Glossary: {{METRIC = numerator / denominator, exactly as our org defines it}}
</data>

<task>
Answer these questions, in order, and stop when they're answered — do not go exploring:
1. {{primary question — e.g., "What is X overall and by group for period P?"}}
2. {{trend/comparison question}}
3. [optional] {{driver question — e.g., "Which categories dominate (Pareto)?"}}
</task>

<method>
- First: profile the data (rows, columns, date range, nulls in key fields, duplicates) and
  show me the profile BEFORE analyzing. If the structure differs from <data>, stop and ask.
- All numbers via code execution. Show row counts for anything you exclude, and why.
- Descriptive statistics only. No causal language — "associated with", never "caused by".
- Flag any group with n < {{20}} as small-sample; show n on every proportion.
- If numbers must reconcile to a known total ({{e.g., "1,204 orders in Q2"}}), verify and
  show the reconciliation before answering.
</method>

<format>
- Headline answer first (one sentence, with the number), then the supporting table.
- Charts: {{chart type if you care}}, axis labels with units, sorted {{descending}},
  target line at {{value}} if relevant. One message per chart.
- End with: assumptions you made, and the 2-3 caveats that most threaten the conclusion.
</format>
```

## Filled example (generic)

```text
<role>You are a careful data analyst. All numbers via code; state n; no silent exclusions.</role>
<data>Attached: returns_q2.xlsx, sheet "Raw", header row 1. One row = one returned unit.
Columns: return_date (date), site (A/B/C), reason_code (string, leading zeros matter),
units (int). Known issue: a totals row at the bottom — exclude it and say so.
Glossary: Return rate = returned units / shipped units; shipped units are in shipped_q2.csv.</data>
<task>1. Return rate by site for Q2, vs the 2.0% target. 2. Top reason codes (Pareto) —
which 3 codes cover 80%? </task>
<method>Profile first and show it. Reconcile: total returns must equal 1,204 (ops report).
Flag n<20. Descriptive only.</method>
<format>Headline first; one bar chart by site with 2.0% target line; n labels; caveats at the end.</format>
```

## What makes this work
- **Code, not vibes:** LLMs are unreliable at multi-digit arithmetic; with code execution the model writes and runs a script, so the math is real. If your tool can't run code, don't trust computed numbers.
- **Schema-first:** naming exact columns and what one row means eliminates the top source of wrong answers (the model guessing your grain and denominator).
- **Profile-before-analyze** catches structure surprises (totals rows, second header) at the cheap end.
- **Reconciliation to a number you already trust** anchors everything else. One anchor beats ten checks.
- **Numbered questions with a stop** prevent the ten-charts-no-answer failure mode.

## Pitfalls
- Asking "any insights?" — you'll get plausible narrative, not analysis. Ask questions.
- Accepting a correlation as a cause; ask "what else could explain this?" before presenting.
- Letting the model "clean" data silently. Every exclusion needs a row count and a reason.
- Copying a number off a chat into a deck without the reconciliation check.
