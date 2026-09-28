# Disruptor Rubric & a Worked Numeric Example

This file hardens the prompt in two ways: (1) a concrete rubric that turns "this player is a
disruptor" into an actual expected-goals adjustment, and (2) a fully worked Poisson example so
any model produces consistent λ/μ → scoreline math.

## 1. Disruptor scoring rubric (1–10) → λ adjustment

A player's "disruptor score" answers: *how much can this individual bend a tight knockout game?*
Translate the score into an adjustment on the **team's expected goals (λ)** — or, for defensive
disruptors, on the **opponent's λ**. Apply a **knockout multiplier (×1.25)** because single games
are higher-variance than league seasons.

### Attacking disruptors (adjust own team's λ)

| Score | Archetype | Examples (this cycle) | λ adjustment* |
|---|---|---|---|
| 9–10 | Generational, beats a set defense alone | Mbappé, Messi (prime), Haaland | **+0.35 to +0.50** |
| 7–8 | Elite difference-maker | Salah, Yamal, Bellingham, Son, Vinícius | **+0.20 to +0.30** |
| 5–6 | High-quality creator/finisher, can decide a game | James Rodríguez (creator), Enner Valencia (finisher), Taremi (poacher) | **+0.10 to +0.20** |
| 3–4 | Reliable starter, system contributor | most first-choice internationals | +0.00 to +0.10 |
| 1–2 | Rotation / squad | — | 0.00 |

\* Per-match, relative to the team's base λ. These are **deltas vs. a baseline where the player
plays a normal game**, used most when toggling availability (injury/suspension) or hot/cold form.

### Defensive disruptors (subtract from opponent's λ)

| Score | Archetype | λ effect on opponent |
|---|---|---|
| 9–10 | World-class keeper or shut-down CB pairing | **−0.25 to −0.35** |
| 7–8 | Elite individual defender / keeper | **−0.15 to −0.25** |
| 5–6 | Very good organizer / anchor | −0.05 to −0.15 |

### How to apply
1. Start from the statistical/market base λ for each side.
2. Add the **single biggest attacking disruptor** delta per team (don't naively stack five
   attackers — diminishing returns; cap total attacking uplift at ~+0.5).
3. Subtract the opponent's **defensive disruptor** effect.
4. **Availability toggle:** if a 7+ disruptor is OUT (injury/suspension), remove their delta AND
   shorten the underdog's price — this is the highest-value late information.
5. Apply the knockout ×1.25 multiplier to the *net* disruptor delta, then re-derive the grid.

### The cohesion cross-check
Cohesion acts on **defense and draw-probability**, not star power. A cohesive underdog (Iran,
Morocco, Cape Verde, Japan) gets **−0.10 to −0.25 on the goals it concedes** and a **bump to draw
/ low-score probability**. This is why a cohesive team with no 8+ disruptor can still neutralize a
star-laden favorite and reach penalties.

## 2. Worked example — Mexico (1.3) vs Ecuador (1.0)

Goal: show the exact arithmetic from λ to a full output. Using base λ_MEX = 1.3, λ_ECU = 1.0
(Mexico's altitude/home edge already baked in; Ecuador's cohesion already pulling their concession
down). Poisson PMF: `P(k; λ) = e^−λ · λ^k / k!`.

**Step 1 — marginal goal probabilities**

| goals k | P(k; 1.3) MEX | P(k; 1.0) ECU |
|---|---|---|
| 0 | 0.273 | 0.368 |
| 1 | 0.354 | 0.368 |
| 2 | 0.230 | 0.184 |
| 3 | 0.100 | 0.061 |
| 4 | 0.032 | 0.015 |

**Step 2 — score grid** `P(i,j) = P(i;1.3) · P(j;1.0)` (independent Poisson; top cells shown, %):

| MEX\ECU | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 10.0 | 10.0 | 5.0 | 1.7 |
| **1** | 13.0 | 13.0 | 6.5 | 2.2 |
| **2** | 8.5 | 8.5 | 4.2 | 1.4 |
| **3** | 3.7 | 3.7 | 1.8 | 0.6 |

**Step 3 — Dixon-Coles τ nudge.** With a small positive ρ, bump 0-0 / 1-1 slightly and trim
1-0 / 0-1 a touch (the low-score correlation effect). For a tight game this lifts the draw a
couple of points.

**Step 4 — aggregate outcomes** (sum the grid):
- **Mexico win** (i > j): ≈ **44%**
- **Draw** (i = j): ≈ **28%** (→ ~30% after τ nudge)
- **Ecuador win** (i < j): ≈ **28%**
- Most likely scorelines: **1-1 (~13%)**, **1-0 MEX (~13%)**, 0-0 (~10%), 2-1 MEX (~9%)
- **Over 2.5 goals:** ≈ 38% → this is a low-scoring game (**under** favored)
- **BTTS yes:** ≈ 47%

**Step 5 — output the distribution, not "Mexico 1-0."** Report: most likely **1-1**, confidence
**Low**; Mexico narrowly more likely to advance (≈ 56% including a coin-flip-ish penalty shootout);
biggest uncertainty = whether Ecuador's block holds at altitude. *This is exactly the shape every
prediction should take.*

> Sanity check against the market: λ_MEX + λ_ECU = 2.3 implies the Over 2.5 line should be priced
> around the low-40s%. If the book has it much higher, either your λ is too low or the market sees
> goals you don't — reconcile before finalizing.
