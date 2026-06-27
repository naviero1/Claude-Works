# Supplier Part Risk Analysis — Framework & Scoring Rubric (v0.1 draft)

**Purpose:** a single, repeatable method to evaluate **every part** we buy — standard/catalog parts, custom-engineered parts, and **porcine tissue sourced from local slaughterhouses** — and assign each a defensible **risk class** with a matching action plan.

**Status:** First draft. Scoring anchors are adapted from recognized standards (see *Traceability* §9) so the method is audit-defensible. Acceptance thresholds (§6) are **placeholders that management must ratify** before use.

> ⚠️ **Scope assumption:** This draft assumes the porcine tissue feeds a **biomedical / tissue-engineering** application. If the end use is food, pet-food, or research-reagent grade, the governing standards in §8 change. Confirm before finalizing.

---

## 1. Design principle

Risk is not one number. Both ISO 14971 (medical-device risk management) and the AIAG-VDA FMEA method decompose it:

- **ISO 14971** — *risk = probability of occurrence of harm × severity of that harm.* The standard deliberately **does not** mandate a risk matrix or acceptable levels; the manufacturer must **define its own objective acceptability criteria and record the categorization system in the risk management file.**
- **AIAG-VDA FMEA** — splits "probability" into **Occurrence** (how often the cause happens) and **Detection** (chance it escapes), scores **Severity / Occurrence / Detection** 1–10, and prioritizes with **Action Priority (AP: High/Medium/Low)** — which weights **Severity first, then Occurrence, then Detection.** (RPN was *dropped* in the 2019 edition because it weights S, O, D equally.)

We therefore use a **two-layer model**:

| Layer | Applies to | What it scores |
|---|---|---|
| **Layer A — Universal supplier-part risk** | **All** parts | Failure consequence (S), defect likelihood (O), escape likelihood (D) → **Action Priority**; plus **Supply Continuity** and **Supplier Maturity** |
| **Layer B — Biological source risk** | **Tissue parts only** | Herd/source status, abattoir/collection controls, bioburden, viral/TSE inactivation, immunogenicity, + pathogen-exclusion gate |

A tissue part carries **both** an A score and a B score; for biologics the B layer can override and force a higher class. Custom and catalog parts use Layer A only.

---

## 2. Step-by-step process (mirrors ISO 14971 clause flow)

1. **Identify & segment the part** — Tissue / Custom / Catalog (drives which layers apply).
2. **Score Layer A** — Severity, Occurrence, Detection (§3) → derive **Action Priority** (§5).
3. **Score procurement axes** — Supply Continuity + Supplier Maturity (§4).
4. **If tissue → score Layer B** (§7) and run the **pathogen-exclusion gate** (§7.3).
5. **Aggregate → Final Risk Class** (§6).
6. **Assign actions** from the playbook (§6.2): sourcing strategy, incoming-inspection level, audit cadence, safety stock.
7. **Record & trace** — owner, review date, re-evaluation trigger; keep the record in the risk file (§9).

---

## 3. Layer A — core scoring scales (1–10)

Anchors adapted from AIAG-VDA FMEA tables D1/D2/D3 to a purchased-part / medical context.

### 3.1 Severity (S) — consequence if this part fails
| Score | Anchor |
|---:|---|
| 10 | Failure can cause **patient death or serious injury**, or **transmit infectious disease** (no warning). |
| 9 | **Regulatory noncompliance / reportable event**; loss of sterility or biocompatibility. |
| 8 | **Loss of primary product function** — recall-level. |
| 7 | Degradation of primary function. |
| 6 | Loss of a secondary function. |
| 5 | Degradation of a secondary function. |
| 4 | Major appearance/usability defect; rework required. |
| 3 | Minor, noticeable defect. |
| 2 | Slight defect. |
| 1 | No discernible effect. |

### 3.2 Occurrence (O) — likelihood the supplier ships a nonconforming part
| Score | Anchor (supplier/process maturity) |
|---:|---|
| 10 | New supplier/process, **no history**, no prevention controls. |
| 9 | First use of new material/process by this supplier; no validation experience. |
| 8–6 | Increasingly similar to a proven process; partial history; PPM high→moderate. |
| 5–4 | Proven process with minor changes; documented capability. |
| 3–2 | Mature process, **long history of low PPM**, capable (Cpk OK). |
| 1 | Failure cause **eliminated** by design/process control. |

### 3.3 Detection (D) — likelihood a defect **escapes our incoming controls**
| Score | Anchor |
|---:|---|
| 10 | **No incoming inspection or test exists** for this characteristic. |
| 9 | Inspection not specific to the failure mode/cause. |
| 8 | New/unproven test method. |
| 7–5 | Proven method but sampling-based / detects late. |
| 4–2 | Proven method, effective sampling or SPC, catches early. |
| 1 | Defect **cannot pass** (100% automated detection / error-proofing). |

---

## 4. Procurement axes (1–5; 5 = highest risk)

Adapted from the Kraljic supply-risk axis and the CSQP/Gordon supplier-scorecard criteria.

### 4.1 Supply Continuity Risk
| Score | Condition |
|---:|---|
| 5 | **Sole source**, no qualified alternative, long/variable lead time, financially weak supplier, high switching cost. |
| 4 | Single source, alternative exists but unqualified. |
| 3 | Dual source, moderate lead time. |
| 2 | Multi-source, short lead time, stable. |
| 1 | Commodity, many interchangeable sources, financially strong. |

### 4.2 Supplier Maturity Risk *(inverse of scorecard performance)*
Drivers (from CSQP 100-pt scorecard): **certifications (ISO 13485/9001), PPM, SCAR responsiveness, on-time delivery, audit results.**
| Score | Condition |
|---:|---|
| 5 | Uncertified, no quality history, poor/late SCAR response. |
| 4 | Certified to ISO 9001 only; spotty history. |
| 3 | Certified, average scorecard. |
| 2 | Strong scorecard, low PPM, responsive. |
| 1 | ISO 13485 certified, excellent scorecard, validated processes. |

---

## 5. Action Priority (AP) — from S, O, D

Per AIAG-VDA, AP prioritizes **the action**, not just the score, weighting **Severity → Occurrence → Detection**. Simplified working rule (use the full AIAG-VDA AP table for edge cases):

| Condition | AP |
|---|---|
| **S 9–10** with O ≥ 2 (any meaningful chance) | **High** |
| S 7–8 with O ≥ 4, **or** S 4–6 with O ≥ 6 and D ≥ 5 | **High** |
| Mid combinations (moderate S with moderate O/D) | **Medium** |
| Low S, low O, strong detection | **Low** |

- **High** → action to improve prevention/detection **is required**, *or* documented justification that controls are adequate.
- **Medium** → action **should** be taken or justified.
- **Low** → action optional/monitor.
- Any **Severity 9–10** item with AP High/Medium → **management review** regardless of class.

---

## 6. Final Risk Class & acceptability

### 6.1 Classification rule (placeholder — ratify before use)
Assign the **highest** class triggered by any rule below.

| Final Class | Triggered when… |
|---|---|
| **CRITICAL** | Tissue **pathogen Tier-1 gate not cleared** (§7.3); **or** any Layer-B dimension = 5; **or** AP High **with** S 9–10; **or** AP High with Supply Continuity = 5. |
| **HIGH** | AP High; **or** any Layer-B dimension = 4; **or** Supply Continuity = 5; **or** Supplier Maturity = 5. |
| **MEDIUM** | AP Medium; **or** any procurement/Layer-B axis = 3. |
| **LOW** | AP Low and all axes ≤ 2. |

> **ISO 14971 note:** these thresholds are *our* acceptability criteria. The standard requires top management to define and document them as policy, and to record the categorization scheme in the risk management file. Treat the table above as a **draft for ratification**, not an external requirement.

### 6.2 Action playbook by class
| Class | Sourcing | Incoming inspection | Audit cadence | Inventory | Re-eval trigger |
|---|---|---|---|---|---|
| **Critical** | Dual-source mandatory; contingency plan | Tightened / 100% or validated lot release | On-site annually + for-cause | Safety stock + qualified buffer | Any nonconformance; any source/herd change |
| **High** | Qualify a second source | Tightened sampling (e.g. ISO 2859) | On-site every 1–2 yr | Safety stock | Adverse trend; SCAR |
| **Medium** | Monitor single source | Normal sampling | Remote/desk review yearly | Standard | Scorecard drop |
| **Low** | Catalog reorder | Skip-lot / reduced | Self-assessment | Min/reorder | Periodic |

---

## 7. Layer B — Biological source risk (porcine tissue only)

Score each dimension 1–5 (5 = highest risk). Anchors built on *Diseases of Swine* (11th ed.) source-risk framework + xenobiology domain knowledge.

### 7.1 Dimensions
| Dim | What it measures | 5 (worst) → 1 (best) |
|---|---|---|
| **B1 Herd / source status** | Health status & geography of source herd | 5: unknown/open herd, no health data, region with ASF/CSF/FMD/PRV concern → 1: certified closed high-health (SPF/PRRS-neg) herd in disease-free zone |
| **B2 Abattoir / collection controls** | Inspection status, cold chain, traceability | 5: **custom-exempt/uninspected** abattoir, no lot trace, long warm time → 1: federally inspected, validated cold chain, full traceability to source animal/lot |
| **B3 Bioburden & contamination** | Initial microbial load, endotoxin | 5: uncontrolled, untested → 1: low validated bioburden + endotoxin within limits |
| **B4 Viral/TSE inactivation & sterilization** | Validated inactivation capability & SAL | 5: none/unvalidated → 1: validated viral-inactivation + sterilization to defined SAL |
| **B5 Immunogenicity / decellularization** | α-Gal, residual DNA, biocompatibility | 5: not addressed → 1: validated decellularization, residual DNA & α-Gal within limits, biocompatibility tested |

### 7.2 Why abattoir inspection is necessary but **not sufficient**
Ante-/post-mortem inspection screens out overtly diseased animals and gross lesions, but **does not detect** the agents most relevant to biomedical tissue — HEV, *Trichinella* (low burden), *Toxoplasma*, PCV, PERV, latent herpesviruses, subclinical *Salmonella*/MRSA/*Strep suis* carriage. Those require **lab testing, herd history, and source certification.** Inspection is a baseline, not the safeguard.

### 7.3 Pathogen-exclusion gate (run for every tissue lot/source)
| Tier | Agents | Control & gate |
|---|---|---|
| **Tier 1 — Deal-breakers (regulatory/trade)** | African Swine Fever, Classical Swine Fever, Foot-and-Mouth, Pseudorabies (PRV) | Source region/herd must be **status-clear** (WOAH/USDA). **Not clear → CRITICAL, do not source.** |
| **Tier 2 — Handler/recipient zoonoses** | Hepatitis E, *Strep suis*, *Erysipelothrix*, *Trichinella*, *Toxoplasma*, *Brucella*, *Leptospira*, *Salmonella*, MRSA, Influenza A | Requires herd controls + **handler PPE/cut discipline** + targeted testing. Gaps escalate class. |
| **Tier 3 — Biomedical/xeno, invisible to inspection** | **PERV**, porcine cytomegalovirus / herpesviruses, PCV | Require **molecular screening + certified herds** — cannot be excluded by inspection. Gaps escalate class. |

**Controls hierarchy (best→baseline):** certified closed high-health herd → documented herd/geographic status → lab screening for inspection-invisible agents → ante/post-mortem inspection (baseline only) → handler PPE & cut discipline.

---

## 8. Standards this method should cite (governing framework)

| Standard | Role | In our library? |
|---|---|---|
| AIAG-VDA FMEA Handbook (2019) | S/O/D scales, Action Priority | ✅ |
| ISO 14971:2019 | Risk-management process & acceptability | ✅ |
| ISO 13485:2016 / ISO 9001:2015 | Supplier-control & QMS requirements | ✅ |
| **ISO 22442-1/-2/-3** | **Medical devices using animal tissue** — risk mgmt, sourcing/collection controls, **viral/TSE inactivation validation** | ❌ **gap** |
| **ISO 10993 series** | Biological evaluation / biocompatibility | ❌ gap |
| **ISO 14160** | Sterilization of single-use animal-tissue devices (liquid chemical) | ❌ gap |
| **ISO 11135 / 11137** | EO / radiation sterilization validation | ❌ gap |
| **WOAH (OIE) / USDA-FSIS / EMA TSE guidance** | Herd & abattoir status, TSE sourcing | ❌ gap |

---

## 9. Traceability (audit defensibility)

| Rubric element | Source |
|---|---|
| Severity / Occurrence / Detection 1–10 anchors | AIAG-VDA FMEA Handbook, tables D1/D2/D3 |
| Action Priority (H/M/L, Severity-weighted; RPN retired) | AIAG-VDA FMEA Handbook §2.5.10 |
| Risk = severity × probability; manufacturer-defined acceptability; risk management file & traceability | ISO 14971:2019 cl. 3.18, 4.2, 4.4, 4.5, 5.5, 6 |
| Supply Continuity axis (Kraljic supply-risk) | CSQP Handbook, Kraljic portfolio model (Ch. 2) |
| Supplier Maturity / 100-pt scorecard drivers | CSQP Handbook, Fig. 3.4; Gordon, Ch. 1–3 |
| Risk-based audit cadence & finding classes (Critical/Major/Minor) | CSQP Handbook, Ch. 6 (Table 6.1) |
| Porcine agent list, herd/source factors, inspection limits, transmission routes | Diseases of Swine, 11th ed. (Ch. 1, 5, 9, 12 + domain knowledge) |

*Note:* the AIAG-VDA full AP table, the CSQP PPAP/control-plan chapters (Part III), and Gordon's scorecard case study (Ch. 6–9) were beyond the extracted text and should be consulted directly when finalizing.

---

## 10. How to use the template
See `Risk_Scoring_Template.csv` — one row per part. Fill segment, the Layer A scores, procurement axes, and (for tissue) the Layer B columns + pathogen gates. The Final Risk Class and actions follow §6.

---

*v0.1 — generated as a first draft for review. Open items: (1) confirm tissue end-use grade; (2) management to ratify acceptability thresholds (§6.1); (3) acquire gap standards (§8).*
