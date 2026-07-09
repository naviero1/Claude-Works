# Oura Trends — Analysis (Mar 21 – Jul 9, 2026, 111 days)

Source: `oura_trends_2026-03-21_2026-07-09.csv` (shared by Oscar 2026-07-09).
Note: data predates the Oura Ring 5 delivered 6/29 — an older Oura was already
in use, so we have a ~3.5-month baseline.

## Headline numbers (period averages)

| Metric | Avg | Read |
|---|---|---|
| Sleep score | 78 | fair — held back by duration |
| **Total sleep** | **6.6 h/night** | consistently short |
| Readiness score | 80 | good |
| Activity score | 93 | excellent |
| Steps | 10,143/day | excellent (47 days >10k) |
| Avg resting HR | 49 bpm | excellent |
| Lowest resting HR | 44 bpm | excellent |
| Avg HRV | 61 ms | good |
| Respiratory rate | 14.1 | normal |
| Total burn | ~2,974 kcal/day | very active |

## The one big problem: sleep duration

- 66 of 109 nights (**60%**) under 7 hours; 32 nights (**29%**) under 6 hours.
- 33 bedtimes after midnight; typical wake ~6:30–7:00 AM regardless of bedtime,
  so late nights come straight out of sleep.
- Sleep efficiency and deep-sleep scores are mostly strong — the *quality* is
  fine; the *quantity* is the constraint.

## Monthly trend

| Month | Sleep | Readiness | Activity | HRV | RHR | Steps | Sleep h |
|---|---|---|---|---|---|---|---|
| Mar | 78.5 | 81.7 | 87.5 | 61 | 48.7 | 8,996 | 6.66 |
| Apr | 76.3 | 80.9 | 91.7 | 65 | 48.4 | 9,924 | 6.55 |
| May | 77.9 | 77.7 | 94.6 | 59 | 50.0 | 11,747 | 6.59 |
| Jun | 79.7 | 81.4 | 94.3 | 58 | 49.3 | 9,887 | 6.64 |
| Jul (partial) | 77.9 | 74.1 | 89.4 | 61 | 50.9 | 7,610 | 6.42 |

- May: activity peaked (11.7k steps) but readiness dipped and RHR rose — signs of
  pushing volume on short sleep.
- HRV drifted down Apr→Jun (65→58) — worth watching as activity stays high.

## Notable events

- **Jul 6: readiness 38** (period low) with temperature deviation **+1.63 °C**,
  RHR 60.5 (vs ~49 norm), respiratory rate 16 (vs 14) — classic illness (or heavy
  holiday-weekend) signature after July 4th. Jul 4–5 have big non-wear gaps.
  Recovery visible by Jul 8 (readiness 90).
- Other low-readiness days: 5/28, 5/6–5/7, 6/11 — several align with <6 h nights.

## Cross-signal with food data (early hypotheses to test)

- Weekday lunch delivery (11–12 PM) + high activity + short sleep is the pattern.
- Fast-food dinners at home (e.g. McDonald's 8:26 PM on 6/26) precede some of the
  weaker sleep nights — sample too small to conclude; keep logging.
