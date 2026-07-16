# PVA Grade Reference (from supplier brochures)

Source-of-truth specs pulled from the supplier files in [`brochures/`](brochures/):

- **Sekisui Selvol PVOH Brochure (America, EN)** — `brochures/Sekisui_Selvol_PVOH_Brochure_EN.pdf`
- **Kuraray Poval / Exceval / Elvanol Technical Data Sheet (America, EN, 2025-04-30)** — `brochures/Kuraray_Poval_Exceval_Elvanol_TDS_America_EN.pdf`

All viscosities below are **4 % aqueous solution at 20 °C** (cP ≡ mPa·s), the industry proxy
for molecular weight. Higher viscosity number = higher MW.

---

## 1. How to read the two naming systems

| | Sekisui **Selvol** | Kuraray **Poval / Elvanol** |
|---|---|---|
| Naming | 3-digit code (e.g., 165): 1st digit ≈ viscosity class, last two ≈ hydrolysis family | `V-H` (e.g., 56-98): **V** = 4 % viscosity (MW proxy), **H** = % hydrolysis |
| Hydrolysis tiers | Super 99.3+ / Fully 98.0–98.8 / Intermediate 90–97 / Partial 87–89 | Fully ~98 / Medium ~96 / Partial 87–89 (Elvanol homopolymer 99.2–99.7) |

## 2. Selvol molecular-weight ladder (Selvol Table 3)

| 4 % Viscosity | Class | Degree of Polymerization | Weight-avg MW (Mw) | Number-avg MW (Mn) |
|---|---|---|---|---|
| 3–4 cP | Ultra-low | 150–300 | 13,000–23,000 | 7,000–13,000 |
| 5–6 cP | Low | 350–650 | 31,000–50,000 | 15,000–23,000 |
| 22–30 cP | Medium | 1,000–1,500 | 85,000–124,000 | 44,000–65,000 |
| **45–72 cP** | **High** | **1,600–2,200** | **146,000–186,000** | **70,000–101,000** |

> **For freeze–thaw cryogels you want the "High" viscosity + "Super/Fully hydrolyzed" corner** —
> maximum hydroxyl density (crystallites + H-bonding) and maximum chain length (entanglement).

## 3. Cryogel-relevant grades (super- & fully-hydrolyzed, higher MW)

### Sekisui Selvol
| Grade | Hydrolysis % | 4 % Visc (cP) | MW class | Cryogel fit |
|---|---|---|---|---|
| **Selvol 165 / 165SF** | **99.3+** (super) | **62–72** | **High** | ★★★ Best catalog analog to the standard-mix resin. 165SF = super-fine particle (99 % < 120 mesh). |
| Selvol 125 | 99.3+ (super) | 28–32 | Medium | ★★ Softer/weaker gel at same solids. |
| Selvol 350 | 98.0–98.8 (fully) | 62–72 | High | ★★★ High-MW fully hydrolyzed; strong gels, marginally less crystalline than 165. |
| Selvol 325 / 325LA | 98.0–98.8 (fully) | 28–32 | Medium | ★★ Medium MW. |

### Kuraray Poval / Elvanol
| Grade | Hydrolysis % | 4 % Visc (mPa·s) | MW class | Cryogel fit |
|---|---|---|---|---|
| **Kuraray Poval 56-98** | 98.0–98.8 (fully) | 52–60 | High | ★★★ Closest Kuraray high-MW fully-hydrolyzed. |
| Kuraray Poval 28-98 | 98.0–99.0 (fully) | 25–31 | Medium | ★★ |
| **Elvanol 71-30** | **99.2–99.7** (super) | 27–33 | Medium–High | ★★★ Super-hydrolyzed homopolymer; classic high-strength grade. |
| Elvanol 90-50 | 99.2–99.7 (super) | 11.6–15.4 | Low–Medium | ★ Lower MW. |

## 4. Identification of the standard-mix resin, "Selvol S-1551F-D"

- **Not a line item** in the general Selvol brochure (which lists 3-digit grades). It is the
  **supplier/company-designated code** used in the production spec and the second-source
  qualification (see `../PVA second supplier initiative/`), described there as a
  **super-hydrolyzed (~99 %+), high-MW PVA**.
- **Closest catalogued analog: Selvol 165 / 165SF** — super-hydrolyzed (99.3+ %), high-MW
  (62–72 cP; DP 1600–2200; Mw ~146k–186k). The "S-…F" / fine-particle "-D" hints are consistent
  with a **fine-particle super-hydrolyzed high-MW grade** (the 165SF family). *Treat this as a
  well-supported mapping, not a confirmed part number — verify against the S-1551F-D CoA/TDS when it lands.*
- **Corroboration from solids loading:** Selvol's *maximum recommended solids* for **super-hydrolyzed**
  grades is **7–10 %** (Selvol Table 6). The standard mix runs PVA at **~10.6 %** — right at/above that
  ceiling — which is why it needs the full **90–95 °C, 30–45 min** cook, and why it shows a short
  (18-day) shelf life, viscosity creep on storage, and "protect from freezing" handling.

## 5. Why this grade class is right for elastic, reusable phantoms

From the brochures (Selvol Figure 3 / property tables): increasing **MW** → *much higher strength,
higher cohesive strength, higher H-bonding, increased water resistance*; increasing **% hydrolysis**
→ *higher crystallinity, water/humidity resistance, higher melting point (230 °C fully vs 180–190 °C
partial)*. Freeze–thaw cryogelation is driven by **hydroxyl-rich crystallite formation and hydrogen
bonding**, so a **super-hydrolyzed, high-MW** resin gives the strongest, most durable, most elastic
physically-crosslinked gel — ideal for a **reusable injection/training phantom** that must survive
repeated needle passes without falling apart. (The mechanism and freeze–thaw tuning are covered in
the main study report.)

## 6. Brochure notes relevant to the standard-mix process

- **Dissolution:** disperse resin in **cold/room-temp water first**, then heat — never add to
  pre-heated water (high lumping risk; lumps are very hard to cook out). Matches the standard-mix order
  (charge water → add resin → heat). Selvol super-hydrolyzed min cook-out ≈ 205 °F (96 °C), 30 min hold;
  standard mix uses 90–95 °C for 30–45 min (workable, on the low side for super-hydrolyzed — keep the
  full hold time).
- **Keep all tanks/lines free of borax and other crosslinkers** — traces cause coagulation/gelation.
- **Biocide** recommended if solution kept > 24 h (standard mix uses Proxel BD20 / BIT). Selvol lists
  Kathon LX < 50 ppm and Dowicil 75 at 1000–2000 ppm as examples.
- **Plasticizers** (glycerine, ethylene glycol, urea at ~2–5 %) soften PVA — a lever if a softer,
  more fat-like feel is wanted (see main study). Glycerol also acts as a cryoprotectant.
- **Storage of solid resin:** up to 5 years dry; **solution** viscosity rises over time (especially
  high-hydrolysis, high-concentration, cold) — restore by gentle reheat/stir. Do **not** let the
  solution freeze accidentally (that starts cryogelation).
