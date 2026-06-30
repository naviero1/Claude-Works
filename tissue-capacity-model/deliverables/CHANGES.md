# Deliverables — flat-250 pelvic attainment + yield sensitivity

## Update — reverted to single combined pelvic line vs 250 (latest)

Per request, went back to the combined format and dropped the two per-tissue (170/60) graphs.

- **Slide 2: one weekly line** — `(666506 + 666518 + 666541) harvested ÷ 250/wk`, Martins only, 25 weekly points, with the dashed 100% (= 250) ask line. (666518 still all zeros.) This restores the prior combined-weekly chart exactly; slides 1 and 3 and the model are unchanged.
- **Weekly workbook:** the `Pelvic Attainment @250` tab now holds the combined weekly calc (506 + 518 + 541 vs 250); replaces the short-lived 170/60 tab. 18 charts preserved.

---

## Superseded — two pelvic graphs on revised asks (`_update063026` naming originated here)

- **Slide 2 now has TWO weekly charts side by side** (replacing the single combined line), each attainment = weekly harvested ÷ a per-tissue ask:
  - **Female Pelvic (666541) ÷ 170/wk** — line runs ~38–190%.
  - **Pelvic Block (666506) ÷ 60/wk** — line runs ~0–338% (small ask, so harvest often exceeds it); the two no-harvest weeks (12/29, 05/25) are shown as gaps.
  - Dashed grey line = 100% (the ask) on each. 666518 dropped (it was all zeros).
- **Weekly workbook:** new `Pelvic Attainment (170-60)` tab with the per-week harvested / ask / % for both tissues (18 charts preserved). The uploaded file is now canonical.
- Everything else (slide 1, slide 3, the labor-reallocation numbers, the model sheet) is unchanged from the prior iteration.
- Deck delivered as **`Tissue_Capacity_2026_2027_update063026.pptx`**.

---

## Update — labor reallocation + combined pelvic line

Built on the user's revised model (`1387ef2e-…RiskAssessmentTool_v2.xlsx`), now canonical.

- **Martins labor capacity changed: 36 → 40.5 h/wk** (daily 7.2 → 8.1; the only input the user changed). Downstream, per the Tissue_Model: **labor util 99% → 88%**, **labor headroom 1.01× → 1.14×**.
- **Consequence (important):** freezer is now **88%** too, so Martins is **labor/freezer co-limited at ~1.14×** — still below 125%. Because freezer is unaffected by harvest yield, **yield gains no longer move Martins' binding constraint** (overall stays ~1.14× until freezer is addressed). Updated the slide-1 table/headline/"what we're seeing", the slide-2 Martins card, the slide-3 sensitivity (labor-headroom column + "how to read"), and the model's `Pelvic Yield Sensitivity` sheet to reflect this.
- **Slide-2 chart = ONE WEEKLY pelvic line:** `(Pelvic Block 506 + SM Intact 518 + Female Pelvic 541) ÷ 250/wk`, 25 weekly points (switched from biweekly). **666518 is currently all zeros** in the weekly data, so it's in the formula but doesn't move the line. Because the pelvic codes share a single 250 ask, the line frequently sits **above 100%** (combined pelvic output often exceeds 250/wk). Weekly series: `70, 106, 66, 59, 70, 98, 47, 86, 115, 139, 110, 150, 65, 66, 98, 153, 158, 124, 121, 125, 162, 76, 108, 49, 97`.

---


Updated copies of the three source files. Originals remain untouched in [`../source-files/`](../source-files/).
Pelvic scope throughout: **666506 (Pelvic Block Non-Intact) and 666541 (Female Pelvic), at Martin.**

---

## `Tissue_Capacity_2026_2027.pptx`  (3 slides)

> **Current baseline = your revision** (uploaded as `Tissue_Capacity_2026_2027_2.pptx`, 2026-06-29). It keeps everything below and adds your manual edits: milestone-1/2 **progress notes** ("Started… 30 samples/wk for 4 weeks"; "Already root-causing yield spec fails"), the **"Slaughter House" / "Cap type – Tissue family"** legend labels on the slide-1 table, and **"Seasonality"** added to the slide-2 culprits. Future deck edits build on this file.

**Slide 2 — pelvic attainment chart**
- Re-pointed to the **flat-250** basis (`% = harvested ÷ 250`); the "Ask (100%)" line now represents the 250/wk standard.
- **Zeros excluded:** each biweekly point now averages only weeks with harvest > 0, so an off-week no longer halves the point. Only 666506 was affected (weeks 12/29 and 05/25); 666541 had no zero weeks.
  - Female Pelvic (541's): `48, 56, 52, 54, 87, 115, 62, 108, 86, 69, 79, 49`
  - Pelvic Block (506's): `80, 7, 32, 13, 40, 15, 4, 17, 55, 54, 81, 29`
- Fixed the mislabeled series ("Female Pelvic (506's)" → **"Pelvic Block (506's)"**); title/footnote updated to the new basis.

**Slide 1 — inviting finding added**
- The highlighted answer paragraph now carries a one-line sensitivity finding that points to the analysis: *"Lifting pelvic harvest yield pays back hard: +10 pts (25%→35%) frees ~246 pigs & ~4.8 labor-hrs/wk at Martins, and ~+20 pts (→45%) finally clears 125% on labor — see slide 3."*

**Slide 3 — NEW, reference only**
- A clean, themed table of the pelvic harvest-yield sensitivity (the backup for the slide-1 finding). Headroom cells are color-coded (green ≥ 1.25×, red below).

---

## `Part_Supplier_RiskAssessmentTool_v2.xlsx`  (the model)

- **New sheet: `Pelvic Yield Sensitivity`** — a formatted, standalone version of the same analysis "in case you need to show someone." Navy header, highlighted base row, color-coded headroom, thin borders, merged title/notes.
- Injected surgically with its styles added to `styles.xml`; all **6 existing charts** and the conditional formatting / data validation are preserved.

## `Weekly_goals_2026_SUMMARY_062426.xlsx`

- **`Attainment @250 (Pelvics)`** tab regenerated so the biweekly block matches the slide chart (zeros excluded). Weekly detail still shows raw weeks (0 = no harvest, excluded from the biweekly average). All **18 charts** preserved.

---

## The sensitivity analysis (how it was computed)

Follows the **Tissue_Model formulas exactly** (validated to reproduce the model's own outputs):
- `Pigs Consumed (O) = ROUND(Net Harvest J ÷ Harvest Yield N)` → higher yield, fewer pigs.
- `Planned Labor (Q) = J × min/60 + (O − J) × 7/360` → the `(O − J)` term is the **rework on every wasted pig**, so higher yield cuts labor too.

Improvements are in **percentage points** above the 25% base (i.e. +10 pts → yield 0.35). Aggregated at Martins (labor cap 36 h; non-pelvic Martins labor 12.13 h fixed):

| Yield gain | Yield | Pigs freed/wk | Labor freed/wk | Labor headroom | Pig headroom |
|---|---|---|---|---|---|
| Today | 25% | — | — | 1.01× | 1.23× |
| +5 pts | 30% | 144 | 2.8 h | 1.10× | 1.46× |
| +10 pts | 35% | 246 | 4.8 h | 1.17× | 1.68× |
| +15 pts | 40% | 324 | 6.3 h | 1.23× | 1.90× |
| +20 pts | 45% | 384 | 7.5 h | **1.28×** | 2.12× |
| +25 pts | 50% | 432 | 8.4 h | 1.33× | 2.33× |

**Finding:** the **pig** constraint clears 125% immediately, but **labor** — the binding constraint at Martins — needs about **+20 points (yield to 45%)** to cross 1.25× (1.28×). Yield is the lever, but a sizeable lift is required, so pair the yield study with re-balancing labor off Martins (Milestone 3).

> Modeled as percentage points (per your call). Relative gains (25% × 1.10) are available instead — one-line change.
