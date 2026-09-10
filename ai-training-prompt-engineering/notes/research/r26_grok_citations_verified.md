# r26 — Verification of the external (Grok) review's citations (researched 2026-09-10)

Gate for Round 9B/9B-extended holds (PENDING_CHANGES): nothing below touched a
slide until verified here. Verdict: ALL FOUR claim clusters CONFIRMED, each with
corrections; claim 5 (the "12 blocks is a risk" inference) is PARTLY supported
and must be taught with the corrected framing at the end.

## 1. Anthropic's 80% system-prompt cut — CONFIRMED, details corrected
- Primary: "The new rules of context engineering for Claude 5 generation
  models," Thariq Shihipar (Anthropic), claude.com blog, 2026-07-24 (fetched
  2026-09-10). Verbatim: removed "over 80% of Claude Code's system prompt for
  models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our
  coding evaluations."
- The reviewer listed 4 of SIX "Then → Now" rules. All six:
  ① rules → judgement ② examples → design interfaces ③ all upfront →
  progressive disclosure ④ repeat yourself → simple tool descriptions
  ⑤ memory in CLAUDE.md → auto-memory ⑥ simple specs → RICH REFERENCES.
  Rule ⑥ matters for the deck: Anthropic asks for MORE detail in specs — the
  post is not "less of everything." Caveat kept in-post: constraints remain
  valuable "in highly important areas." Ships a `claude doctor` right-sizing
  command (coverage-only; untested).
- Consistent parent guidance: "Effective context engineering for AI agents,"
  anthropic.com/engineering, 2025-09-29: smallest set of high-signal tokens ·
  right-altitude prompts (neither brittle if-else lists nor vague) · few
  diverse CANONICAL examples · just-in-time context via identifiers ·
  compaction, note-taking, sub-agents for long horizons.
- Slide-safe line: "July 2026: Anthropic cut over 80% of Claude Code's system
  prompt for Claude-5-generation models with no measurable loss on its coding
  evals — replacing rule-lists with judgement, example dumps with interfaces,
  up-front stuffing with progressive disclosure — while asking for RICHER
  specs and references, not vaguer ones."

## 2. Chroma "Context Rot" — CONFIRMED
- "Context Rot: How Increasing Input Tokens Impacts LLM Performance," Chroma
  technical report (Hong, Troynikov, Huber), 2025-07-14 —
  trychroma.com/research/context-rot (fetched 2026-09-10). 18 models confirmed
  (Claude Opus 4/Sonnet 4/3.7/3.5/Haiku 3.5 · o3, GPT-4.1 family, GPT-4o,
  GPT-4 Turbo, GPT-3.5 · Gemini 2.5 Pro/Flash, 2.0 Flash · Qwen3 ×3).
- Findings: performance degrades as input grows, "in surprising and
  non-uniform ways," on even trivial tasks; LongMemEval focused ~300-token
  input beats the same content in ~113k tokens; one distractor already hurts;
  lower needle-question similarity degrades faster; shuffled haystacks beat
  logically structured ones (counterintuitive — verified in-report).
- Caveats: Jul-2025 report on 2024–25-era models — teach as "degrades with
  length; windows are not uniform," never as a permanent percentage.

## 3. OWASP agentic Top 10 + Singapore OpenClaw — CONFIRMED, names corrected
- Real name: "OWASP Top 10 for Agentic Applications for 2026," OWASP GenAI
  Security Project, published 2025-12-09 (official release) —
  genai.owasp.org (fetched 2026-09-10). COMPLEMENTS the LLM Top 10 the deck
  already cites (deck_close sources slide). Risks ASI01–ASI10: goal hijack ·
  tool misuse · identity/privilege abuse · agentic supply chain · unexpected
  code execution · memory/context poisoning · insecure inter-agent comms ·
  cascading failures · human-agent trust exploitation · rogue agents (names
  cross-checked via Cycode summary — pull the official PDF before printing
  all ten on a slide).
- Singapore: IMDA "Case Study: Responsible Deployment of OpenClaw — Applying
  Singapore's Model AI Governance Framework for Agentic AI," 2026-05-14
  (11-page PDF read in full; framework v1.0 2026-01-19), PLUS the formal
  advisory: CSA AD-2026-005, 2026-05-28. Say "IMDA case study + CSA advisory."
- NEW additive numbers (beyond the deck's CVE-2026-25253 + Cisco item):
  400+ OpenClaw CVEs by late Apr 2026 (100+ high, 10+ critical, via OpenCVE) ·
  341 malicious ClawHub skills found 2026-02-01 growing to 824 by 2026-02-16
  (Koi Security) · controls: multiple narrow-role agents over one all-powerful
  agent · least privilege · human-approval checkpoints enforced by
  SYSTEM-LEVEL controls because prompt-layer guardrails "are not fail-safe and
  may be bypassed or 'forgotten'" (the regulator's own version of "a gate in
  the prompt is a suggestion").

## 4. OpenAI GPT-5.6 guidance — CONFIRMED; the comparative sentence is primary
- developers.openai.com "Model guidance" for the GPT-5.6 family (page undated;
  GPT-5.6 launched 2026-07-09 per Axios). Near-verbatim: "GPT-5-class models
  follow prompt contracts closely, so conflicting rules can create more
  instability than missing detail." NOT reviewer synthesis.
- Lean prompts: removing repeated instructions/examples and simplifying tool
  descriptions can improve performance; OpenAI-internal evals: leaner system
  prompts scored ~10–15% higher with 41–66% fewer tokens, 33–67% lower cost
  (VENDOR-INTERNAL, unreplicated — always flag). Outcome-first: "describe the
  destination rather than prescribing every step."
- Upgrades r20 NOT-TO-DO 1's sourcing to a primary 5.6-era citation.

## 5. "Twelve rich blocks into a 2026 flagship is a risk" — PARTLY; teach corrected
Strongest 2026 evidence indicts CONFLICTS and RULE-PILES, not length/structure
per se — and mid-tier models more than flagships. Instruction Stacking Collapse
(arXiv:2608.02639, 2026-07-31, preprint): 1–20 verifier-checked constraints
drop follow-rate ~96%→as low as 20%, driven by pairwise conflicts — but tested
Sonnet 4.6/GPT-5-mini/Gemini 2.5 Flash and found STRONGER MODELS ROBUST.
Anthropic's 80% cut showed "no measurable loss" — proving the deleted material
was REDUNDANT, not harmful. Chroma's volume effects operate far beyond a
12-block brief. Honest teaching frame: a long, internally consistent brief on a
2026 flagship mostly costs tokens, latency, and maintenance; the demonstrated
PERFORMANCE risk concentrates where blocks contradict or micro-rules pile up —
i.e., r20's existing "density, not length" line. "Twelve blocks = degradation
on a flagship" as a flat claim is NOT established; teach design-thick/ship-lean
as economy + conflict-avoidance + maintainability, not model fragility.

## UNVERIFIED — never on a slide
"800 → 164 tokens" for the Claude Code cut (aggregator embellishment; use
"over 80%" only) · Jul-2 2026 World's-Fair announcement (secondary; cite the
blog) · exact GPT-5.6 guide publication date · openai.com "Builder's guide to
GPT-5.6" contents (403) · OpenAI 10–15%/41–66%/33–67% (vendor-internal) ·
OWASP "100+ experts" + exact ASI names pending the official PDF · Instruction
Stacking Collapse peer-review status · `claude doctor` behavior.
