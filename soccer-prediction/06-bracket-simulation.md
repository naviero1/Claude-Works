# Bracket Simulation — From R32 to the Trophy

A single chained "predict each winner" path is fragile: one upset breaks the whole chain.
The right tool for **tournament** odds is **Monte Carlo simulation** — play the bracket
thousands of times, each match resolved by its probability model, and count how often each
team lifts the cup. This file gives the method and a market-anchored set of trophy odds.

## Method (reproducible)

```
INPUTS
- Bracket tree (R32 → R16 → QF → SF → Final), from the official source.
- A match model: function(teamA, teamB, venue) → P(A win in 90), P(draw), P(B win),
  built from the layered model (market anchor + Dixon-Coles λ/μ + players + cohesion).
- For knockouts, convert draws to an advancement probability via a penalty model
  (≈ 50/50, nudged by keeper quality + shootout history + cohesion/nerve).

ALGORITHM  (N = 10,000+ sims)
for each simulation:
    bracket = copy(initial_bracket)
    for each round R32 → Final:
        for each tie in round:
            p = match_model(tie.home, tie.away, tie.venue)
            winner = sample_advancer(p)          # includes ET/pens for draws
            advance(winner)
    record(champion, finalists, semifinalists)
aggregate:
    trophy_prob[team]   = count(champion == team) / N
    finalist_prob[team] = count(team in finalists) / N
    ...

CALIBRATE
- The simulated trophy probabilities should broadly match the de-vigged outright market.
- If they diverge a lot, your per-match model is over/under-confident — adjust and re-run.
- This is the key discipline: the market is the truth-check on the whole simulation.
```

### Doing it inside an LLM (no code)
Ask the model to: (1) estimate each tie's advancement probability with the prompt, (2)
multiply probabilities along each team's path to the final, (3) report path-to-title odds.
This is an analytic approximation of the Monte Carlo and is good enough for a quick read; a
real script (Python + NumPy) is better for the full distribution and for correlation effects.

## Market-anchored trophy odds (current read)

Blended outright market (de-vigged) is the anchor; the "model lean" column is where the
layered analysis nudges it (players in form, cohesion, draw difficulty, bracket path).

| Team | Market trophy % | Model lean | Rationale |
|---|---|---|---|
| 🇫🇷 France | 18–20% | **↑ ~21%** | Mbappé + Dembélé both red-hot; deepest attack; soft-ish R32 (Sweden missing CB Hien). |
| 🇪🇸 Spain | ~14% | **→ 14%** | Elite control, but Yamal minutes-managed and a flat 0-0 vs Cape Verde shows they can be parked-bus'd. |
| 🇦🇷 Argentina | ~14% | **→ 14%** | Holders, Messi + cohesion; very soft R32 (Cape Verde). Path opens up nicely. |
| 🏴 England | 11–13% | **↓ ~11%** | Talented but Senegal R32 is the round's toughest "favorite" draw. |
| 🇵🇹 Portugal | ~10% | **↑ ~11%** | Bruno Fernandes + Vitinha; easiest marquee R32 (Ghana). |
| 🇧🇷 Brazil | ~9% | **→ 9%** | Dangerous, but Japan R32 is a genuine banana skin. |
| 🇩🇪 Germany | ~5% | **↓ ~4%** | Lost Schlotterbeck (out, torn ankle ligs); volatile (7-1 then lost to Ecuador). |
| 🇳🇱 Netherlands | ~4% | **↓ ~3.5%** | Both first-choice CBs (Timber, de Ligt) out, drawn into Morocco coin-flip immediately. |
| 🇳🇴 Norway | ~3% | **↑ ~3.5%** | Haaland (4 goals in 2 games) is a 10/10 disruptor; can drag anyone to a 1-0. |
| 🇧🇪 Belgium | ~2% | **→ 2%** | Courtois + De Bruyne + Doku, but inconsistent group and a tricky Korea draw. |
| 🇨🇴 Colombia · 🇯🇵 Japan · 🇲🇦 Morocco | ~2% each | **↑ Morocco** | Morocco the live dark horse on 2022-style cohesion. |
| Field (others) | remainder | — | Mexico (altitude home run), Croatia (vet savvy), Senegal (pace) as outside shouts. |

> These are reconciled estimates as of 2026-06-27; re-run after each round with refreshed
> markets and time-decayed team strengths.

## The two halves & potential blockbusters
Build the bracket tree from the official source, then watch for the marquee collision points:
- A **France vs Spain** or **France vs England** semifinal is the market's most likely
  "final before the final."
- **Argentina's** quarter looks the softest on paper — flag whether the model agrees or the
  market is underrating someone in their path.

When the R16 is set, regenerate this table from a fresh simulation rather than editing by hand.
