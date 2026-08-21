# Research Notes — "From Prompts to Agents" Training
**Compiled:** August 21, 2026 · **Method:** ten parallel research passes, every fact verified against
primary sources on that date; each file carries inline URLs and flags anything UNVERIFIED.
**Purpose:** single source of truth behind the deck, the cheat sheet, and the prompt library.

## The research files (`notes/research/`)

| File | Covers | Feeds |
|---|---|---|
| `r1_history.md` | Verified milestone timeline 1950→2026, eras framing, adoption stats | Part 1 (slides 5–6) |
| `r2_concepts.md` | Tokens, context windows (per-model sizes Aug 2026), RAG, embeddings, hallucination mechanism, reasoning models, MoE, fine-tuning | Part 1 (slides 7–13) |
| `r3_techniques.md` | Vendor prompting guidance (all four, fetched live), technique taxonomy with original papers, myths (tips/politeness), reasoning-model changes, sycophancy (Science 2026) | Part 3 |
| `r4_agentic.md` | Agent definitions/loop, MCP status, agentic prompting best practices (per-element sourcing), generative-vs-agentic contrast, injection/least-privilege/OpenClaw-skills risks | Part 5 |
| `r5_tools.md` | Assistant + agentic tool landscape Aug 2026 (models verified), expertise map, benchmark caveats | Part 2 |
| `r6_chinese.md` | DeepSeek moment, Qwen/Kimi/GLM/MiniMax/Baidu/Tencent, what they brought, consumer-app vs self-hosted governance, Stanford AI Index gap numbers | Part 2 (slides 16–17) |
| `r7_management.md` | Prompt libraries: why, per-tool mechanisms (Projects/Skills/Gems/Prompt Gallery), template conventions, registries, governance | Part 6 |
| `r8_applied.md` | File-creation capabilities per vendor (verified), fidelity caveats (vendors' own admissions), task prompting patterns with evidence (arithmetic, assertion-evidence, LLM-as-judge) | Part 4 |
| `r9_library_a.md` | Extraction of Oscar's library: internal crash course (5 building blocks, CRISP, techniques), Phoenix & Taylor Five Principles, Venkataraman, Ibrahim John | Part 3 continuity + reading list |
| `r10_library_b.md` | Extraction: Berryman & Ziegler, Chip Huyen *AI Engineering* | Reading list + Part 5 grounding |

## Headline verified facts used on slides

- ChatGPT ~100M users in 2 months (Reuters/UBS, Feb 2023); 900M+ weekly users (Feb 2026); Gemini app 1B monthly users (Aug 11, 2026).
- Stanford AI Index 2026: 88% of organizations use AI somewhere; generative AI ~70%; agent deployment single-digit % in most functions; US–China top-model gap ~3% (from 18–32 pts in 2023); US private AI investment ~23× China's.
- ~1M-token context is the Aug-2026 flagship standard (Claude Fable/Sonnet 5, GPT-5.6, Gemini 3.1 Pro, DeepSeek V4, Qwen, Kimi) — consumer apps often enforce less; "lost in the middle" persists (Liu et al. 2023).
- Anthropic long-context guidance: docs at top, query at end — up to ~30% better.
- Google Oct-2024 guide: effective prompts average ~21 words (dropped from the newer edition — teach as directional).
- Format brittleness: up to 76-point accuracy swings from formatting alone (Sclar et al., ICLR 2024).
- Sycophancy: 11 models affirm users ~49% more than humans (Cheng et al., Science 2026; arXiv 2510.01395).
- Reasoning-model era guidance: OpenAI "avoid chain-of-thought prompts"; zero-shot first; Anthropic "prefer general instructions over prescriptive steps"; contradictions cost reasoning tokens.
- MCP: donated to Linux Foundation's Agentic AI Foundation Dec 9, 2025; ~0.5B SDK downloads/month by Jul 2026.
- DeepSeek moment: R1 Jan 20, 2025 (MIT license); Nvidia −$589B Jan 27, 2025; "$5.6M" = final-run compute only (SemiAnalysis: hardware >$500M).
- Harmonic Security (22M enterprise prompts, 2025): ~1 in 25 went to China-based AI apps.
- GPT-4 ≈59% on 3×3-digit multiplication (Faith & Fate, NeurIPS 2023) → all numbers via code execution.
- Microsoft's own Excel Agent Mode benchmark: 57.2% vs ~71.3% human (SpreadsheetBench).
- LLM-as-judge: >80% human agreement (MT-Bench) but position/verbosity/self-preference biases; 2026: consistency ≠ fairness.
- OpenClaw: ~247K GitHub stars (Mar 2026); CVE-2026-25253 1-click RCE; Cisco found the #1 community skill exfiltrating data; maintainer's own "too dangerous" warning.

## Aggregated UNVERIFIED / handle-with-care list

Each research file ends with its own list; the ones that touch slide content:
- Claude Code "$1B annualized" — reported, not primary-verified (kept out of the deck).
- Kimi "K3" naming conflicts across sources (r2/r5 vs r6) — deck avoids specific Kimi version numbers; says "Kimi K2 line."
- Exact GPT-5.6 context (~1.05M) — third-party trackers only; deck says "~1M standard."
- Google "21 words" — Oct 2024 edition only; flagged in speaker notes.
- Stanford AI Index exact wording — deck rounds to "~3%"; pull the primary PDF before quoting precise Elo numbers externally.
- OWASP LLM01 page returned 403; definition corroborated via secondary sources.

## Standing rules carried over from the previous training
- Name-agnostic: no internal document names or confidential examples in any training material.
- Policy-neutral: the organization's AI policy and approved-tool list outrank all tool guidance in the material.
- Every currency-sensitive claim is dated ("as of Aug 2026").
