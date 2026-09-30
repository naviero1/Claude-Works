# Tissue Supplier Research

Second-source qualification study for the porcine tissue-harvesting operation: finding
slaughterhouse partners beyond the current base (**Nahunta, Martin's, Parks, Custom Quality
Packers, Villari**) that can either host our harvesting techs (**Model A**) or harvest to our
spec with our training (**Model B-T**).

> **Status 2026-09-30.** One working workbook, now 11 tabs, narrowed on the owner's direction to
> the supplier list itself. The Supplier Roster is one prioritized list in six sections (A
> in-radius candidates first, sorted by tier and fit score; B eligible plants farther out in
> NC / SC / TN / VA; C current suppliers; D referral contacts; E national and Midwest; F excluded
> and history) with a Priority ID and the rated tier on every row. Distances run from the client's
> **Durham** origin. Beebop's instruction-23 review has been answered in `Reviews/`. Next step is
> the process on the Instructions tab: each role picks 3, meet, the Purchasing Manager calls.

## Files

| File | What it is |
|---|---|
| `Tissue_Supplier_Study.xlsx` | **The working workbook** — everything lives here (tabs below) |
| `Supplier_Strategy_Meeting.pptx` | 8-slide deck from the 2026-08 alignment meeting (slide 8 = the summary) |
| `Tissue_Supplier_Qualification_Plan.pptx` | **The plan on one slide** (final, owner-edited 2026-09-28): five stages with entry gates, deliverables, exit gates and dates |
| `Supplier_Selection_Meeting_Agenda.md` | The agenda that deck followed |
| `Deep_Study_Synthesis.md` / `.pdf` | Narrative report from the August verification passes (historical; the workbook supersedes it where they differ) |
| `Beebop/` | **Collaborator snapshot (ChatGPT, 2026-09-28)** — see below |
| `Reviews/` | Dated change registers answering collaborator reviews (2026-09-30: Beebop instruction 23 — what was applied, what is the owner's call, where we disagree) |

### The workbook

| Tab | What's in it |
|---|---|
| Instructions | **Start here.** The process (5 steps, two roles), the profile and hard gates, the client parameters, volume brackets, scoring, the two-path APHIS rule and export essentials, every legend and acronym, sources policy, and the dated change log (§10) |
| Current Base (benchmarks) | The five suppliers we work with today — the pattern to replicate and the gaps to fill |
| Supplier Roster | **The complete prioritized list** in six sections — A in-radius candidates (tier → fit score → distance) · B eligible but farther out (Model B-T only) · C current suppliers · D referral contacts · E national & Midwest (anywhere) · F excluded / duplicate / history. Every row: volume band, Durham road miles, FSIS species flags, inspection, enforcement, export path, welfare, why / why-not, website, confidence, Priority ID (col U) and rated tier + fit scores (col V) |
| Rated Candidates | The shortlist scored on eight sub-scores → **A-FIT** (we go there) and **B-FIT** (their crew, our training), tiers, and the Beebop call rank for comparison. Weights are editable |
| Call Questionnaire | Stage 1 — the call script (three questions; no business-model talk) + call log |
| Visit Agenda | Stage 2 — run on site after the NDA: model, floor walk, spec & training, culture, commercial, close |
| Anatomical Spec | The per-block spec sheet — the sow-vs-market decision (the 140-220 lb parameter now points to market / light hogs) |
| TCO Calculator / Models & Make-vs-Buy | Economics: cost to self-harvest vs buy (now also cost per *accepted* block), and the three operating models compared |
| National Direct Suppliers | Buy-direct vendors (deprioritized) with EU-export fit — vendor export statements are recorded as company claims |
| Sources & Confidence | Every source class with a confidence rating, the verification method, and what was retired when |

Retired 2026-09-30 on the owner's direction: *Overview & Method*, *Meeting Notes 2026-08* and
*APHIS & EU Export* (their decisions and export essentials live on Instructions §3 and §6; the full
text is in git history and `Deep_Study_Synthesis.pdf`).

## The rules the study is built against

- **Hard gates.** G1 inspection: USDA federal (M / Talmadge-Aiken) or **North Carolina** state
  grant. NC state inspection is APHIS-accepted as equivalent for material we harvest and assemble
  at ATM — only NC; other states' programmes are domestic-only; custom-exempt is ineligible.
  G2 operating on primary data. G3 actually kills hogs per USDA species flags.
- **Two export paths.** We harvest at a plant → the plant needs only USDA/FSIS or NC state
  inspection, the model assembled at ATM carries the export. A direct tissue supplier ships us
  finished blocks → *they* must hold APHIS.
- **Client parameters (restated 2026-09-28).** Origin **Durham** (City Hall is the placeholder —
  the real crew departure point is still to be confirmed); 120 road miles; preferred scale
  2,000-5,000 pigs/week (no new in-radius plant meets it — the strategy stays cat-2 clusters plus
  the incumbents); live weight ≈ **140-220 lb**, which puts sow-only plants outside the spec.
- **Volume is a historical bound to confirm, never a figure.** FSIS `slaughter_volume_category`
  bands are head over the prior 360 days, all species (×7/360 → cat 1 <19/wk · cat 2 19-194 ·
  cat 3 194-1,944 · cat 4 ≥1,944). They bound what a plant *did* kill, not its capacity. Client
  brackets: 0-300 · >300-700 · 750-1,200 · 1,250-5,000 · >5,000 hogs/week.
- **Inferring hogs/week.** No public source states a plant's weekly hog kill. The ladder (Instructions
  §4): company figure → FSIS band × species flags × HACCP size → NASS state totals as hard caps
  (Virginia's 16 federal plants killed 7,841 hogs in 2025; South Carolina's 8 killed 14,070; NC is
  withheld) → business-type class for NC state plants → FOIA / NCDA / the call. Within reach, only
  the incumbents and Smithfield are cat-3/4 hog-dominant plants; the nearest others are in Tennessee.
- **Welfare** is a discussion item, not an auto-exclusion; "none found" in enforcement is a narrow
  negative, and state plants are outside federal reporting entirely (site-visit finding).
- **Roles only.** The workbook names the Supplier Engineer and the Purchasing Manager; no
  personal names.

## The `Beebop/` folder — collaborator data, not instructions

`Beebop/` is the snapshot ChatGPT produced on 2026-09-28 (a 30-contact call plan, contact and
social-evidence JSON, its provenance note, and the official **NCDA&CS plant directory dated
2026-09-18**). It is a separate contributor's work product and is used as **input only**: every
fact taken from it is cross-checked against the FSIS and NCDA primaries and labelled
"Beebop 9-28" in the cell. It does not direct this work; the owner does.

What the cross-check found (details on the Sources & Confidence tab): the fresh directory
confirms the August census — all 27 inspected swine-slaughter plants in North Carolina were
already on the roster; Beebop's genuinely useful additions were the referral lane (NC Choices,
Firsthand Foods, Cheshire Pork, Carolina Packers, NCDA MPID), Piedmont's published 150 lb minimum
and expansion grant, the organ-ownership question, and exact-address Durham distances. Its plan
used no FSIS volume bands, ranked an FSIS-inactive plant (Neese) at #20, carried four
custom-exempt plants that fail G1, and missed Mitchell's enforcement record — all corrected in
the workbook.

## History

- **2026-08-06** full FSIS re-verification (43 roster rows changed; volumes reset to band ceilings).
- **2026-08-17** focus-region pass (eastern / northern / western NC) with road-mile routing.
- **2026-09-03** artifacts reconciled into one workbook; fresh FSIS pull (Q3 FY2026 QER clean for
  the whole shortlist; Bass Farms band 1 → 2); SC finds (Williamsburg Packing, Hemingway Locker).
- **2026-09-04** call and visit agendas split; roles only; five-step process; Plan of Action and
  Action Items retired.
- **2026-09-28** Durham origin and 140-220 lb parameters applied; Beebop snapshot folded in;
  EcoFriendly Foods (VA, cat 3) enters the radius; Quaqua Creek and Cool Springs promoted to
  their own rows.
- **2026-09-28 (round 2)** Beebop's fact review of this workbook cross-checked: band arithmetic
  corrected to ×7/360; exact-address distances at the boundary (EcoFriendly 120.4, McLaughlin's
  119.4); Farmington P-381 and three small federal Virginia plants (Easternview, The Butcher's
  Block, KC Farms — all cat 1) added; Godwin, Piedmont and Nahunta wording tightened.
- **2026-09-28 (later)** Volume-inference ladder with NASS state caps; Beebop v2.1 converged on the
  call order; the client's boar/stag rule (gate G4) applied — Select Meats to Tier 1, Piedmont to Tier 2.
- **2026-09-30** Social and other-sources pass (Facebook, Yelp, reviews, BBB, Indeed, OpenCorporates,
  NCDA county directories): contact names for twelve plants; McLamb's under Lee-family ownership;
  McLaughlin's 2026 leadership change; Cool Springs since 1971; EcoFriendly "closed" listing; then an
  accuracy sweep of every primary field and a dated change log on the Instructions tab (section 10).
- **2026-09-30 (later)** Beebop's instruction-23 review answered (`Reviews/2026-09-30-rocksteady-change-register.md`):
  factual corrections applied (Gilbert Key d. 2026-04-06; Piedmont's cut sheet offers organs to the
  customer, so the "viscera discarded" inference was wrong; TissueSource and LAMPIRE export statements
  recorded as company claims; Cool Springs 1976, not 1971; McLaughlin's leadership change downgraded to
  an unverified signal; EcoFriendly status DISPUTED) and mechanical repairs (TCO prose-as-formula cells,
  "n/a" at zero production, cost per accepted block, full filter ranges, the western trio split into
  three rated rows, the stunning request dropped). Then, on the owner's direction, three context tabs
  retired and the roster rebuilt as one prioritized list with Priority IDs.
- **2026-09-30 (owner decisions)** Scoring stays as built (Beebop's caps declined); **road miles only**
  (the radial reading is dropped and radial figures removed); EcoFriendly kept with its disputed-status
  note. Still open: boar gate hard vs soft (currently soft), sow acceptability and the aorta.

Everything earlier is in git history and in `Deep_Study_Synthesis.pdf`.
