# Tissue Capacity Model — Intake

**Status:** Intake only (files ingested, understood, and documented). No analysis deliverables built yet.
**Branch:** `claude/tissue-capacity-model-intake-3ptz7p`
**Intake date:** 2026-06-29

---

## What this is

A by-part / by-supplier **capacity and supplier-risk model** for porcine **tissue components** used to build **surgeon-training models**. Demand for the training models is decomposed (via a bill-of-materials) into individual tissue part numbers, those tissues are **allocated across four slaughterhouses**, and each slaughterhouse is capacity-checked against pigs, labor, and freezer constraints, then weighted by **harvesting / spec / freeze-thaw yields**.

Two source workbooks were intaken (originals in [`source-files/`](source-files/)):

| File | What it is |
|---|---|
| `Part_Supplier_RiskAssessmentTool_v2.xlsx` | The **capacity + supplier-risk model**. Holds the demand→tissue BOM, slaughterhouse allocations, per-tissue yields/labor, per-slaughterhouse capacity math, and the supplier risk scorecards (`Tissue_Model`, `Part_Model`). |
| `Weekly_goals_2026_SUMMARY_062426.xlsx` | The **weekly harvesting actuals**: per-week "Ask vs Achieved" by slaughterhouse and tissue, rolled up into attainment %, YTD, and 2026 projections. This is the source of the attainment data the boss's slide is built from. |

> Note: the two `Weekly_goals` uploads were byte-identical (same MD5 `d79b677...`), so only one copy is kept.

---

## The ask (from "Goal updates", boss's note)

> **Executive summary** — single slide with the **by-part supplier capacity for tissue components** (exclude low-risk, no-risk components) **relative to 2027 demand**. **Do we have risk of not meeting 125% of 2027 demand?** Due **next Wednesday (2/24)**.
>
> **What are the next suppliers/parts that show as needing mitigation plans** from your supplier risk analysis and capacity assessment? Could we indicate those mitigation steps as next milestones?
> - **Conduct study at Martins for reasons for Harvest yield loss on Pelvic Blocks.**

## Your slide notes

- On the attainment chart: **use a consistent denominator of 250** instead of each tissue's own weekly "ask." In the weekly file every tissue/house has a different ask vs attainment, which makes the bars non-comparable. Re-graphing attainment as **harvested ÷ 250** puts every tissue on the same baseline. *(See `FINDINGS.md` for a worked example.)*

> Heads-up: the **PowerPoint itself was not uploaded** — only the two Excel files and the "Goal updates" screenshot. If you want me to actually build/edit the slide, the deck (or a blank target) will need to come over too.

---

## Where the numbers live (quick map)

**Capacity / risk model (`Part_Supplier_RiskAssessmentTool_v2.xlsx`):**

| Sheet | Role |
|---|---|
| `ModelsDemand_ToTissue` | Surgeon-model quarterly demand (Q2'25→Q4'27 "BP") → BOM matrix decomposing each model into tissue PNs → **Total Needed per tissue**. |
| `Rule` | The BOM **rule matrix**: how many of each tissue PN go into each surgeon model (e.g. Colorectal uses 3 Aorta, 5 Ureter…). References an external `Tissue Forecasting Tool.xlsx`. |
| `SHAllocations` | Each tissue's quarter volume split across **Nahunta / Martins / Customs / Parks** (% + volume + capacity). |
| `Yields-Labor-Cube` | Per tissue: **Labor** (min), **Cube** (freezer), risk **Tier**, plus per-SH **Spec yields**, **Harvesting yields**, pigs consumed, freeze-thaw yield. Also the risk-scoring dropdown vocabularies. |
| `Martins` / `Nahunta` / `Customs` / `Parks` | Per-slaughterhouse **capacity engines** — pigs/week, labor cap, freezer cube, trips, and the resulting weekly throughput per tissue. |
| **`Tissue_Model`** | **The by-part-supplier capacity + risk scorecard** (39 rows). Per tissue×supplier: throughput, yields, pigs/labor/freezer **headroom**, plus risk dims (permits, APHIS/FSIS, ISO, relationship, financial, geopolitical, disruption, cyber). **This is the core of the exec-summary ask.** |
| `Part_Model` | Same scorecard shape for **non-tissue** parts (currently mostly an empty template — 2 rows). |
| `Notes` | Sparse meeting agenda notes. |
| `Old`, `Old2`, `CalcDaily`, `Sheet1/3`, `Yields-Labor-Cube` | Legacy / scratch / daily calc engine. |

**Weekly actuals (`Weekly_goals_2026_SUMMARY_062426.xlsx`):**

| Sheet | Role |
|---|---|
| `Year to date` | **YTD Ask / Achieved / attainment %** per tissue per house, plus "Projected Harvest for '26" and projected %. Best single source for the exec rollup. |
| `Attainment & Alloc Summary` | Selectable week-range summary: avg ask/wk, avg harvested/wk, % of ask, attainment % per tissue per house. |
| `Attainment & Allocations` | Long-format weekly rollup: each week's Total Ask/Attained/Attainment %/Gap + per-house split + volume %. |
| `Over Time` | Weekly harvested per tissue, wide format (every week as a column) — good for trend lines. |
| `<MM_DD_YY>` weekly tabs (`12_29_25`…`07_06_26`) | Raw weekly entry sheets: per-house **Ask vs Achieved**, broken out by day (M–F) and by harvesting tech (Jordan/Nahunta, Jesus/Martin, Wilfredo/Custom). |
| `Productivity`, `By Week & House`, `Q1 to Date`, `Q2`, `PvA Data` (hidden), `Tissue Codes` | Supporting rollups, pivots, and the tissue PN ↔ common-name reference. |

---

## Glossary

**Slaughterhouses (tissue suppliers):** Nahunta, **Martins** (Martins Pork Products), Customs, Parks.
**Harvesting techs:** Jordan (Nahunta), Jesus (Martin), Wilfredo (Custom).

**Yield types** (multiplied to get usable output):
- **Spec / Process yield** — fraction of a harvested tissue that meets spec.
- **Harvesting yield** — fraction successfully harvested from the animal (the Pelvic Block problem lives here).
- **Freeze-Thaw yield** — fraction surviving the freeze/thaw cycle.

**Terms:** BP = Business Plan (forecast); APHIS = USDA animal-health permit status; FSIS = food-safety inspection level; Tier = risk/complexity tier (1 simplest → 4); Headroom = spare capacity above demand; Ask = weekly harvest goal; Attainment = achieved ÷ ask.

**Tissue PN ↔ common name:** see `source-files` → `Tissue Codes` sheet (e.g. 666506 = Pelvic Block Non-Intact, 666541 = Female Pelvic, 666522 = Ureters, 666501 = Aorta).

---

## Headline signals already visible

Full detail and the data tables behind these are in **[`FINDINGS.md`](FINDINGS.md)**. In short:

- **Pelvic family at Martins is the standout miss** — directly matches the boss's "study at Martins for Pelvic Block harvest-yield loss":
  - Male Pelvic (666540): **17%** YTD attainment
  - Pelvic Block Non-Intact (666506): **58%**
  - Female Pelvic (666541): **74%**
  - Root cause is in the model: Pelvic blocks carry **0.25 harvesting yield** (vs 0.85–0.95 for most tissues).
- Other low attainment: XL Hearts (666536) **52%**, Liver w/GB (666513) **62% at Customs**.
- These low-yield, lower-headroom, single/dual-sourced tissues are the **mitigation candidates** the second part of the ask is after.

---

## Suggested next steps (not yet done)

1. Build the **single-slide exec summary**: by-part-supplier capacity vs **2027 demand × 1.25**, filtered to medium/high-risk tissues only — answers "do we have risk of not meeting 125% of 2027 demand?"
2. Re-graph attainment with the **flat 250 denominator** per your note.
3. Draft the **mitigation/milestone list** (Martins Pelvic Block yield study first), pulled from the low-attainment + low-headroom tissues.
4. Get the **PowerPoint deck** uploaded if you want me to produce the actual slide rather than the underlying tables/figures.
