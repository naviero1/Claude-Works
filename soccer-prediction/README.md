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
| [`04-round-of-32-predictions.md`](04-round-of-32-predictions.md) | Worked predictions for all 16 Round of 32 fixtures using the methodology. |

## The layered model in one picture

```
  MARKET ANCHOR        →  de-vigged Kalshi / Polymarket / Bet365 implied probabilities
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

> Predictions are model estimates for research/entertainment. Per-match betting lines
> firm up in the 48h before kickoff; always refresh them before relying on a forecast.
