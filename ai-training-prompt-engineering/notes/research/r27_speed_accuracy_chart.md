# r27 — Model speed vs. capability chart data (retrieved 2026-09-13)

Powers the Field Guide Part 7 chart "how fast vs. how capable — the major models
and their versions" (owner request, Round 15). [REFRESH QUARTERLY — model names
and numbers churn.]

## Source & methodology

All numbers transcribed 2026-09-13 from the Artificial Analysis model leaderboard
(https://artificialanalysis.ai/leaderboards/models). Three independent fetches;
overlapping rows agreed across fetches (Fable 5.1 high 51/56, Opus 5 max 51/53,
GPT-6 Astra medium 50/50 — consistent).

- **Capability axis** = Artificial Analysis **Intelligence Index v4.3** — a
  composite of 10 evaluations (AA-Briefcase, GDPval-AA v2, AutomationBench-AA,
  Terminal-Bench v4.0, SciCode, Humanity's Last Exam, GDP.pdf, CritPt,
  AA-Omniscience, AA-LCR v1.1). It is a benchmark composite, NOT accuracy on any
  specific workplace task — label honestly.
- **Speed axis** = median API output speed, tokens/second, as measured by AA.
- Each model is plotted at its **strongest reasoning setting** listed (max/xhigh/
  high per row below); "(Non-reasoning)" variants exist for many and are faster
  and weaker — noted, not plotted.
- The page shows no explicit "last updated" date; the retrieval date is the stamp.

## Plotted points (intelligence, speed t/s — the AA row used)

### Anthropic
- Claude Fable 5.1 — 53, 67 (row: "max with fallback")
- Claude Opus 5 — 51, 53 (max)
- Claude Sonnet 5 — 38, 76 (max)
- Claude Haiku 4.5 — 18, 88 (row: "Claude 4.5 Haiku (reasoning)")

### OpenAI
- GPT-6 Astra — 53, 60 (max)
- GPT-5.6 Sol — 47, 58 (max)
- GPT-5.6 Terra — 42, 108 (max)
- GPT-5.6 Luna — 38, 120 (max)
- GPT-5.5 Instant — 27, 132 (row: "GPT-5.5 Instant (June 2026)")
- o3 — 20, 140 (the 2025 reasoning generation, for the version arc)

### Google
- Gemini 3.8 Flash — 41, 277 (high)
- Gemini 3.7 Flash — 40, 311 (medium; high = 39/288)
- Gemini 3.6 Flash — 34, 207
- Gemini 3.1 Pro — 30, 115 (row: "Gemini 3.1 Pro Preview")
- Gemini 3.5 Flash-Lite — 23, 365

### xAI
- Grok 4.6 — 44, 58 (high; xhigh = 44/60)
- Grok 4.5 — 39, 56 (high)
- Grok 4.3 — 25, 118 (medium)

### Open weights (self-hostable)
- GLM-5.3 (Z.ai) — 45, 66 (max)
- Kimi K3 (Moonshot) — 44, 37 (max)
- DeepSeek V4.1 Flash — 40, 210 (max)
- DeepSeek V4 Pro — 36, 76 (row: "V4 Pro 0813 (max)")
- Qwen3.8 Max (Alibaba) — 40, 40

## Deliberately NOT plotted
- Gemini "Deep Think" / Ultra — consumer-app mode, not API-benchmarked on AA;
  no Gemini Pro rows beyond 3.1 Pro Preview exist on the leaderboard (verified
  by direct question against the page).
- Meta "Muse Spark 1.3" (AA: 48, 239) and Llama rows — Meta is not in the
  course's assistant landscape (r12) and no second source in the repo
  corroborates the Muse line; excluded rather than half-verified.
- Speed-specialist hosts (Celeris-1 1,342 t/s; Mercury 2 832 t/s) — serving
  demos, not the assistants trainees will meet.
- Effort sub-variants (medium/low/Non-reasoning rows) — one point per model
  version keeps the chart readable; the low-effort points sit faster & weaker.

## Consumer-app vs API seam (say in the caption)
The chart measures API-served models. The consumer apps on the trading-cards
slide (r12, Sep 9 2026) may run different siblings: ChatGPT ships the GPT-5.6
family (Sol/Terra/Luna) while GPT-6 Astra is the API frontier; the Gemini app
runs 3 / 3.1 Pro / 3.6 Flash while the API line reaches 3.8. Both true — the
caption carries "API-measured; the app in your pocket may run an older sibling."

## Ripple applied
Field Guide Part 7 spectrum-table DeepSeek cell updated from "V3 line / R1
line" (r12-era) to the current V4 Pro (reasoning) / V4.1 Flash (fast) pair —
the R1 story stays historical on the Part 2 DeepSeek-moment slide.

## UNVERIFIED / handle with care
AA has no visible dataset date (retrieval date used) · "SpaceXAI" is AA's
creator label for Grok (consistent with the Feb-2026 SpaceX acquisition, r13) ·
Intelligence Index weights are AA's own — treat rankings within ±2 points as
ties · Fable 5.1 rows carry "(with fallback)" in AA's naming — plotted as the
flagship line.
