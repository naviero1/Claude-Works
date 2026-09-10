# r23 — Currency checks: letter-counting, Grok modes, hallucination chart (researched 2026-09-10)

Powers three Round-6 holds (PENDING_CHANGES): the S7 tokens-claim reframe, the S12 Grok
row, and the S13 hallucination chart. R7 discipline: sources + dates; UNVERIFIED
quarantined at the end.

## 1. "Letter counting and character-exact edits fail" — PARTLY OUTDATED as stated

Verdict: the MECHANISM (tokens, not letters) is still correct and still causes real
failures — but the famous single-word examples are effectively fixed on current
frontier models. The S7 bold bullet overclaims; the speaker note ("memorized — don't
run it live") was already right.

- "Strawberry" is answered correctly by current frontier models (GPT-5.5, Grok 4.3,
  Gemini 3.5 Flash, Claude — opper.ai AI-roundtable page, retrieved 2026-09-10,
  page undated; systematic 100-trial test already near-perfect Aug 2025:
  minimaxir.com/2025/08/llm-blueberry, 2025-08-12).
- The fix is partly memorization/routing, NOT letter-vision — the BLUEBERRY incident:
  days after GPT-5 launch (2025-08-07), the free tier's non-reasoning router path
  confidently insisted "blueberry" has 3 b's (it has 2) and argued with correctors;
  reasoning paths passed (minimaxir 2025-08-12; thejournal.ie Aug 2025;
  distractify.com Aug 2025).
- What STILL fails (2025–26 evidence, fast-tier vs reasoning-tier split matters):
  · Character position/index inside words — CharBench (1M+ questions): average
    accuracy 43.6%; positional tasks as low as 32.3%; best model (GPT-4o) ~64% on
    find-first-occurrence; degrades with token length. NO reasoning models tested —
    evidence for fast tiers (arXiv:2508.02591, 2025-08-04, rev. 2026-04-06).
  · Character insert/delete/extract within tokens — still hard, high cross-model
    variance (arXiv:2506.10641, 2025-06).
  · Counting a letter across long words/paragraphs — errors scale with length and
    occurrence count (arXiv:2412.18626, 2024-12; journal ACM TIST 2026,
    dl.acm.org/doi/10.1145/3818606). Reasoning modes usually pass by spelling out —
    a token-burning WORKAROUND, not letter-vision.
  · Exact word counts (produce exactly N words / count a passage) — still documented
    2025–26 on all tiers (community.openai.com 2025 thread; CAPEL arXiv:2508.13805,
    2025-08; OuLiBench, CLiC-it 2025; pbjmarketing.com retrieved 2026-09-10).
  · "How many tokens is this text" — fails on ALL tiers incl. reasoning (no runtime
    tokenizer access): near-zero correlation predicting own token lengths
    (arXiv:2502.06258, 2025-02). The safest "still fails" claim on the list.
- Live-safe demo: THE TOKENIZER WEBPAGE (it shows the bricks; it can't "get it
  right"). Primary: platform.openai.com/tokenizer (live 2026-09-10; blocks bots,
  loads in a browser — PRELOAD IT). Backups: tiktokenizer.vercel.app (HTTP 200
  2026-09-10), gpt-tokenizer.dev. Near-safe live model variant: ask "how many tokens
  is this paragraph?" then reveal the true count on the tokenizer page — fails on
  every tier, reveal is on-message. Do NOT run strawberry (memorized) or blueberry
  (now famous) live.
- Slide reframe (R15-compliant): "letter-counting on famous words is now memorized —
  but character-position edits, paragraph-scale counts, exact word counts, and
  'count your own tokens' still fail, especially on fast/free tiers; reasoning modes
  fix some of it by spelling words out (premium, and a workaround — it reads bricks
  either way)."

## 2. Grok mode names — Sep 2026 (r18-format row)

Grok (grok.com / X app) — mode picker: **Auto · Fast · Expert · Heavy**. "Heavy"
(multi-agent) requires SuperGrok Heavy. The Grok-3-era buttons — Think, Big Brain,
DeepSearch, DeeperSearch, Fun Mode — are RETIRED (doc/mode-payload audit found zero
occurrences, prompt-architects.com 2026-08-27). Real-time X data is not a separate
mode — integrated into search/answering. Tiers: Free (rate-limited) · SuperGrok Lite
$10/mo · SuperGrok $30/mo · SuperGrok Heavy $300/mo · X Premium $8 / Premium+ $40
bundles; Jun-2026 restructure = one weekly usage pool on paid plans. Flagship:
Grok 4.6 (2026-08-12; 4.5 2026-07-08; timeline via Wikipedia retrieved 2026-09-10;
pricing cloudzero.com 2026-09-01 + suprmind.ai 2026-08-05 agree on $0/$30/$300).
⚠ x.ai/grok.com block automated fetch — NOTHING here is first-party; re-confirm in
the live app before training day. [REFRESH QUARTERLY]
Slide row (compressed): "Auto · Fast · Expert · Heavy (multi-agent, $300 tier) —
old Think/DeepSearch buttons retired".

## 3. Hallucination chart for S13 — RECOMMENDED: abstain-vs-guess (Option B)

- OPTION B (recommended): OpenAI "Why Language Models Hallucinate" (arXiv:2509.04664,
  2025-09-04; corroborated via GPT-5 System Card arXiv:2601.03267) — SimpleQA:
  · o4-mini (older reasoning model): abstains 1% · correct 24% · WRONG 75%
  · gpt-5-thinking-mini: abstains 52% · correct 22% · wrong 26%
  Metric in one sentence: "same simple factual questions — what fraction of answers
  were right, wrong, or 'I don't know'." Punchline: near-identical accuracy, ~3×
  fewer false statements when trained to say "I don't know". Caveat ON SLIDE:
  OpenAI's own research on its own two models, one benchmark — teaches the
  MECHANISM, not a market ranking. (Perfect fit: it illustrates "the confident
  guess" character directly and can't be misread as vendor comparison.)
- OPTION A (only if a many-logos chart is demanded): Vectara HHEM leaderboard
  (github.com/vectara/hallucination-leaderboard, as of 2026-05-11; methodology
  vectara.com blog 2025-11-19): grounded-summarization hallucination rates, e.g.
  Gemini 2.5 Flash-Lite 3.3% · GPT-5.4-nano 3.1% · GPT-5.4 7.0% · Gemini 2.5 Pro
  7.0% · Claude Haiku 4.5 9.8% · Claude Sonnet 4.5 12.0% · Gemini 3 Pro 13.6% ·
  Grok variants 5.8–20.2%. MANDATORY caveats: summarization grounding only, not
  general truthfulness; reasoning-tier models sometimes score WORSE — not a
  smartness ranking. REJECT circulating "GPT-5 Pro ~1.0% / Claude Opus 4.7 ~1.2%"
  figures (aggregator claims, irreconcilable with the leaderboard).

## UNVERIFIED — never present as fact

- Copilot's strawberry-class behavior (no dedicated 2026 test; "runs GPT-5.x so
  mirrors ChatGPT" is inference).
- Current free-tier ChatGPT on NOVEL blueberry-class words (Aug-2025 failure
  documented; Sep-2026 status untested).
- Opper roundtable run date (page undated).
- Grok default mode Fast vs Auto (sources conflict) · Expert on free tier or not
  (sources conflict) · SuperGrok Lite $10 (aggregators only) · which model each
  tier/mode routes to (xAI publishes no mapping). Check the live app.
- Vectara "Feb 2026 dataset overhaul" date (use the 2025-11-19 blog date).
- openai.com / platform.openai.com contents (403 to bots) — verified via arXiv/
  system card/secondaries; eyeball the tokenizer page in a browser pre-training.
