# Supplier Part Risk Model — Project Notes & Handoff

Single consolidated record of this project so any future session can resume without re-deriving anything. Created at the end of the originating session.

---

## 1. Context & scope (confirmed)

- **Org / division:** Intuitive Surgical — a division that builds **tissue models**, **NOT** implantable medical devices.
- **The "part" of interest:** **ex-vivo porcine tissue** sourced from **local slaughterhouses**, used as a substrate for **surgical R&D, instrument/energy-device testing, and training**. Also covers standard/catalog and custom-engineered purchased parts.
- **Goal:** one repeatable **Supplier Part Risk Analysis** format to evaluate *every* part (catalog, custom, tissue) by multiple criteria and assign a defensible risk class + action plan.
- **Use tier (confirmed):** tissue feeds **V&V** — there is a **V&V quality test before it goes into production**. → highest-rigor **T1** tier. That existing V&V test is the **acceptance/Detection gate** the rubric should wrap around (not replace).

### Key scope correction (v0.1 → v0.2)
Because tissue models are **not medical devices**:
- Medical-device standards (ISO 14971/13485/**22442**/10993/14160) are **optional references, not governing**.
- Xenotransplant concerns (**PERV, decellularization, α-Gal, residual DNA**) are **out of scope** (implant concerns, not ex-vivo test/training tissue).
- Real risk re-centered on: **handler biosafety (zoonoses)**, **model fitness-for-purpose**, **lot-to-lot consistency & traceability**, **cold chain**, **waste/disposal**.

---

## 2. Deliverables (committed, branch `claude/google-drive-pdf-access-y6xftb`)

| File | What it is |
|---|---|
| `supplier-part-risk-analysis/Supplier_Part_Risk_Analysis_Framework.md` | **v0.2** — method, two-layer model, anchored scoring rubric, action playbook, standards, traceability |
| `supplier-part-risk-analysis/Risk_Scoring_Template.csv` | Worksheet — one row per part; use-tier + Layer A + procurement axes + Layer B + two gates; 4 worked example rows |
| `supplier-part-risk-analysis/PROJECT_NOTES_and_Handoff.md` | This file |
| `DRIVE_RESOURCES.md` / `drive_pdfs.json` (repo root) | Index of all 922 Drive PDFs (separate but related — the source library) |

### The model in one paragraph
**Two layers.** *Layer A (all parts):* FMEA **Severity/Occurrence/Detection** 1–10 → **Action Priority (H/M/L)** (Severity-weighted; RPN retired), plus **Supply Continuity** and **Supplier Maturity** (1–5). *Layer B (tissue only):* **B1 fitness-for-purpose, B2 freshness/cold chain, B3 consistency & traceability** (weights heaviest for T1/V&V), **B4 handler biosafety/zoonoses, B5 waste/disposal** (1–5), plus a 2-tier **gate** (legal sourcing/reportable disease; handler zoonoses). Highest triggered rule sets **Final Risk Class** (Critical/High/Medium/Low), each with a sourcing / intake-acceptance / audit-cadence / buffer playbook. Acceptability thresholds are **self-defined** (Quality + EHS to ratify).

---

## 3. Source extractions (grounding — so future sessions need not re-read the books)

These were extracted live from PDFs in the Drive. Drive file IDs in §4.

### 3a. AIAG-VDA FMEA Handbook (2019) — fully read
- **Severity (S) 1–10**, **Occurrence (O) 1–10**, **Detection (D) 1–10** — tables D1/D2/D3 (DFMEA) and P1/P2/P3 (PFMEA).
  - O anchored on technology novelty + maturity of prevention controls (10 = first-ever/no V&V; 1 = cause eliminated).
  - D anchored on test-method maturity + timing (10 = test not yet developed; 1 = proven always-detects).
- **RPN retired**: "RPN alone is not an adequate method… gives equal weight to S, O, and D." S×O and RPN removed from the 2019 edition.
- **Action Priority (AP)** replaces RPN: maps all 1000 S×O×D combos to **High/Medium/Low**, weighting **Severity → Occurrence → Detection**. AP prioritizes *the action*, not the score. High = action required or documented justification; Medium = should; Low = could. S 9–10 with AP H/M → management review.

### 3b. ISO 14971:2019 — fully read (used as principle, not governing)
- **risk = probability of occurrence of harm × severity of harm** (cl. 3.18).
- Process: risk analysis → evaluation → control → production/post-production.
- **No mandated risk matrix and no specified acceptable levels** — manufacturer must **define objective acceptability criteria** (top-mgmt policy, cl. 4.2) and **record the categorization system in the risk management file** (cl. 5.5).
- Risk management file requires **traceability per hazard**: analysis → evaluation → control implementation/verification → residual-risk results.

### 3c. CSQP Handbook (Durivage/ASQ) — Parts I–II read (rest truncated)
- **Kraljic segmentation** (profit impact × supply risk): Strategic / Leverage / Bottleneck / Routine — drives sourcing approach. Underlying factor = **switching cost**.
- **100-pt supplier scorecard (Fig 3.4)**: Quality & ops = 45 (SCAR 15, repeated SCAR 10, SCAR responsiveness 10, rework 5, lot conformance 5); Costs = 20; Purchasing = 35 (on-time 10, expedited 10, PO doc issues 10, responsiveness 5).
- **Weighted selection (Table 2.1)** example weights: Cost 4, Quality 5, Location 1, Reliability 2, Payment 3.
- Performance categories: Quality (PPM, RMA, SCAR metrics), Delivery (OTD), Cost (TCR), Responsiveness, + **Risk** (financial instability, capacity, distance, political) and Innovation.
- **Audit cadence = risk-based** (criticize fixed schedules): weight by product safety impact, compliance history, prior audits, major changes, CAPA indicators. **Finding classes:** Critical / Major / Minor (Table 6.1) → CAPA timing required/recommended.
- *Truncated (not recovered):* PPAP levels (Tables 10.2/10.3), control plans, APQP detail, supplier-risk-classification table (11.2), QMS maturity grid (9.2). → re-read CSQP Part III if needed for custom-part qualification.

### 3d. Gordon, *Supplier Evaluation & Performance Excellence* — Ch.1–3 read (rest truncated)
- Segmentation dimensions: risk, cost, quality, delivery, service, technology, product development, responsiveness, communications. Underlying factor = switching cost/dependence.
- Top supply risks (AMR poll): supplier disruption 49%, logistics 17%, natural disaster 14%, strategic 13%, geopolitical 8%.
- COPQ ≈ 10–25% of sales; **poor *supplier* quality ≈ 25–70% of COPQ**.
- *Truncated:* scorecard case study, weighting scheme, qualification detail (Ch.4–10).

### 3e. Diseases of Swine, 11th ed. — Ch.1–5 read; disease chapters TOC-only (rest domain knowledge)
**Porcine agents relevant to ex-vivo tissue handling:**
- **Gate-1 (legal/reportable, trade):** African Swine Fever, Classical Swine Fever, Foot-and-Mouth, Pseudorabies (PRV). Source region/herd must be status-clear.
- **Handler zoonoses (the dominant real risk):** **Hepatitis E**, ***Strep suis*** (meningitis/sepsis — serious), ***Erysipelothrix*** (erysipeloid), *Brucella*, *Leptospira*, *Salmonella*, **MRSA** (livestock-assoc), **Influenza A**, ***Trichinella*** (muscle), *Toxoplasma*.
- **Transmission for raw tissue:** skin breaks/inoculation (Strep suis, Erysipelothrix, Brucella, Lepto), blood/fluids (HEV, Lepto, Brucella), aerosol during cutting (flu, Strep suis), ingestion/mucosal (Salmonella, HEV, Toxo, Trichinella). Reproductive/abortion material = highest hazard.
- **Source-tier factors:** closed vs open herd; health-status certification (SPF/PRRS-neg); biosecurity level; geographic/WOAH disease status; feral-swine contact; surveillance records.
- **Inspection limit (critical):** ante-/post-mortem inspection screens overt disease & gross lesions but **MISSES** HEV, Trichinella (low burden), Toxo, subclinical Salmonella/MRSA/Strep suis carriers. → inspection is a baseline, not a safeguard; controls = certified herds + PPE/cut discipline + **CDC/NIH BMBL** practices.
- **NOT relevant here** (implant-only, excluded): PERV, PCMV/herpesviruses, PCV.

---

## 4. Drive file IDs (for re-reading sources)

| Book | fileId |
|---|---|
| AIAG-VDA FMEA Handbook (2019) | `1mbI08xT9nbuwYsYDu5i1M98_hw8eKJSs` |
| ISO 14971:2019 | `1i660P0nXK8xcLEvwSF-06tVkqVVszLxN` |
| CSQP Handbook (Durivage) | `1qUs1iGHHtFVQpXGsK621zy5iHE7vyWtq` |
| Supplier Evaluation (Gordon) | `1SrSp8SJSGy9tC_9xF87CmnRTsqhTBwp0` |
| Diseases of Swine, 11th ed. | `1nFzSqMiefpI_VDPWEaVz2MoPMY1-Mald` |
| ISO 13485:2016 | `1Ug4vsK2hl6qnCGlVxQG6PrrRz4Cpag-p` |
| ISO 9001:2015 | `1XAwDhM8V-EIJTPG0YSsSCQ_YKwYJf75Q` |
| ASQ Certified Quality Engineer Handbook (5th) | `1k9kSYOJODEV83N0DJQMejshCa70TL_gc` |
| Supply Chain Risk Mgmt (Schlegel & Trent) | `1eRCsivFV2Wrp0SNILWlWkZOTp-v4kQ5J` |
| Supply Chain Risk Handbook (Zsidisin & Ritchie) | `1gsSUnq7dKsEQHukvvEO_yGugXzDWxmBm` |

*Tissue-fidelity references (Layer B1):* search the Drive's **Biochem/Biology** folders for Badylak "Smart Materials for Tissue Engineering" and Bronzino "Tissue Engineering and Artificial Organs".

---

## 5. Open items / next steps

1. **Get the existing V&V quality test** (what it checks, acceptance criteria, owner, gaps) → wire it in as the Detection/acceptance gate. *Biggest lever.*
2. **Real part/tissue list** (or ~12 representative) to replace example rows.
3. **Source profile** — # slaughterhouses, inspection status, current handler/biosafety controls → grounds Supply Continuity + B4.
4. **Ratify acceptability thresholds** (§6.1 of framework) — Quality + EHS.
5. **Build the auto-calculating spreadsheet** (Excel/Sheets) — auto-derive Action Priority + Final Risk Class. *Was the agreed next build step; not yet done.*

### Acquisition list (mostly free — no expensive ISO device standards needed)
1. **CDC/NIH BMBL** — biosafety levels/practices for porcine tissue handling (free).
2. **USDA APHIS / state Dept. of Agriculture** — legal byproduct/inedible-material sourcing (free).
3. **OSHA biosafety / general-duty** material (free; note 1910.1030 bloodborne is human-source).
4. **IATA DGR / 49 CFR UN3373 (Cat. B)** — only if tissue is shipped between sites.
5. **Internal test-method-validation reference** (ISO/IEC 17025-style) — because V&V/T1 applies; supports the B3 consistency axis.

---

*End of handoff. All work above is committed and pushed to `claude/google-drive-pdf-access-y6xftb`.*
