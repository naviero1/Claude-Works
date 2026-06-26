# QC Inspections — Suppliers

Compiled incoming-quality-control (IQC) and ATM quality data for pelvic block tissue, by supplier/slaughterhouse.

## Files

- **Pelvic_Blocks_Quality_062626.xlsx** — master workbook (current). Compiled 06/26/26; SH IQC visits 1–14 (through harvest 06/25/26). Supersedes the 06/10 version (kept in git history).

## Workbook map

| Sheet | Stage | Purpose |
|---|---|---|
| `Slaughterhouse IQC` | **Pre-freeze** | SH-floor inspections by ATM inspectors. Self-contained — does *not* feed the sheets below. Source for the tally sheets the quality techs send in. |
| `Master Data` | Post-freeze (ATM) | Long-format defect log — one row per (date × lot × defect). Single source of truth for everything below it. |
| `Receipt Summary` | Post-freeze (ATM) | One row per receipt event with totals + rejection rate. |
| `Defect Pivot 666541-F / 666540-M / 666518-F` | Post-freeze (ATM) | Defect × date pivots per part, SUMIFS off `Master Data`. |
| `Defect Trends- ATM` | Post-freeze (ATM) | Defect-centric trend view per slaughterhouse. |
| `Supplier Comparison` | Post-freeze (ATM) | Martins vs Parks side-by-side. |
| `Defect Atlas` | Reference | Visual reference per defect category. |

## Updating with new SH IQC tally sheets

The `Slaughterhouse IQC` sheet has five blocks. To add a visit:

1. **Inspection Metadata** — add a Visit row (dates, SH, inspector, SH tech, intact/non-intact lots + PNs).
2. **Raw Inspection Data** — one row per harvest-date × lot × condition. Enter `# Inspected/Pass/Fail` + scrap reason only; First Pass Yield is a formula (`=IFERROR(H/G,0)`).
3. **Batch-Level Rollup** — one row per lot aggregated across harvest dates; extend the TOTAL `SUM` range.
4. **SH → ATM Yield Comparison** — add rows (ATM columns stay 0 until the matching ATM receipt arrives).
5. **Notes** — append any judgment calls.

Recurring interpretation calls to flag rather than guess: tally sheets that combine two harvest days without splitting counts, lot numbers that look carried-over from a prior week, and PN typo normalization (e.g. 668518 → 666518).

## ATM quality data (no batch numbers)

Going forward the ATM quality data will no longer carry batch/lot numbers. Plan is a separate sheet populated/inferred from Tableau exports — TBD.
