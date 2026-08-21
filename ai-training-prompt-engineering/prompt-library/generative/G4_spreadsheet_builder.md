# G4 · Spreadsheets (build, clean, formula help)

**Type:** Generative · **Version:** 1.0 · **Use when:** creating a workbook from data or a description, cleaning a messy sheet, or getting formulas written and explained.
**Works in:** Claude (file creation, Claude for Excel), ChatGPT (+ Excel add-in), Copilot in Excel (Agent Mode), Gemini in Sheets.

---

## Template A — Build a workbook

```text
<task>
Build an .xlsx workbook: {{one line — what it is for and who reads it}}.
</task>

<data>
{{attach source file(s) or paste the table; name sheet + header row; say what one row means}}
</data>

<structure>
Tab 1 "README": purpose, data sources with as-of date, every metric defined
(numerator/denominator), assumptions, and a change log row per version.
Tab 2 "{{Data}}": the clean row-level data — one header row, no merged cells, one row = {{grain}},
codes stored as text (leading zeros preserved), dates as real dates ({{ISO}}).
Tab 3 "{{Summary}}": {{the pivot/aggregate view — rows, columns, metrics}}.
[optional] Tab 4 "{{Dashboard}}": {{charts — one message per chart, titles state the finding}}.
</structure>

<rules>
- Formulas, not pasted values, wherever a number derives from the data — I need it to update.
- No hidden columns/rows; no merged cells in data ranges.
- Conditional formatting: {{e.g., red when below target X}}.
- Validate before finishing: totals on Summary reconcile to Data row counts; show me the check.
</rules>
```

## Template B — Clean a messy sheet

```text
The attached sheet is messy. Clean it into a proper table WITHOUT changing any values:
- One header row; unmerge everything; remove blank/decoration rows and typed totals rows
  (recompute totals instead — tell me if they don't match the typed ones).
- Normalize: {{dates to ISO; site names per this list: {{...}}; codes as text}}.
- Do not deduplicate, impute, or "fix" outliers — list suspected duplicates/oddities
  separately for my review.
Deliver: the cleaned file + a change log (every rule applied, rows affected) + an issues list.
```

## Template C — Formula help (in Excel/Sheets)

```text
In {{Excel | Google Sheets}}: my table {{name/range}} has columns {{exact names, e.g.,
"C = Ship Date (date), F = Qty (number), H = Site (text)"}}.
Write a formula for cell {{X}} that {{plain-language goal, e.g., "sums Qty for Site 'A'
shipped in July"}}.
Explain it piece by piece BEFORE I insert it, note versions ({{365 | 2019}}) if it matters,
and give me one test I can do by hand on 3 rows to confirm it's right.
```

---

## What makes this work
- **Exact column names** — the single highest-leverage habit for spreadsheet prompts (it's Microsoft's own #1 Copilot-in-Excel tip). "The date column" is a guess; "C = Ship Date" is a spec.
- **README tab as part of the deliverable**: definitions and assumptions travel with the file, so the workbook survives handoff.
- **"Values unchanged, rules logged"** turns cleaning from silent mutation into an auditable transform.
- **Formula explained + hand-check on 3 rows** catches the classic near-miss formula before it ships.

## Pitfalls
- Accepting a workbook without opening it: check 3-5 numbers against source by hand, always.
- Letting the model paste computed values where formulas belong — the file dies on first data update.
- Merged-cell "pretty" layouts in data tabs — they break sorting, pivots, and every future analysis.
- Uploading sheets with hidden confidential tabs — the model reads the whole file, not just the tab you mean.
