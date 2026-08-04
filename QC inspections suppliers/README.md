# QC Inspections — Suppliers

Compiled incoming-quality-control (IQC) and ATM quality data for pelvic block tissue, by supplier/slaughterhouse.

## Files

- **Pelvic_Blocks_Quality_062626.xlsx** — master workbook (current). Compiled 06/26/26; SH IQC visits 1–14 (through harvest 06/25/26). Supersedes the 06/10 version (kept in git history).

## Workbook map

| Sheet | Stage | Purpose |
|---|---|---|
| `Slaughterhouse IQC` | **Pre-freeze** | Product-agnostic SH-floor inspection log — one row per part per harvest date, all families (pelvic 666541/506/518, thoracic 666521, …). Family subtotals + a grand total, then the SH→ATM comparison and data notes. Self-contained — does *not* feed the ATM-side sheets below. |
| `SmartAssessment` | Analysis | Claude's working analyst notes: objective, stage/yield model, root-cause findings (incl. the Parks 05/11 event), defect-origin tagging, spec corrections, caveats, and recommended next steps. Verify with Quality before external use. |
| `Quality Dashboard` | Analysis | Live first-pass-yield views by **Product Family** (Pelvic Block / Thoracic), by **Part** (666541/506/518/521), and by **Slaughterhouse** (Martins/Parks/Nahunta), with FPY/scrap heatmaps and a part-by-part read. All figures pull live from the Inspection Log. |
| `Master Data` | Post-freeze (ATM) | Long-format defect log — one row per (date × lot × defect). Single source of truth for everything below it. |
| `Receipt Summary` | Post-freeze (ATM) | One row per receipt event with totals + rejection rate. |
| `Defect Pivot 666541-F / 666540-M / 666518-F` | Post-freeze (ATM) | Defect × date pivots per part, SUMIFS off `Master Data`. |
| `Defect Trends- ATM` | Post-freeze (ATM) | Defect-centric trend view per slaughterhouse. |
| `Supplier Comparison` | Post-freeze (ATM) | Martins vs Parks side-by-side. |
| `Defect Atlas` | Reference | Visual reference per defect category. |

## Updating with new SH IQC tally sheets

The `Slaughterhouse IQC` sheet is one product-agnostic **Inspection Log** plus rollups. To add a visit:

1. **Inspection Log** — add one row per part per harvest date: Harvest Date, Slaughterhouse, Inspector, SH Tech, Product Family, Part #, Description, Lot, then `# Inspected/Pass/Fail` + scrap reason. First-Pass Yield is a formula (`=IFERROR(J/I,0)`); keep rows in date order and extend the log range (`$…$6:$…$49`) used by the totals if you add rows.
2. **Totals by Product Family** — driven by `SUMIF` over the log; the grand total covers all families. No manual edits unless the log range grows.
3. **SH → ATM Yield Comparison** — batch-tracked intact lots only (Martins 666541); ATM columns stay 0 until the matching receipt arrives.
4. **Notes** — append any judgment calls.
5. The **Quality Dashboard** tab updates automatically (by Family / Part / Slaughterhouse).

Recurring interpretation calls to flag rather than guess: tally counts that don't foot (inspected ≠ pass + fail), tally sheets that combine two harvest days without splitting counts, lot numbers carried over from a prior week, and PN typo normalization (e.g. 668518 → 666518). New product families (e.g. thoracic 666521) are first-class — just set the Product Family column.

## ATM quality data (no batch numbers)

The ATM quality data no longer carries batch/lot numbers, so it can't be split by supplier. The earlier Tableau-scrap tab was removed; ATM figures now live only in the ATM-side analysis tabs.
