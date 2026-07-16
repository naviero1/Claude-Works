# World Cup 2026 — Data Snapshot (as of 2026-06-27)

Hosts: USA / Canada / Mexico. Format: 48 teams, 12 groups (A–L). Advancing to Round of 32:
12 group winners + 12 runners-up + 8 best third-placed teams. **Final: July 19, MetLife
Stadium (NJ).** The **final group games conclude June 27** — including the **Group K decider
Colombia vs Portugal (Jun 27, 7:30 PM)**, which sets their R32 seeding (both likely already
through). **Round of 32 runs June 28 → July 3.**

> **Correction (v1.2):** Colombia and Portugal are in the **same group (K)** and play tonight —
> they are *not* an R32 tie. The R32 seeding below (Colombia→Croatia, Portugal→Ghana) assumes
> the expected group outcome and may swap depending on tonight's result. See the live worked
> example in [`09-live-odds-market-reference.md`](09-live-odds-market-reference.md).

## Market-implied trophy odds (the team-strength tiers)

Blended from Polymarket and Kalshi outright markets (implied probability to *win
the tournament*). These set our relative strength tiers. Note how bunched the top is — a
function of the 48-team format and comparable elite-squad depth.

| Tier | Team | ~Implied win % | Notes |
|---|---|---|---|
| 1 | **France** 🇫🇷 | 18–20% | Lone clear favorite. Perfect group, +8 GD, Mbappé firing. |
| 2 | **Spain** 🇪🇸 | ~14% | Won Group H but a flat 0-0 vs Cape Verde tempered the market. |
| 2 | **Argentina** 🇦🇷 | ~14% | Holders; surged ahead of England/Brazil on strong showings. |
| 3 | **England** 🏴 | 11–13% | 4-2 win over Croatia among results; deep squad. |
| 3 | **Portugal** 🇵🇹 | ~10% | Within striking distance. |
| 3 | **Brazil** 🇧🇷 | ~9% | Trailing the Euro elite but dangerous. |
| 4 | **Germany** 🇩🇪 | ~5% | Volatile: 7-1 vs Curaçao, then lost to Ecuador. |
| 4 | **Netherlands** 🇳🇱 | ~4% | |
| 5 | Norway 🇳🇴 | ~3% | Haaland disruptor factor. |
| 5 | Japan / Colombia / Belgium | ~2% each | |
| — | Morocco, others | lower | Morocco a live dark horse on cohesion. |

Kalshi WC-winner market volume exceeded **$577M** — deep, well-disciplined pricing.

## Notable group-stage results & narratives (prediction signals)

- **France** — won all three (combined ~10-2), beat Senegal 3-1 and Norway 4-1; Mbappé
  multi-goal. Peak momentum, top market tier.
- **Germany — the over-rating trap** — thrashed Curaçao **7-1**, then **lost 2-1 to Ecuador**.
  A naive goals-scored model overrates them; form/cohesion flags the wobble.
- **Spain** — clinched Group H with a 1-0 over Uruguay, but a **0-0 vs Cape Verde** showed
  they can be frustrated by a compact, cohesive side.
- **Cinderellas (high morale, cohesive, low expectation):** **Cape Verde** — smallest nation
  ever to reach the knockouts, first World Cup, advanced on collective discipline. **Egypt** —
  first-ever knockout berth (Salah = disruptor).
- **Attacking form spikes:** Senegal 5-0 Iraq; Sweden 5-1 Tunisia; Belgium 5-1 New Zealand;
  Japan 4-0 Tunisia.
- **USA** — won Group D, then lost 3-2 to Türkiye: fragile heading into the knockouts.
- **Iran** — organized, hard to break down; eliminated/now a third-place qualifier but a
  cohesion benchmark (drew Belgium 0-0).

## Round of 32 fixtures (all 16)

Dates/venues per FIFA scheduling sources; some slotting depends on final third-place seeding.

| # | Match | Venue | Window |
|---|---|---|---|
| 1 | South Africa vs Canada | Los Angeles | Jun 28 |
| 2 | Brazil vs Japan | Houston | Jun 29 |
| 3 | Germany vs Paraguay | Boston | Jun 29 |
| 4 | Mexico vs Ecuador | **Estadio Azteca, Mexico City (altitude)** | Jun 30 |
| 5 | Netherlands vs Morocco | Monterrey | Jun 30 |
| 6 | Côte d'Ivoire vs Norway | Dallas | Jun 30 |
| 7 | France vs Sweden | New York / New Jersey | Jun 30 |
| 8 | Belgium vs South Korea | Seattle | Jul 1 |
| 9 | USA vs Bosnia & Herzegovina | Santa Clara | Jul 1 |
| 10 | England vs Senegal | Atlanta | Jul 1 |
| 11 | Spain vs Austria | Inglewood (LA) | Jul 2 |
| 12 | Switzerland vs Iran | Vancouver | Jul 2 |
| 13 | Portugal vs Ghana | Toronto | Jul 2 |
| 14 | Australia vs Egypt | Arlington | Jul 3 |
| 15 | Argentina vs Cabo Verde | Miami Gardens | Jul 3 |
| 16 | Colombia vs Croatia | Kansas City | Jul 3 |

> Later rounds (Round of 16 onward) are not yet "known" fixtures — they resolve as the
> bracket fills. Predict them by chaining R32 winners forward, or simulate the bracket.

## Sources
- FIFA official standings — https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/standings
- Round of 32 confirmed matches (SI) — https://www.si.com/soccer/every-confirmed-round-of-32-match-2026-world-cup
- Sky Sports bracket & route to final — https://www.skysports.com/football/news/11095/13556636/world-cup-2026-bracket-and-knockout-fixtures-whos-facing-who-in-the-last-32-and-route-to-final
- Olympics.com R32 full schedule — https://www.olympics.com/en/news/fifa-world-cup-2026-bracket-round-32-full-schedule-live-updates
- Polymarket WC winner market — https://polymarket.com/event/world-cup-winner
- Kalshi WC winner market — https://kalshi.com/markets/kxmenworldcup/mens-world-cup-winner/kxmenworldcup-26
- Aggregated outright odds (Oddspedia) — https://oddspedia.com/insights/football/world-cup-2026-outright-odds
- Kalshi & Polymarket odds tracker (DeFiRate) — https://defirate.com/prediction-markets/world-cup-odds/
