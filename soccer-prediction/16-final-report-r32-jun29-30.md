# Final Report — R32 (Netherlands–Morocco tonight · CIV–Norway · France–Sweden · Mexico–Ecuador)

*Research/analysis, not financial advice. "Advance" = to reach the Round of 16 (incl. ET/pens).*

## Results so far — grading

| Game | Predicted | Actual | Call |
|---|---|---|---|
| South Africa–Canada | Canada to advance (60%) | **Canada 1-0** (adv) | ✓ result |
| Brazil–Japan | Brazil to advance (70%), **bet = pass** | **Brazil 2-1** (adv) | ✓ result + **exact score**; pass was correct (no edge) |
| Germany–Paraguay | scoreline Ger 2-1; **bet = Paraguay-advance value** | **1-1 → extra time** (Paraguay led 1-0 in reg.; Germany ET goal VAR-ruled out); final pending | scoreline ✗, **but the bargain was vindicated** |

**The Germany–Paraguay takeaway is the headline:** my *scoreline* model missed (it's a draw/ET, not a
Germany win), but the **betting call nailed it** — we said 86% on Germany was inflated and
Paraguay-to-advance (priced **15%**) had real equity, and Paraguay just took the tournament favorite
to penalties. Process over single-game prediction: the edge call was right even where the scoreline
guess was wrong.

---

## The four games

### 1. 🇳🇱 Netherlands vs Morocco — TONIGHT 9 PM — **THE BET** (unchanged, conviction ↑)
Market **NED 62% / MAR 38%** to advance; my model **53 / 47**. Recommended **Allocation A**
(Morocco-to-advance value, **+$15 EV, 54% P(profit)**). **Difference vs the allocation done earlier:
none in the numbers** — but **conviction is up**, because Germany–Paraguay just proved live that the
crowd over-prices favorites in exactly these to-advance spots. (Morocco edge = cohesion + Bono in a
shootout vs a Dutch back line missing both first-choice CBs.)

| | Objective | Allocation | EV | P(profit) |
|---|---|---|---|---|
| **A ✅** | Max-EV | $65 MAR-adv · $20 1-1 · $15 MAR 1-0 | **+$15** | 54% |
| B | Max P(profit) | $80 NED-adv · $20 1-1 | −$13 | 60% |
| C | Balanced | $30 MAR-adv · $18 1-1 · $12 NED 1-0 · $12 0-0 · $14 NED 2-1 · $14 MAR 2-1 | +$1 | 39% |
| D | Low-scoring | $35 Under 2.5* · $20 1-1 · $20 0-0 · $25 MAR-adv | +$1 | 38% |

### 2. 🇨🇮 Côte d'Ivoire vs Norway — TMRW 1 PM — **MARGINAL PASS** (updated with real prices)
Market **NOR 65% / CIV 36%**; my model **NOR 63 / CIV 37** → **essentially aligned**. With the *real*
exact-score prices (vs my earlier estimates), allocation **A (CIV/draw lean) is marginally +EV
(+$4.6, 51%)** — but that's **within model noise**, not a conviction bet. The rest are −EV.
**Verdict: small dab on the CIV/draw side at most, or pass.** Norway (Haaland) fairly priced.

| Objective (real prices) | EV | P(profit) |
|---|---|---|
| A) Max-EV (CIV/draw) | **+$4.6** | 51% |
| B) Max P(profit) (Norway) | −$4.1 | 68% |
| C) Balanced | −$5.4 | 39% |

Extra-Time market: **Yes 38%** vs my draw-after-90 ~27% — but "No ET" pays ~1.0×, so unbettable.
Scores: 1-1 14% · NOR 1-0 11% · NOR 2-1 10% · NOR 2-0 9% · CIV 2-1 8%.

### 3. 🇫🇷 France vs Sweden — TMRW 5 PM — **low-conviction Sweden-advance value**
Market **France 89% / Sweden 12%** to advance; my model **France 80%** (max ~85% even at λ 2.4). So
the market is more bullish on France than the model at *any* reasonable λ → **Sweden-to-advance
(mkt 12%, model 15–20%) is the value**. Scores: France 2-0 / 1-1 / 1-0; O2.5 55%; goals 1.3 / 1.6.

**Caveat (important):** lower conviction than Morocco. The big EV rests on the model being right that
France is "only" 80–85%, when France have been the tournament's best team (10 group goals) and Sweden
are weak + missing CB Hien — so 89% might just be *correct*. Sweden's case: Isak + Gyökeres can nick a
goal and force ET.

| | Objective | Allocation | EV | P(profit) |
|---|---|---|---|---|
| A | Max-EV (Sweden dart) | $40 SWE-adv · $25 1-1 · $20 0-0 · $15 SWE 1-0 | +$46 | 33% |
| B | Max P(profit) (France) | $90 FRA-adv · $10 SWE-adv | −$3 | 80% (best +$1) |
| **C ✅** | **Balanced** | $18 FRA 2-0 · $16 FRA 1-0 · $14 FRA 2-1 · $12 FRA 3-0 · $40 SWE-adv | **+$18** | **59%** |
| D | Concentrated Sweden | $70 SWE-adv · $30 1-1 | +$62 | 29% |

**Recommend C** (robust to Sweden's true number); A/D for value hunters; B is the trap.

### 4. 🇲🇽 Mexico vs Ecuador — TMRW 9 PM — **Ecuador-advance value** (moderate conviction)
Market **MEX 64% / ECU 37%** to advance; my model **57 / 43** → **Ecuador-to-advance is the value**.
Lowest-total game on the board (model O2.5 38%) — **but the market agrees** (it prices 0-0 at 16%,
1-1 at 15%), so an *Under* play is **not** value; the edge is *only* Ecuador-advance. Mexico's edge =
home + altitude (Azteca); Ecuador's case = quality (Caicedo, Plata, beat Germany) + Mexico's
first-choice keeper out (Malagón → Ochoa).

| | Objective | Allocation | EV | P(profit) |
|---|---|---|---|---|
| A | Max-EV | $100 ECU-adv | +$15.5 | 43% |
| **D ✅** | **Ecuador value + draw hedge** | $70 ECU-adv · $15 1-1 · $15 0-0 | **+$6** | **51%** |
| B | Balanced (+ Mexico hedge) | $55 ECU-adv · $25 MEX 1-0 · $20 MEX 2-0 | −$2 | 63% |
| C | Max P(profit) (Mexico) | $85 MEX-adv · $15 ECU-adv | −$7 | 57% |

**Recommend D** — positive EV *and* >50% to profit. Moderate conviction; don't oversize (Mexico's
altitude/home edge is real).

---

## ✅ Complete slate — recommended play per game
| Game | Verdict | Recommended | EV / P(profit) |
|---|---|---|---|
| 🇳🇱 Netherlands–Morocco | **BET** (highest conviction) | A: $65 MAR-adv · $20 1-1 · $15 MAR 1-0 | +$15 / 54% |
| 🇲🇽 Mexico–Ecuador | **BET** (moderate) | D: $70 ECU-adv · $15 1-1 · $15 0-0 | +$6 / 51% |
| 🇫🇷 France–Sweden | **small/optional** (low conv.) | C: France scores + $40 SWE-adv | +$18 / 59% |
| 🇨🇮 CIV–Norway | marginal pass | small A (CIV/draw) or skip | +$5 / 51% |
| 🇧🇷 Brazil–Japan | **pass** | — | no edge |
| 🇩🇪 Germany–Paraguay | done | C (Paraguay dart) — vindicated (ET) | — |

**Conviction ranking of the live edges:** Morocco-advance > Ecuador-advance > Sweden-advance.
All three are *fade-the-overpriced-favorite* plays; Morocco is the cleanest (CB injuries), Sweden the
thinnest (France genuinely dominant).

---

## Bottom line
- **Tonight:** bet **Netherlands–Morocco, Allocation A** (Morocco to advance) — conviction reinforced by the Germany–Paraguay result.
- **Tomorrow:** **CIV–Norway = pass** (no edge). **France–Sweden = likely pass** (send market to confirm). **Mexico–Ecuador = the one to watch** — lowest total on the board; send the market and it's the most probable +EV play of the four.
