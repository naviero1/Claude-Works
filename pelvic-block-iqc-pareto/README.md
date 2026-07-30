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
| `source_IQC_Martins_failed_blocks_2026-05-27.xlsx` | Original IQC tally sheet (kill 2026-05-27). |
| `source_IQC_Martins_failed_blocks_2026-07-08.xlsx` | Original IQC tally sheet (kill 2026-07-08). |
| `source_IQC_Martins_failed_blocks_2026-07-28_rasmin.xlsx` | Original IQC tally sheet (kill 2026-07-28, inspector Rasmin). |
| `source_IQC_Martins_failed_blocks_2026-07-28_toni.xlsx` | Original IQC tally sheet (kill 2026-07-28, inspector Toni). |
| `Pareto_preview.png` / `Station_rollup_preview.png` | Static previews of the two key charts (combined). |
| `build_workbook.py` / `make_previews.py` | Reproducible builders (defect taxonomy + root-cause map live in `build_workbook.py`). |

### Workbook sheets
1. **README** — how the framework works + process flow.
2. **Inspection Log** — master data, one row per block. *Append future inspections here.*
3. **Defect Taxonomy** — controlled vocabulary (D1–D11) + root-cause map (process step, supplier station, 6M cause, mechanism, corrective action).
4. **Pareto** — auto-calculating defect Pareto (chart) + rollup by supplier station.
5. **Root Cause 5-Why** — RCA template, seeded for the vital-few defects, with a Lessons-Learned column.
6. **Dashboard** — combined KPIs + a per-batch breakdown to watch the trend.

## Data so far — SH: Martins (4 inspection sheets, 3 kill dates)

| Kill date | Inspected | Pass | Fail | First Pass Yield | Top defect |
|-----------|-----------|------|------|------------------|-----------|
| 2026-05-27 | 31 | 8 | 23 | **25.8%** | Membrane damage (15) |
| 2026-07-08 | 26 | 1 | 25 | **3.8%** | Membrane damage (16) |
| 2026-07-28 *(Rasmin + Toni)* | 42 | 1 | 41 | **2.4%** | Membrane damage (18) |
| **Combined** | **99** | **10** | **89** | **10.1%** | Membrane damage (49) |

- **122 defect occurrences** across 89 failed blocks (avg **1.4 defects/failed block**).
- Yield **collapsed and stayed low** across the three kill dates (25.8% → 3.8% → 2.4%) — a sustained trend to raise with the supplier, not a one-off.
- The two 2026-07-28 sheets (inspectors Rasmin & Toni) are aggregated under the single 07-28 kill date; inspector names are preserved in the log's Inspector column.

### Vital few (~80% of all defects)
| Rank | Defect | Count | % |
|------|--------|-------|---|
| 1 | Membrane damage in critical area (D6) | 49 | 40% |
| 2 | Ureters not embedded (D1) | 17 | 14% |
| 3 | Urethra breach — cut/laceration/hole/separation (D5) | 14 | 11% |
| 4 | Bowel/colon/rectum breach (D8) | 9 | 7% |
| 5 | Suspensory ligaments damaged (D4) | 8 | 7% |

### Where they're born — rollup by supplier station
**84% of all defects (102 of 122) trace to one station: Evisceration (S3).** Carcass splitting (S4 — urethra breaches + bladder-neck separation) is second at 12%. Lead the supplier conversation with **evisceration knife technique and gut-pull/traction handling in the pelvic zone**, then splitting-saw alignment.

### Food-safety flag
D6 (membrane breach) and **D8 (bowel/colon/rectum breach)** are *Critical* — a bowel/colon/rectum breach is a fecal-contamination risk and should be a CCP at the supplier's bung-dropping/evisceration station. Bladder breach (D12) is a urine-contamination concern (Major).

### Open items (pending disposition)
1. 5 blocks from the 2026-05-27 batch — *8″ hole in the bladder suspensory ligament, ureter intact* — recorded as **Pass** pending ME/DE determination (per tally-sheet note). If reclassified Fail, tag **D4**.
2. Rasmin's 2026-07-28 sheet handwritten total read *"1 Pass / 22 failures"*, but the per-row entries sum to **29 fails** — the granular rows were used. Worth confirming with the inspector.

## Taxonomy changes (as new batches were ingested)
- **Added D11 — Bladder neck separation**, **D12 — Bladder cut/hole (breach)**, **D13 — Block too short/undersized** (new defect modes).
- **Broadened D5** "Urethra cut" → "Urethra breach (cut / laceration / hole / separation)".
- **Broadened D8** "Bowel cut/opened/separated" → "Bowel / colon / rectum breach".

## Adding the next inspection
1. In **Inspection Log**, add one row per inspected block (metadata + Result + verbatim reason).
2. Put a `1` in each defect column (D1–D11) that applies. New defect type? Add it to **Defect Taxonomy** first.
3. Pareto + Dashboard recalc automatically. Re-sort the Pareto table high→low if the ranking shifts (counts are live; row order is not).
