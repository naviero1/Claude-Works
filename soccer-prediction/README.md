# Soccer Score Prediction — Research & Prompt Lab

A living project to build a portable, model-agnostic prompt for predicting soccer
match scorelines, grounded in the Dixon-Coles statistical tradition and extended with
betting-market signals, player-level analysis, and team-cohesion factors.

**Design philosophy:** *Stats-led, mindset adjusts.* A well-calibrated statistical /
market base is primary; qualitative signals (injuries, motivation, momentum, chemistry)
nudge it rather than drive it. The research is clear that sentiment *alone* is roughly a
coin flip — its value is as an **adjustment layer** on a sound quantitative base.

## Contents

| File | What it is |
|---|---|
| [`01-methodology.md`](01-methodology.md) | The theory: Maher → Dixon-Coles → modern extensions, plus how betting markets, players, and cohesion enter the model. |
| [`02-prediction-prompt.md`](02-prediction-prompt.md) | **The deliverable** — the curated, reusable prompt to paste into any AI model. |
| [`03-world-cup-2026-data.md`](03-world-cup-2026-data.md) | Live tournament snapshot: results, standings, market odds (as of 2026-06-27). |
| [`04-round-of-32-predictions.md`](04-round-of-32-predictions.md) | Worked predictions for all 16 Round of 32 fixtures (v1.1, player-adjusted). |
| [`05-disruptor-rubric-and-worked-example.md`](05-disruptor-rubric-and-worked-example.md) | Turns "X is a disruptor" into a ±λ number; a fully worked Poisson example. |
| [`06-bracket-simulation.md`](06-bracket-simulation.md) | Monte-Carlo method for trophy odds + a market-anchored current read. |
| [`07-predict-and-score-log.md`](07-predict-and-score-log.md) | Brier/log-loss scoring template to grade forecasts vs outcomes. |
| [`08-player-ratings.md`](08-player-ratings.md) | Disruptor leaderboard, R32 availability watch, cohesion index, per-team ratings. |
| [`09-live-odds-market-reference.md`](09-live-odds-market-reference.md) | How to read Polymarket/Kalshi, de-vig, and extract λ; worked example. |
| [`10-portfolio-2026-06-27.md`](10-portfolio-2026-06-27.md) | Per-game predicted results + bet-style suggestions for June 27; anchored where market data exists. |
| [`11-staking-allocation-2026-06-27.md`](11-staking-allocation-2026-06-27.md) | Bankroll/unit framework + concrete stake sizing across June 27 games. |
| [`12-r32-scoreline-scenarios.md`](12-r32-scoreline-scenarios.md) | Top-5 scoreline distributions for all 16 R32 games (Poisson+DC). |
| [`13-matchday-analysis-playbook.md`](13-matchday-analysis-playbook.md) | **Oscar's method, merged** — disruption scoring, archetypes, half-by-half goals, $100 allocation. |
| [`tools/fetch_odds.py`](tools/fetch_odds.py) · [`tools/match_analysis.py`](tools/match_analysis.py) | Odds connector + per-match Poisson/DC analysis (scores, halves, early goal). |

## The layered model in one picture

```
  MARKET ANCHOR        →  de-vigged Kalshi / Polymarket implied probabilities
  + STATISTICAL BASE   →  Dixon-Coles attack/defense → expected goals (λ, μ)
  + FORM & DECAY       →  recent matches weighted more (time decay ξ); signal vs noise
  + PLAYERS            →  star/disruptor availability & impact; key absences
  + COHESION           →  collective > sum of parts (settled XI, system, chemistry)
  + CONTEXT            →  home/altitude, rest, stakes, knockout pressure, H2H
  + MINDSET            →  morale, momentum, narrative, public/media sentiment
  ─────────────────────────────────────────────────────────────────────────────
  = SCORELINE DISTRIBUTION  (not a single fake-precise score)
```

## Status

- **v1.0** — initial methodology, prompt, WC2026 data snapshot, and R32 predictions.
- **v1.1** — added disruptor rubric + worked example, bracket simulation, scoring log, and a full
  player-ratings reference (real club/CL/Copa Libertadores/MLS data + EA FC cross-check);
  R32 predictions re-adjusted for player availability and cohesion.

> Predictions are model estimates for research/entertainment. Per-match betting lines
> firm up in the 48h before kickoff; always refresh them before relying on a forecast.
