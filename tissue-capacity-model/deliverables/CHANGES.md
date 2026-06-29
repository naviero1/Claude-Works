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
- The highlighted answer paragraph now carries a one-line sensitivity finding that points to the analysis: *"+10% harvest yield frees ~79 pigs and ~1.5 labor-hrs/wk at Martins — see slide 3."*

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

Improvements are **relative** to the 25% base (i.e. +10% → yield 0.275). Aggregated at Martins (labor cap 36 h; non-pelvic Martins labor 12.13 h fixed):

| Yield gain | Yield | Pigs freed/wk | Labor freed/wk | Labor headroom | Pig headroom |
|---|---|---|---|---|---|
| Today | 25.0% | — | — | 1.01× | 1.23× |
| +5% | 26.3% | 41 | 0.8 h | 1.04× | 1.29× |
| +10% | 27.5% | 79 | 1.5 h | 1.06× | 1.35× |
| +15% | 28.8% | 113 | 2.2 h | 1.08× | 1.40× |
| +20% | 30.0% | 144 | 2.8 h | 1.10× | 1.46× |
| +25% | 31.3% | 173 | 3.4 h | 1.12× | 1.52× |

**Finding:** yield gains clear the **pig** constraint past 125% almost immediately (+5%), but **labor** — the binding constraint at Martins — only reaches 1.12× even at +25%. Yield helps materially, but labor still needs re-balancing off Martins (Milestone 3).

> If you meant harvesting-yield improvement in **percentage points** (25% → 35% at "+10%") rather than relative, it's a one-line change — the numbers get substantially larger (e.g. +10pts frees ~246 pigs/wk). Say the word.
