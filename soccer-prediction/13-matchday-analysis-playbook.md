# Match-Day Analysis Playbook (v2) — Oscar's method, merged

The operational prompt for analyzing a specific match. Merges Oscar's framework (disruption
scoring, $100 allocation, half-by-half goals, rivalry/animosity, physical profiles) with the
project's market-anchored Dixon-Coles system. Use it per match, ideally with a live
Kalshi/Polymarket screenshot.

> Research/analysis, not financial advice. Markets settle on 90'+stoppage. $100 is a fixed
> analysis bankroll, not a recommendation to stake real money.

---

## Inputs to gather (analyze ≥2 of the 3 outcomes' teams)

1. **Market screenshot** (Kalshi/Polymarket): 3-way + totals + team-totals + BTTS + goalscorer.
2. **Per team:**
   - **Disruptive players** + degree (rubric below); **are they playing this match?**
   - **Form (last 10):** results, goals/assists, and *which opponents* (quality-adjust).
   - **Physical/skill archetype** (ESPN: age / height / weight + skill) → e.g. "light, skillful,
     high-press attack" vs "tall, heavy, deep block". Look for **mismatches** (pace vs slow CBs,
     aerial threat vs small backline, legs vs an old midfield).
   - **Cohesion** (settled XI, same-club spine, drilled system) and **experience** (knockout/
     tournament pedigree).
3. **Matchup context:** cultural **rivalry/animosity** (→ volatility, cards, upsets), **past
   upsets** (does the underdog have form of beating this caliber?), head-to-head.
4. **Ask Oscar** (former player, watches the games) for what the data can't show: who *looks*
   sharp, fitness eye-test, tactical setup, the vibe. Ask explicitly when his read would change
   the call.

## Disruption scoring (weighted, H2H-aware)

Rate each likely starter's **disruption degree (1–10)** — capacity to swing a tight game.
Calibration examples (Oscar's scale):
- **10:** Messi, Mbappé · **8–9:** Kane, Bellingham, Musiala, Kimmich, Yamal, Haaland, L. Díaz,
  Vinícius · **6–7 ("relatively"):** Cherki, Pulisic, James Rodríguez, Mac Allister, Enzo,
  Lautaro (older), · grade down for age/role.

Then weight it:
1. **Availability gate** — not playing → 0. (Rotation/injury/suspension.)
2. **Form multiplier** — last-10 output, quality-adjusted for opponents faced.
3. **H2H neutralization** — what matters is the *net* disruption that survives the matchup: your
   attackers vs their ability to stop them, and vice-versa. Compute **team A net − team B net**;
   that difference is the edge, not the raw star count.
4. Convert the net edge into a **±λ adjustment** (see [`05-disruptor-rubric-and-worked-example.md`](05-disruptor-rubric-and-worked-example.md)).

## Goals model (with halves)

- λ_home, λ_away from team strength + the market totals (reconcile to Over/Under and team-totals).
- **Half split:** 1H ≈ **45%** of total goals, 2H ≈ **55%** (2nd halves score more — fatigue,
  chasing, subs). Report expected goals per half.
- **Early goal:** P(≥1 goal in first ~15 min) = 1 − e^(−(λ_h+λ_a)·15/90).
- **"Lots of goals?"** = Over 2.5 / Over 3.5 probabilities.
- Compute with `tools/match_analysis.py` for consistency.

## Volatility & experience modifiers
- **Rivalry/animosity** → widen the distribution, expect more cards and a higher upset chance.
- **Experience gap** → in tight/knockout games, nudge toward the more battle-tested side.
- **Past upsets** → if the underdog has recent form beating this tier, lift their tail.

---

## OUTPUT (exactly these three sections)

**1) Platform probabilities vs my prediction.** De-vigged Kalshi/Polymarket 3-way (+ totals/BTTS)
side-by-side with my model's numbers, after the analysis above. State the **single reason** for any
divergence (disruption edge, cohesion, archetype mismatch, rivalry, market bias). Remember the
market is *crowd belief* — name why it's wrong before deviating.

**2) Score predictions.** At least **2 likely scorelines with probabilities**, who wins, plus:
**early goal?** (first-15 prob), **lots of goals?** (O2.5/O3.5), and **goals by 1st / 2nd half**.

**3) $100 allocation strategy.** Diversified across outcomes/props, hunting **bargain bets**
(where my prob > de-vigged market prob = +EV). Provide two styles and pick one:
- **Value-max (Kelly):** concentrate on the biggest +EV edges; stake ∝ edge / (odds−1), ¼-Kelly.
- **Probability-of-profit-max (spread/Dutch):** distribute across the 2–3 most likely results so
  more scenarios return > $100 (higher chance of *some* profit, lower EV).
- Show a table: outcome · my % · market % · edge · $ allocated · payout if it hits · and the
  portfolio's **P(profit)** and **expected return**. Cap any single outcome sensibly; note the
  scenarios where the $100 loses.

---

## Worked allocation mechanics (template)

For each candidate bet at market price `m` (decimal odds `o = 1/m`), with my probability `p`:
```
edge   = p − m
EV($1) = p·(o−1) − (1−p)         # positive ⇒ bargain bet
Kelly f = edge / (o − 1)         # use 0.25·f, skip if edge ≤ 0
```
Example (illustrative — anchor to the live market): if my model says **draw 30%** but the market
prices the draw at **24%** (`o≈4.17`), edge = +6%, ¼-Kelly ≈ 0.25·(0.06/3.17) ≈ 0.47% of bankroll
→ on $100, ~$2.4 on the draw as the bargain leg; spread the rest across the favored result(s) to
lift P(profit).

## Collaboration note
Oscar is a former player who watches the matches. Treat his eye-test (sharpness, fitness, tactical
shape, "who looks off") as a **first-class input** — a strong prior on the qualitative layers that
can override lagging stats. Ask him directly whenever his read would move the allocation.
