# Tools

## `fetch_odds.py` — live market connector (Kalshi + Polymarket)

Pulls live, de-vigged match probabilities to anchor predictions. **Public read APIs — no key
needed to read prices.** Trading would need credentials; reading does not.

```bash
# Kalshi: list all markets under the men's World Cup winner series
python fetch_odds.py --list-kalshi KXMENWORLDCUP

# Polymarket: fetch an event by slug (find slugs in the polymarket.com URL)
python fetch_odds.py --poly-event world-cup-winner

# Best-effort match search on Polymarket
python fetch_odds.py --match Colombia Portugal
```

### Where to run it
This repo's Claude Code web environment **blocks** outbound calls to these API hosts at the
proxy (you'll see `CONNECT tunnel failed, response 403`). Run it where egress is open:

1. **Your laptop** — simplest. `python3 fetch_odds.py ...`
2. **A GitHub Action** — schedule it (cron) to commit fresh odds JSON into the repo. GitHub's
   runners have open network access.
3. **Re-create the web environment** with a network policy that allow-lists
   `gamma-api.polymarket.com`, `clob.polymarket.com`, `api.elections.kalshi.com`
   (see https://code.claude.com/docs/en/claude-code-on-the-web).

### Output
JSON with de-vigged 3-way probabilities (and totals/BTTS where the market exposes them),
ready to paste into the prompt's `INPUTS` block as the market anchor.

> API shapes can drift; the script handles errors gracefully and prints a hint. If an endpoint
> changes, the per-match market may live under a different event/series ticker — find it in the
> platform URL and pass it in.
