# r20 — The 2026 prompting playbook: TO DO / NOT TO DO / EXPIRED (researched 2026-09-09)

Powers the S30 redesign (owner: "compile a useful list of to-dos, not-to-dos, and
no-longer-to-dos — make sure it fully makes sense"). Built on r3/r15 + fresh verification
of the 2025–26 vendor guides. [NEW] = anchor not previously in the repo.

## TO DO (reliably helps today)
1. State the task precisely — verb, constraints, success criteria, and the WHY behind
   each rule (Anthropic 2026; Yang et al., 2025; revised 2026: unstated requirements guessed right only 41.1%).
2. Structure with delimiters (XML/Markdown) and standardize ONE tested, versioned
   template (Anthropic · OpenAI · Google guides; He 2024: wrapper alone swings up to 40%).
3. Zero-shot first; add 3–5 targeted, diverse examples only when format/tone matters
   (OpenAI reasoning best practices; Anthropic 2026).
4. Long inputs: documents at top, instructions at the END — and for very long context,
   bookend instructions at BOTH ends (Anthropic up-to-~30%; [NEW] GPT-4.1 guide 2025:
   both ends beat either alone).
5. Give an out + require citations (Omar 2025: hallucination 66%→44%; Anthropic docs).
6. Concrete numeric budgets for measurable outputs — words, bullets, tool calls
   ([NEW] GPT-5.1 guide: "adheres well to concrete length guidance"; GPT-5 guide: tool
   budgets & stop criteria).
7. Persona + audience for VOICE and level, never for accuracy (PersonaLLM 2024: traits
   detectable up to 80%; Google PTCF; Anthropic role guidance).
8. Self-check against NAMED criteria, evaluation blinded from generation (CoVe 2024:
   FactScore 55.9→71.4; Cheng, Science 2026 for blinding).
(9. if space: metaprompting — official at all three vendors; OPRO 2024, GEPA 2026.)

## NOT TO DO (hurts or wastes effort today)
1. Contradictory instructions — reasoning models burn tokens reconciling them (GPT-5
   guide 2025).
2. Tips, threats, deadline pressure — null on average, ±35% per-question chaos (Wharton
   R3 2025; Salinas & Morstatter 2024).
3. Bare "do not hallucinate" commands — trigger a "Safety Tax": over-refusal of facts
   that ARE in the context ([NEW] arXiv:2601.02023, Jan 2026; use the positive out+cite
   pattern instead).
4. Revealing your preferred answer, or "are you sure?" as verification (Cheng, Science
   2026: +49% affirmation; Sharma 2023: flips correct answers).
5. Piling micro-rules — even frontier models degrade past ~150 simultaneous
   instructions, biased toward earlier rules ([NEW] IFScale, arXiv:2507.11538; GPT-5.5
   guide: "smallest prompt that preserves the product contract").
6. ALL-CAPS / ALWAYS / NEVER as an emphasis crutch — reserve absolutes for true
   invariants ([NEW] GPT-5.x guides; Gemini 3 guide: avoid overly persuasive language).
7. Demanding JSON/schemas a human will just read — zero benefit; when structure IS
   needed, use structured outputs and reason-first-format-second (OpenAI 2024; Tam 2024
   tempered by 2025 replications — per r15, never teach "JSON hurts reasoning" as fact).
8. Concluding "the model can't do X" from one phrasing — formatting alone swings up to
   76 points (Sclar ICLR 2024; Wharton R1).

## NO LONGER TO DO — EXPIRED (was right in 2022–23; obsolete now, with replacement)
1. "Let's think step by step" / manual CoT — reasoning is built in; adds latency and
   variability (OpenAI: "avoid chain-of-thought prompts"; Anthropic 2026; Wharton R2;
   Sprague ICLR 2025: gains were mostly math/logic). → Pick a reasoning model / set
   effort. Origin worth telling: Kojima 2022 took GSM8K 10.4%→40.7% — it WAS real.
2. Piles of few-shot exemplars (10+) — minimal/negative on instruction-tuned models;
   actively degrades R1-class reasoners (Brown 2020 origin; R1 paper 2025; FewMMBench
   2026). → Zero-shot first, then 3–5 format-definers.
3. "You are a world-class expert" for accuracy — failed replication at scale (Zheng
   2024: 162 personas; Wharton R4 Dec 2025: null + dumbed-down personas hurt). →
   Task-specific instructions; persona for voice only.
4. "Take a deep breath" and other magic phrases — one optimizer's local optimum for one
   model on one benchmark, never universal (OPRO ICLR 2024). → The phrase died; the
   METHOD won: automated prompt optimization.
5. Emotional appeals (EmotionPrompt's "important to my career") — the famous "115%" was
   the cherry-picked best case; honest average ~2.6% relative, null on modern models
   ([NEW] arXiv:2409.20303 replication-crisis recalc; Wharton R3). → Clarity; stakes as
   factual CONTEXT ("this goes to a regulator") is fine — it changes the task, not the
   mood.
6. "Instructions, ###, then text" + chopping documents for tiny windows — written for
   4–8K contexts; placement guidance inverted at ~1M (Liu 2023 mechanism persists;
   Anthropic: docs top, query END; GPT-4.1: both ends). → TO DO 4.
7. Hand-run self-consistency (10 samples, majority vote) + micro-decomposing every task
   — absorbed into test-time compute; over-prescribing steps underperforms
   outcome-first prompts (Wang ICLR 2023 origin; Anthropic 2026; [NEW] GPT-5.5 guide:
   "give a clear destination, let it choose the path"). → Effort settings; chain only
   for auditable intermediates (a feature for regulated work).
8. Carrying your GPT-4-era prompt stack to each new model — legacy scaffolds actively
   degrade newer models ([NEW] GPT-5.5 guide via Willison, Apr 2026: "begin migration
   with a fresh baseline"). → Re-baseline and re-test on every upgrade (= the PDCA slide).

## Contested / depends (notes, not columns)
Politeness (real but small, direction inconsistent — PLUM Apr 2026 up to ~11% either
way; be normally civil, don't engineer tone) · CoT still legitimate for small/local/
non-reasoning models — the expiry is frontier-specific · repetition: verbatim
bookending in long context ✓, paraphrased blanket repetition ✗ · prompt LENGTH is the
wrong variable — information density is right (detail helps, filler and rule-count
hurt) · one sparse emphasized invariant is fine — the crutch at scale is the problem.

## Coherence seams (state in notes so the columns never look self-contradictory)
Caps constrain quantity, absolutes lock judgment (TO DO 6 vs NOT 6) · repeat verbatim
or not at all (TO DO 4 vs NOT 1) · CoT's dual status called out explicitly · task
detail ≠ rule piles (TO DO 1 vs NOT 5) · give-an-out is "don't-hallucinate" said
positively — itself a demo of "say what TO do."

## UNVERIFIED (re-check before sliding)
Politeness/emotion on 2026 reasoning-mode flagships (no credible study either way) ·
"UPPERCASE IS ALL YOU NEED" (unestablished rigor — do not cite) · Safety-Tax magnitudes
(direction only) · the claim that GPT-5.5 calls hard word caps counter-productive
(blog-only, tension with GPT-5.1 primary — verify before weakening TO DO 6) · whether
Wharton R3 tested the literal career phrasing · IFScale's ~150 threshold on 2026
flagships · Dobariya & Kumar peer-review status.

Key new sources: arXiv 2508.00614 · 2601.02023 · 2409.20303 · 2507.11538 · 2604.16275 ·
developers.openai.com GPT-4.1/5/5.1 guides · simonwillison.net GPT-5.5 guide (Apr 2026) ·
ai.google.dev prompting strategies · philschmid.de Gemini 3 practices.
