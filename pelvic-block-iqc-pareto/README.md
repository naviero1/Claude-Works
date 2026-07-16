# Pelvic Block IQC — Pareto & Root-Cause Framework

Incoming Quality Control (IQC) analysis of **rejected porcine femoral pelvic blocks**.
The goal is to turn free-text scrap reasons into a repeatable Pareto + root-cause
framework that pinpoints **where in the supplier's process each defect is created**,
so corrective action can be taken *before* the eviscerated tissue block reaches us.

## The process (where a defect can be born)

Everything up to *"delivered to us"* is the **supplier's** (slaughterhouse) to control:

```
Live animal → S1 Sticking/Bleeding → S2 Bung dropping/Rodding → S3 Evisceration (knife + gut pull)
            → S4 Carcass splitting (saw) → S5 Handling & Pit drop → [ delivered to us ]
                                                                        │
                    OUR side:  harvest techs receive block from pit → spec-out / accept → IQC (this data)
```

## Files

| File | What it is |
|------|-----------|
| `Pelvic_Block_IQC_Pareto_RootCause.xlsx` | **Main deliverable.** 6-sheet workbook (below). Counts are formula-driven off the Inspection Log, so new batches update the Pareto/Dashboard automatically. |
| `source_IQC_Martins_failed_blocks_2026-07-08.xlsx` | Original IQC tally sheet, unchanged. |
| `Pareto_preview.png` / `Station_rollup_preview.png` | Static previews of the two key charts. |
| `build_workbook.py` | Reproducible builder (defect taxonomy + root-cause map live here). |

### Workbook sheets
1. **README** — how the framework works + process flow.
2. **Inspection Log** — master data, one row per block. *Append future inspections here.*
3. **Defect Taxonomy** — controlled vocabulary (D1–D10) + root-cause map (process step, supplier station, 6M cause, mechanism, corrective action).
4. **Pareto** — auto-calculating defect Pareto (chart) + rollup by supplier station.
5. **Root Cause 5-Why** — RCA template, seeded for the vital-few defects, with a Lessons-Learned column.
6. **Dashboard** — batch KPIs (yield, top defect, food-safety flags).

## This batch — SH: Martins, Kill/Harvest 2026-07-08

- **26 blocks inspected · 1 pass · 25 fail → First Pass Yield 3.8%**
- **53 defect occurrences** across 25 failed blocks (avg **2.1 defects/failed block**)

### Vital few (~79% of all defects)
| Rank | Defect | Count | % |
|------|--------|-------|---|
| 1 | Membrane damage in critical area (D6) | 16 | 30% |
| 2 | Ureters not embedded (D1) | 11 | 21% |
| 3 | Suspensory ligaments damaged (D4) | 8 | 15% |
| 4 | Urethra cut (D5) | 7 | 13% |

### Where they're born — rollup by supplier station
**77% of all defects (41 of 53) trace to one station: Evisceration (S3).** Carcass splitting (S4, urethra cuts) is a distant second at 13%. The supplier conversation should lead with **evisceration knife technique and gut-pull/traction handling in the pelvic zone.**

### Food-safety flag
Defects D6 (membrane breach) and **D8 (bowel cut/opened)** are *Critical* — a bowel breach is a fecal-contamination risk and should be treated as a CCP at the supplier's bung-dropping/evisceration station.

## Adding the next inspection
1. In **Inspection Log**, add one row per inspected block (metadata + Result + verbatim reason).
2. Put a `1` in each defect column (D1–D10) that applies. New defect type? Add it to **Defect Taxonomy** first.
3. Pareto + Dashboard recalc automatically. Re-sort the Pareto table high→low if the ranking shifts (counts are live; row order is not).
