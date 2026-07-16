# Belly-Fat PVA Cryogel — Formulation & Freeze–Thaw Study

**Scope:** the science behind the fixed [standard mix](00_standard_mix.md), and how to tune it —
**mainly via freeze–thaw parameters** — to hit human abdominal-fat mechanics for **injection and
surgical-training phantoms**, where mechanical/tactile realism is the priority.

**Ground rule:** the standard mix (composition, ~10.6 % super-hydrolyzed high-MW PVA, NaCl, Proxel BD20,
Proline pigments, 90–95 °C cook) is **held fixed**. Everything below tunes the **downstream
freeze–thaw step**, which is what actually forms the gel.

> **Evidence base.** Findings are drawn from a multi-source, adversarially fact-checked research pass
> (27 sources → 122 extracted claims → 25 verified by 3-vote adversarial checking, 22 confirmed).
> Each claim below is tagged **[Verified]**, **[Context]** (reported but not independently confirmed),
> or **[Uncertain]**. Full citations in [§12](#12-references). Caveats in [§13](#13-caveats--open-questions).

---

## 1. TL;DR — what to do

1. **Your resin class is right.** Freeze–thaw cryogels *require* fully-/super-hydrolyzed (98–99 %+),
   high-MW PVA. Partially hydrolyzed grades won't gel at ~10 %. **[Verified]**
2. **The gel is made by the freeze–thaw, not the cook.** The 90–95 °C step just dissolves the PVA;
   crystallites + phase-separated domains form during freezing/thawing. **[Verified]**
3. **You are almost certainly too stiff for fat.** At ~10 % PVA, **2–5 freeze–thaw cycles → ~65–180 kPa**,
   but abdominal fat is **~1–25 kPa**. To move toward fat, use **the fewest cycles that still gives a
   handleable gel (start at 1–2)** and a **slow, controlled thaw**. **[Verified modulus band; Context on fat target]**
4. **Biggest single lever = going from 1 → 2 cycles** (largest step-change is after cycle 2). Treat
   cycle count as a coarse knob and **thaw rate** as the fine knob. **[Verified]**
5. **Your 0.8 % NaCl is helping** — it softens the gel (disrupts the H-bonds that seed crystallites) and
   depresses the freezing point. Keep it; just know it's a mechanical variable, not only a "salt." **[Context]**
6. **Pin two numbers before optimizing:** (a) the real target modulus for *your* anatomy/procedure, and
   (b) your current product's modulus at its current cycle count. Then close the gap with cycles + thaw rate.

---

## 2. How the standard mix becomes a gel (the physics)

The cook (90–95 °C, 30–45 min) only produces a **PVA solution**. Gelation happens later, during
**freeze–thaw physical crosslinking (cryogelation)**:

- **Freeze-concentration.** As water freezes into ice crystals, the remaining PVA is squeezed into
  shrinking unfrozen channels — locally concentrating the polymer far above the bulk 10.6 %. **[Verified]**
- **Crystallite junctions.** In those concentrated regions, PVA chains hydrogen-bond and pack into
  **nanoscale crystallites (~3 nm, spaced ~19 nm** by small-angle neutron scattering) that act as
  physical, thermoreversible crosslinks. **[Verified]**
- **Phase separation is a second, independent mechanism.** Modern work shows crystallites are **not** the
  whole story: freezing also drives **liquid–liquid (spinodal) phase separation** into PVA-rich and
  PVA-poor domains, and those PVA-rich domains stiffen the gel **on their own** — especially after the
  3rd cycle. At matched crystallinity, freeze–thawed gels are significantly stiffer than merely aged
  gels. **[Verified]**
- **Result:** a tough, elastic, macroporous, water-swollen network held together by crystallites +
  phase-separated domains — no chemical crosslinker, no toxic residue. That's why PVA cryogel suits a
  **reusable** injection/training phantom.

**Design consequence:** because the junctions are physical (crystallites), **how you freeze and thaw
directly sets the mechanics.** More/colder/longer freezing and more cycles → more crystallites →
stiffer. Fewer cycles and gentle thaw → softer.

## 3. Why super-hydrolyzed, high-MW PVA (and where S-1551F-D fits)

The crystallite mechanism needs lots of **hydroxyl groups that can pack tightly**, so hydrolysis and
MW are decisive:

| Lever | Effect on cryogel | Evidence |
|---|---|---|
| **Degree of hydrolysis** | Must be **fully/super-hydrolyzed (98–99 %+)**. Residual acetate groups (in 87–89 % "partially hydrolyzed" grades) block crystallization — those grades **stay liquid** at ~10 % and only gel above ~12 wt%. | **[Verified]** — PMC11597501; Takamura; US-phantom study (≥98 % works, 80/88 % fails) |
| **Molecular weight** | Needs **Mw above ~61,000 g/mol**; at the threshold gels disintegrate on handling, while **high-MW (e.g. Mw ~195,000, "PVA 56-98") gives the best durability**. Determined at ~10 % PVA / 6 cycles — exactly your regime. | **[Verified]** — PMC11597501 |

**Your resin.** S-1551F-D is a solid grade that dissolves at ~90 °C and runs at ~10.6 % — behavior
consistent with a **super-hydrolyzed, high-MW** PVA, which is the correct class. On identity, be precise:

- Your procurement docs call it **"Selvol S-1551F-D or equivalent"** (see `../PVA second supplier initiative/`).
- **But "1551" is not a published Selvol standard grade** — Sekisui's public line uses 3-digit numbers
  (103, 107, 125, 165, 203/S, 205/S, 325, 350, 523, 540…) and an **"S" *suffix*** (e.g. 205**S**) for
  fine-particle versions, not an "S-…" prefix. So S-1551F-D is best treated as a **supplier/OEM code**,
  not decodable from the public brochure. **[Verified that 1551 isn't in the standard line]**
- **Closest published analog: Selvol 165 / 165SF** (99.3+ %, 62–72 cP, DP 1600–2200, Mw ~146k–186k) —
  see [`01_pva_grade_reference.md`](01_pva_grade_reference.md). Also Kuraray **Poval 56-98** and
  **Elvanol 71-30**.
- **Action:** get the **S-1551F-D TDS/CoA** (hydrolysis %, MW/DP, 4 % viscosity) into `brochures/` to
  confirm. This is open question #1.

## 4. The tuning levers you actually have

Three levers control cryogel stiffness. Two are usable **without touching the standard mix**:

| Lever | Direction | Magnitude | Usable at fixed mix? |
|---|---|---|---|
| **Number of freeze–thaw cycles** | ↑ cycles → ↑ stiffness (monotonic, diminishing returns; **biggest jump after cycle 2**; plateau ~3–5) | 10 % PVA: ~65→180 kPa across 2→5 cycles | ✅ **Primary knob** |
| **Thaw rate** | slower thaw → generally more/【larger crystallites → firmer; fast thaw → softer/more porous | Under-quantified but real "third knob" | ✅ **Fine knob** |
| **PVA concentration** | ↑ conc → ↑ stiffness (10→15→20 % gave **+69 %/+137 %** tangent modulus) | Large/coarse | ⛔ Fixed at 10.6 % (coarse reserve only) |

- **Cycle count is coarse and powerful.** The **single largest step-change is after the 2nd cycle**
  (pore size up 2–3×, porosity up 1.5–2×, net strengthening); G′ then plateaus around 3–5 cycles. So
  **1 → 2 cycles is a big move; 4 → 5 barely matters.** **[Verified]**
- **Note:** the old rule that properties "max out at ~6 cycles" was **refuted** in this pass (0–3 vote).
  Don't design around a 6-cycle plateau; design around the **2nd-cycle step + a soft 3–5 plateau**. **[Verified refutation]**
- **Freeze parameters that bracket your case (usable starting point):** solutions of ~8–12 wt%
  (brackets 10.6 %), **1–5 cycles, freeze at −20 °C for ~19 h, thaw at a controlled ~0.3 °C/min.** **[Verified]**

## 5. Target: how soft should belly fat be?

Human abdominal **subcutaneous/visceral adipose tissue is very soft** — reported elastic moduli cluster
in the **low kPa range (roughly ~1–25 kPa** depending on method, strain, and subcutaneous vs visceral),
with several sources in the single-digit kPa band. It is also strongly **viscoelastic** (stress-relaxing,
rate-dependent). **[Context — see caveat]**

**The key implication:** at 10 % PVA, **even 2 cycles (~65 kPa) already overshoots fat.** To land in the
soft-fat window you must push toward the **bottom of the cycle range (1–2, possibly a single cycle)**,
lean on **slow thaw**, and let the **NaCl softening** help. There is a real floor — a gel too soft to
handle won't survive repeated needle passes — so the goal is *the softest cycle count that still gives a
reusable, self-supporting block*.

> **Two numbers to measure first** (don't optimize blind):
> 1. **Target:** the modulus of the actual tissue you're mimicking, for your procedure. Pin it from the
>    adipose-mechanics literature (§12) or, better, measure explanted/analog tissue on your own rig.
> 2. **Baseline:** your *current* product's modulus at its *current* cycle count. The gap between these
>    two, in cycles, is your optimization target.

## 6. Recommended freeze–thaw protocol (starting point)

A concrete, literature-anchored starting protocol to bracket belly-fat feel while keeping the mix fixed.
**Treat these as starting set-points to calibrate on your equipment, not final values.**

| Step | Setting | Rationale |
|---|---|---|
| **Cast** | Pour degassed solution into the mould; **de-bubble** (vacuum or rest warm) | Trapped air = acoustic/needle artefacts |
| **Freeze** | **−20 °C**, hold **~12–19 h** (ensure full core freeze) | Standard cryogel freeze; long enough for crystallite nucleation |
| **Thaw** | **Slow, controlled ~0.3 °C/min** to room temp (or overnight in a programmable chamber / insulated ramp) | Thaw rate is your fine stiffness knob; controlled thaw also improves batch reproducibility |
| **Cycles** | **Start at 1; make a 2-cycle and 3-cycle set in parallel** | The 1↔2↔3 range spans soft→firm; the answer for fat is almost certainly here |
| **Anneal/rest** | Let gels **equilibrate ≥24 h** before testing | Properties keep evolving right after thaw |
| **Store** | Sealed, in the gel's own fluid or a humidity-controlled bag; keep **biocided** | Prevent dehydration/syneresis; Proxel BD20 already in mix |

**Do not** freeze the packaged *solution* accidentally — an unintended freeze starts cryogelation in the
drum (this is why the standard mix ships "protect from freezing").

## 7. Key numeric parameters (reference table)

| Parameter | Value / range | Notes | Source |
|---|---|---|---|
| PVA class for cryogel | Fully/super-hydrolyzed **98–99 %+**; **Mw > 61,000** | Below this: no stable gel at 10 % | PMC11597501 |
| Standard-mix PVA loading | **~10.6 wt%** (11.58 % TS) | Fixed | Standard mix |
| Crystallite size / spacing | **~3 nm / ~19 nm** | SANS | Wan review |
| E (Young's), 10 % PVA, 2–5 cycles | **~65–180 kPa** | Unconfined compression | Duboeuf 2009; Wan/Millon |
| E, 10 % PVA, 6 cycles, 45 % strain | up to **~1.18 MPa** | Large-strain, high-rate | Millon |
| Stiff load-bearing series (upper bound) | 1–18 MPa comp / 0.1–0.4 MPa shear | Patent; **irrelevant to fat**, upper bound only | US7776352 |
| Concentration effect | 10→15→20 % = **+69 %/+137 %** tangent E | Coarse lever (mix fixed) | Wong 2012 (via Wan) |
| Biggest cycle step-change | **after 2nd cycle**; plateau ~3–5 | Pore size ↑2–3×, porosity ↑1.5–2× | Lozinsky 2008 |
| Freeze set-point | **−20 °C, ~19 h** | Bracketing protocol | Lozinsky 2008 |
| Thaw rate | **~0.3 °C/min** controlled | Fine knob | Lozinsky 2008 |
| **Adipose target (to confirm)** | **~1–25 kPa** (low kPa, viscoelastic) | Context, not independently verified | Alkhouli 2013; §12 |
| Aging/reproducibility | Modulus stable over time with controlled technique; batch reproducibility ~4–8 % | Achievable | Duboeuf 2009 |

## 8. Additive effects (what the non-PVA ingredients do to the gel)

| Ingredient (in fixed mix) | Effect on cryogel | Confidence |
|---|---|---|
| **NaCl 0.8 wt%** | **Softens** — dissolved salt disrupts inter-/intra-chain H-bonds needed for crystallites → lower crystallinity → weaker/softer gel; also **depresses freezing point** (slows/alters ice formation). Baseline 0.137 M is ~2× the tested 0.0625 M range but same direction; still well below the salting-out regime. | **[Context]** (2–1) |
| **Proxel BD20 (BIT biocide)** | Preservation for a wet, reusable phantom (needed if solution held > 24 h). **Effect on freeze–thaw crystallization/mechanics not measured** in any verified source. | **[Uncertain]** |
| **Petal Pink / Taupe Proline pigments** | Cosmetic realism. **Effect on cryogelation not measured**; particulates *could* nucleate ice/scatter ultrasound, but unquantified. | **[Uncertain]** |

**Optional levers if you ever move beyond the fixed mix** (flagged, not recommended yet):
- **Glycerol / cryoprotectant** — softens (plasticizes) and can improve tactile feel + freeze uniformity;
  glycerol also tunes speed-of-sound toward tissue. Changes the mix → out of current scope. **[Context]**
- **Cellulose / graphite / glass-bead scatterers** — only if you need **ultrasound** echogenicity; not
  needed for pure mechanical/needle training. **[Context]**

## 9. Pitfalls & durability

- **Syneresis / dehydration.** Cryogels slowly expel water and can stiffen/shrink at the surface if
  stored dry. Keep sealed and humid; store in fluid. **[Context]**
- **Aging / creep.** Properties keep evolving after thaw; **equilibrate ≥24 h before QC**, and with a
  controlled freeze/thaw technique modulus is reported **stable over time** (reproducibility ~4–8 %). **[Verified]**
- **Batch reproducibility.** Control the three levers tightly (cycle count, freeze profile, **thaw rate**);
  uncontrolled thaw is the usual reproducibility killer. **[Verified]**
- **Full-formulation unknowns.** The *combined* effect of NaCl + biocide + pigments on freeze–thaw kinetics
  and long-term mechanics was **not directly measured** in the literature — validate empirically on your
  own product. **[Caveat]**
- **Sterility/shelf life.** Solution shelf life is short (18 days, protect from freezing); the *gelled*
  phantom's usable life depends on hydration + biocide. **[from initiative docs]**

## 10. Why PVA cryogel vs the alternatives (brief)

| Material | Reusable? | Needle/tactile feel | Notes |
|---|---|---|---|
| **PVA cryogel (yours)** | ✅ durable, no refrigeration | Excellent, self-healing-ish around needle tracks | Tunable by freeze–thaw; non-toxic; the right base for a reusable trainer |
| Gelatin | ❌ perishable, melts | Good but fragile | Cheap single-use imaging phantom |
| Agar/agarose | ❌ brittle, perishable | Poor for needles | Imaging, not training |
| Ballistic gel | ⚠ | OK | Melts, remelts; forensic use |
| Silicone (platinum-cure) | ✅ very durable | Different feel; sutures well | Great outer skin; poor ultrasound; not water-swollen |
| **Chemically crosslinked PVA** | ✅ | Firmer | Uses crosslinkers (glyoxal/glutaraldehyde/borate) → toxicity/handling; freeze–thaw avoids this |

The takeaway from the needle-phantom review literature: **PVA cryogel is the standard reusable choice**
precisely because it's tunable, tissue-like, and crosslinker-free. **[Verified from UMB review]**

## 11. Prioritized experimental plan

A tight DOE to dial in belly-fat feel **without changing the standard mix**. Run in order.

**P0 — Establish ground truth (before any optimization)**
1. Get the **S-1551F-D TDS/CoA** → confirm hydrolysis %, MW/DP, viscosity (open Q#1).
2. **Measure your current product's modulus** at its current cycle count on a defined rig
   (unconfined compression, fixed strain/rate; also do a needle-insertion-force capture).
3. **Fix a target**: pull an adipose modulus/viscoelastic target for your specific anatomy/procedure
   (§12), or measure a reference tissue on the same rig. *Deliverable: target kPa + tolerance.*

**P1 — Cycle-count sweep (the coarse knob)**
4. Cast identical moulds; make **1, 2, 3 (and 4) cycle** sets, all with the **same controlled −20 °C /
   ~0.3 °C/min** profile. Equilibrate 24 h. Measure E, stress-relaxation, needle force.
   *Expect the 1→2 jump to dominate; pick the cycle count that brackets your target.*

**P2 — Thaw-rate fine-tune (the fine knob)**
5. At the chosen cycle count, vary **thaw rate** (e.g. ~0.1, 0.3, 1 °C/min, plus a "dump to room temp"
   control). Re-measure. *Use thaw rate to fine-trim modulus and surface feel.*

**P3 — Realism & durability**
6. **Needle realism**: puncture-force curve + subjective feel vs target tissue; check track closure /
   reusability over N passes.
7. **Aging/reproducibility**: re-test at 1, 7, 30 days; run 3 independent batches → quantify %CV.
   Confirm syneresis is controlled by your storage method.

**P4 — Only if P1–P3 can't reach soft-fat feel while staying handleable** (would change the fixed mix — decision gate)
8. Evaluate **glycerol (plasticizer/cryoprotectant)** at low % to soften without losing integrity, and/or
   a small **concentration** reduction. Treat as a formal change-control to the standard mix, not a default.

---

## 12. References

**PVA cryogel physics & tuning**
- Wan et al., *Poly(Vinyl Alcohol) Cryogels for Biomedical Applications* (review). https://www.eng.uwo.ca/chemical/faculty/wan_w/pdf/publications/Ref_25.pdf
- Holloway, Lowman, Palmese, *The role of crystallization and phase separation in the formation of physically cross-linked PVA hydrogels*, RSC **Soft Matter** (2013). https://pubs.rsc.org/en/content/articlelanding/2013/sm/c2sm26763b
- *Freeze–thaw PVA cryogel — hydrolysis/MW threshold study* (2024), PMC11597501. https://pmc.ncbi.nlm.nih.gov/articles/PMC11597501/
- Lozinsky et al., *Cryostructuring of polymer systems*, **Colloid Journal** (2008) — 2nd-cycle step-change; −20 °C/19 h, 0.3 °C/min thaw. https://link.springer.com/article/10.1134/S1061933X08020117
- *PVA cryogels: effect size of concentration, number of cycles and thawing rate* (2025), **Eur. J. Pharm. Biopharm.** https://www.sciencedirect.com/science/article/pii/S093964112500253X
- Duboeuf et al., *PVA cryogel Young's modulus stability with time* (2009), **Medical Physics** — 70–180 kPa / 2–5 cycles. https://aapm.onlinelibrary.wiley.com/doi/10.1118/1.3065031
- *Crystallinity vs concentration/cycles* (2012), **Biomedical Materials**, PMID 22287550. https://pubmed.ncbi.nlm.nih.gov/22287550/
- Mechanism preprint (UCST microphase-then-crystallization), arXiv 2510.06720 *(non-peer-reviewed; corroborated by RSC above)*. https://arxiv.org/pdf/2510.06720
- PVA-hydrogel patent (upper-bound stiff series), US 7,776,352. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7776352

**Adipose-tissue mechanics (target values — to pin down)**
- Alkhouli et al., *Mechanical properties of human adipose tissue…*, **Am J Physiol Endocrinol Metab** (2013). https://journals.physiology.org/doi/full/10.1152/ajpendo.00111.2013
- *Adipose mechanical characterization*, **Processes** 10(9):1798 (MDPI). https://www.mdpi.com/2227-9717/10/9/1798
- *Subcutaneous adipose tissue mechanics*, **J Mech Behav Biomed Mater** (2023). https://www.sciencedirect.com/science/article/pii/S1751616123002771
- *Linear viscoelastic behavior of subcutaneous adipose tissue*. https://www.researchgate.net/publication/23640394_Linear_viscoelastic_behavior_of_subcutaneous_adipose_tissue
- *Adipose indentation/viscoelasticity*. https://www.sciencedirect.com/science/article/abs/pii/S1350453312000938

**Phantom materials, additives & protocols**
- *Tissue-Mimicking Materials for Ultrasound-Guided Needle Intervention Phantoms: A Comprehensive Review*, **Ultrasound Med Biol** (2022). https://www.umbjournal.org/article/S0301-5629(22)00509-9/abstract
- Formulation/additive & durability sources: PMC7684317 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7684317/), PMC10882697 (https://pmc.ncbi.nlm.nih.gov/articles/PMC10882697/), S0301562922005798 (https://www.sciencedirect.com/science/article/abs/pii/S0301562922005798), PMID 34799525 (https://pubmed.ncbi.nlm.nih.gov/34799525/), PMC11851462 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11851462/).

**Supplier grade data**
- Sekisui Selvol PVOH — product line & Selvol 125 spec: https://www.sekisui-sc.com/products/polyvinyl-alcohol/ ; and `brochures/Sekisui_Selvol_PVOH_Brochure_EN.pdf`
- Kuraray Poval TDS: https://q-mexibras.com.mx/wp-content/uploads/2021/03/TDS_Poval_en_20.pdf ; and `brochures/Kuraray_Poval_Exceval_Elvanol_TDS_America_EN.pdf`

## 13. Caveats & open questions

**Caveats**
- Numeric tuning figures (65–180 kPa band; 69 %/137 % concentration effect; 0.3 °C/min) are
  **protocol-specific** to particular freeze temps, dwell times, thaw rates, and grades — treat as
  representative datasets, **calibrate on your own equipment**.
- **Adipose target moduli (~1–25 kPa) are contextual**, not independently verified numbers — pin them
  before finalizing tolerances.
- The **combined effect of the full baseline** (NaCl **+** biocide **+** pigments) on freeze–thaw kinetics
  and long-term mechanics was **not directly measured** anywhere — validate empirically.
- The "properties plateau at ~6 cycles" rule was **refuted**; use the **2nd-cycle step + 3–5 plateau** model.
- **S-1551F-D identity/specs remain unconfirmed** (not a public Selvol standard number).

**Open questions (drive the experiment plan)**
1. Exact identity & spec of **S-1551F-D** (hydrolysis %, MW/DP, 4 % viscosity; which supplier line).
2. Source-anchored **belly-fat targets** (Young's & shear modulus, stress-relaxation constants, needle
   insertion/puncture forces) for your specific anatomy/procedure.
3. At fixed 10.6 % PVA, **how few cycles + what thaw rate** land in the sub-25 kPa soft-fat regime **while
   staying handleable/reusable** — and whether a single-cycle gel can be made durable enough.
4. How **NaCl + Proxel BD20 + Proline pigments** jointly affect crystallization kinetics, final modulus,
   syneresis/creep, and batch reproducibility — and whether **glycerol/DMSO** meaningfully soften/improve
   feel without hurting sterility/shelf life.
