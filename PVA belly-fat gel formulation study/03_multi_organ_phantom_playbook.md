# Multi-Organ Phantom Playbook — Extending the PVA Cryogel Base Beyond Belly Fat

**Goal:** replicate organs *other than* adipose (lung, liver, kidney, muscle, vessel, brain, etc.) for
**surgical and injection training**, reusing the lab's existing **~10 % super-hydrolyzed high-MW PVA
cryogel** as the shared base "block," plus complementary materials where PVA isn't the right tool.

> **Evidence base & honesty note.** The PVA-centric core below is from a second adversarially
> fact-checked research pass (26 sources → 121 claims → 22 verified). Claims are tagged **[Verified]**,
> **[Context]** (reported, not independently confirmed), or **[Engineering]** (sound domain guidance /
> our synthesis, *not* verified in this research pass — validate before relying on it). The research pass
> **could not verify** several things you asked about — most non-PVA recipes, and quantitative targets
> for bone/cartilage/tendon/nerve/skin/brain-mechanics — so those are given as **[Engineering]** and
> flagged in [§10](#10-what-is-not-yet-verified). Full citations in [§11](#11-references).

---

## 1. The big idea: one base, many organs

The single most useful verified result: **a ~10 wt% PVA-in-water cryogel is a proven multi-organ base,
and freeze–thaw (FT) cycle count is the primary stiffness dial.** The *same* PVA-C base has been used in
peer-reviewed work to build **brain, blood vessel, atherosclerotic artery, breast, prostate, liver,
thyroid, and lung** phantoms — you differentiate organs mainly by **(a) FT cycle count** and **(b) a
small set of functional additives.** **[Verified]**

So you do **not** need a new chemistry per organ. You already run the base. To make another organ you
turn three dials:

1. **FT cycle count** → sets **stiffness** (coarse). ~20 kPa at 1 cycle → ~600 kPa at 10 cycles in the
   gold-standard tensile study; ~11→82 kPa (1→10 cycles) in another 10 % study; **plateau ~5–7 cycles.** **[Verified]**
2. **Glycerol** → **softens** the gel (lowers Young's modulus) **and raises speed of sound** toward
   tissue — a two-for-one lever for soft, acoustically-correct organs. **[Verified]**
3. **Scatterers / attenuators** (only if imaging matters) → set ultrasound echogenicity and attenuation.**[Verified]**

**Reality check (ties back to the belly-fat study):** even the softest PVA-C (~11–20 kPa at 1 cycle) is
**still too stiff for the very softest tissues** (fat, brain, liver *in vivo* ~1–16 kPa). For those you
need **low cycle count + glycerol** (and, for fat, the NaCl softening you already use). **[Verified]**

## 2. The reference competitor: IMRA Surgical (Australia)

The company you're thinking of is **IMRA Surgical**, an Australian maker whose **Pindari** line is
**hydrogel-based synthetic organ models** for surgical training — built to "simulate real tissue feel and
surgical response" to **suturing, electro-cautery, and stapling**, with **no cadavers, no animal tissue,
no refrigeration** (the exact PVA-cryogel value proposition). They've also partnered with **Telix
Pharmaceuticals** on radio-guided-surgery training. **[Verified via direct source review]**

Their published catalog is a soft-tissue surgical library you can benchmark against:

| Anatomy | Model / procedure |
|---|---|
| Torso / abdomen | Female ("Hydra") & male ("DadBod") torso trainers; abdominal dome |
| Uterus | Hysterectomy, myomectomy |
| Kidney | Partial nephrectomy |
| Colon | Right hemicolectomy |
| Stomach | Gastric model, staple pads |
| Abdominal wall / groin | Ventral & inguinal hernia |
| Urinary | Urethrovesical anastomosis |
| Skin | "Roboset HydroSkin" |

They don't publish their exact chemistry, but "hydrogel + reusable + tissue feel + no refrigeration"
maps directly onto PVA-C — meaning your existing base is a credible foundation for a comparable library.
Other global makers to benchmark (materials in parentheses): **SynDaver** (proprietary hydrogel/salt-water
"SynTissue"), **Lazarus3D** (3D-printed soft silicone/hydrogel), **True Phantom Solutions**, **Simulab**,
**CIRS/Sun Nuclear** (imaging phantoms), **Kyoto Kagaku**, **Limbs & Things**. **[Engineering — vendor landscape, not verified in this pass]**

## 3. The additive toolkit (verified roles)

These are the levers that turn the base into specific organs. Roles below are **[Verified]** from the
prostate multi-tissue study (Butcher 2024) and the acoustic-ranking study (Chen 2022) unless noted.

| Additive | What it does | Use it for |
|---|---|---|
| **Glycerol** (5–12 %) | **Plasticizer: lowers Young's modulus** (softer) **and raises speed of sound** (glycerol SoS ~1964 m/s vs water ~1497). Also a cryoprotectant. | Softening stiff-by-default PVA toward fat/brain/liver feel; nudging SoS up to hit tissue targets |
| **Silicon carbide (SiC)** ~1 % | **Echogenic B-mode scatterer** (makes tissue "bright" on ultrasound) | Any organ that must image realistically on US |
| **Alumina (Al₂O₃)** ~0.5 % | **Raises acoustic attenuation** to tissue levels | Tuning attenuation to per-organ targets |
| **Microcrystalline cellulose** (~20 µm, 1 %) | Acoustic scatterer used in the validated **lung** phantom | Lung parenchyma; general speckle |
| **Ethylene glycol** (cryoprotectant) | Enables a **single 24-h FT cycle** to make a stable phantom (vs many cycles) | Faster processing; softer gels |
| **Biocide** — benzalkonium chloride 0.5 % *(their study)* / **your Proxel BD20 (BIT)** | Antimicrobial for a wet, **reusable** phantom | Every reusable model |
| **NaCl** (you already use 0.8 %) | Softens (disrupts crystallite H-bonds); depresses freezing point | Fat and other soft tissues |

**Concrete verified multi-tissue recipes from one 12 % PVA base** (Butcher et al. 2024, prostate model) —
a template for "same base, different organ":

- **Prostate:** 12 % PVA (Mw 89–98k) + **10 % glycerol + 1 % SiC + 0.5 % Al₂O₃**, **5 FT cycles**
- **Hypoechoic tumor inclusion:** 12 % PVA (Mw 130k) + **12 % glycerol + 0.5 % Al₂O₃** (no SiC), **10 FT cycles**
- **Blood vessel:** 12 % PVA + **1 % SiC** (no glycerol), **10 FT cycles** **[Verified]**

## 4. Per-organ playbook

**How to read this:** *Acoustic* targets (speed of sound, attenuation) are **[Verified]** from Chen 2022
(Table 1, after Mast 2000 / ICRU / Gong). *Mechanical* targets are mixed — some **[Verified]**, many
**[Engineering]** (typical literature ranges to confirm on your own rig). The **PVA-C approach** column is
your starting point from the base.

| Organ | Speed of sound (m/s) | Attenuation (dB/cm/MHz) | Young's modulus target | PVA-C approach (from your base) | Conf. |
|---|---|---|---|---|---|
| **Fat / adipose** (current) | **1478** | **0.48** | ~1–25 kPa (soft) | 1–2 FT cycles; NaCl softening (your mix) | Acoustic ✅ / mech Context |
| **Breast** | **1510** | **0.75** | glandular ~a few–20 kPa | low–moderate FT + fat regions; SiC for echo | Acoustic ✅ / mech Eng |
| **Liver** | **1595** | **0.5** | **human in-vivo ~2–16 kPa**; bovine ex-vivo ~0.6–0.9 kPa ✅ | low–moderate FT + 1 % cellulose; **glycerol to soften to human values** | Acoustic ✅ / mech ✅ |
| **Kidney** | **1560** | **1.0** | ~5–40 kPa (cortex/medulla differ) | moderate FT; cast **layered** cortex/medulla + hollow calyx; Al₂O₃ up (atten high) | Acoustic ✅ / mech Eng |
| **Cardiac muscle** | **1576** | **0.52** | myocardium ~10–40 kPa | moderate–high FT; anisotropy via fibers | Acoustic ✅ / mech Eng |
| **Skeletal muscle** | ~1547–1580 | ~0.5–1.0 | bovine ex-vivo ~1.5–2.1 kPa ✅ (functionally firmer, anisotropic) | higher FT + embedded fibers for grain | Acoustic Eng / mech ✅ |
| **Blood vessel / artery** | ~1540–1600 | — | wall stiff (hundreds kPa→MPa); tune healthy→atherosclerotic | **12 % PVA + 1 % SiC, high FT (up to 10)**; mandrel-cast tube; more cycles = more diseased | ✅ (recipe + trend) |
| **Prostate** | ~1540–1560 | ~0.8–1.0 | ~15–40 kPa | **12 % PVA + 10 % glycerol + 1 % SiC + 0.5 % Al₂O₃, 5 FT** (verified recipe) | ✅ (recipe) |
| **Brain** | ~1540–1560 | ~0.6 | very soft ~0.5–3 kPa | **1 FT cycle + glycerol** (PVA-C brain phantom demonstrated) | Use ✅ / mech Eng |
| **Thyroid** | ~1540 | ~0.8 | ~9–36 kPa (elastography) | multi-cycle PVA-C (demonstrated) | Use ✅ / mech Eng |
| **Lung** (see §5) | ~650 (aerated!) or soft-tissue if de-aerated | high/variable | **1.4–6.1 kPa** ✅ | **10 % PVA-C + 1 % 20 µm cellulose, ~1 FT** + aeration strategy | ✅ target/recipe |
| **Skin / subcutaneous** | ~1540–1600 | ~0.5–1.0 | epidermis/dermis firm (100s kPa–MPa) | high-FT PVA or **silicone** top layer over fat | Eng |
| **Cartilage / tendon** | ~1600–1700 | — | firm (~1–100 MPa) | high-FT + fibers, or non-PVA | Eng |
| **Nerve** | ~1540 | — | ~few–tens kPa, tubular | fine PVA-C tubes | Eng |
| **Bone** | ~2800–4000 | very high | rigid (GPa) | **not PVA** — plaster/epoxy/3D-printed rigid core | Eng |

**Acoustic reference targets (verified, Chen 2022):** Fat 1478 m/s · 950 kg/m³ · 0.48 dB/cm/MHz; Breast
1510 · 1020 · 0.75; Kidney 1560 · 1051 · 1.0; Cardiac 1576 · 1060 · 0.52; Liver 1595 · 1060 · 0.5. **AIUM
general design goal: SoS 1540 m/s, attenuation 0.3–0.7 dB/cm/MHz.** PVA-C's own SoS is 1520–1616 m/s
(highest of common hydrogels, closest to liver) and its intrinsic attenuation ~0.34–0.58 dB/cm/MHz —
**well-suited to stiffer/higher-SoS organs (liver, kidney, muscle)**, with attenuation manageable via
density/additives. **[Verified]**

> ⚠️ **Animal-vs-human trap.** Several published PVA-C organ phantoms target **animal ex-vivo** tissue —
> e.g. a PVA-C liver phantom at **129 kPa Young's / 43 kPa shear targets *rabbit* liver**, which is
> **~8–60× stiffer than human liver in vivo (~2–16 kPa)**. For a **human** injection/surgical trainer,
> anchor to **human in-vivo** values and use **fewer cycles + glycerol** to get there. **[Verified caveat]**

## 5. Lung — the hard case

Lung is the genuinely difficult organ because real parenchyma is **aerated, spongy, and very low density**.
Two things are firmly established; the aeration method is not.

**What's verified:**
- **Stiffness target: ~1.4–6.1 kPa** (measurement-method dependent: micro-indentation 1.4 kPa → cavitation
  rheology 6.1 kPa; consistent with human lung ~1–5 kPa). **[Verified — Polio 2018]**
- **Base recipe (solid parenchyma):** **10 % w/w PVA-C (99 % hydrolyzed, Mw 89–98k) + 1 % microcrystalline
  cellulose (20 µm)** as the acoustic scatterer, single FT cycle. **[Verified — PMC9957311]**

**What's *not* yet verified (treat as [Engineering] — validate):** the actual **aeration / low-density**
strategies. Candidate approaches to introduce the sponge-like air structure:
- **Porogen / salt / sugar leaching** — mix in a soluble particulate, then dissolve it out to leave pores.
- **Gas-filled inclusions / microbubbles** — entrain controlled gas for aerated acoustics.
- **Freeze-dried PVA sponges / syntactic foams** — hollow microspheres in the matrix.
- **Foaming agents** during solution prep.

> The research pass **could not verify a specific aerated-lung recipe or achieved density** — the confirmed
> evidence gives you a stiffness target and a solid-parenchyma base, not the aeration cookbook. If lung is
> a priority, this is the #1 candidate for a dedicated deep-dive (see [§10](#10-what-is-not-yet-verified)).

## 6. When PVA isn't the right block (complementary materials)

PVA-C is your workhorse for **soft, water-swollen, reusable, needle-friendly, ultrasound-compatible**
tissue. It is **not** ideal everywhere. The following is **[Engineering]** guidance (the research pass did
not verify non-PVA recipes; the UMB needle-phantom review is the anchor reference):

| Block | Best for | Trade-offs |
|---|---|---|
| **Gelatin** | Cheap single-use imaging phantoms; soft feel | Perishable, melts near body temp, not reusable |
| **Agar / agarose** | Imaging speckle, thermal stability | Brittle, poor needle feel, perishable |
| **Ballistic gelatin** | Wound/ballistics; moderate feel | Melts/remelts; not durable |
| **Silicone (platinum-cure, Ecoflex/Dragon Skin)** | Durable **skin**, outer layers, suturable surfaces | Different feel; **poor ultrasound** (low SoS ~1080 m/s); not water-swollen |
| **Polyacrylamide** | Firm, transparent optical/US phantoms | Monomer toxicity in prep |
| **Carrageenan / konjac** | Softer hydrogel feel, some thermal robustness | Niche; less characterized |
| **Rigid (plaster / epoxy / 3D-printed)** | **Bone**, rigid scaffolds | Not tissue-like otherwise |

**Rule of thumb:** water-swollen soft organ that needs needles + ultrasound → **PVA-C**. Durable skin or a
suturable outer surface → **silicone**. Rigid structure → **printed/cast rigid**. Cheap disposable imaging
target → **gelatin/agar**.

## 7. Building layered, composite models (fat over muscle over organ)

Real training targets are layered. **[Engineering]** guidance:
- **Co-processing:** cast tissues in sequence and let them **share freeze–thaw cycles** so PVA-C layers
  **fuse at the interface** (PVA-C bonds well to itself). Cast the deep organ first, partially cycle, then
  overpour muscle, then fat, so outer layers see fewer cycles (softer) than deeper ones.
- **Cycle budgeting:** a layer's final stiffness = (its formulation) × (total cycles it experiences).
  Plan the pour order so each layer lands at its target cycle count.
- **Dissimilar materials** (silicone skin over PVA-C fat): bond mechanically (mesh/undercuts) or with a
  compatible adhesive; silicone won't fuse to hydrogel.
- **Reusability:** keep everything **biocided** (your Proxel BD20) and **hydrated/sealed**; PVA-C needle
  tracks largely self-close, which is why it suits repeated injection practice.
- **Sterility/shelf life:** the gelled phantom's life depends on hydration + biocide, not the solution's
  18-day limit.

## 8. Materials-vs-organ matrix (quick reference)

**[Engineering]** synthesis (PVA rows anchored by verified data; non-PVA rows are guidance):

| | Fat | Breast | Liver | Kidney | Muscle | Vessel | Brain | Lung | Skin | Bone |
|---|---|---|---|---|---|---|---|---|---|---|
| **PVA-C (yours)** | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★ (+cellulose/aeration) | ★★ | ✗ |
| Silicone | ★★ | ★★ | ★ | ★ | ★ | ★★ | ✗ | ✗ | ★★★ | ✗ |
| Gelatin/agar | ★ (US only) | ★★ | ★★ | ★★ | ★ | ★ | ★ | ★ | ✗ | ✗ |
| Rigid (print/epoxy) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ★★★ |

★★★ strong fit · ★★ workable · ★ marginal · ✗ not suitable.

## 9. How to expand — recommended sequence

1. **Reuse the base.** Your belly-fat solution *is* the multi-organ base. Start every new organ from it.
2. **Pick the organ's two numbers:** target **stiffness** (human in-vivo) and, if imaging matters,
   **SoS + attenuation** (§4 table).
3. **Set stiffness with FT cycles** (calibrate your own cycles→modulus curve once — absolute values are
   protocol-specific to your Selvol 165-class resin). Use **glycerol** to reach soft organs and to lift SoS.
4. **Add scatterers/attenuators only if you image** (SiC for echo, Al₂O₃ for attenuation, cellulose for lung).
5. **Prototype the easy wins first** (liver, kidney, muscle, vessel, prostate — all verified from the PVA
   base), then tackle **lung** (needs an aeration method) and **non-PVA** parts (skin/bone) last.
6. **Validate against human values**, not animal ex-vivo (see the liver caveat).

## 10. What is *not* yet verified

The research pass was rigorous but PVA-focused. It **did not verify**, and these remain **[Engineering]**
placeholders to confirm before you rely on them:
- **Non-PVA recipes** (silicone, gelatin, agar, ballistic gel, konjac, PAA) — only PVA's acoustic ranking
  vs other hydrogels is verified.
- **Quantitative targets** for **bone, cartilage/tendon, nerve, skin/subcutaneous**, and detailed
  **brain** and **heart** *mechanics*.
- **Lung aeration methods** (foams/porogens/microbubbles/sponges) and achieved densities.
- **Layer-bonding / needle-realism / sterility protocols** beyond the glycerol + biocide roles.
- Absolute PVA modulus values are **protocol/MW-specific** — calibrate your own base.

**Suggested follow-up:** a dedicated research pass on **(a) non-PVA blocks + the missing organs
(bone/cartilage/nerve/skin/brain-heart mechanics)** and **(b) the lung-aeration cookbook** would close
these gaps with the same citation rigor. Say the word and I'll run it.

## 11. References

**PVA-C multi-organ base & tuning**
- Surry et al., *Poly(vinyl alcohol) cryogel phantoms for use in ultrasound and MR imaging*, **Phys Med Biol** 49(24), 2004. https://iopscience.iop.org/article/10.1088/0031-9155/49/24/009 · https://pubmed.ncbi.nlm.nih.gov/15724540/
- Fromageau et al., *Estimation of PVA cryogel mechanical properties…*, **IEEE UFFC** 54(3), 2007 (tensile-validated, 20→600 kPa over 1→10 cycles). https://pubmed.ncbi.nlm.nih.gov/17375819/
- Butcher et al., *Multi-tissue PVA prostate phantom* (recipes for prostate/tumor/vessel; additive roles), **Bioengineering (MDPI)** 11(11):1052, 2024, PMC11591372. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11591372/
- Bisht et al., *PVA hydrolysis threshold + viscosity blending + single 24-h FT cycle*, **ACS Omega**, 2024, PMC10882697. https://pmc.ncbi.nlm.nih.gov/articles/PMC10882697/
- PVA-C vessel: *healthy→atherosclerotic artery via FT cycles*, **Physica Medica**, 2019. https://www.sciencedirect.com/science/article/abs/pii/S1120179719305022
- Kumar & Sheet, *PVA-C rabbit-liver & thyroid phantom*, **Ultrasound Med Biol** 52(2), 2026 (⚠ rabbit-liver 129 kPa). https://www.sciencedirect.com/science/article/abs/pii/S0301562925004089

**Per-organ property targets**
- Chen et al., *Acoustic characterization of tissue-mimicking hydrogels* (SoS/attenuation table; AIUM goal; PVA ranking), **Ultrasound Med Biol** 48(1), 2022. https://www.sciencedirect.com/science/article/pii/S030156292100380X
- Chen et al., *Young's modulus of ex-vivo bovine muscle/liver*, **IEEE UFFC** 43(1), 1996. http://brl.illinois.edu/Publications/1996/Chen-UFFC-191-1996.pdf
- Polio et al., *Cross-platform lung parenchyma stiffness (1.4–6.1 kPa)*, **PLOS ONE**, 2018, PMC6192579. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6192579/
- Lung phantom: *10 % PVA-C + 1 % microcrystalline cellulose*, PMC9957311. https://pmc.ncbi.nlm.nih.gov/articles/PMC9957311/

**Materials comparison & builds**
- *Tissue-Mimicking Materials for Ultrasound-Guided Needle Intervention Phantoms: A Comprehensive Review*, **Ultrasound Med Biol**, 2022. https://www.umbjournal.org/article/S0301-5629(22)00509-9/abstract
- Multi-layer / needle-realism sources: PMC6657873 (https://pmc.ncbi.nlm.nih.gov/articles/PMC6657873/), PMC12933378 (https://pmc.ncbi.nlm.nih.gov/articles/PMC12933378/), Springer 42235-021-0031-1 (https://link.springer.com/article/10.1007/s42235-021-0031-1).

**Company**
- IMRA Surgical (Pindari): https://imrasurgical.com/ · product library https://imrasurgical.com/product-demo-library · IMRA × Telix collaboration (radio-guided surgery training).
