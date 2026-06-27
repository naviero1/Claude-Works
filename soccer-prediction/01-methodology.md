# Methodology — From Dixon-Coles to a Market-Anchored, Cohesion-Aware Predictor

## 1. The statistical lineage

### Maher (1982) — independent Poisson
A football match is two Poisson processes: home goals `X ~ Poisson(λ)`, away goals
`Y ~ Poisson(μ)`. Each team has an **attack** and **defense** strength; λ and μ are built
from the attacker's attack vs the defender's defense. Simple and surprisingly competent,
but it mis-predicts draws and low scores, and treats all past matches as equally relevant.

### Dixon & Coles (1997) — the gold standard
*"Modelling Association Football Scores and Inefficiencies in the Football Betting Market"*
(Journal of the Royal Statistical Society, Series C). Two decisive improvements over Maher:

**Expected goals from team strengths**
```
λ (home expected goals) = α_home × β_away × γ
μ (away expected goals) = α_away × β_home
```
- `α_i` = attack rating of team i, `β_i` = defense rating (higher β = leakier defense)
- `γ` = global home-advantage multiplier
- Whole league described by `2N + 2` parameters (attack+defense per team, plus γ and ρ)

**(a) The τ low-score correction (parameter ρ).** Independent Poisson under-predicts the
four lowest scorelines. τ re-weights exactly those:
```
τ(0,0) = 1 − λ·μ·ρ
τ(1,0) = 1 + μ·ρ
τ(0,1) = 1 + λ·ρ
τ(1,1) = 1 − ρ
τ(x,y) = 1            otherwise
```
This captures the real-world "cagey 0-0 / 1-0" effect that pure Poisson misses.

**(b) Time decay (parameter ξ).** Recent matches matter more. Each historical match is
weighted `φ(Δt) = exp(−ξ · Δt)`, where Δt is time since the match. Tuning ξ sets the
"half-life" of form — this is what makes the model *dynamic* rather than static.

**Full match likelihood** (what you maximize to fit ratings):
```
L = Π over matches  [ τ(x,y; λ,μ) · Poisson(x; λ) · Poisson(y; μ) ]^φ(Δt)
```

### Modern descendants (what to borrow, conceptually)
- **Bivariate Poisson** (Karlis & Ntzoufras, 2003): models goal correlation via a shared
  latent term instead of the τ patch — better on draws.
- **Bayesian hierarchical** (Baio & Blangiardo, 2010): teams "borrow strength" via priors.
  This is the formal home for *qualitative* inputs — injuries, motivation, rivalry, a club's
  "political moment" all enter as adjustments to prior attack/defense distributions.
- **State-space / dynamic models**: ratings evolve game-to-game like a Kalman filter,
  capturing form and momentum.
- **xG-based & ML**: replace raw goals with expected goals (less noisy "deserved" signal).
  Consistent research finding: ML rarely beats a well-tuned Dixon-Coles by much — the
  statistical model is a stubbornly strong baseline.

## 2. The betting-market layer — our strongest single prior

Market-implied probabilities are among the best-calibrated forecasts that exist, because
real money disciplines them. We anchor on three complementary venues:

| Venue | Type | What it gives us | Caveat |
|---|---|---|---|
| **Kalshi** | Regulated US prediction market (event contracts) | Continuous, de-vigged-ish probabilities; deep volume ($500M+ on WC winner) | Thinner on obscure single matches until days before |
| **Polymarket** | Crypto prediction market | Real-time crowd probability; fast to react to news | Same thinness on minor matches; reflects a particular trader base |
| **Bet365** | Traditional sportsbook | Sharp 1X2 / over-under / BTTS lines on every match | Prices include the **vig (overround)** — must be removed |

**De-vigging (remove the bookmaker margin).** Sportsbook odds sum to >100% implied
probability. Normalize:
```
implied_i      = 1 / decimal_odds_i
fair_prob_i    = implied_i / Σ implied_j      (so probabilities sum to 1)
```
Prediction markets (Kalshi/Polymarket) are already close to fair probabilities.

**How to blend.** Use the market as the **prior** (the number to beat), then ask: *do my
statistical + player + cohesion + mindset adjustments justify deviating from it?* If they
don't, defer to the market. A disciplined predictor moves off the market only with a reason.

- **Outright (winner) odds** → relative team-strength tiers for the whole tournament.
- **Per-match 1X2 odds** → the direct prior for a specific game.
- **Over/Under & BTTS lines** → the market's view of total goals → sanity-checks λ + μ.

## 3. The player layer — stars and disruptors

Team-strength ratings are *averages*; individual players create fat tails.

- **Disruptors / variance-raisers** — players who can win a tight game single-handedly
  (e.g. a Mbappé, Haaland, Salah). Their presence widens the favorite's scoreline upside and
  shortens "upset" odds when they're *absent*. Weight key-attacker availability heavily.
- **Defensive anchors / spine** — a world-class keeper or center-back compresses the
  opponent's λ. Losing the spine (injury/suspension) is often underpriced by naive models.
- **Set-piece specialists** — in tight knockout games, dead-ball quality is a real edge.
- **Availability check** — for each side, confirm: key attacker(s), first-choice keeper,
  defensive leader, suspensions (yellow-card accumulation in tournaments), late fitness tests.

Rule of thumb: a single elite disruptor is worth more in **knockout** football (one game,
high variance) than across a league season.

## 4. The cohesion layer — collective > sum of parts

Your core insight: some teams overperform their talent because they play as a unit, and some
underperform because they don't. This is real and often mispriced.

**Signals of high cohesion (upgrade the team):**
- Settled, repeated starting XI; players from the same domestic clubs; long-serving manager
  with a clear, drilled system.
- Defensive organization and compactness (low xG conceded despite modest individual names).
- *Examples this cycle:* **Cape Verde** (a tiny nation reaching the knockouts on collective
  discipline), **Iran** (organized, hard to break down), **Morocco** (the 2022 blueprint:
  elite team-shape beating bigger names), **Japan** (cohesive, high-pressing unit).

**Signals of low cohesion (downgrade despite talent):**
- A "collection of stars" with no settled system; new manager; disrupted preparation;
  reliance on individual moments rather than patterns of play.
- Big results against weak opponents but stumbles against organized sides (a classic
  over-rating trap — see Germany's 7-1 then loss this cycle).

**Practical encoding:** cohesion mainly adjusts **defensive solidity** (lowers the goals a
cohesive underdog concedes) and **draw/low-score probability** (cohesive underdogs drag
favorites into tight games and penalties). It rarely makes an underdog a *favorite*, but it
routinely turns a "comfortable" line into a coin-flip.

## 5. Context layer

Rest days and travel; altitude and heat (**Mexico City's Estadio Azteca ≈ 2,240 m** is a
genuine factor); fixture congestion; stakes (must-win vs dead rubber — irrelevant in pure
knockouts but huge in groups); knockout pressure and penalty-shootout history; head-to-head.

## 6. Mindset layer (the lightest-weight adjustment)

Morale, momentum, narrative, and public/media sentiment. The evidence: sentiment **alone**
is ~50% accurate (a coin flip) on 1X2, so it is never a base — only a tie-breaker between
otherwise-balanced scenarios, or a flag for an "emotionally loaded" game (host nation,
cinderella with nothing to lose, a team in crisis). An LLM's edge here is breadth of recent
context a pure stats model can't see — used carefully and labeled with low confidence.

## 6b. Mentality, belief & irreducible uncertainty — the "Uruguay principle"

The most important idea pure stats models miss: **a team can systematically overperform its
raw talent through mentality** — collective belief, defensive resilience, big-game temperament,
tactical discipline. **Uruguay is the archetype** ("garra charrúa"): outside Valverde (genuinely
elite) and Bentancur, few individual "disruptors" — Núñez is erratic — yet they can hold or draw
a far more talented Spain. That is not a fluke; it's mentality + organization compressing a
talent gap. The same DNA shows up in Croatia, Morocco, Iran, Japan, and the Greece-2004 archetype.

This has three modeling consequences:

1. **Mentality raises the underdog's floor and pulls games toward draws/penalties.** Increase
   P(draw) and the underdog's defensive solidity; favor unders. Talent + belief mixed together
   is what produces "unpredictable results."
2. **Don't over-price favorites against high-belief, well-organized sides.** A favorite that
   talent alone says is 75–80% should often be marked down toward 55–65% here. **Widen the
   distribution.**
3. **It is a source of irreducible uncertainty.** Some single games are genuinely unpredictable;
   the honest output is a *flatter* distribution (e.g., 50/30/20), not false precision. This is
   *why* we anchor to markets and report distributions — the market already prices much of this,
   and a distribution captures "the upset is live" in a way a point estimate never can.

**Detecting high-mentality sides:** a history of punching above talent in big games; strong
defensive organization and an experienced spine; "nothing to lose" or "wounded giant" narratives;
derby/rivalry intensity; proven shootout temperament. **Mentality vs cohesion:** cohesion = how
well they play together (system/chemistry); mentality = belief/resilience under pressure. They
compound, and mentality especially spikes in knockouts and shootouts.

## 7. Output discipline

Always produce a **distribution**, never a single fake-precise score:
- Final expected goals λ, μ
- Top scorelines with probabilities (a score grid)
- Win / Draw / Win split (%)
- Over/Under 2.5 and BTTS
- Single most-likely scoreline **with a confidence label**
- The upset path, and the single biggest source of uncertainty

If data is thin, **widen the distribution** rather than faking precision. Track predictions
vs outcomes and score them (Brier / log-loss) so the method improves over time.

## Sources
- Dixon, M. & Coles, S. (1997), *Modelling Association Football Scores and Inefficiencies in
  the Football Betting Market*, JRSS-C — https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/1467-9876.00065
- Dixon-Coles + time-weighting walkthrough — https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling-dixon-coles-and-time-weighting/
- Bayesian state-space EPL model (JRSS-C 2025) — https://academic.oup.com/jrsssc/article/74/3/717/7929974
- ML for soccer match prediction (survey, arXiv) — https://arxiv.org/pdf/2403.07669
- Combining ML and human experts (arXiv) — https://arxiv.org/pdf/2012.04380
- Bayesian approach to football performance (Frontiers, 2025) — https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1486928/full
