# The Fast-Casual Compendium — second edition

A rebuilt and verified version of *The Thirty · A Fast-Casual Nutrition Compendium*
(Research Triangle, North Carolina), covering delivery dishes scored on seven health
criteria plus flavor and cost.

## What is here

| File | What it is |
|---|---|
| `dataset.json` | The full machine-readable dataset: 60 entries with all nine criterion scores, macros, price, DoorDash store id, build description, and 116 scored alternative orders with their columns separated. |
| `compact.json` | The same 60 entries without the alternatives, plus precomputed derived metrics (health per dollar, sodium per gram of protein, and so on). |
| `source-v1.txt` | Extracted text of the first edition, for reference. |
| `build/` | Everything that generates the second edition. |

## How the second edition is built

Nothing in the document is typed by hand. The pipeline is:

```
details_cu.json ─┐
corrections_v1.json ─→ apply_corrections.py ─→ details_corrected.json
                                                      │
                                     figures.py ──────┴──→ figures.json
                                                      │
                          charts.py, score.py, style.css
                                                      │
                                        build.py ─────┴──→ compendium.html
```

* **`score.py`** — the scoring model, recovered by fitting the first edition's own
  published scores. Feeding the published macros back through it reproduces all 60
  printed overall scores to within 0.10 (mean deviation 0.023), so new entries can be
  scored on exactly the same basis as old ones.
* **`apply_corrections.py`** — applies verified corrections and rescores the affected
  entries. Every correction carries the source it was checked against.
* **`figures.py`** — computes every statistic the document prints, including the
  correlations, the leave-one-out robustness checks, the Welch tests, and the searched
  weekly rotations.
* **`charts.py`** — generates the inline SVG charts, themed through CSS custom
  properties so they work in light and dark.
* **`build.py`** — assembles the page.

## Rebuilding

```sh
cd build
python3 apply_corrections.py   # rescore against verified figures
python3 figures.py             # recompute every printed statistic
python3 build.py               # emit compendium.html
```

## The recovered scoring model

```
KID    = clamp(10 × (2000 − sodium_mg) / 1650)
SUG    = clamp(10 × (22 − sugar_g) / 19)
MUS    = 0.7 × clamp(10 × (protein/(cal/100) − 2) / 7)
       + 0.3 × clamp(10 × (protein_g − 20) / 25)
LIV    = 0.65 × clamp(10 × (16.5 − satfat_g) / 14.5)
       + 0.35 × clamp(10 × (1000 − cal) / 500)
COST   = 0.6 × clamp(10 × (35 − price) / 25)
       + 0.4 × clamp(10 × (0.90 − price/protein_g) / 0.65)
FLAVOR = (char 0–3 + acid 0–2 + ferment 0–2 + aromatics 0–3
          + richness 0–2 + texture 0–2 − strip penalty 0–3) / 14 × 10

GUT, ENE and INF are rubric judgements and are not derivable from the macros.

health  = (KID + LIV + MUS + GUT + ENE + INF + 0.7×SUG) / 6.7
overall = (health×6.7 + FLAVOR×0.5 + COST×0.5) / 7.7
```
