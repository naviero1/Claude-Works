# Live Odds — Market Reference (Polymarket · Kalshi)

How to read and use the betting markets that anchor every prediction. Built from live
Polymarket + Kalshi screenshots of the **Colombia vs Portugal** Group K decider (June 27, 2026),
which doubles as a worked example.

## What each market gives you, and how to convert it

| Market | Platform terms | Use in the model |
|---|---|---|
| **3-way moneyline** (Win/Draw/Win) | "COL / Tie / POR" | The **anchor**. De-vig → prior P(home)/P(draw)/P(away). |
| **Spread** ("win by over 1.5") | Polymarket/Kalshi "Spread" | Sanity-checks how decisive the favorite is → margin shape. |
| **Totals** (Over/Under 2.5) | "Over 2.5 goals" | Implies **total expected goals** λ_home + λ_away. |
| **Team Total** (Over 1.5 each) | "Portugal over 1.5" | Splits the total into **individual λ_home and λ_away**. |
| **BTTS** | "Both teams to score" | Cross-checks that both λ are healthy (BTTS high ⇒ neither λ tiny). |
| **First team to score** | "First Team to Score" | Confirms who the market thinks controls the game. |
| **Exact score / correct score** | "Exact Score", "1st Half Exact Score" | The market's **own scoreline distribution** — compare to your Poisson grid. |
| **Goalscorer (1+)** | Kalshi "Goalscorer" | **Validates the disruptor model** — who the market expects to score. |
| Corners / cards / novelty | "Game Props", "Mentions" (VAR, Own Goal…) | Ignore for scoreline prediction; noise/entertainment. |

**Key rule (knockouts):** Both platforms settle moneyline on **90 minutes + stoppage only — NOT
extra time or penalties** (stated explicitly in their "Important information"). So in a knockout,
the 3-way "Tie" price is the probability of a draw *after 90*, which then goes to ET/pens. Convert
to *advancement* separately (≈ split the draw ~50/50, nudged by keeper + shootout history).

### De-vigging the 3-way
Implied probabilities sum to >100% (the margin). Normalize:
```
fair_i = implied_i / (implied_home + implied_draw + implied_away)
```

### Extracting λ (expected goals) from the markets — no guessing
1. Total goals: pick the Over/Under 2.5 prob → solve for λ_total that a Poisson on the *combined*
   goals reproduces (Over 2.5 ≈ 55% ⇒ λ_total ≈ 2.8).
2. Team totals: "Team over 1.5" prob pins each side's λ (Poisson P(X≥2)). Portugal over 1.5 ≈ 51%
   ⇒ λ_POR ≈ 1.6; Colombia over 1.5 ≈ 34% ⇒ λ_COL ≈ 1.1.
3. Check they're consistent with BTTS and the 3-way. Now your scoreline grid is **market-anchored**,
   not invented.

## Worked live example — Colombia vs Portugal (Group K decider, Jun 27, 7:30 PM)

**Market snapshot (Polymarket / Kalshi agree closely):**

| Market | Polymarket | Kalshi |
|---|---|---|
| 3-way (COL / Tie / POR) | 28 / 25 / 50 | 27 / 25 / 50 (×3.40 / ×3.80 / ×1.93) |
| POR win by >1.5 | 26% | 27% |
| Over 2.5 goals | 55% | 56% |
| Team total — POR over 1.5 | 52% | 51% |
| Team total — COL over 1.5 | — | 34% |
| BTTS | 60% | 59% |
| First to score (POR / COL / none) | 58 / 37 / 7 | 58 / 36 / 8 |
| Goalscorer 1+ (Kalshi) | — | Ronaldo 42, **L. Díaz 23**, B. Fernandes 21, L. Suárez(COL) 19, **James 12**, Vitinha 11 |

**De-vigged anchor:** sum ≈ 103 ⇒ **POR ≈ 49% / Tie ≈ 24% / COL ≈ 27%** (after 90 min).

**Implied goals:** λ_POR ≈ 1.6, λ_COL ≈ 1.1 (λ_total ≈ 2.7–2.8). Portugal favored, both likely
to score (BTTS ~59%), Portugal more likely to strike first (58%).

**Layered read:**
- *Players:* Goalscorer market confirms the research — **Luis Díaz (23%) is Colombia's real threat,
  not James (12%)**; Ronaldo (42%) the most-likely scorer overall, Bruno/Vitinha the creators.
- *Mentality/context:* both sides are likely already through Group K, so this is partly a
  **seeding game** — rotation and lower intensity are real; that *widens* the distribution and
  slightly lifts the draw. No "wounded underdog" mentality edge for either side here.
- *Cohesion:* roughly even; Portugal has more individual ceiling.

**Model output (demonstration):**
- Most likely scorelines: **1-1 (~14%), 2-1 POR (~12%), 1-0 POR (~11%), 0-0 (~8%)**
- **Portugal ~2-1**, confidence **Low–Medium** (seeding-game variance)
- W/D/W (90'): POR 49 / draw 24 / COL 27 — *we defer to the market; no edge to deviate*
- Over 2.5: ~55%; BTTS: ~59% — lean over/BTTS-yes, matching the market

> This game is graded in [`07-predict-and-score-log.md`](07-predict-and-score-log.md) as the first
> live test of the method — check it after tonight's result.

## Workflow for feeding me odds
- **Screenshots:** send Polymarket/Kalshi shots; I read the 3-way + totals + team
  totals + BTTS + goalscorer and produce a fully anchored prediction.
- **What's most valuable:** the 3-way moneyline (anchor), the team totals (the λ split), and the
  goalscorer market (disruptor check). Those three pin the whole forecast.
