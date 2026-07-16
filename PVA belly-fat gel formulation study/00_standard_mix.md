# Standard Mix — Belly-Fat PVA Gel (Fixed Baseline)

> **Status: FIXED / "what works."** This is the proven production formulation and is the
> anchor for the whole study. The research report tunes the downstream **freeze–thaw**
> process and mechanics *around* this mix — it does **not** replace it. Supplier brochures
> for the raw materials are collected in [`brochures/`](brochures/).

## Batch summary

| | Wet | Dry |
|---|---|---|
| **Batch size (g)** | 2261.50 | 261.94 |
| **Theoretical % total solids** | **11.58 %** | |
| **PVA-only solids fraction** | 240 / 2261.50 = **10.61 %** | (matches the "~10 % solids" target) |

## Raw materials

| Material | Mass frac | Wet g/batch | Solid g/batch | Role |
|---|---|---|---|---|
| **Selvol S-1551F-D** (PVA resin) | 0.1061 | 240.00 | 240.00 | Structural polymer. Super-hydrolyzed (~99 %+), high-MW PVA. Treated as 100 % solids. Specs per supplier CoA/brochure. |
| **Proxel BD20** | 0.0010 | 2.26 | 0.44 | Biocide/preservative — 1,2-benzisothiazolin-3-one (BIT), ~20 % active (Lonza). |
| **NaCl** | 0.0080 | 18.00 | 18.00 | Salt, ~0.80 wt %. Tonicity/conductivity; modest effect on gelation & acoustics. |
| **Petal Pink Proline Powder** | 0.0013 | 3.00 | 3.00 | Pigment (flesh/fat tone). |
| **Taupe Proline Powder** | 0.0002 | 0.50 | 0.50 | Pigment (flesh/fat tone). |
| **Water** | 0.8834 | 1997.74 | 0.00 | Solvent, ~88.34 wt %. |
| **Subtotal** | 1.0000 | 2261.50 | 261.94 | |

## Procedure (as run)

1. Charge vessel with **1997.74 g water**; begin moderate agitation.
2. Add **240.00 g Selvol S-1551F-D**.
3. Add **18.00 g NaCl**.
4. Add **3.00 g Petal Pink Proline Powder**.
5. Add **0.50 g Taupe Proline Powder**.
6. Begin heating to **194–203 °F (90–95 °C)**, steady agitation.
7. Hold at **194–203 °F (90–95 °C)** for **30–45 min** with mixing (full dissolution, no fisheyes/gels).
8. Add **2.26 g Proxel BD20** during the **final 10 min** of mixing (hot addition).
9. Adjust solids if necessary.
10. Filter through **200 micron** into packaging.

## Known constraints / QC (from the PVA supplier initiative)

- **Shelf life:** ~18 days — made fresh to order, no stockpiling.
- **Protect from freezing** in shipping/storage — the *solution* must not freeze prematurely
  (freezing is the deliberate downstream gel-forming step; an accidental freeze pre-gels the drum).
- **CoC / CoA per shipment:** lot #, production date, **% TS**, final **pH**, **Brookfield viscosity**
  (spindle #3, 10 RPM, 25 °C). Viscosity target/tolerance being finalized from incumbent CoA history.
- Contact surfaces **316L SS**; jacketed temp-controlled tank; cool to ≤40 °C after hold.
- Incumbent supplier: **SNP**; second-source qualification in progress (see `../PVA second supplier initiative/`).

## How the gel is formed

The procedure above yields the **PVA solution**. The **belly-fat gel** is produced
**downstream by freeze–thaw** (physical cryogelation of the dissolved PVA). Freeze–thaw
cycle count, temperatures, rates, and dwell times are the primary levers for the gel's
softness, modulus, and needle feel — see the main study report.
