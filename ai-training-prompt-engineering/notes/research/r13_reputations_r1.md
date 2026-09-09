# r13 — Assistant reputations ("known for") & the R1-vs-o1 numbers (researched 2026-09-09)

Powers the v1.5 "known for" layer on the assistants slide and the DeepSeek-moment
comparison chart. Every fact dated with a source URL; UNVERIFIED items at the bottom.

## "Known for" — verified per assistant

### ChatGPT (the owner's "writes better than Claude" — REFUTED as a blanket claim)
- LMArena Creative Writing category, June 2026 snapshot: Anthropic's
  claude-opus-4-6-thinking #1 at 1497 Elo (5,500+ votes); Anthropic holds six of the top
  ten; only non-Anthropic/non-Google entrant in the top ten is grok-4.20-beta1 (1462)
  (https://officechai.com/learn/these-are-the-best-ai-models-for-creative-writing-june-2026/).
- EQ-Bench Creative Writing v3, Aug 2026: Claude Opus 5 #1 (2105), Kimi K3 #2 (2060),
  GPT-5.6 Sol #3 (1959) (https://eqbench.com/creative_writing.html). Caveat: judge is
  Claude Sonnet 4.6 since Mar 2026 (same-family bias risk) — pair with the human-vote
  LMArena result, which agrees.
- Blind fiction testing of GPT-5.6 tiers found writing was not the 5.6 release's headline
  gain (https://usenoren.ai/blog/gpt-5-6-writing-test); practitioner comparisons: Claude =
  more natural long-form needing less editing; ChatGPT = faster drafts, options, short
  marketing copy.
- Defensible card line: "The everything assistant — fastest at drafts, options and
  marketing copy; largest user base." Do NOT print "writes better than Claude."

### Claude
- SWE-bench Verified, Sept 2026: Claude Opus 5 96.0% (Anthropic launch figure), Claude
  models fill the top slots; benchmark near saturation
  (https://www.morphllm.com/claude-benchmarks; https://benchlm.ai/benchmarks/sweVerified).
- Real work: OpenAI's own GDPval (2025-09-25) found Claude Opus 4.1 best on 220 real
  knowledge-work tasks, ≥ human experts 47.6% of the time, beating GPT-5
  (https://openai.com/index/gdpval/); GDPval-AA v2 (Artificial Analysis, Sept 2026):
  Claude Opus 5 leads at 1862 Elo.
- Long documents: 1M-token context GA since 2026-03-13; default on Sonnet 5 (2026-06-30).
- Cowork-vs-Copilot: NO head-to-head benchmark exists. The better verified fact:
  **Microsoft's Copilot Cowork (launched 2026-03-09) licenses Anthropic's Claude Cowork
  agent technology** (GeekWire, Mar 2026; TechCrunch 2026-07-07). Say that, not "slightly
  better."

### Gemini
- 1B+ monthly active users in 2026 — Google's fastest-growing product
  (https://blog.google/innovation-and-ai/products/gemini-app/one-billion-monthly-users/).
- Default AI across Workspace since Mar 2026 (Gmail/Docs/Calendar/Meet context); native
  multimodal + the viral Nano Banana image line.

### Copilot
- 30M+ paid M365 Copilot seats (Microsoft FY26 Q4 earnings, 2026-07-29), from 15M in Jan
  2026; M365 install base ~450M seats — unmatched enterprise distribution.
- Lives inside the M365 compliance boundary (permissions, DLP, audit, Purview).
- Card nuance: not known for frontier models — it licenses others', including Claude.

### Perplexity
- ~94% of answers carry inline citations, ~8.2 sources per answer (margen.net 2026 —
  secondary); lowest citation-error rate in CJR/Tow Center testing (37% vs 67% ChatGPT
  Search; study Mar 2025). ~780M queries in May 2025 (CEO figure).
- Card line: "Research with receipts."

### Grok
- "Unhinged" is a **literal named voice-mode personality** since Grok 3 (Feb 2025)
  (https://www.techradar.com/computing/artificial-intelligence/grok-3s-voice-mode-is-unhinged-and-thats-the-point).
- Fewer-guardrails positioning + real-time X data; it also genuinely places (top-ten
  LMArena creative writing, June 2026).
- Caveat line: July 2025 "MechaHitler" episode (~16 hours of antisemitic output after a
  bad prompt update, public apology — CNN 2025-07-12) → care for brand-sensitive work.

## DeepSeek-R1 vs OpenAI o1 — the January 2025 numbers (for the chart)

All benchmark figures from the R1 paper, arXiv:2501.12948 (2025-01-22); comparison model
o1-1217.

| Benchmark | DeepSeek-R1 | OpenAI o1-1217 | Winner |
|---|---|---|---|
| AIME 2024 (pass@1) | 79.8% | 79.2% | R1 (+0.6) |
| MATH-500 (pass@1) | 97.3% | 96.4% | R1 (+0.9) |
| Codeforces (human percentile) | 96.3 | 96.6 | o1 (slight) |
| GPQA Diamond (pass@1) | 71.5% | 75.7% | o1 (+4.2) |
| SWE-bench Verified | 49.2% | 48.9% | R1 (+0.3) |

Pricing (Jan 2025): R1 $0.55 in / $2.19 out per M tokens (cache-hit input $0.14) vs o1
$15 / $60 → **27.3–27.4x cheaper** (sources: nxcode.io pricing guide;
pricepertoken.com/pricing-page/model/openai-o1). Equivalent framing: a $100 o1 workload ≈
$3.60 on R1.

**Chart honesty rules:** headline "matched capability, ~27x cheaper output" is defensible
ONLY with GPQA and Codeforces kept in the chart (o1 led both) — "matched on most, not a
clean sweep." Codeforces numbers are human percentiles, not accuracy — label the axis.

**Since then (one line for notes):** DeepSeek stayed the open-weight value leader but
slipped off the leading edge — NIST CAISI (May 2026) put DeepSeek V4-Pro ~8 months behind
the frontier (DeepSeek claims 3–6); independent harnesses found gaps vs self-reported
numbers (https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro).

## UNVERIFIED (do not use without re-checking)

- LMArena creative-writing #1 for Sept 2026 specifically (June snapshot verified; check
  the live leaderboard before shipping the slide).
- Perplexity MAU (conflicting 45M vs 230M; use the CEO query-volume figure instead).
- Any single SWE-bench **Pro** number (conflicting harnesses; name the harness or omit).
- "Cowork slightly better than Copilot" — no benchmark; use the licensing fact.
- Perplexity citation stats are from secondary stats sites; CJR study is the solid anchor.
