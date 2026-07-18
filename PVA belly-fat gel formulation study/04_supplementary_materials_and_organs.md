# Supplement — Non-PVA Blocks, Missing Organs, Lung Aeration & Composite Builds

Companion to [`03_multi_organ_phantom_playbook.md`](03_multi_organ_phantom_playbook.md). This closes (as far
as the evidence allows) the four gaps that the PVA-centric passes left open: **(1) non-PVA building-block
recipes, (2) targets for bone/cartilage/tendon/nerve/skin/brain-heart mechanics, (3) the lung-aeration
cookbook, and (4) multi-layer bonding / needle realism / storage.**

> **Honesty note — read this first.** A third adversarially fact-checked pass (31 sources → 142 claims → 24
> verified) **strongly closed gap #1** (gelatin, agar/agarose, silicone) with quantitative, cited recipes.
> It **could not verify** gaps #2–#4: soft-lung aeration recipes, most missing-organ moduli, and bonding/
> storage protocols returned **no surviving verified claims** — these topics are genuinely sparse in the
> peer-reviewed literature. Below, verified content is **[Verified]**; everything in gaps #2–#4 is
> **[Engineering]** (sound domain guidance / typical literature ranges, *not* verified here — confirm before
> relying on it). Tags carry through from the earlier reports.

---

## 1. Non-PVA building blocks (VERIFIED recipes)

These are the complementary "other blocks" to PVA-C, with real numbers you can start from.

### 1a. Gelatin (the classic ultrasound TMM)

- **Madsen graphite/alcohol gel (the foundational recipe).** Water-based gelatin + uniformly dispersed
  **graphite powder** + controlled **n-propanol**. Two independently tunable knobs: **speed of sound
  1520–1650 m/s** (set by *alcohol*) and **attenuation 0.2–1.5 dB/cm at 1 MHz**, ~proportional to frequency
  (set by *graphite*). Graphite is the combined scatterer/attenuator. **[Verified — Madsen et al., Med Phys 1978]**
- **Oil-in-gelatin (elastography / fat feel).** Gelatin + **castor oil** + graphite + n-propanol →
  **SoS 1554–1558 m/s, attenuation 0.4–1.07 dB/cm/MHz, Young's modulus 10–26 kPa** (shear ~0.88–10.24 kPa).
  Castor-oil fraction is the SoS/attenuation lever. **[Verified — Nguyen et al. 2014, medium confidence (2-1)]**
- **Evaporated-milk gelatin (tunable, reproducible).** **111 g gelatin (bloom 125/175/250) per ~1 L**
  (11.1 % by mass), water base **50 % de-ionized water / 50 % evaporated milk**, + 10 drops Vyse defoamer →
  **SoS ~1551–1553 m/s, attenuation 0.50–0.54 dB/cm/MHz, density ~1057–1067 kg/m³.** **Stiffness set by
  bloom number:** Young's **9.5 kPa (125) → 18.8 kPa (175) → 29.4 kPa (250)**. **[Verified — Farrer et al. 2015]**
- **Trade-off:** gelatins match tissue **acoustically and tactilely** and are cheap, but **degrade over
  days–weeks** (crosslinkers/preservatives extend to weeks–months) → **best for disposable/short-term**
  phantoms, not reusable trainers. **[Verified — Mencarelli et al. 2024, medium (2-1)]**

### 1b. Agar / agarose (imaging phantoms)

- **Agar + wood-powder scatterer:** 2 % w/v agar + 4 % w/v wood powder → **SoS 1487–1533 m/s, ~0.53 dB/cm/MHz.** **[Verified — Drakos 2021]**
- **IEC water-based agar:** agar + glycerol + Al₂O₃ + SiC + benzalkonium chloride + water → **SoS 1479–1553 m/s,
  attenuation 0.6–2 dB/MHz/cm, Young's modulus 120–401 kPa.** **[Verified, medium (2-1)]**
- **Agar/gelatin mixtures (durable elastography):** tunable by dry-weight ratio; **7–10 month stability,
  bacteria-resistant** → good for **longer-lived heterogeneous** phantoms, tunable US + MRI. **[Verified — Madsen 2005]**
- **Organ-specific FUS agar phantoms (acoustics):** **Brain** = agar 2 % + SiO₂ 1.2 % + evaporated milk 25 % →
  **SoS 1485 m/s, 0.59 dB/cm-MHz**; **Muscle** = agar 2 % + SiO₂ 2.1 % + evaporated milk 40 % → **SoS 1529 m/s,
  0.99 dB/cm-MHz**. Silica = scatterer/attenuator knob; evaporated milk = SoS knob. **[Verified — Drakos et al. 2017]**
  *(Acoustics only — no verified brain/muscle modulus values.)*
- ⚠ Several agar SoS values run **below** the 1540 m/s tissue reference. A detailed agarose gram-recipe from a
  patent was **refuted** — don't cite specific agarose masses.

### 1c. Silicone (durable, reusable — but acoustically mismatched)

- **Acoustic limitation:** pure platinum-cure silicones sit **far below tissue** — **Ecoflex ~972 m/s,
  Dragon Skin Medium ~981 m/s** (~37 % below 1540). **Fix:** **+30 % glycerol raises Ecoflex to ~1041–1055 m/s**
  (still below tissue); solid/metal fillers (Al₂O₃) lower it. → Silicone is for **tactile/surgical realism,
  not ultrasound fidelity.** **[Verified — Cabrelli et al. 2016]**
- **Ecoflex softness ladder** (100 % modulus, ASTM D-412): **00-10/00-20 = 8 psi, 00-30 = 10 psi, 00-50 = 12 psi,
  Ecoflex 5 = 15 psi**. Mix **1A:1B**, room-temp cure, **shrinkage < 0.001 in./in.** (dimensionally stable). **[Verified — Smooth-On TB]**
- **Slacker Tactile Mutator (softener) dose-response** (Dragon Skin 10; pre-mix into Part B, then add Part A):
  **100B+50 Slacker → ~Shore 00-30; +100 → 000-50; +150 → 000-20; +200 → 000-7** (increasing tack/flesh-like
  rebound). Lets one base silicone be dialed across the soft-tissue range. **[Verified — Smooth-On]**
  *(Deadener, Silicone Thinner ratios, and mineral-oil softening were not verified — treat as [Engineering].)*

### 1d. Other gels — [Engineering, not verified here]

- **Ballistic gelatin** (10 % or 20 %, 250-bloom): good needle/penetration feel; melts, not durable.
- **Polyacrylamide** (+ egg-white/BSA): transparent; **thermochromic HIFU** lesion phantoms; acrylamide monomer is toxic in prep.
- **Carrageenan / konjac glucomannan:** softer hydrogel feel, some thermal robustness; less characterized.

## 2. Materials-vs-organ matrix

Acoustic anchors are **[Verified]**; needle-feel/durability/cost are **[Engineering]** synthesis.

| Material | Reusable | Needle feel | Ultrasound | CT/MRI | Cost | Best organs |
|---|---|---|---|---|---|---|
| **PVA-C (yours)** | ★★★ | ★★★ | ★★★ (SoS 1520–1616) | good | low–med | fat, liver, kidney, muscle, vessel, prostate, brain, breast, thyroid |
| **Gelatin (Madsen/oil-in-gel)** | ★ (days–wks) | ★★★ | ★★★ (1520–1650, tunable) | good | low | disposable US targets; fat (oil-in-gel) |
| **Agar / agarose** | ★★ (mos, +biocide) | ★★ | ★★ (1479–1553) | good/MRI | low | brain/muscle US, heterogeneous elastography |
| **Silicone (Ecoflex/Dragon Skin)** | ★★★ | ★★ (suturable skin) | ✗ (972–1055) | poor US | med–high | **skin**, outer/suturable layers, dry surgical feel |
| **Polyacrylamide** | ★★ | ★★ | ★★ | good | med | HIFU/thermal lesion phantoms |
| **Rigid (epoxy/plaster/3D-print/foam)** | ★★★ | ✗ | ✗ | ✓ | med | **bone**, rigid scaffolds, CT lung-density |

## 3. Missing-organ targets — [Engineering, confirm before use]

The research pass verified **only brain & muscle *acoustics*** (§1b). The mechanical targets below are
**typical literature ranges from domain knowledge, NOT verified in this pass** — confirm against primary
sources or your own measurements before designing to them.

| Organ | Young's / shear modulus (typical) | Acoustic / notes | PVA-C or other approach |
|---|---|---|---|
| **Brain (grey/white)** | very soft, **E ~1–4 kPa; shear (MRE) ~1–3 kPa** | Brain agar recipe verified: SoS 1485 m/s | 1 FT cycle + glycerol; or agar for imaging |
| **Heart / myocardium** | passive **~10–40 kPa** (diastolic), stiffer in systole | SoS ~1576 (verified, rpt 03) | moderate FT + fiber anisotropy |
| **Skin** | dermis/epidermis firm **~0.1–2 MPa**; subcutis soft ~1–30 kPa | layered | **silicone** top layer over PVA-C fat |
| **Cartilage** | **~0.5–1 MPa** (aggregate modulus) | stiff, smooth | high-FT PVA or cast polyurethane |
| **Tendon / ligament** | **tensile E ~0.5–1.5 GPa** (very stiff) | fibrous, anisotropic | fiber-reinforced high-FT PVA or non-gel |
| **Nerve** | **~0.5 MPa tensile**, tubular fascicles | fine tubes | fine PVA-C tubes / mandrel cast |
| **Bone — cortical** | **E ~15–20 GPa** | SoS ~3000–4000 m/s; high atten | epoxy/plaster/3D-print; **CIRS/Gammex bone-equivalent** |
| **Bone — trabecular** | **E ~0.1–2 GPa** (porous) | — | rigid foam / porous print |

## 4. Lung aeration cookbook

Two distinct problems — separate them:

**A) Soft, needle/ultrasound parenchyma.**
- **Verified anchors (from rpt 03):** stiffness target **1.4–6.1 kPa**; base recipe **10 % w/w PVA-C
  (99 % hydrolyzed, Mw 89–98k) + 1 % 20 µm microcrystalline cellulose** scatterer. **[Verified]**
- **Aeration methods (to reach lung's spongy low density) — [Engineering, NOT verified here; literature is thin]:**
  - **Porogen / salt / sugar leaching** — disperse a soluble particulate (e.g., 100–300 µm sugar/salt) into the
    PVA solution, gel, then dissolve it out to leave interconnected pores.
  - **Gas foaming / whipped emulsion** — entrain controlled gas (mechanical whipping or a foaming surfactant)
    before the first freeze cycle.
  - **Hollow microspheres / microbubbles** — blend gas-filled or hollow polymer spheres for aerated acoustics
    (A-lines) at controlled density.
  - **Freeze-dried PVA sponge** — lyophilize a cryogel to a reticulated sponge, then re-hydrate partially.
  > **Status: no verified soft-lung aeration recipe or achieved density exists** in this evidence base. This is
  > the single biggest remaining gap and is best closed by **direct primary-source reading + your own trials**
  > (measure density, stiffness, and US A-lines on each method) rather than further automated search.

**B) CT-density lung (radiodensity realism).**
- **Verified/sourced:** commercial rigid foams reproduce lung CT density well — **General Plastics
  LAST-A-FOAM FR-7100** across **~66–303 kg/m³** (brackets inflated-lung ~200–400 kg/m³), with a linear CT
  response of **~0.95 HU per kg/m³** (intercept ~−1003 HU); NIST used a similar low-cost foam as a CT lung
  density reference. **[Sourced — Kemerink/NIST-related CT-foam studies]** These are **rigid** (not
  needle/tactile) — use them for **CT** realism or as a rigid lung core, not for injection feel.

## 5. Multi-layer builds, needle realism & storage — [Engineering, not verified here]

No verified claims survived for these; the following is sound practice to validate:
- **Hydrogel-to-hydrogel:** PVA-C fuses to itself if layers **share freeze–thaw cycles** — cast deep organ
  first, partially cycle, overpour muscle then fat so outer layers see fewer cycles (softer). Plan a **cycle
  budget** per layer (final stiffness = formulation × total cycles experienced).
- **Silicone-to-hydrogel:** they don't chemically bond — use **mechanical keying** (mesh, undercuts, dovetails)
  or a compatible primer/adhesive.
- **Vessel/lumen casting:** **mandrel** (remove a rod) or **lost-core** (cast around a low-melt/soluble core,
  then melt/dissolve it) to form hollow tubes; PVA-C tubes are well suited.
- **Needle realism:** PVA-C needle tracks largely **self-close**, supporting repeated injection practice; tune
  puncture force with cycle count and glycerol.
- **Reusability/sterility/anti-dehydration:** keep **biocided** (your **Proxel BD20 / BIT**; benzalkonium
  chloride 0.5 % is a verified alternative in the phantom literature), store **sealed and hydrated** (in the
  gel's own fluid or a humid bag); a **humectant (glycerol)** in the mix reduces drying.

## 6. Status board — what's solid vs what to validate

| Topic | Status |
|---|---|
| Non-PVA recipes (gelatin, agar/agarose, silicone) | ✅ **Verified**, quantitative |
| Brain & muscle **acoustics** (agar) | ✅ Verified |
| Missing-organ **moduli** (bone/cartilage/tendon/nerve/skin/heart/brain-mech) | ⚠ **[Engineering]** — typical ranges, confirm |
| Soft-lung **aeration** recipes/densities | ❌ **Open** — literature thin; needs trials |
| CT-density lung (foam) | ✅ Sourced (rigid foams) |
| Multi-layer bonding, needle realism, storage | ⚠ **[Engineering]** — no verified data |
| Ballistic gel / polyacrylamide / carrageenan / konjac details | ⚠ **[Engineering]** — not verified |

**Recommendation.** Three research passes have hit diminishing returns on gaps #2–#4 — the remaining items
(soft-lung aeration, exact organ moduli, bonding protocols) are sparse enough in the literature that they're
best closed by **targeted primary-source reading and bench experiments**, not more broad automated search.
The non-PVA recipes in §1 are ready to use as-is.

## 7. References

**Gelatin / agar / silicone (verified)**
- Madsen, Zagzebski, Banjavic, Jutila, *Tissue-mimicking materials for ultrasound phantoms*, **Med Phys** 5(5):391–394, 1978. https://pubmed.ncbi.nlm.nih.gov/713972/
- Nguyen et al. (oil-in-gelatin TMM), via 2024 review PMC11200625. https://pmc.ncbi.nlm.nih.gov/articles/PMC11200625/
- Farrer et al., *Characterization of a gelatin/evaporated-milk tissue-mimicking phantom*, **J Ther Ultrasound** 3:9, 2015. https://link.springer.com/article/10.1186/s40349-015-0030-y
- Madsen et al., *Tissue-mimicking agar/gelatin materials…*, 2005, PMID 16306655. https://pubmed.ncbi.nlm.nih.gov/16306655/
- Drakos et al., *Agar-based FUS phantoms (brain/muscle acoustics)*, **J Ther Ultrasound** 5:14, 2017. https://link.springer.com/article/10.1186/s40349-017-0093-z
- Mencarelli et al., *Material selection for reusable vs disposable phantoms*, **J Mater Sci** 2024. https://link.springer.com/article/10.1007/s10853-024-09610-8
- Cabrelli et al., *Silicone acoustic properties & tuning*, **J Ultrasound** 2016, PMC5126009. https://pmc.ncbi.nlm.nih.gov/articles/PMC5126009/
- Smooth-On: Ecoflex series TB (https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf); Slacker (https://www.smooth-on.com/products/slacker/)
- Agarose TMM patent (SoS/atten; specific masses refuted): US5902748A. https://patents.google.com/patent/US5902748A/en

**Lung CT-density foam (sourced)**
- CT lung-density foam characterization (LAST-A-FOAM FR-7100; 66–303 kg/m³; ~0.95 HU/(kg/m³)), PMC2673671. https://pmc.ncbi.nlm.nih.gov/articles/PMC2673671/
- CT lung density reference phantom (NIST-referenced foam), PMC12196240. https://pmc.ncbi.nlm.nih.gov/articles/PMC12196240/

**Tissue property references (for confirming §3)**
- IT'IS Foundation tissue-properties database (acoustic). https://itis.swiss/virtual-population/tissue-properties/database/acoustic-properties
