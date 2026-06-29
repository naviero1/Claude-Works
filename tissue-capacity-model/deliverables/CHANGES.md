# Deliverables — flat-250 pelvic attainment + yield sensitivity

Updated copies of the three source files. Originals remain untouched in [`../source-files/`](../source-files/).
Pelvic scope throughout: **666506 (Pelvic Block Non-Intact) and 666541 (Female Pelvic), at Martin.**

---

## `Tissue_Capacity_2026_2027.pptx`  (3 slides)

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
