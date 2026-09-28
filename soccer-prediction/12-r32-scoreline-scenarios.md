# Round of 32 — 5-Scenario Scoreline Portfolio

Top-5 most likely scorelines per game with probabilities, from a **Poisson + Dixon-Coles** model
(λ per team from strength/form/cohesion + market tiers; ρ = −0.06 low-score correction). Home team
listed first; venues are neutral except hosts (Mexico, USA, Canada).

> 90-minute distributions. In knockouts a draw goes to extra time/penalties — a "draw %" is **not**
> an elimination %. Research/analysis, not betting advice.

Format: **scoreline — probability** · then **W / D / W** and Over-2.5 / BTTS.

---

## v2 REASSESSMENT — market-informed (after Polymarket exact-score boards)

Two upgrades from reading the live exact-score markets on Brazil–Japan, Germany–Paraguay,
Netherlands–Morocco, Côte d'Ivoire–Norway:

1. **Advance probability** (what knockout markets actually quote) = `P(win 90') + P(draw) × q`,
   where `q` = the better side's shootout/ET edge `0.5 + 0.5·(winFav−winDog)/(winFav+winDog)`. This
   fixed my earlier under-counting of favorites winning in ET/pens.
2. **Selective λ nudges** toward the market *only where defensible*: Brazil 1.55→**1.65** (Japan
   also missing Mitoma/Minamino, so I'd over-docked Brazil) and Norway 1.40→**1.50** (Haaland). I
   **held** Germany and Netherlands — the market looks inflated there for structural reasons.

| # | Game | Advance (mine) | Market | Read |
|---|---|---|---|---|
| 1 | South Africa–Canada | SA 40 / **Can 60** | — | model-only |
| 2 | Brazil–Japan | **Bra 70** / Jap 30 | Bra 74 | **aligned** ✓ |
| 3 | Germany–Paraguay | **Ger 76** / Par 24 | Ger 86 | **FADE** → Paraguay-to-advance (mkt 14%) is **value** |
| 4 | Netherlands–Morocco | **Net 53** / Mor 47 | Net 62 | **FADE** → Morocco-to-advance (mkt 38%) is **the bargain** (NED missing both 1st-choice CBs) |
| 5 | Côte d'Ivoire–Norway | CIV 37 / **Nor 63** | Nor 66 | **aligned** ✓ |
| 6 | France–Sweden | **Fra 80** / Swe 20 | — | model-only |
| 7 | Mexico–Ecuador | **Mex 57** / Ecu 43 | — | low total |
| 8 | England–DR Congo | **Eng 83** / DRC 17 | — | model-only |
| 9 | Belgium–Senegal | **Bel 56** / Sen 44 | — | Senegal live |
| 10 | USA–Bosnia | **USA 60** / Bos 40 | — | model-only |
| 11 | Spain–Austria | **Spa 83** / Aus 17 | — | model-only |
| 12 | Portugal–Croatia | **Por 63** / Cro 37 | — | model-only |
| 13 | Switzerland–Algeria | **Swi 60** / Alg 40 | — | model-only |
| 14 | Colombia–Ghana | **Col 72** / Gha 28 | — | model-only |
| 15 | Australia–Egypt | Aus 46 / **Egy 54** | — | coin-flip |
| 16 | Argentina–Cabo Verde | **Arg 88** / CV 12 | — | model-only |

**The two bargains the market is offering** (where my model and the crowd disagree for a defensible
reason): **Paraguay to advance** (Germany priced like a lock at 86% despite losing to Ecuador in the
groups) and **Morocco to advance** (Netherlands at 62% while missing both first-choice center-backs).
Both anchor to *to-advance* markets, not 90-minute lines.

> Per-game scoreline distributions below; Brazil (#2) and Norway (#5) updated for the λ nudge.

---

### 1. South Africa vs Canada  (λ 1.05 – 1.35)
- draw 1-1 — **13.6%**
- Canada 1-0 — **11.5%**
- draw 0-0 — **9.8%**
- South Africa 1-0 — **8.8%**
- Canada 2-1 — **8.7%**
- **W/D/W:** SA 28% / draw 29% / Canada 43% · O2.5 43% · BTTS 49%

### 2. Brazil vs Japan  (λ 1.65 – 1.00)  🔒 *market-anchored*
- draw 1-1 — **12.4%**
- Brazil 1-0 — **11.0%**
- Brazil 2-0 — **9.6%**
- Brazil 2-1 — **9.6%**
- draw 0-0 — **7.8%**
- **W/D/W:** Brazil 52% / draw 26% / Japan 22% · **Advance: Brazil 70% / Japan 30%** (mkt 74 — aligned ✓)

### 3. Germany vs Paraguay  (λ 1.60 – 0.80)
- Germany 1-0 — **13.8%**
- draw 1-1 — **12.3%**
- Germany 2-0 — **11.6%**
- draw 0-0 — **9.8%**
- Germany 2-1 — **9.3%**
- **W/D/W:** Germany 56% / draw 26% / Paraguay 18% · O2.5 43% · BTTS 45%

### 4. Netherlands vs Morocco  (λ 1.30 – 1.20)
- draw 1-1 — **13.6%**
- Netherlands 1-0 — **9.9%**
- Morocco 1-0 — **9.1%**
- draw 0-0 — **9.0%**
- Netherlands 2-1 — **8.3%**
- **W/D/W:** Netherlands 38% / draw 29% / Morocco 33% · O2.5 46% · BTTS 52%  *(coin-flip)*

### 5. Côte d'Ivoire vs Norway  (λ 1.10 – 1.50)  🔒 *market-anchored*
- draw 1-1 — **13.0%**
- Norway 1-0 — **10.4%**
- Norway 2-1 — **9.2%**
- Norway 2-0 — **8.4%**
- draw 0-0 — **8.2%**
- **W/D/W:** CIV 27% / draw 27% / Norway 46% · **Advance: Norway 63% / CIV 37%** (mkt 66 — aligned ✓)

### 6. France vs Sweden  (λ 2.00 – 0.90)
- France 2-0 — **11.0%**
- draw 1-1 — **10.5%**
- France 1-0 — **10.4%**
- France 2-1 — **9.9%**
- France 3-0 — **7.3%**
- **W/D/W:** France 62% / draw 22% / Sweden 16% · O2.5 55% · BTTS 52%

### 7. Mexico vs Ecuador  (λ 1.20 – 1.00)  — *altitude, Azteca*
- draw 1-1 — **14.1%**
- Mexico 1-0 — **12.5%**
- draw 0-0 — **11.9%**
- Ecuador 1-0 — **10.3%**
- Mexico 2-0 — **8.0%**
- **W/D/W:** Mexico 40% / draw 31% / Ecuador 30% · O2.5 38% · BTTS 45%  *(low-scoring)*

### 8. England vs DR Congo  (λ 2.00 – 0.80)
- England 2-0 — **12.2%**
- England 1-0 — **11.6%**
- draw 1-1 — **10.3%**
- England 2-1 — **9.7%**
- England 3-0 — **8.1%**
- **W/D/W:** England 65% / draw 22% / DR Congo 14% · O2.5 53% · BTTS 48%

### 9. Belgium vs Senegal  (λ 1.40 – 1.20)
- draw 1-1 — **13.2%**
- Belgium 1-0 — **9.7%**
- Belgium 2-1 — **8.7%**
- draw 0-0 — **8.2%**
- Senegal 1-0 — **8.2%**
- **W/D/W:** Belgium 41% / draw 28% / Senegal 31% · O2.5 48% · BTTS 53%  *(live underdog)*

### 10. USA vs Bosnia  (λ 1.40 – 1.10)
- draw 1-1 — **13.4%**
- USA 1-0 — **10.7%**
- draw 0-0 — **9.0%**
- USA 2-1 — **8.8%**
- Bosnia 1-0 — **8.3%**
- **W/D/W:** USA 43% / draw 28% / Bosnia 29% · O2.5 46% · BTTS 51%

### 11. Spain vs Austria  (λ 2.00 – 0.80)
- Spain 2-0 — **12.2%**
- Spain 1-0 — **11.6%**
- draw 1-1 — **10.3%**
- Spain 2-1 — **9.7%**
- Spain 3-0 — **8.1%**
- **W/D/W:** Spain 65% / draw 22% / Austria 14% · O2.5 53% · BTTS 48%

### 12. Portugal vs Croatia  (λ 1.50 – 1.10)
- draw 1-1 — **13.0%**
- Portugal 1-0 — **10.4%**
- Portugal 2-1 — **9.2%**
- Portugal 2-0 — **8.4%**
- draw 0-0 — **8.2%**
- **W/D/W:** Portugal 46% / draw 27% / Croatia 27% · O2.5 48% · BTTS 53%

### 13. Switzerland vs Algeria  (λ 1.40 – 1.10)
- draw 1-1 — **13.4%**
- Switzerland 1-0 — **10.7%**
- draw 0-0 — **9.0%**
- Switzerland 2-1 — **8.8%**
- Algeria 1-0 — **8.3%**
- **W/D/W:** Switzerland 43% / draw 28% / Algeria 29% · O2.5 46% · BTTS 51%

### 14. Colombia vs Ghana  (λ 1.60 – 0.90)
- draw 1-1 — **12.5%**
- Colombia 1-0 — **12.4%**
- Colombia 2-0 — **10.5%**
- Colombia 2-1 — **9.5%**
- draw 0-0 — **8.9%**
- **W/D/W:** Colombia 53% / draw 26% / Ghana 20% · O2.5 46% · BTTS 48%

### 15. Australia vs Egypt  (λ 1.10 – 1.20)
- draw 1-1 — **14.0%**
- Egypt 1-0 — **11.2%**
- draw 0-0 — **10.8%**
- Australia 1-0 — **10.2%**
- Egypt 2-1 — **7.9%**
- **W/D/W:** Australia 33% / draw 30% / Egypt 38% · O2.5 40% · BTTS 47%  *(coin-flip)*

### 16. Argentina vs Cabo Verde  (λ 2.20 – 0.70)
- Argentina 2-0 — **13.3%**
- Argentina 1-0 — **11.6%**
- Argentina 3-0 — **9.8%**
- Argentina 2-1 — **9.3%**
- draw 1-1 — **9.0%**
- **W/D/W:** Argentina 71% / draw 19% / Cabo Verde 10% · O2.5 55% · BTTS 45%

---

## Notes
- **Computed**, not eyeballed: `tools/`-style Poisson+DC grid (script in commit). λ inputs encode
  team strength, recent form, players (e.g. Brazil without Raphinha, Ghana without Kudus), cohesion,
  and host/altitude edges (Mexico).
- **These are model priors.** Anchor each to the live Polymarket/Kalshi 3-way before betting — and
  per the June-27 lesson, treat the draw/low-score scenarios in tight games as *underrated*, not
  overrated, especially the coin-flips (Netherlands–Morocco, Australia–Egypt) and low totals
  (Mexico–Ecuador).
- Draw % is a 90-minute figure; the higher-seed usually advances more often than the win % alone
  (extra-time/penalty edge).
