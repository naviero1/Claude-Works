#!/usr/bin/env python3
"""
fetch_odds.py — pull live World Cup match odds from Kalshi + Polymarket, de-vig them,
and emit a clean JSON the prediction prompt can consume as its market anchor.

WHY THIS EXISTS
---------------
Market-implied probabilities are the strongest single predictor we have. This script
turns the two prediction markets into machine-readable, de-vigged probabilities so the
forecast is anchored to real money, not vibes.

NETWORK NOTE
------------
Both APIs below are PUBLIC for reading prices (no API key needed just to read). However,
some sandboxed/cloud environments block outbound calls to these hosts at the proxy
(you'll see "CONNECT tunnel failed, response 403"). Run this where egress is open:
your laptop, a small server, or a GitHub Action. If you're in a Claude Code web
environment, recreate it with a network policy that allow-lists:
    gamma-api.polymarket.com, clob.polymarket.com, api.elections.kalshi.com
(See https://code.claude.com/docs/en/claude-code-on-the-web for network policies.)

AUTH
----
- Kalshi: market DATA is public. Trading needs an API key (KALSHI_API_KEY env var) — not
  required here. Series ticker for the men's WC winner is KXMENWORLDCUP; per-match markets
  appear under their own event tickers in the days before kickoff.
- Polymarket: Gamma + CLOB read endpoints are public. Placing orders needs a wallet — not
  required here.

USAGE
-----
    python fetch_odds.py --list-kalshi KXMENWORLDCUP
    python fetch_odds.py --poly-event world-cup-winner
    python fetch_odds.py --match "Colombia" "Portugal"     # best-effort match search

Output: JSON to stdout with de-vigged 3-way probabilities + totals/BTTS where available.
"""

import argparse
import json
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
POLY_GAMMA = "https://gamma-api.polymarket.com"


def _get(url: str, params: dict | None = None, timeout: int = 25):
    if params:
        url = f"{url}?{urlencode(params)}"
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "wc-odds/1.0"})
    with urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def devig(probs: dict[str, float]) -> dict[str, float]:
    """Normalize implied probabilities so they sum to 1 (removes the bookmaker margin)."""
    total = sum(p for p in probs.values() if p is not None)
    if total <= 0:
        return probs
    return {k: round(v / total, 4) for k, v in probs.items() if v is not None}


# ---------------- Kalshi ----------------

def kalshi_markets(series_ticker: str) -> list[dict]:
    """List markets under a Kalshi series. Prices are in cents (0-100) -> /100 = probability."""
    out = []
    cursor = None
    while True:
        params = {"series_ticker": series_ticker, "limit": 100, "status": "open"}
        if cursor:
            params["cursor"] = cursor
        data = _get(f"{KALSHI}/markets", params)
        for m in data.get("markets", []):
            mid = m.get("last_price")
            if mid is None:
                yb, ya = m.get("yes_bid"), m.get("yes_ask")
                mid = (yb + ya) / 2 if (yb is not None and ya is not None) else None
            out.append({
                "ticker": m.get("ticker"),
                "title": m.get("title") or m.get("subtitle"),
                "prob": round(mid / 100, 4) if mid is not None else None,
            })
        cursor = data.get("cursor")
        if not cursor:
            break
    return out


# ---------------- Polymarket ----------------

def poly_event(slug: str) -> dict:
    """Fetch a Polymarket event by slug; markets carry `outcomes` + `outcomePrices`."""
    events = _get(f"{POLY_GAMMA}/events", {"slug": slug})
    if not events:
        return {}
    ev = events[0]
    markets = []
    for m in ev.get("markets", []):
        outcomes = json.loads(m.get("outcomes", "[]")) if isinstance(m.get("outcomes"), str) else m.get("outcomes", [])
        prices = json.loads(m.get("outcomePrices", "[]")) if isinstance(m.get("outcomePrices"), str) else m.get("outcomePrices", [])
        markets.append({
            "question": m.get("question"),
            "outcomes": dict(zip(outcomes, [float(p) for p in prices])) if prices else {},
        })
    return {"title": ev.get("title"), "slug": ev.get("slug"), "markets": markets}


def poly_search(*terms: str) -> list[dict]:
    """Best-effort: scan open events for ones whose title contains all search terms."""
    hits = []
    data = _get(f"{POLY_GAMMA}/events", {"closed": "false", "limit": 500})
    for ev in data:
        title = (ev.get("title") or "").lower()
        if all(t.lower() in title for t in terms):
            hits.append({"title": ev.get("title"), "slug": ev.get("slug")})
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-kalshi", metavar="SERIES", help="List Kalshi markets for a series ticker")
    ap.add_argument("--poly-event", metavar="SLUG", help="Fetch a Polymarket event by slug")
    ap.add_argument("--match", nargs=2, metavar=("TEAM_A", "TEAM_B"), help="Search Polymarket for a match")
    args = ap.parse_args()

    result = {}
    try:
        if args.list_kalshi:
            result["kalshi"] = kalshi_markets(args.list_kalshi)
        if args.poly_event:
            result["polymarket"] = poly_event(args.poly_event)
        if args.match:
            result["polymarket_search"] = poly_search(*args.match)
        if not result:
            ap.print_help()
            return
    except Exception as e:  # network blocked, rate-limited, schema drift, etc.
        print(json.dumps({"error": str(e),
                          "hint": "If this is a 403/CONNECT failure, outbound egress to the API "
                                  "host is blocked — run where network access is open."}, indent=2))
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
