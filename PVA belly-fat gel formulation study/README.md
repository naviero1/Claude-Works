# PVA Belly-Fat Gel — Formulation Study

A citation-rich study on formulating **PVA freeze–thaw cryogels** (~10 % solids) to mimic human
**abdominal adipose ("belly fat")** for **injection and surgical-training phantoms**, anchored to the
lab's proven production **standard mix**. The literature is used as *reference for what works* — the
standard mix stays fixed; the study explains the science and tunes the **downstream freeze–thaw** step.

## Contents

| File | What it is |
|---|---|
| [`00_standard_mix.md`](00_standard_mix.md) | The **fixed baseline** formulation (Selvol S-1551F-D PVA, NaCl, Proxel BD20, Proline pigments) + process, QC specs, shelf life. |
| [`01_pva_grade_reference.md`](01_pva_grade_reference.md) | Brochure-grounded **PVA grade reference** — Selvol/Kuraray MW & hydrolysis specs, cryogel-relevant grades, and identification of S-1551F-D. |
| [`02_belly_fat_freeze_thaw_study.md`](02_belly_fat_freeze_thaw_study.md) | **Main study**: cryogelation physics, freeze–thaw tuning, belly-fat mechanical targets, recommended protocol, numeric tables, pitfalls, and a prioritized experiment plan. |
| `03_multi_organ_phantom_playbook.md` | *(in progress)* Extending the PVA-cryogel base to **other organs** (lung, liver, kidney, muscle, vessel, etc.) + profile of IMRA Surgical. |
| [`brochures/`](brochures/) | Supplier TDS/brochures (Selvol, Kuraray) + drop-zone for the rest. |

## Headline findings (belly fat)

- **Resin class is correct.** Freeze–thaw cryogels require **fully/super-hydrolyzed (98–99 %+), high-MW**
  PVA — partially hydrolyzed grades won't gel at ~10 %.
- **The freeze–thaw makes the gel, not the cook.** Crystallites (~3 nm) + phase-separated domains form
  during freezing/thawing.
- **You're likely too stiff for fat.** ~10 % PVA at 2–5 cycles → ~65–180 kPa, but fat is ~1–25 kPa →
  use **fewer cycles (1–2) + slow controlled thaw**; the **0.8 % NaCl already softens** the gel.
- **Biggest lever = 1→2 cycles** (largest step-change after cycle 2); the "6-cycle plateau" idea is refuted.

See [`02_...`](02_belly_fat_freeze_thaw_study.md) §13 for caveats and the open questions that drive the
experiment plan.

## Method

Findings synthesized from a multi-source, adversarially fact-checked research pass (27 sources → 122
claims → 25 verified by 3-vote checking, 22 confirmed), combined with the supplier brochures in
`brochures/`. Every claim in the study is tagged **[Verified] / [Context] / [Uncertain]** with citations.
