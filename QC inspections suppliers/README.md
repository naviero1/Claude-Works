# QC Inspections — Suppliers

Incoming-quality-control (IQC) data for tissue harvested at the slaughterhouse (SH), by supplier/slaughterhouse and **tissue type**. Post-freeze **ATM** (receipt) quality data will be added here when it arrives.

## Files

- **SH_IQC_Inspections.xlsx** — master workbook (current). SH-floor IQC inspections, Apr 13 – Aug 19 2026, across Martins, Parks and Nahunta. (Renamed from `Pelvic_Blocks_Quality_*`; earlier versions are in git history.)

## Workbook map

| Sheet | Purpose |
|---|---|
| `Slaughterhouse IQC` | The core: one product-agnostic **Inspection Log** — one row per part per harvest date, all tissue types (Pelvic 666541/506/518, Thoracic 666521, …). Then **Totals by Tissue Type** + a grand total, an **ATM Receipt Comparison** placeholder (for future ATM data), and data notes. |
| `Quality Dashboard` | Live first-pass-yield views by **Tissue Type**, by **Part**, and by **Slaughterhouse**, with FPY/scrap heatmaps and a tissue/part read. All figures pull live from the Inspection Log. |
| `Monthly Breakdown` | Month-by-month (Apr–Aug) view per tissue × slaughterhouse × part combo: FPY + fails overview matrices, then a detail block per combo with volumes and **issues found**, normalized into standard defect categories (urethra/bladder, membrane, bowel, short/mesentery, critical-area, ureter, lung, heart, other). Volume rows live; defect tags analyst-coded from scrap notes. |
| `SH vs ATM by Batch` | Batch-to-batch comparison for lots inspected at both stages (matched on batch number): SH sample results vs ATM full-batch receipt review, with both inspection dates, the SH→ATM review lag in days, ATM scrap reason codes per batch (matrix + full code legend). 12 matched batches (Martins 666541 + Nahunta 666521). |
| `Apr 2026` … `Aug 2026` | One tab per month: month summary by tissue × slaughterhouse (with top defect), the month's most recurring defects ranked per combo (count, % of fails, data bars), and the full list of that month's inspections. Static snapshots — extend with a new month tab as data arrives. |
| `SmartAssessment` | Working analyst notes: stage/yield model, root-cause findings, spec corrections, caveats, next steps. Verify with Quality before external use. (May lag the latest data.) |
| `Defect Atlas` | Visual reference per defect category (photos). |

## Updating with new SH IQC tally sheets

Add to the **Inspection Log** on `Slaughterhouse IQC`: one row per part per harvest date — Harvest Date, Slaughterhouse, Inspector, SH Tech, **Tissue Type**, Part #, Description, Lot, then `# Inspected / Pass / Fail` + scrap reason. First-Pass Yield is a formula (`=IFERROR(J/I,0)`). Keep rows in date order. The **Totals by Tissue Type**, grand total, and the whole **Quality Dashboard** are driven by `SUMIF`/`SUM` over the log range and update automatically as the log grows.

New tissue types (e.g. thoracic, bariatric) are first-class — just set the **Tissue Type** column. New parts appear automatically in the by-part views once added to the dashboard's part list.

Convention: people are referred to by **first name only** throughout the workbook and decks (no last names).

When appending log rows, also tag the new fails into the defect categories on the `Monthly Breakdown` tab (its volume rows update live; the category counts are manual).

Recurring interpretation calls to flag rather than guess: tally counts that don't foot (inspected ≠ pass + fail), sheets that combine two harvest days without splitting counts, lot numbers carried over from a prior week, PN typo normalization (e.g. 668518 → 666518), and date-field typos (trust the filename/kill date). Re-sent sheets are matched to existing rows so nothing is double-counted.

## ATM quality data (coming)

ATM = post-freeze **receipt** inspection, when product is received here (product sits frozen ~1–1.5 months first). ATM data no longer carries batch/lot numbers, so it will be compared by **tissue type / part and time window** rather than by lot. The `ATM Receipt Comparison` block on the Slaughterhouse IQC tab is reserved for it. (The legacy ATM-side analysis tabs and the ATM Tableau tab were removed in the redesign; they remain in git history.)
