# Predict-and-Score Log

The discipline that makes a predictor trustworthy: record every forecast *before* kickoff and
grade it *after*. Two proper scoring rules, both "lower is better":

- **Brier score** (for the W/D/L probabilities): `mean over outcomes of (p − actual)²`, where
  actual = 1 for the result that happened, 0 otherwise. Range 0 (perfect) to 2 (worst).
- **Log-loss**: `−ln(p_assigned_to_actual_outcome)`. Punishes confident wrong calls harshly.
  Useful for catching over-confidence.

Also track a simple **exact-scoreline hit rate** and **result hit rate** (did we call W/D/L),
but treat the probabilistic scores as the real measure — calling "France to win" right tells
you little; assigning it a *well-calibrated probability* is the skill.

## How to log (per match)
1. Before kickoff, paste the prompt output and record: predicted scoreline, P(home)/P(draw)/
   P(away), Over 2.5 %, BTTS %, confidence, and the **market line you anchored to**.
2. After the match, fill actual result, then compute Brier + log-loss for the W/D/L vector.
3. Note *why* a miss happened (red card, keeper worldie, lineup surprise) — that's the
   feedback that improves the next round.

## Round of 32 log

| Match | Predicted | P(H/D/A) % | Market P(H/D/A) % | Actual | Result ✓/✗ | Score ✓/✗ | Brier | Note |
|---|---|---|---|---|---|---|---|---|
| South Africa–Canada | 1–2 | 23/27/50 | — | | | | | |
| Brazil–Japan | 2–1 | 55/24/21 | — | | | | | |
| Germany–Paraguay | 2–1 | 58/26/16 | — | | | | | Paraguay missing suspended Diego Gómez |
| Mexico–Ecuador | 1–1 (MEX pens) | 44/30/26 | — | | | | | Altitude (Azteca) |
| Netherlands–Morocco | 1–1 | 41/29/30 | — | | | | | NED missing both 1st-choice CBs |
| Côte d'Ivoire–Norway | 1–2 | 22/26/52 | — | | | | | Haaland 4 goals in 2 games |
| France–Sweden | 3–1 | 68/20/12 | — | | | | | Sweden missing CB Hien |
| Belgium–South Korea | 2–1 | 55/25/20 | — | | | | | |
| USA–Bosnia | 2–1 | 50/27/23 | — | | | | | |
| England–Senegal | 2–1 | 55/25/20 | — | | | | | Toughest "favorite" draw |
| Spain–Austria | 2–0 | 70/20/10 | — | | | | | |
| Switzerland–Iran | 1–0 | 48/30/22 | — | | | | | Lowest-scoring; pens live |
| Portugal–Ghana | 3–1 | 68/20/12 | — | | | | | |
| Australia–Egypt | 1–2 | 30/30/40 | — | | | | | Coin-flip; Salah factor |
| Argentina–Cabo Verde | 2–0 | 80/14/6 | — | | | | | |
| Colombia–Croatia | 2–1 | 48/28/24 | — | | | | | James vs aging Croatia core |

**Fill the Market P(H/D/A) column from de-vigged Polymarket/Kalshi lines in the 48h
before each game** — comparing our number to the market is half the value of the log.

## June 27 group-stage portfolio (final matchday)

Predictions from [`10-portfolio-2026-06-27.md`](10-portfolio-2026-06-27.md). Only Colombia–Portugal
is market-anchored; others are model estimates.

| Match | Predicted | P(H/D/A) % | Market P(H/D/A) % | Actual | Result ✓/✗ | Score ✓/✗ | Note |
|---|---|---|---|---|---|---|---|
| Panama–England | 0–3 | 7/13/80 | — | **0–2** | ✓ | ✗ | ENG win ✓, margin off · Brier .06 |
| Croatia–Ghana | 1–0 (CRO) | 49/30/21 | 51/30/19 🔒 | **2–1** | ✓ | ✗ | CRO win ✓; **Under 2.5 LOST** (3 g) · Brier .39 (mkt .37) |
| Colombia–Portugal | 1–2 (POR) | 27/24/49 | 27/24/49 🔒 | **0–0** | ✗ | ✗ | Draw; **Over+BTTS LOST**; cagey seeding game · Brier .89 |
| DR Congo–Uzbekistan | 1–1 | 37/30/33 | — | **3–1** | ✗ | ✗ | DRC win; passed (0u) · Brier .60 |
| Algeria–Austria | 1–2 (AUT) | 32/28/40 | — | **3–3** | ✗ | ✗ | Wild draw; passed (0u) · Brier .78 |
| Jordan–Argentina | 0–2 (ARG) | 5/11/84 | 5/11/85 🔒 | **1–3** | ✓ | ✗ | ARG win ✓; Messi started+scored → trigger correctly stood down · Brier .04 |

**June 27 grade:** results **3/6** correct (England, Croatia, Argentina ✓; Colombia–Portugal, DRC,
Algeria–Austria ✗), exact scores **0/6**, mean Brier ≈ **0.46**. On all three market-anchored games
the market beat us *narrowly*. **Staked P&L: −2.0u** — both active bets lost (Croatia–Ghana Under;
Colombia–Portugal Over/BTTS). The Jordan–Argentina trigger **correctly stood down** (Messi started),
and the three passes avoided further losses. Lesson: the Colombia–Portugal **0-0** is the one I
*flagged but didn't back* — I noted the cagey/rotation seeding-game scenario and an Under hedge, then
sided with the market's Over. The contrarian read was right; I didn't trust it.

## After the round
- Compute mean Brier and mean log-loss across the 16 games; that's your round score.
- Compare to two baselines: (a) always predict the market favorite, (b) the raw market
  probabilities. **Beating the raw market is the real bar** — it's hard, and most rounds you
  won't, which is itself useful calibration.
- Update team attack/defense strengths with the new results (time-decay weight them), refresh
  the markets, and regenerate Round-of-16 predictions + a new bracket simulation.

## Running tally
| Round | Mean Brier | Mean log-loss | Result hit | Exact score hit | Beat market? |
|---|---|---|---|---|---|
| R32 | | | | | |
| R16 | | | | | |
| QF | | | | | |
| SF+ | | | | | |
