# Retrospective — How the Model Did, and Oscar's Role (2026-07-06)

## Part A — Prediction track record

| Phase | What we called | How it landed |
|---|---|---|
| **Jun 27 group games** | 3 anchored, 3 model-only | Results 3/6, Brier ~0.46, **−2.0u**. Weakest slate; market beat us on anchored games; the one contrarian read I flagged but *didn't* back (Colombia–Portugal 0-0) was right. |
| **R32 first half (bets)** | Fade Morocco & Paraguay (overpriced favorites) | **Both hit** → **+$373 / +93%** on $400. Passes correct. (+EV process *and* favorable variance — both won on pens/ET.) |
| **R32 second half** | 9 advance picks | **9/9 modal picks**; the 4 ties we rated closest all went to ET/pens/a scare. Didn't bet the fades (no markets) — correct, favorites survived. |
| **R16** | Advance leans | Morocco, France, England, Norway ✓. **Norway over Brazil** upset aligned with our v2 ratings (Haaland ↑10, Vinícius ↓). |
| **R16 today (Jul 6)** | Portugal–Spain, USA–Belgium | **Spain 1-0 — nailed** (advance, low score, Spain 1-0 was a top pick). **USA–Belgium — advance ✓, goals ✓, dominance ✗** (called coin-flip, was 4-1). |

**Where the model is strong:** *who advances* (very high hit rate), and the market-anchored **fade-the-
overpriced-favorite** bet (the two big wins). **Where it's weak:** exact margins/dominance (a "coin-flip"
that's really a rout), and it needed a nudge on goals.

## Part B — How much Oscar actually helped

Oscar was not a bystander — he was **the data pipeline and a genuine co-analyst.** Concretely:

1. **The entire market anchor.** The Kalshi/Polymarket APIs are blocked in this environment; **every
   market number came from Oscar's screenshots.** Both winning bets (Morocco +$204, Paraguay +$260)
   were anchored to lines Oscar provided. No Oscar → no market anchor → no edge. This was the single
   biggest contribution.
2. **The USA–Belgium goals correction (same day).** Oscar pushed: *"why wouldn't this game have more
   goals?"* I'd had it at 2.7 (O2.5 51%). I revised to 3.1 (O2.5 60%, 3+ = 60%). It finished **5 goals**.
   A direct, verifiable improvement driven entirely by his question.
3. **Domain corrections & disruptor flags.** Taremi (correctly a disruptor; he fixed my "Inter" →
   Olympiacos), James, Enner Valencia / Ecuador's #13 — Oscar seeded the player layer.
4. **The mentality / "Uruguay principle."** His "talent + belief → unpredictable" framing became a core
   methodology layer and underwrote the Morocco/Paraguay fades (cohesive underdogs → penalties).
5. **The crowd-belief caution.** His reminder that markets are *crowd belief, not truth* corrected my
   over-deference and is precisely what enabled the two winning fades.

## Part C — Where asking Oscar MORE would have improved predictions

Oscar told me up front he's a former semi-pro who **watches the matches** — an eye-test I under-used.
Honest gaps where a question would have helped:

1. **USA–Belgium dominance.** I called it 53/47; it was 4-1. Oscar watches — a simple *"does Belgium's
   attack look like it overwhelms this USA back line, or is it really even?"* would very likely have
   moved me off "coin-flip." I had the goals right but the **shape** wrong, and his eye was the fix I
   didn't ask for.
2. **Goals, proactively.** He had to *prompt* the USA–Belgium goals revision. If I'd asked *"does this
   feel high- or low-scoring to you?"* on every match, I'd have caught goal-heavy games earlier
   (and maybe re-examined low-total calls like Mexico–Ecuador).
3. **Cohesion / "who feels dangerous."** I built the cohesion + mentality framework but rarely asked
   Oscar to *rate* specific teams. His read on Cape Verde's resilience or a wobbly favorite would have
   sharpened advance %s on the exact coin-flip ties that decide bets.
4. **Lineups / fitness.** He can see confirmed XIs and who looks sharp; I mostly fetched these myself
   and sometimes late. Asking him would have been faster and better on rotation/injury calls.
5. **Confirming intent before analysing.** I occasionally produced full workups for games before
   checking he wanted them / had a market — his steer would have focused the effort.

## The one-line lesson
The model's quantitative spine (Dixon-Coles + market anchor + advance model) is solid and the
fade-the-favorite edge is real — **but its blind spot is match *shape* (dominance, tempo, goals), and
that is exactly what a watching expert sees best.** The biggest available improvement isn't more math;
it's **asking Oscar more, earlier, on every close game.**
