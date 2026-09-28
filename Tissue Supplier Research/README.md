# Tissue Supplier Research

Second-source qualification study for the porcine tissue-harvesting operation: finding
slaughterhouse partners beyond the current base (**Nahunta, Martin's, Parks, Custom Quality
Packers, Villari**) that can either host our harvesting techs (**Model A**) or harvest to our
spec with our training (**Model B-T**).

> **Status 2026-09-28.** One working workbook, 14 tabs. Distances now run from the client's
> **Durham** origin (the earlier Pikeville figures are kept alongside). The ChatGPT research
> snapshot in `Beebop/` has been cross-checked and folded in. Next step is the process on the
> workbook's Instructions tab: each role picks 3, meet, the Purchasing Manager calls.

## Files

| File | What it is |
|---|---|
| `Tissue_Supplier_Study.xlsx` | **The working workbook** — everything lives here (tabs below) |
| `Supplier_Strategy_Meeting.pptx` | 8-slide deck from the 2026-08 alignment meeting (slide 8 = the summary) |
| `Supplier_Selection_Meeting_Agenda.md` | The agenda that deck followed |
| `Deep_Study_Synthesis.md` / `.pdf` | Narrative report from the August verification passes (historical; the workbook supersedes it where they differ) |
| `Beebop/` | **Collaborator snapshot (ChatGPT, 2026-09-28)** — see below |

### The workbook

| Tab | What's in it |
|---|---|
| Instructions | **Start here.** The process (5 steps, two roles), the profile and hard gates, the client parameters, volume brackets, scoring, every legend and acronym, sources policy |
| Overview & Method / Meeting Notes 2026-08 | Study context and the meeting record (incl. the two-path APHIS rule) |
| Current Base (benchmarks) | The five suppliers we work with today — the pattern to replicate and the gaps to fill |
| Supplier Roster | Every plant assessed (NC / SC / VA / TN / Midwest + national vendors): volume band, Durham road miles, FSIS species flags, inspection, enforcement, export path, welfare, why / why-not, website, confidence with source |
| Rated Candidates | The shortlist scored on eight sub-scores → **A-FIT** (we go there) and **B-FIT** (their crew, our training), tiers, and the Beebop call rank for comparison. Weights are editable |
| Call Questionnaire | Stage 1 — the call script (three questions; no business-model talk) + call log |
| Visit Agenda | Stage 2 — run on site after the NDA: model, floor walk, spec & training, culture, commercial, close |
| Anatomical Spec | The per-block spec sheet — the sow-vs-market decision (the 140-220 lb parameter now points to market / light hogs) |
| TCO Calculator / Models & Make-vs-Buy | Economics: cost to self-harvest vs buy, and the three operating models compared |
| APHIS & EU Export | The two-path rule, APHIS vs FSIS vs state inspection, EU by-product and device rules |
| National Direct Suppliers | Buy-direct vendors (deprioritized) with EU-export fit |
| Sources & Confidence | Every source class with a confidence rating, the verification method, and what was retired when |

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

Everything earlier is in git history and in `Deep_Study_Synthesis.pdf`.
