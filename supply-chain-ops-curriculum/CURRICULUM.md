# The Curriculum — A Self-Designed Degree in Supply Chain & Operations

This sequences the ~140 topics in `DOMAIN-MAP.md` into five stages built around one rule: **every module ends in a deliverable at your current job**, because for a no-degree 20-year professional, the portfolio of public, dollarized artifacts *is* the credential. Peripheral options live in `PERIPHERALS.md`.

## The thesis

The common denominator across your 20 years — labor standards at Smithfield, LMS-Light and the MOS at Lowe's, BPMN/BRD work at NAVSUP — is that **you turn messy operational reality into measured, governed systems**: standards, scorecards, dashboards, and operating rhythms that executives fund and act on. You have done this three times for internal operations. Your current role asks you to do it a fourth time, pointed outward at a fragile, sole-source, perishable biological supply base, with no ISO 13485 skeleton handed to you.

That absence is the opportunity: you get to design the quality–procurement–risk operating system yourself, which is a resume-level accomplishment, not a burden. The identity this builds is the **full-stack supplier engineer** — one person who can verify a supplier's capacity quantitatively, negotiate its contract, qualify its material, score its risk in dollars, and build the dashboard that governs it — with a defensible niche moat in **biological/cold-chain supply** that almost no supplier quality engineer possesses.

## How to use this

- Stages are sequential; modules within a stage can interleave. Timelines assume ~5–7 hrs/week around a demanding job **with zero slack** — expect real life to stretch them 20–30%, and that's fine.
- Each stage names what is **droppable when work spikes**. Nothing here is mandatory except the two legally/safety-required trainings in Stage 1.
- Credentials are placed where their body of knowledge overlaps the stage you're already studying, so exam prep double-counts.
- An adversarial review pass corrected the first draft; corrections are integrated below and flagged where they change advice you might have heard elsewhere.

---

## Stage 1 — Name What You Own (months 0–3)

**Goal:** convert existing strengths into visible supplier-facing wins within a quarter, and close the compliance gaps that make you the site authority overnight.

### 1.1 Speak SQE: relabel the toolkit
*Domains: Supplier Engineering, Industrial Engineering, Business Strategy*

You already do supplier capacity verification (Lowe's capacity modeling), supplier scorecards (Smithfield vendor accountability toolkit), and policy deployment (the Lowe's MOS = Hoshin Kanri). Learn the industry vocabulary — PPM, OTD, SCAR, QBR, PPAP/FAI, demonstrated vs. rated capacity, Hoshin — so twenty years of work becomes legible in supplier-engineering language.

**Deliverable:** rewritten resume + 3–4 written case studies (LMS-Light, vendor accountability toolkit, $50M capital justifications) in SQE language, and a one-page "full-stack supplier engineer" role charter presented to your manager — putting the current role on paper for the first time. (It is not even on your resume yet.)

### 1.2 Supplier scorecard & spend cube
*Domains: Supplier Engineering, Procurement, Data Analytics, Business Analysis*

KPI/scorecard design for suppliers (quality, OTD, responsiveness), spend cube construction (supplier × category × site, Pareto/tail spend), Power BI star-schema + DAX depth, and a supplier review cadence — your MOS pattern applied to suppliers.

**Deliverable:** a live Power BI supplier scorecard + company spend cube feeding a monthly supplier performance review that you chair. *Honesty note (regraded): your Smithfield toolkit governed equipment vendors, not material suppliers — this port is real new work, not a re-run.*

### 1.3 Ship it legally: biological shipping, biosafety & cold chain
*Domains: Warehouse/Logistics, Risk, Supplier Engineering*

Category A/B classification (UN3373), packing instructions P620/P650, dry ice UN1845, data loggers and excursion response, specialty couriers and chain of custody, USDA/CDC permit touchpoints. **Paired with personal biosafety training**: OSHA bloodborne pathogens, BSL-2 practices, PPE/sharps — required if you physically receive, inspect, or audit biological materials and supplier floors. Both are days-long, cheap, and degree-free.

**Deliverable:** IATA infectious-substances/dry-ice shipper certification + bloodborne pathogens/BSL-2 training completed; a written site shipping SOP and excursion-response playbook adopted by operations.

*Cold chain was regraded from "strengthen" to "new": Smithfield perishables intuition is real, but validated cold-chain distribution (thermal packaging qualification, lane validation, excursion disposition) is a genuine learning curve — budget for it.*

### 1.4 Formal corrective action: 8D & SCAR discipline
*Domains: Supplier Engineering, Industrial Engineering*

8D layered on your Apollo RCA mastery; SCAR issuance and escalation governance; NCR flow and disposition (use-as-is / rework / return); containment; CAPA effectiveness verification; cost of poor quality.

**Deliverable:** a SCAR/8D template pack and NCR log, exercised on the first real supplier nonconformance.

### 1.5 Three small errands with outsized returns *(added by the review pass)*

1. **Contract triage primer (~10 hours).** You are signing supplier agreements *today*, and without ISO 13485 the contract and quality agreement effectively ARE your quality system. Before Stage 2's full contracting module: what PO T&Cs commit you to, what a quality agreement must contain, Incoterms orientation, and when to escalate to counsel. Do not approve terms for months with no framework.
2. **Freezer-failure playbook.** Inbound shipping is not the only cold-chain exposure: a ULT freezer or LN2 failure over a weekend can destroy months of irreplaceable donor-derived inventory. Draft a loss-of-storage contingency (alarms, backup power, transfer plan) now; full storage qualification comes in Stage 2. Your Arduino/RFID/IoT background makes a monitoring-and-alerting build a fast, visible win.
3. **Price the degree question once.** Get the 2001–2005 University of Lima transcript evaluated (WES or ECE), and price two completion routes: a competency-based online BS (e.g., WGU) vs. the MITx MicroMasters→master's ladder. Several ceilings this plan works around (CMA blocked, CAP uncertain, HR degree screens) disappear entirely with a completed degree — a plan that never prices that option is incomplete. Decide once, with numbers; revisit at Stage 5.

**Stage 1 droppables when work spikes:** 1.4 slides right; 1.1's case studies can trail. The IATA + biosafety trainings and the contract triage primer do not slide — they are the legally/operationally required floor.

---

## Stage 2 — Build the Operating System (months 3–9)

**Goal:** design the missing skeleton of the role — a fit-for-purpose quality system, repeatable qualification and audit machinery, a category strategy with real negotiation method, and an ISO 31000-grounded risk practice tuned to biological supply fragility.

### 2.1 Fit-for-purpose QMS & supplier qualification
*Domains: Supplier Engineering, Business Analysis, Quality*

ISO 9001:2015 structure (clause 8.4 is literally your job description), document/record control, risk-based thinking; GLP awareness (21 CFR Part 58) and research-grade vs. GMP-grade distinctions; risk-tiered supplier qualification (questionnaires, site surveys, ASL governance, quality agreements); BPMN mapping of the supplier lifecycle — your NAVSUP skill pointed at your own company.

**Added by the review pass — the customer-facing half:** you will be *on the receiving end* of audits. Your med-device/pharma customers will audit you as their tier-1 supplier, and without ISO 13485 you are the person who defends the supplier-control story. Learn audit hosting, customer supplier-quality questionnaires, and **requirements flow-down** (what customers' GLP protocols and tissue-provenance needs demand of *your* acceptance criteria). Also fold in **procurement ethics and one-person controls**: conflicts of interest, gifts/anti-bribery (FCPA awareness), supplier code of conduct, and segregation-of-duties guardrails — as sole buyer you personally embody every control a procurement department normally separates, and any customer or investor audit looks there first.

**Deliverable:** a documented, BPMN-mapped supplier qualification process with tiered requirements, a governed ASL, a quality-agreement template, a one-page procurement policy with self-designed controls, and a **customer-facing quality dossier** you could hand an auditing customer tomorrow.

### 2.2 Supplier auditing
*Domains: Supplier Engineering, Quality*

ISO 19011 principles; system vs. process vs. product audits; audit planning and checklist design; remote/desk audits; findings classification, reporting, corrective-action closure. Take an ISO 9001:2015 Lead Auditor course (Exemplar Global / CQI-IRCA, ~40 hours). *Correction: the course confers method and credibility, not a license — second-party supplier audits require no license at all. Its value is that you have never conducted a structured audit, and this is the fastest way to learn how.*

**Deliverable:** an annual supplier audit program + your first complete structured supplier audit — plan, checklist, report, closed corrective actions.

### 2.3 Category strategy, sole-source dynamics, negotiation & contracts
*Domains: Procurement, Economics, Business Strategy*

Kraljic segmentation and supplier preferencing; Porter's Five Forces on supply markets; sole-source and seller's-market tactics; customer-of-choice behavior for a small buyer; negotiation method (BATNA, integrative trades, repeated-game and anchoring dynamics); full contract fundamentals — MSA/SOW structure, quality clauses, risk allocation (warranty, liability, indemnity, IP), Incoterms 2020. **Added: NDA and supplier-IP discipline** — NDAs before technical exchanges, protecting supplier proprietary process data you collect during audits and should-cost work, and data-handling rules for where supplier documents may and may not go (dashboards, shared drives, AI tools).

**Deliverable:** a Kraljic-segmented map of the entire supply base with per-quadrant strategies, plus a written negotiation plan executed on one live contract renewal or LTA.

### 2.4 SCRM foundation: ISO 31000, FMEA & biological supply fragility
*Domains: Risk, Supplier Engineering, Industrial Engineering*

ISO 31000 framework, risk criteria, register and heat-map craft done properly (and their documented limits — Hubbard's critique); supplier/process FMEA (AIAG-VDA) paired with your RCA practice as its reactive twin; sole/single-source mapping, dual-sourcing economics, alternate qualification, buffer strategy; donor-network failure modes (seasonality, herd health, variability, consent/traceability); business-continuity starter (BIA). **Added: the legal frameworks for tissue, by name** — FDA 21 CFR Part 1271 (HCT/P) and its research-use boundaries, UAGA and why tissue is priced as recovery fees rather than sold, IRB/consent documentation standards, and where "research use only" materials legally sit. A supplier engineer who cannot say whether a supplier's material falls inside or outside Part 1271 cannot assess compliance risk in his own supply base. **Added: validated on-site storage** — ULT/LN2 qualification, temperature mapping, alarm systems, backup power (completing Stage 1's playbook).

**Deliverable:** a lightweight SCRM playbook (your one-person risk operating model) + FMEAs on the top 3 critical suppliers, ending in at least one leadership-funded mitigation.

**Stage 2 droppables:** 2.2's course can slide a quarter (do the reading and shadow-audit meanwhile). 2.1 and 2.4's tissue-law content should not slide — they are what customers and investors probe.

---

## Stage 3 — Quantitative Core & First Credentials (months 9–18)

**Goal:** formalize the statistical, cost, and data machinery that makes your decisions defensible — and cash in the first no-degree credential. *(The review pass split the original overloaded stage: planning/CPIM moved to Stage 4 so this stage fits alongside a full-time job.)*

### 3.1 Statistical quality toolkit (CSQP/CQE body of knowledge)
Rigorous inference (hypothesis tests, CIs, power, regression diagnostics); SPC and capability including short-run/high-mix SPC for biological variability; acceptance sampling (Z1.4, Z1.9, c=0, OC curves, skip-lot, CoA-based acceptance); MSA/gage R&R, calibration basics; DOE orientation.

**Deliverable:** a right-sized incoming acceptance plan for research-grade biological materials, documented with its statistical rationale and in daily use — plus the **ASQ CSQP exam** passed on the back of this study.

### 3.2 Should-cost, TCO & supplier financial health
Cost breakdown structures and should-cost modeling for custom low-volume items — your time-study engine aimed at supplier quotes; TCO and landed cost (freight, duty, cold-chain handling, expiry loss; Incoterms depth); supplier financial-health screening (ratio analysis, D&B signals, Altman Z, red flags in small private suppliers); make-vs-buy with relevant/avoidable-cost framing; escalation/indexation clauses (PPI pass-through).

**Deliverable:** a should-cost + TCO model deployed in one live LTA negotiation, and a financial-health screen added to the supplier risk register with a monitoring cadence — your "risky supplier" judgments now carry numbers.

### 3.3 Data spine upgrade: SQL, Python & master data
SQL proper (joins, window functions, CTEs; feeding Power BI from a database instead of workbooks) — *regraded to "new": no SQL deliverable exists anywhere in your history; the Power Query concepts transfer but budget real learning time*. pandas/Python replacing fragile VBA; supplier and item master-data discipline; lot/CoA traceability as the substitute for a mandated QMS data structure.

**Deliverable:** a SQL-backed supplier/item master with lot-level CoA traceability and one automated Python pipeline replacing a manual workbook process.

**Stage 3 droppables:** 3.3 can stretch across Stage 4. The CSQP exam anchors this stage — protect it.

---

## Stage 4 — Planning, Dollars, AI & Executive Voice (months 18–32)

**Goal:** complete the planning half of the hybrid role, express risk in dollars executives can fund, automate the one-person function, and package the whole operating system in executive language. Two exams live here (CPIM, then CSSBB *or* CQE) — space them.

### 4.1 Planning for perishable, lumpy supply (+ CPIM)
Inventory policy under shelf life (safety stock, service levels, reorder points, expiry-aware carrying cost); intermittent-demand forecasting (Croston/SBA) in R/Python; MRP logic and planning parameters (completing your SAP BOM depth); Factory Physics laws for supplier lead-time conversations; a lightweight supply-readiness S&OP — your MOS pattern loaded with demand/supply content.

**Deliverable:** documented safety-stock and reorder policies for the top critical materials + a monthly supply-readiness S&OP you design and chair — the visible unification of procurement, capacity, and risk into one cadence. **ASCM CPIM** exam here (no prerequisites at all).

### 4.2 Dollar-quantified risk & resilience
Expected monetary value; Monte Carlo simulation of supply risk in Python/Excel; calibrated estimation (Hubbard); TTR/TTS resilience metrics and node-failure stress tests for sole-source biological inputs; cost-of-disruption and risk-adjusted TCO; contractual risk transfer (force majeure, liability, cargo insurance for cold-chain shipments); BCP with BIA and a tabletop exercise.

**Deliverable:** an expected-dollar-ranked supplier risk dashboard ("this exposure is $180k/yr; mitigation costs $40k") driving at least one funded resilience investment, plus the company's first tested continuity plan for tissue supply.

### 4.3 AI & automation for the one-person function
Ops copilot patterns: structured extraction from supplier PDFs/CoAs, RFQ comparison, intake triage (low-code Power Automate/AI Builder first; Python/RAG as skills mature); process mining on P2P and supplier lead-time logs (PM4Py/Celonis); evaluation and guardrails. **Hard requirement added by the review pass:** a written supplier-data confidentiality rule set *before* any supplier document feeds an AI tool — Stage 2's NDA discipline applied to your own tooling. Feeding suppliers' cost structures and audit findings into LLM tools without data-handling rules is a concrete legal and relationship risk.

**Deliverable:** a working copilot or automation that measurably cuts supplier-document/RFQ processing time, demoed to leadership, plus an internal AI-enablement training you author — extending your Vintun prompt-engineering training into an ops-AI signature.

### 4.4 Executive strategy, communication & operating model
Pyramid Principle / SCQA and hypothesis-driven structuring; competitive strategy applied to supply markets; target-operating-model design of your own function; business cases for resilience and capability spend; benefits realization; ADKAR/Kotter named onto your plant-closure and rollout record.

**Deliverable:** an annual supplier strategy memo + a target-operating-model blueprint for the supplier engineering function, presented to executives — the document that turns "all over the place" into a function you visibly designed and own.

### 4.5 Supplier development & experimental rigor *(droppable to Stage 5)*
Joint kaizen at supplier sites; transferring your lean/CI training craft to struggling niche suppliers; DOE applied to supplier/material qualification (factorials, ANOVA in Minitab).

**Deliverable:** one completed supplier development engagement with before/after metrics — the differentiator almost no SQE can execute, and a flagship interview story.

**Certify the statistics here: ASQ CSSBB or CQE (pick one; they overlap heavily).** *Correction on the "affidavit-ready" claim: CSSBB requires completed projects documented as Six Sigma projects with signed affidavits. Your kaizen/SMED/RPM work is savings-documented CI, not DMAIC-framed Six Sigma — feasible to reframe, but it takes deliberate write-ups and a former manager willing to sign. Start that legwork a year early.*

---

## Stage 5 — Branch & Capstone (months 32–48+)

Pick **one** branch (revisit annually); the others remain optionality. Each has a capstone credential and a public artifact.

| Branch | For the trajectory | Core content | Capstone |
|---|---|---|---|
| **A — Sourcing & Supply Risk Leadership** | Strategic sourcing / category management | CPSM BoK, tariffs/nearshoring (your bilingual LatAm edge), advanced contracting (indexation, capacity reservation), commodity literacy for animal-protein inputs | **CPSM** (5-yr no-degree route — verify ISM counts your mixed IE/vendor years *in writing* before paying) + 2–3 written category playbooks |
| **B — Transformation & Consulting** | Independent or firm consulting | PMP + CBAP formalization, SAP MM/P2P depth, SCOR/APQC vocabulary, process mining at depth, offer design & pricing | **PMP** (no-degree path: HS diploma + 60 months leading projects + 35 contact hours) + a dollarized end-to-end case study of the operating system you built in Stages 1–4 |
| **C — Analytics & Planning Leadership** | S&OP / digital supply chain | MITx SCM MicroMasters (SC0x–SC4x), discrete-event simulation (SimPy) and optimization (PuLP/OR-Tools), PL-300 → DP-600, supplier risk scoring with tree ensembles | **MITx MicroMasters** — open enrollment, rigorous, and can ladder into an accredited master's: the long-run cure for the missing degree |
| **D — Quality Leadership in the Biological Niche** | Director of Supplier Quality, biotech tools / ex-vivo / CRO | CQE (completing the ASQ triple), AATB/ISBER depth, GDP and thermal packaging qualification (ISTA 7D/7E), IQ/OQ/PQ awareness, CBCP once BC experience accrues | The company's mature QMS under your ownership + one **public artifact** (conference talk, ISBER/AATB contribution, or published article on supplier engineering for ex-vivo materials) — becoming a named authority in an underserved niche |

---

## Credential strategy (sequenced, no-degree-verified)

| # | Credential | Org | When | Why — and the fine print |
|---|---|---|---|---|
| 1 | IATA Dangerous Goods (Infectious Substances Cat A/B + dry ice) **+ OSHA BBP/BSL-2 training** | IATA-accredited (e.g., Saf-T-Pak); OSHA-authorized | Stage 1, months 1–2 | Legally/safety required for the role; zero degree gatekeeping; days and a few hundred dollars; recurrent every 24 months. Fastest credential-to-authority conversion available. |
| 2 | ISO 9001:2015 Lead Auditor course | Exemplar Global / CQI-IRCA provider | Stage 2 | No prerequisites. Teaches the audit method you've never formally practiced. It is training + credibility, **not a license** — none is needed for second-party audits. |
| 3 | **CSQP** — Certified Supplier Quality Professional | ASQ | Stage 3, after the statistical module | The credential matching your exact title; its BoK ≈ Stages 1–3. Eligibility: **8 years on-the-job in the BoK, ≥3 in a decision-making role; a degree only waives years, never required** — your ~20 years qualify outright. (One agent claimed "5 years"; that is wrong — the requirement is 8.) |
| 4 | **CPIM** — Planning & Inventory Management | ASCM (APICS) | Study Stage 4, exam ~months 20–26 | **No degree or experience prerequisite at all.** BoK maps 1:1 onto your planning gaps. Chosen over CSCP (breadth) because planning depth beats breadth for your actual gaps; CSCP stays an optional later add. |
| 5 | **CSSBB** *or* **CQE** | ASQ | Stage 4, months 28–34 | Certifies the statistical layer of 20 years of CI work. CSSBB eligibility is project-affidavit-based (no degree) but needs DMAIC-framed write-ups and a signer — start early. CQE: 8 years, 3 decision-making, no degree required. Pick one; the other can follow in Branch D. |
| 6 | Branch capstone: CPSM / PMP / MITx MicroMasters / CQE+CBCP | ISM / PMI / MITx / ASQ+DRI | Stage 5 | All have real no-degree routes (verify CPSM experience-counting with ISM in writing first; PMI-PBA, if ever swapped in, also requires 2,000 hours on project teams; CBAP also needs professional references). Choosing **one** prevents the credential-collecting trap. |

**Deliberately cut:** CSCP (redundant with CPIM now), CIPS (pick CPSM *or* CIPS by target market, not both), CMA (degree-blocked — use its Part 1 materials as a free syllabus anyway), CAP (eligibility uncertain without a degree — confirm with INFORMS before ever paying), Lean Bronze/Silver (subsumed by CSSBB), CMC (verify degree rules; the portfolio serves the same trust function), PMI-PBA (CBAP wins on recognition). Verify current availability/branding of the ASCM Supply Chain Resilience Certificate before relying on it — ASCM restructures certificates periodically.

---

## Career trajectories this supports

1. **Director of Supplier Quality & Supply Chain (biotech tools / ex-vivo / CRO niche)** — grow in place: the operating system you build in Stages 1–4 IS the function, and at a scaling company its designer is its natural leader. Emphasize Stages 1–2 fully, 3.1, Branch D.
2. **Strategic Sourcing / Category & Supply Risk Manager** — your most credible market pivot: 20 years of vendor-facing engineering + should-cost modeling few buyers can do, in a lane where the missing degree matters least against commercial results. Emphasize 2.3, 3.2, 4.2, Branch A.
3. **Supply Chain & Procurement Transformation Consultant** — extends the Vintun track; the supplier operating system becomes a dollarized case study and calling card. Emphasize 1.1, 4.3, 4.4, Branch B.
4. **Supply Chain Analytics / Planning Leader** — "the supply chain person who can actually build the models": SQL/Python/simulation on your proven ETL→dashboard→MOS pattern. Emphasize 3.3, 4.1, 4.3, Branch C.

## Timeline honesty

The full plan is ~48 months at a sustained 5–7 hrs/week. The per-stage estimates assume zero slack for work crises, exam retakes, or life. That is why every stage names its droppables, why only Stage 1's compliance floor is non-negotiable, and why the branch structure defers everything that can be deferred. The plan is a map, not a debt.
