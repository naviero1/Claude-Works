# Tissue Supplier Research

Second-source qualification study for the porcine tissue-harvesting operation —
finding additional slaughterhouse suppliers (and national direct-tissue vendors)
beyond the current base of **Nahunta** (great culture, Medium tier) and
**Martin's Pork Products** (Falcon NC, Est. M6720 under the Talmadge-Aiken programme).

> **Last verification pass: 2026-08-06.** Every supplier row was matched against USDA's
> own files — the **FSIS Establishment Demographic Data** and the **MPI Directory by
> Establishment Number** — with each match validated on **city and state** so name
> collisions could not slip through. **43 roster rows changed.** See *What the
> verification pass changed*, below.

## Deliverables

| File | What it is |
|---|---|
| `Tissue_Supplier_Study.xlsx` | The working workbook — 13 tabs, described below |
| `Supplier_Strategy_Meeting.pptx` | 7-slide stakeholder deck for the alignment meeting |
| `Supplier_Selection_Meeting_Agenda.md` | The ~60-minute agenda the deck follows |
| `Deep_Study_Synthesis.md` / `.pdf` | Narrative report. **Read ADDENDUM 2 first, then ADDENDUM 1** — each corrects everything after it |

### The workbook

| Tab | What's in it |
|---|---|
| Overview & Method | Purpose, the target spec (volume **open**, classified by tier; cert rules; welfare), the two operating models, key findings |
| Meeting Notes 2026-08 | What was decided in the stakeholder meeting, including the corrected APHIS rule |
| Action Items | Sequenced meetings + the **12-entry priority contact order** + RFQ/P templates (email and short site/call) |
| Anatomical Spec | Fill-in per-block spec (pelvic / bariatric / thoracic) — decides **sow vs market hog**, still action #1 |
| Legend & Scoring | Status/fit codes, the **FSIS species flags**, the **volume-category → weekly-ceiling mapping**, how "Fit" is judged |
| Supplier Roster | Master list by region: **NC** (primary), **SC / TN / VA**, **Iowa & Midwest** — with **Animal class (FSIS flags)**, **Volume tier**, **USDA/FSIS enforcement**, **APHIS export status** and **Within 120 mi?** columns |
| National Direct Suppliers | Vendors selling finished porcine tissue/organs, price-per-tissue where real, plus an **EU-export fit** column |
| Models & Make-vs-Buy | Model A (we harvest on-site) vs Model B (they harvest) vs buy-direct, and cost drivers |
| TCO Calculator | Editable calculator — total cost to self-harvest one organ/block, with a per-slaughterhouse comparison grid and a buy-direct benchmark |
| APHIS & EU Export | The two-path rule, APHIS vs FSIS vs state inspection, **AWA licence ≠ APHIS export listing**, how to check status yourself, what the EU requires (Reg 1069/2009 & 142/2011), the medical-device angle |
| Call Question Sheet | Outreach script to qualify each plant, incl. an EU-export section |
| Sources & Confidence | Every source + a confidence rating, and the method behind the verification pass |
| Deep Study (Verified) | Output of the 21-agent adversarial-verification re-run. **A point-in-time record** — cells that failed later verification are marked `⚠ SUPERSEDED` in place; nothing was deleted |

## The rules this study is built against

**Volume is OPEN — capacity is not a filter.** No plant is excluded for being too small or
too large; every supplier is listed and classified into a tier instead:
**Small 0–300/wk · Medium 350–2,500/wk · Medium-High 2,500–5,000/wk · High >5,000/wk**
(301–349 = Small/Medium boundary; 2,500 = the Medium / Medium-High hinge). Tier drives the
*operating model*, not inclusion: Small → Model A / aggregation; Medium → single-plant
programme; Medium-High → regional packers and cull-sow plants (larger anatomy); High →
Model B or a biologics arm, where the constraint is access, not volume.

**The APHIS rule has two paths** (confirmed in the 2026-08 meeting):

- **Path 1 — we harvest.** A slaughterhouse we harvest at needs only **USDA/FSIS inspection**.
  APHIS is *not* required of the plant. We assemble the model at ATM and that carries the export.
- **Path 2 — direct supply.** A supplier who ships us finished tissue blocks **must be able to
  hold APHIS**. This is a gating requirement for every direct tissue supplier.

**Nahunta is exportable.** APHIS accepts **North Carolina state inspection** as equivalent to
federal for this purpose. **Only NC** — no other state programme carries the equivalence, so a
state-inspected plant anywhere else would need USDA/FSIS to serve as a Path 1 harvest site.

**Model A prefers a 120-mile radius**, for all slaughterhouses. Distances in the roster are real
road miles routed from the Pikeville NC anchor (35.4971, −77.9819). *If the radius should be
measured from ATM or another operating base instead, say so and the column can be recomputed.*

**Welfare/culture (the Nahunta standard)** is a scored tie-breaker — documented humane-handling
actions drop a plant to CAUTION. With volume no longer a gate, welfare and certification are the
main differentiators.

## What the verification pass changed

**Weekly volumes were systematically overstated.** Figures inferred from head-per-day quotes,
distribution footprint or trade press repeatedly ran above the plant's own USDA volume-category
ceiling. The categories are banded head per 360 days:

| `slaughter_volume_category` | Head / 360 days | Hard weekly ceiling |
|---|---|---|
| 1 | fewer than 1,000 | under ~19 / wk |
| 2 | 1,000 – 9,999 | ~19 – 192 / wk |
| 3 | 10,000 – 99,999 | ~192 – 1,917 / wk |
| 4 | 100,000 or more | ~1,917 / wk and up |

A category is a **ceiling and a floor, not an estimate**. Use it to falsify a claimed figure,
never to replace one. On that test these failed: **Larry's Sausage** (claimed 200–800/wk, capped
at ~192), **Acre Station** (~400/wk, capped at ~192), **Midwest Research Swine** (~385/wk, capped
at ~192), **Fayette Packing** (called "the largest of the TN group", actually under ~19/wk),
**Bass Farms** (described as a pure kill floor, actually under ~19/wk).

**The contact order changed at the top.**

- **Parks Family Meats (M18296A, Warsaw NC) is now #2.** FSIS records it
  `slaughter_or_processing_only = Slaughter` — a pure kill floor, the only NC plant on the roster
  verified to be built that way, and the structure Model A wants. `market_swine_slaughter = Yes`
  **and** `roaster_swine_slaughter = Yes`, so it is *not* roaster-exclusive and market-weight
  anatomy is available. Category 3, one 15,000 sq ft floor, one decision-maker, 45 road miles.
- **Custom Quality Packers (M20129, Sims NC) is now #4** — three "unknown" fields closed: active
  **federal** grant (not "TA-20129"), market + roaster flagged, category 3, bracketing the
  ~500/wk company figure. With **Flowers Slaughter House (M21747)** in the same town it makes a
  Wilson County cluster one crew can serve.
- **Larry's Sausage drops from #3 to #11** — federal M8305 not "TA-8305", category 2, sow-only.
- **Bass Farms and Gunnoe Sausage are removed.**
- **EcoFriendly Foods (M21938)** replaces Gunnoe as the Virginia entry — all four swine classes
  flagged, category 3, and the "ceased operations ~2020" report is refuted by an active grant.

**Five "USDA-inspected" labels had nothing behind them** and are withdrawn: Caughman's Meat
Plant, Sessoms Packing, Assured Community Processing (claimed M2123), Country Slaughter and Meats
(claimed M32012), and Gunnoe. **Triad Meat Custom Processing** is excluded on species — the only
FSIS slaughter establishment at Madison NC is a halal plant with no swine flags. Two pairs of rows
turned out to be **the same plant listed twice** and are marked `DUPLICATE`.

**Two corrections went in the suppliers' favour:** Riverside Meats and Acre Station both had
"custom-exempt" labels refuted — each holds an active federal grant, so product is inspected and
saleable.

## Important caveats

- **Treat every weekly volume in this workbook as a ceiling to confirm on the phone**, not as a
  figure. The USDA category tells you what a plant *cannot* exceed; only the plant can tell you
  what it actually kills.
- **"None found" in the enforcement column is not a clean bill.** The ten FSIS Quarterly
  Enforcement Reports (FY2024 Q1 – FY2026 Q2) were retrieved and searched directly, but they list
  suspensions, NOIEs and withholding actions only — *not* ordinary noncompliance records, which is
  what a humane-handling problem looks like before it escalates. The FSIS FOIA in the Action Items
  tab is what closes that gap. Nahunta, being state-inspected, sits outside FSIS reporting
  entirely, so for Nahunta welfare must be a **site-visit** finding.
- **An APHIS Animal Welfare Act licence is not an APHIS Veterinary Services export listing.**
  Several vendor claims conflate the two; only the export listing matters for EU-bound product.
- **The sow vs market hog question is still internal and still unanswered.** It decides roughly
  half the candidate pool and no further research can settle it — fill in the Anatomical Spec tab.
- The **TCO Calculator's numbers are illustrative placeholders** — replace them with your real
  time-studies, rental terms, wages, freight and holding costs.
