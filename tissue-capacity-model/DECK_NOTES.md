# Deck intake — `Tissue_Capacity_2026_2027.pptx`

**File:** `source-files/Tissue_Capacity_2026_2027.pptx` · 2 slides · 13.33×7.5" widescreen.

This is the boss's exec-summary deck — and it's **already substantially built**. It directly answers both halves of the "Goal updates" ask (capacity vs 125% of 2027 demand + mitigation milestones). What remains are a few edits/verifications, captured under **Open items** below (including your own "Add 250 as denominator" note, which currently lives as a sticky note on slide 2 and hasn't been applied to the chart yet).

> Note: this deck could not be rendered to images in this environment (LibreOffice failed to load it here), so the content below is extracted from the file's XML/text, tables, chart data, and speaker notes — not from a visual render.

---

## Slide 1 — "Tissue Supplier Capacity vs. 2027 Demand — Can We Cover 125%?"

**Subtitle:** Utilization at the busiest quarter of 2027. Headroom = the demand multiple a site can absorb before its first constraint binds (target ≥ 1.25× = 125%).

**Headline answer:** *"Yes — but the risk is isolated to Martins. It sits at 1.0× headroom (labor-bound), so it cannot cover 125% of 2027 demand. Every other site clears 125%."*

**CAPACITY BY SUPPLIER** (cells = % of capacity used; bar = headroom; dashed line = 125% target):

| Supplier | Pigs | Labor | Freezer | Headroom | vs 125% | Binding constraint · driver |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **Martins** | 81% | **99%** | 88% | **1.01×** | **Below 125%** | Labor · Pelvic block |
| Customs | 79% | 47% | 44% | 1.27× | Just clears | Kill cap |
| Nahunta | 73% | 34% | 41% | 1.38× | Clears | Kill cap · Thor/bari |
| Parks | 50% | 13% | 21% | 2.00× | Clears | Kill cap · Pelvic (low yield) |

**WHAT WE'RE SEEING:** Martins is labor-bound at 99% (~1.0× headroom, tight even at 100%); root cause is the pelvic block — low harvest yield and the rework that follows eat Martins' labor. Every other site clears 125%, but their limit is **kill (pig) capacity**, not labor or freezer (which sit wide open at Nahunta and Customs).

**NEXT STEPS (MILESTONES):**
1. **Run the Martins pelvic-block yield study** — pull bad pelvics and root-cause the harvest loss. 10%+ on harvesting yield → headroom/capacity improvement on pigs and labor.
2. **Ramp Parks as a 2nd pelvic source** once its upstream yield root-cause lands.
3. **Re-balance** labor-/freezer-heavy tissues off Martins → Customs (new freezer) and Nahunta (open labor).

**Source line:** Part_Supplier_RiskAssessmentTool_v2.xlsx · Tissue_Model. Headroom = 1 ÷ highest constraint utilization at busiest-quarter 2027 demand.

**Speaker notes (key extra):** Customs only clears by ~2 points and is kill-bound (new freezer removed freezer as the limiter). Spare capacity elsewhere is labor & freezer, **not pigs** — so move labor-/freezer-heavy tissues there, not pig-heavy ones. ⚠️ *Caveat in the notes:* "the model header cell (A1) reads 'Q4'26 BP'. Confirm the displayed quantities are the busiest-quarter **2027** scenario, not Q4 2026, or relabel."

---

## Slide 2 — "Where Each Tissue Is Constrained"

**Subtitle:** Binding constraint per site and the tissues driving it — busiest quarter of 2027.

Per-site constraint cards:

| Site | Constraint · Util · Headroom | Driver tissues |
|---|---|---|
| **Martins** | LABOR · 99% · 1.01× | Female Pelvic (666541), Pelvic Block (666506), Bariatric (666502), Aorta (666501) |
| Customs | KILL CAP · 79% · 1.27× | Bariatric (666502), Aorta (666501), Vena Cava (666523), Omentum (666516), Pancreas (666517) |
| Nahunta | KILL CAP · 73% · 1.38× | Aorta (666501), Thoracic (666521), Pancreas (666517), Omentum (666516), Full Thor & Bari (666507) |
| Parks | KILL CAP · 50% · 2.00× | Female Pelvic (666541) — *pelvic quality on observation; potential capacity once resolved* |

**Chart — "PELVIC ATTAINMENT vs ASK @Martin's — BIWEEKLY, 2026 YTD – Harvesting Yield"** (line chart, attainment = harvested ÷ ask, biweekly):

| Date | Female Pelvic (541's) | "Female Pelvic (506's)" | Ask |
|---|:---:|:---:|:---:|
| 12/29 | 100% | 100% | 100% |
| 01/12 | 116% | 18% | 100% |
| 01/26 | 108% | 80% | 100% |
| 02/09 | 112% | 33% | 100% |
| 02/23 | 91% | 100% | 100% |
| 03/09 | 96% | 19% | 100% |
| 03/23 | 51% | 5% | 100% |
| 04/06 | 80% | 31% | 100% |
| 04/20 | 63% | 100% | 100% |
| 05/04 | 51% | 89% | 100% |
| 05/18 | 58% | 100% | 100% |
| 06/01 | 49% | 100% | 100% |

Speaker-note takeaway: Female Pelvic ran ≥100% through Feb then **slid steadily to ~50% by June** — the worsening, high-volume problem, exactly where 2027 demand grows fastest. Pelvic Block was erratic early (batch timing) and recovered to ~100% in Q2. Male Pelvic excluded (being wound down; Q2 demand cut to 200, ~1% attainment).

**Footnote:** attainment = harvested ÷ ask (biweekly); Male Pelvic excluded; codes are Intuitive part numbers.

---

## Open items (your notes + things to fix before presenting)

1. **"Add 250 as denominator"** — your sticky note on slide 2. The chart today normalizes each tissue to *its own* ask (Ask = 100%). Your ask is to re-base attainment on a **flat 250** (`harvested ÷ 250`) so the series are comparable across tissues. *Not yet applied.*
2. **"Why is attainment dropping?"** — your note lists the suspected culprits: **harvesting yield, labor**. (The model backs this up: Pelvic harvesting yield = 0.25 and Martins is labor-bound — see `FINDINGS.md §4`.)
3. **Quarter-label caveat** — confirm the figures are **busiest-quarter 2027**, not Q4'26; the model's header cell A1 reportedly reads "Q4'26 BP". Relabel or re-point if needed.
4. **Chart series mislabel** — the second series is titled "Female Pelvic (506's)", but **666506 is Pelvic Block Non-Intact**, not Female Pelvic. Likely should read "Pelvic Block (506's)".
5. **Stray shapes on slide 1** — leftover text fragments ("SH", "Labor · Pelvic block") appear duplicated/orphaned; clean up before presenting.

None of these are applied yet — this is intake only. Say the word and I'll make any/all of these edits to the deck.
