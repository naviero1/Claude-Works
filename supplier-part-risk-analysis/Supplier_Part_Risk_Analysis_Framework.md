# Supplier Part Risk Analysis — Framework & Scoring Rubric (v0.2 draft)

**Context:** Built for a **tissue-models** operation (ex-vivo **porcine tissue** sourced from local slaughterhouses, used as a substrate for **surgical R&D, instrument/energy-device testing, and training** — *not* an implantable medical device). Also covers standard/catalog and custom-engineered purchased parts.

**Status:** Draft. Scoring anchors are adapted from recognized risk methods (see *Traceability* §9) so the method is defensible. Acceptance thresholds (§6) are **placeholders to be ratified internally** (Quality + EHS).

> ✅ **Scope correction from v0.1:** Tissue models are **not medical devices**, so medical-device standards (ISO 14971/13485/**22442**/10993/14160) are **optional good-practice references, not governing**. Xenotransplant concerns (PERV, decellularization, α-Gal, residual DNA) are **out of scope** — they apply to implants, not test/training substrates. The biological layer is re-centered on **handler biosafety** and **model fitness-for-purpose**.

---

## 1. Design principle

Risk is multi-dimensional. We keep the **FMEA scoring engine** (it's general-purpose and audit-friendly) but point it at the consequences that actually matter for tissue models: **staff infection, invalid test/training results, and operational/compliance loss.**

- **FMEA (AIAG-VDA)** — score **Severity / Occurrence / Detection** 1–10; prioritize with **Action Priority (AP: High/Medium/Low)**, which weights **Severity → Occurrence → Detection**. (RPN was retired in 2019 because it weights S/O/D equally.)
- **Self-defined acceptability** — the ISO 14971 *principle* still helps even though the standard doesn't govern us: **we** define and document our own objective acceptability criteria and keep the records. Here that means a **Quality + EHS** policy, not a regulatory submission.

**Two-layer model:**

| Layer | Applies to | What it scores |
|---|---|---|
| **Layer A — Universal supplier-part risk** | **All** parts | Failure consequence (S), defect likelihood (O), escape likelihood (D) → **Action Priority**; plus **Supply Continuity** and **Supplier Maturity** |
| **Layer B — Tissue risk** | **Tissue only** | **Fitness-for-purpose**, **lot-to-lot consistency & traceability**, **handler biosafety**, **cold chain**, **waste/disposal** + a legal/biosafety **gate** |

A tissue part carries **both** A and B scores; Layer B can override and force a higher class. Custom and catalog parts use Layer A only.

---

## 2. Use-case tier (tissue only) — sets the consistency bar

How strict the **consistency/traceability** requirement is depends on what the model is *for*. Tag each tissue part:

| Use tier | Examples | Consistency/traceability rigor |
|---|---|---|
| **T1 — V&V / test data** | Energy-device performance, design verification, claims support | **Highest** — reproducible lots, full traceability, test-method validation, controlled acceptance criteria |
| **T2 — Training** | Surgeon wet-labs, instrument familiarization | **Medium** — fidelity matters; statistical reproducibility less critical |
| **T3 — R&D / prototyping** | Feasibility, early design iteration | **Lower** — flexible fidelity |
| **T4 — Demo / marketing** | Trade shows, sales demos | **Appearance/behavior** over data integrity |

> **Open item:** confirm which tiers apply (a part may span several). T1 is the only tier that pulls in test-method-validation rigor (e.g., ISO/IEC 17025-style repeatability) — if any tissue feeds V&V data, that axis weights heavily.

---

## 3. Layer A — core scoring scales (1–10)

S/O/D structure from AIAG-VDA, anchors re-pointed at tissue-model consequences.

### 3.1 Severity (S) — consequence if this part / tissue fails its purpose
| Score | Anchor |
|---:|---|
| 10 | **Staff exposure causing serious zoonotic infection**; **or** invalid tissue model produces erroneous **V&V data that could drive an unsafe device decision**. |
| 9 | **Compliance breach** — illegal/undocumented byproduct sourcing, biohazard-waste or lab-safety violation. |
| 8 | Model failure **invalidates a critical test/study** — must repeat; major program/schedule impact. |
| 7 | Degrades validity of test or training results. |
| 6 | Loss of a secondary test/training capability. |
| 5 | Degraded secondary capability. |
| 4 | Usable but poor fidelity; re-prep/rework needed. |
| 3 | Minor inconsistency, noticeable. |
| 2 | Slight. |
| 1 | No discernible effect. |

### 3.2 Occurrence (O) — likelihood the supplier delivers nonconforming material
| Score | Anchor (supplier/source maturity) |
|---:|---|
| 10 | New supplier/source, **no history**, no controls. |
| 9 | First use of new source/process; no validation experience. |
| 8–6 | Increasingly similar to a proven source; partial history; defect rate high→moderate. |
| 5–4 | Proven source with minor changes; documented track record. |
| 3–2 | Mature source, **long history of good conformance**. |
| 1 | Failure cause **eliminated** by control. |

### 3.3 Detection (D) — likelihood a problem **escapes our incoming/intake checks**
| Score | Anchor |
|---:|---|
| 10 | **No intake inspection/acceptance check exists** for this characteristic. |
| 9 | Check not specific to the failure mode (e.g., visual only, misses freshness/pathology). |
| 8 | New/unproven acceptance method. |
| 7–5 | Proven method but sampling-based / detects late. |
| 4–2 | Proven method, effective sampling, catches early. |
| 1 | Problem **cannot pass** (100% check / error-proofing). |

---

## 4. Procurement axes (1–5; 5 = highest risk)

From Kraljic supply-risk segmentation + CSQP/Gordon scorecard criteria.

### 4.1 Supply Continuity Risk
| Score | Condition |
|---:|---|
| 5 | **Sole source**, no qualified alternative, variable availability, high switching cost. |
| 4 | Single source, alternative exists but unqualified. |
| 3 | Dual source, moderate reliability. |
| 2 | Multi-source, reliable. |
| 1 | Many interchangeable sources. |

### 4.2 Supplier Maturity Risk *(inverse of scorecard performance)*
Drivers (CSQP 100-pt scorecard): quality/defect history, corrective-action responsiveness, on-time delivery, documentation, audit results.
| Score | Condition |
|---:|---|
| 5 | No quality system, no history, poor/late corrective action. |
| 4 | Basic controls; spotty history. |
| 3 | Average track record. |
| 2 | Strong record, responsive. |
| 1 | Mature quality system, excellent record. |

---

## 5. Action Priority (AP) — from S, O, D

Severity-weighted, per AIAG-VDA. Working rule (use the full AP table for edge cases):

| Condition | AP |
|---|---|
| **S 9–10** with O ≥ 2 | **High** |
| S 7–8 with O ≥ 4, **or** S 4–6 with O ≥ 6 and D ≥ 5 | **High** |
| Moderate S with moderate O/D | **Medium** |
| Low S, low O, strong detection | **Low** |

- **High** → action required *or* documented justification controls are adequate.
- **Medium** → action should be taken or justified.
- **Low** → optional / monitor.
- Any **Severity 9–10** with AP High/Medium → escalate to management/EHS review.

---

## 6. Final Risk Class & acceptability

### 6.1 Classification rule (placeholder — ratify with Quality + EHS)
Assign the **highest** class triggered.

| Final Class | Triggered when… |
|---|---|
| **CRITICAL** | Tissue **legal/biosafety gate not cleared** (§7.3); **or** any Layer-B dimension = 5; **or** AP High with S 9–10; **or** AP High with Supply Continuity = 5. |
| **HIGH** | AP High; **or** any Layer-B dimension = 4; **or** Supply Continuity = 5; **or** Supplier Maturity = 5. |
| **MEDIUM** | AP Medium; **or** any procurement/Layer-B axis = 3. |
| **LOW** | AP Low and all axes ≤ 2. |

### 6.2 Action playbook by class
| Class | Sourcing | Intake acceptance | Audit cadence | Buffer | Re-eval trigger |
|---|---|---|---|---|---|
| **Critical** | Dual-source required; contingency plan | Tightened / lot-by-lot acceptance | On-site annually + for-cause | Qualified buffer stock | Any nonconformance; source/herd change |
| **High** | Qualify a second source | Tightened sampling | On-site every 1–2 yr | Safety stock | Adverse trend; corrective action |
| **Medium** | Monitor single source | Normal sampling | Remote/desk review yearly | Standard | Scorecard drop |
| **Low** | Reorder | Reduced / skip-lot | Self-assessment | Min/reorder | Periodic |

---

## 7. Layer B — Tissue risk (porcine, ex-vivo, non-implant)

Score each 1–5 (5 = highest risk).

### 7.1 Dimensions
| Dim | Measures | 5 (worst) → 1 (best) |
|---|---|---|
| **B1 Fitness-for-purpose / fidelity** | Right species/organ/cut; mechanically representative; no disqualifying pathology or damage | 5: wrong/variable anatomy, unfit → 1: specified anatomy, validated representativeness |
| **B2 Freshness / cold chain** | Time-from-slaughter, temperature control, degradation | 5: uncontrolled warm time, unknown age → 1: validated cold chain, defined max time-to-use |
| **B3 Lot-to-lot consistency & traceability** | Reproducibility + source/species/date/lot records *(weight by use tier §2)* | 5: no traceability, high variability → 1: full traceability, controlled lot acceptance (req'd for T1/V&V) |
| **B4 Handler biosafety / zoonotic exposure** | Staff infection risk from raw tissue + controls in place | 5: no PPE/biosafety practice, untested source → 1: BMBL-aligned practice, PPE, source controls, trained staff |
| **B5 Waste / biohazard disposal** | Compliant disposal & decontamination | 5: no defined biohazard waste path → 1: compliant disposal + decon validated |

### 7.2 Handler biosafety — the dominant tissue risk
Raw porcine tissue exposes **your staff** to zoonoses, the highest-likelihood real harm here. Key agents (from *Diseases of Swine*):
- **Through skin breaks / contact:** *Strep suis* (serious — meningitis/sepsis), *Erysipelothrix* (erysipeloid), *Brucella*, *Leptospira*.
- **Blood/fluids & ingestion:** Hepatitis E, *Salmonella*, *Toxoplasma*, *Trichinella*.
- **Aerosol during cutting:** Influenza A, *Strep suis*.
- **Colonization:** livestock-associated MRSA.

**Control hierarchy:** source from health-monitored herds → **PPE + cut discipline** (the key control) → biosafety practices per **CDC/NIH BMBL** at the appropriate biosafety level → trained handlers → defined waste/decon. *Abattoir inspection alone is not a safeguard — it misses HEV, Trichinella, Toxo, subclinical carriers.*

### 7.3 Legal / biosafety gate (run for every tissue source)
| Tier | Concern | Gate |
|---|---|---|
| **Gate 1 — Legal sourcing & reportable disease** | African/Classical Swine Fever, FMD status; legal byproduct/inedible-material sourcing (USDA/APHIS, state ag) | Source must be **legally documented & status-clear**. Not clear → **CRITICAL, do not source**. |
| **Gate 2 — Handler zoonoses** | HEV, *Strep suis*, *Erysipelothrix*, *Brucella*, *Leptospira*, *Salmonella*, MRSA, Influenza A, *Trichinella*, *Toxoplasma* | Requires PPE + BMBL-aligned practices + trained staff. Gaps escalate class. |

*(v0.1 had a third "xeno" tier — removed: PERV/PCMV/PCV are implant concerns, not relevant to ex-vivo test/training tissue.)*

---

## 8. Standards & references that actually apply

**Governing (occupational / operational — not device regulation):**
| Reference | Role | Have it? |
|---|---|---|
| **CDC/NIH BMBL** (Biosafety in Microbiological and Biomedical Laboratories) | Safe handling of porcine tissue; biosafety levels & practices | ❌ (free from CDC) |
| **OSHA biosafety / general duty** (note: 1910.1030 bloodborne is human-source — animal tissue falls under general biosafety) | Worker protection | ❌ (free) |
| **USDA APHIS / state Dept. of Agriculture** | Legal sourcing of animal byproduct / inedible material | ❌ (free) |
| **IATA DGR / DOT 49 CFR (UN3373, Cat. B)** | If tissue is shipped between sites | ❌ (ref) |
| Local biohazard / medical-waste disposal rules | Disposal path | ❌ (jurisdiction-specific) |

**Optional good-practice references (rigor, not required):**
| Reference | When useful | Have it? |
|---|---|---|
| AIAG-VDA FMEA Handbook (2019) | The S/O/D + Action Priority engine | ✅ |
| ISO 14971:2019 | Borrow the acceptability-criteria *discipline* | ✅ |
| ISO/IEC 17025 (or internal test-method validation) | **Only if tissue feeds V&V data (T1)** — repeatability/reproducibility | ❌ |
| Tissue-engineering / biomechanics texts (Badylak; Bronzino) | Defining "representative" fidelity (B1) | ✅ |

> **Net change from v0.1:** the medical-device standards I flagged as critical gaps (ISO 22442/10993/14160) are **no longer needed**. The real reference gap is **biosafety/handling/sourcing** material, most of which is **free** (CDC BMBL, OSHA, USDA APHIS).

---

## 9. Traceability (defensibility)

| Rubric element | Source |
|---|---|
| S/O/D 1–10 anchors; Action Priority (Severity-weighted; RPN retired) | AIAG-VDA FMEA Handbook, tables D1/D2/D3, §2.5.10 |
| Self-defined acceptability discipline + record-keeping | ISO 14971:2019 (cl. 4.2/4.4/5.5/6) — used as principle, not as governing standard |
| Supply Continuity (Kraljic) | CSQP Handbook, Ch. 2 |
| Supplier Maturity / scorecard drivers | CSQP Handbook Fig. 3.4; Gordon Ch. 1–3 |
| Risk-based audit cadence & finding classes | CSQP Handbook Ch. 6 (Table 6.1) |
| Porcine zoonoses, transmission routes, inspection limits | Diseases of Swine, 11th ed. (Ch. 1/5/9/12 + domain knowledge) |
| Handling biosafety practices | CDC/NIH BMBL *(to be acquired)* |

---

## 10. Using the template
See `Risk_Scoring_Template.csv` — one row per part. Tag tissue parts with a **use tier** (§2), fill Layer A + procurement axes + (for tissue) Layer B and the legal/biosafety gate. Final class & actions follow §6.

---

*v0.2 — re-scoped for tissue models (non-device). Open items: (1) confirm tissue use tier(s) (§2) — V&V vs training/R&D/demo; (2) Quality + EHS to ratify acceptability thresholds (§6.1); (3) acquire CDC BMBL + USDA/APHIS sourcing guidance (§8, mostly free).*
