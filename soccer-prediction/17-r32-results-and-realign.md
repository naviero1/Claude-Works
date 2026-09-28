# R32 — Results Report & Realigned Predictions (from July 1)

## Part A — Results so far vs our calls

All 7 first-half R32 games are in. Both of our headline bets — Morocco and Paraguay to advance,
the two "fade the overpriced favorite" plays — **hit**.

| Game | Result | Who advanced | Our model lean | Our bet | Outcome |
|---|---|---|---|---|---|
| South Africa–Canada | Canada 1-0 | Canada | Canada 60% ✓ | (pass) | ✓ |
| Brazil–Japan | Brazil 2-1 | Brazil | Brazil 70% ✓ | **pass** (no edge) | ✓ correct pass |
| Germany–Paraguay | 1-1 → **Paraguay** adv | Paraguay | Germany 76% (modal) | **Paraguay-adv @15%** | ✅ **BET WON** |
| Netherlands–Morocco | 1-1 → **Morocco** (pens) | Morocco | NED 53% (coin-flip) | **Morocco-adv @38%** | ✅ **BET WON** |
| Côte d'Ivoire–Norway | Norway 2-1 | Norway | Norway 63% ✓ | (marginal pass) | ✓ correct pass |
| France–Sweden | France 3-0 | France | France 80% ✓ | C (France scores + Sweden dart) | ✓ small win |
| Mexico–Ecuador | Mexico 2-1 | Mexico | **Mexico 57%** ✓ | D (Ecuador-adv value) | ✗ bet lost |

### Betting P&L (if the recommended allocations were staked at $100/game)
| Game | Allocation | Return | Net |
|---|---|---|---|
| Netherlands–Morocco | A ($65 MAR-adv + $20 1-1 + $15 MAR 1-0) | $304 | **+$204** |
| Germany–Paraguay | C ($34 PAR-adv + $12 1-1 + Germany scores) | $360 | **+$260** |
| France–Sweden | C (France scores + $40 Sweden-adv) | $109 | +$9 |
| Mexico–Ecuador | D ($70 ECU-adv + draws) | $0 | −$100 |
| **Total** | **$400 staked** | **$773** | **+$373 (+93%)** |

### The honest read
- **Process worked:** the system found the two spots where the crowd over-priced a favorite
  (Germany 86%, Netherlands 62% missing both CBs), bet the +EV underdog, and both advanced. It also
  **correctly passed** the no-edge games (Brazil, CIV–Norway) and the diversified France allocation
  banked a small win off the exact-score hedge even though the Sweden thesis was wrong.
- **But respect variance:** Morocco won *on penalties* and Paraguay went the distance — both were
  near-coin-flips in the moment, and we got the good side. The bets were +EV (that's the durable
  part); a +93% slate will regress. The **Mexico–Ecuador loss** is the reminder: that fade was
  lower-conviction (Mexico's altitude/home edge was real), and it lost — exactly as the "don't
  oversize" caveat warned.
- **Calibration:** modal advance picks 5/7; **betting edges 3 of 4 profitable**; the edge lived
  where we said (to-advance markets on overpriced favorites), not in scorelines or totals.

---

## Part B — Realigned predictions, all 9 upcoming R32 games (Jul 1–3)

Model = Poisson + Dixon-Coles with the upgraded advance probability. **These are model priors** — no
live markets yet; the edge only appears once we compare to Polymarket/Kalshi. Flagged below: which
games are most likely to hide a *fade-the-favorite* edge (the pattern that just paid off twice).

| Date | Game | Advance | W/D/W | Top scores | O2.5 | Edge watch |
|---|---|---|---|---|---|---|
| Jul 1 | **England–DR Congo** | Eng **83** / DRC 17 | 65/22/14 | Eng 2-0, Eng 1-0, 1-1 | 53 | heavy fav — value only if mkt >88% |
| Jul 1 | **Belgium–Senegal** | Bel **56** / Sen 44 | 41/28/31 | 1-1, Bel 1-0, Bel 2-1 | 48 | ⭐ **close — Senegal-adv if Belgium overpriced** |
| Jul 1 | **USA–Bosnia** | USA **60** / Bos 40 | 43/28/29 | 1-1, USA 1-0, 0-0 | 46 | host USA — watch for Bosnia value |
| Jul 2 | **Spain–Austria** | Spa **83** / Aus 17 | 65/22/14 | Spa 2-0, Spa 1-0, 1-1 | 53 | heavy fav — likely fair |
| Jul 2 | **Portugal–Croatia** | Por **63** / Cro 37 | 46/27/27 | 1-1, Por 1-0, Por 2-1 | 48 | ⭐ **Croatia experienced — fade-Portugal candidate** |
| Jul 2 | **Switzerland–Algeria** | Swi **60** / Alg 40 | 43/28/29 | 1-1, Swi 1-0, 0-0 | 46 | close — Algeria attacking |
| Jul 3 | **Australia–Egypt** | Aus 46 / **Egy 54** | 33/30/38 | 1-1, Egy 1-0, 0-0 | 40 | coin-flip; Salah; lowest total |
| Jul 3 | **Argentina–Cabo Verde** | Arg **89** / CV 11 | 73/18/9 | Arg 2-0, Arg 1-0, Arg 3-0 | 58 | heavy fav — CV genuine minnow, likely fair |
| Jul 3 | **Colombia–Ghana** | Col **72** / Gha 28 | 53/26/20 | 1-1, Col 1-0, Col 2-0 | 46 | Ghana missing Kudus — Colombia likely fair |

### Where the next edges most likely are
1. **Belgium–Senegal** — my model has it nearly even (Bel 56/Sen 44). If the market prices Belgium
   like a comfortable favorite (≥65%), **Senegal-to-advance is the next Morocco/Paraguay-style play**
   — Senegal have the pace/power and Belgium were unconvincing in groups.
2. **Portugal–Croatia** — Croatia are battle-tested and tournament-savvy; if Portugal is overpriced,
   **Croatia-to-advance** is value (and this one is genuinely a draw-machine → goes to pens often).
3. **Australia–Egypt** — true coin-flip the market may tilt; Salah is the swing.

**Heavy favorites** (England, Spain, Argentina) are usually fairly priced — only worth a fade if the
market pushes them past ~88% (the France–Sweden trigger), which mostly opens thin underdog value.

### What I need to turn priors into bets
For each game you want sized, send the **Polymarket/Kalshi to-advance % for both teams** (and a few
exact scores). **Priority: Belgium–Senegal and Portugal–Croatia** — those are the likeliest +EV
fades. I'll run the 4-allocation menu the moment I have the numbers.
