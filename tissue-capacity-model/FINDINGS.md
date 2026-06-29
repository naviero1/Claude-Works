# Findings — data behind the intake

> Pulled directly from the two source workbooks during intake. These are the tables that feed the exec-summary slide and the mitigation list. Nothing here is a new model — it's extracted/organized from what's already in the files.

---

## 1. YTD attainment by tissue (Ask vs Achieved)

Source: `Weekly_goals…xlsx` → **`Year to date`** sheet (window 12/29/25 → 06/15/26). Sorted worst-attainment first. "Proj '26" = sheet's projected full-year harvest; "Proj %" = projected harvest ÷ projected demand.

| PN | Tissue | Lead house | YTD Ask | YTD Achieved | **Attain %** | Proj '26 % |
|---|---|---|---:|---:|:---:|:---:|
| 666540 | **Male Pelvic** | Martin | 1,400 | 242 | **17%** | 0.11 |
| 666536 | XL Hearts | Nahunta | 270 | 140 | **52%** | 1.08 |
| 666506 | **Pelvic Block Non-Intact** | Martin | 3,001 | 1,733 | **58%** | 0.89 |
| 666513 | Liver w/ Gallbladder | Custom | 210 | 130 | **62%** | 0.54 |
| 666541 | **Female Pelvic** | Martin | 5,860 | 4,320 | **74%** | 2.13 |
| 666530 | Stomach | Custom | 250 | 205 | 82% | 1.61 |
| 666502 | Bariatric | Martin | 4,156 | 3,716 | 89% | 1.57 |
| 666519 | Spleen | Nahunta/Custom | 696 | 616 | 89% | 1.47 |
| 666521 | Hearts | Nahunta | 592 | 525 | 89% | 1.53 |
| 666516 | Omentum | Nahunta/Custom | 618 | 554 | 90% | 0.77 |
| 666523 | Vena Cava | Martin/Custom | 648 | 583 | 90% | 1.39 |
| 666509 | Jejunum 6' | Nahunta | 950 | 881 | 93% | 1.25 |
| 666531 | Diaphragms | Nahunta/Custom | 320 | 297 | 93% | 1.75 |
| 666517 | Pancreas | Nahunta/Custom | 632 | 592 | 94% | 0.84 |
| 666522 | Ureters | all three | 4,525 | 4,320 | 95% | 0.97 |
| 666507 | Full Body | Nahunta | 400 | 392 | 98% | 1.39 |
| 666501 | Aorta | Martin | 6,021 | 5,871 | 98% | 0.92 |
| 666505 | Liver | Nahunta/Custom | 690 | 621 | 90% | 1.53 |
| 666511 | Kidney | Nahunta | 80 | 80 | 100% | 1.43 |
| | **TOTAL (all tissues)** | | **25,598** | **20,247** | **79%** | 1.10 |

**Read:** the four worst performers are **three Pelvic-family tissues at Martin** plus XL Hearts. Together they are the core of both the "risk vs demand" story and the mitigation list.

---

## 2. The 250-denominator re-graph (your slide note)

Today each tissue's attainment is measured against its *own* weekly ask, and those asks vary widely — so the bars aren't comparable:

| Tissue | Native avg ask/wk (All SH) | Avg harvested/wk |
|---|---:|---:|
| Aorta | 250.3 | 248.4 |
| Female Pelvic | 244.4 | 177.2 |
| Ureters | 188.2 | 185.0 |
| Pelvic Block Non-Intact | 122.9 | 74.6 |
| Bariatric | 172.5 | 158.1 |

*(Source: `Attainment & Alloc Summary`, Average mode, 25-week window.)*

Your fix: **hold the ask at a flat 250 for every tissue** and plot `harvested ÷ 250`. Same data, one common baseline:

| Tissue | Harvested/wk ÷ **250** |
|---|:---:|
| Aorta | 99% |
| Bariatric | 63% |
| Ureters | 74% |
| Female Pelvic | 71% |
| Pelvic Block Non-Intact | **30%** |

This makes the Pelvic shortfall visually obvious instead of being hidden by a smaller native ask. (When we build it, decide whether 250 is per-tissue-per-week or per-house-per-week — the weekly tabs hold both.)

---

## 3. Capacity headroom by tissue × supplier

Source: `Part_Supplier_RiskAssessmentTool_v2.xlsx` → **`Tissue_Model`**. "Headroom" = spare capacity multiple above current allocation (lower = tighter); Tier 1 simplest → 4 hardest; SourceDep = how many suppliers can make it.

Tightest / most exposed rows (lower headroom or single-source):

| PN | Tissue | Supplier | Tier | Wkly net | **Headroom** | Source dep |
|---|---|---|:---:|---:|:---:|---|
| 666506 | Pelvic Block | **Martins** | 2 | 52 | **1.01** | **Single** |
| 666541 | Female Pelvic | **Martins** | 2 | 164 | **1.67** | Multi (Martins+Parks) |
| 666502 | Bariatric | Martins | 3 | 125 | 1.20 | Dual |
| 666522 | Ureter | Martins | 2 | 86 | 1.20 | Dual |
| 666507 | Full Thor/Bari | Nahunta | 3 | 8 | 1.38 | — |
| 666516 | Omentum | Customs | 3 | 13 | 1.38 | — |
| 666523 | Vena Cava | Customs | 3 | 18 | 1.61 | — |

**Read:** Pelvic Block at Martins is both **single-sourced** and at **~1.0 headroom** (essentially no slack) — the highest-risk capacity row in the model.

---

## 4. Why the Pelvic Blocks miss — the yield mechanics

Source: `Yields-Labor-Cube` and the `Martins` capacity sheet. Most tissues harvest at **0.85–0.99**; the Pelvic family is far lower:

| Tissue | Martins harvesting yield | vs typical |
|---|:---:|:---:|
| Aorta (666501) | 0.95 | baseline |
| Bariatric (666502) | 0.95 | baseline |
| **Pelvic Block (666506)** | **0.25** | ▼ |
| **Female Pelvic (666541)** | **0.25** | ▼ |
| Male Pelvic (666540) | **0.05** | ▼▼ |

A 0.25 harvesting yield means **~75% of attempted Pelvic harvests are lost** before they ever reach spec/freeze-thaw. That is the quantified version of the boss's instruction to **"conduct a study at Martins for reasons for Harvest yield loss on Pelvic Blocks."** The `Martins` sheet also flags a **labor gap** ("Because of labor Gap at Martins") as a contributing constraint.

---

## 5. 2027 demand context (for the 125% question)

Source: `ModelsDemand_ToTissue`. Surgeon-model demand is forecast quarterly through **Q4'27 BP**; the BOM matrix converts a selected quarter into **Total Needed per tissue**. To answer *"risk of not meeting 125% of 2027 demand?"* the model needs:

1. Sum the four **2027 quarters** (Q1'27–Q4'27 BP) per tissue → annual 2027 tissue demand.
2. Multiply by **1.25**.
3. Compare against **annualized Ops-Ready throughput** (`Tissue_Model` col Y / headroom) summed across that tissue's suppliers.
4. Filter to **medium/high-risk** tissues only (drop low/no-risk per the ask).

The pieces all exist in the workbook; this comparison is the main build for the slide and is **not yet assembled**.

---

## Mitigation candidates (first cut)

In priority order, from the data above:

1. **Pelvic Block (666506) @ Martins** — single-source, ~1.0 headroom, 0.25 harvest yield, 58% YTD. → *Harvest-yield study at Martins (boss's named milestone).*
2. **Male Pelvic (666540) @ Martins** — 17% attainment, 0.05 harvest yield, projection only 11% of demand.
3. **Female Pelvic (666541) @ Martins** — 74% attainment, low headroom, same 0.25 yield family.
4. **XL Hearts (666536)** — 52% attainment.
5. **Liver w/ Gallbladder (666513) @ Customs** — 62% attainment, projected 54% of demand.

Each would get a mitigation step → milestone (yield study, second-source qualification, labor add at Martins, etc.) for the slide's second ask.
