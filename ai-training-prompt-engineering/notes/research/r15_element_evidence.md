# r15 — Per-element evidence refresh (researched 2026-09-09)

Powers the v1.5 importance-first element slides (Part 3) and their notes. Verified against
primary sources on 2026-09-09. ⚠ marks items that nuance or correct earlier repo notes.

## Examples / few-shot
- Brown et al. 2020 (NeurIPS): TriviaQA 64.3% zero-shot → 68.0% one-shot → 71.2% few-shot;
  LAMBADA few-shot 86.4%, +18 pts past prior SOTA (arXiv:2005.14165).
- Lu et al. ACL 2022: example ORDER swings results between "near state-of-the-art and
  random guess performance" (arXiv:2104.08786). ⚠ Prefer this verbatim phrasing over any
  invented percentages.
- Min et al. EMNLP 2022: randomly replacing labels in demonstrations "barely hurts
  performance" — examples teach label space, input distribution, FORMAT, not facts
  (arXiv:2202.12837).
- 2026 counter-trend: instruction-tuned models benefit minimally or regress with added
  demonstrations (FewMMBench, arXiv:2602.21854) — corroborates the R1 few-shot caveat.
- ⚠ r9_library_b's "one example: 10% → near 50%" (secondhand book claim) superseded by
  the primary Brown numbers.

## Role / persona
- Zheng et al. EMNLP 2024 (in repo): 162 personas, no accuracy gain.
- Wharton Prompting Science Report 4 (Dec 7, 2025; SSRN 5879722): six-model replication —
  no expert persona reliably improved accuracy; LOW-knowledge personas ("toddler")
  significantly HURT. "Focus on task-specific instructions."
- PersonaLLM (NAACL 2024 Findings, aclanthology 2024.findings-naacl.229): personas DO
  reliably shape output — assigned Big Five traits identifiable in text by humans up to
  80% of the time. The quantified positive case: roles steer voice, not IQ.

## Task / specificity
- Yang et al. (arXiv:2505.13360, v3 2026): models infer unspecified requirements right only
  41.1% of the time; under-specified prompts 2× as likely to regress across model updates;
  requirements-aware optimization +4.8% avg.
- Explicit I/O specs, edge cases, stepwise breakdowns drive detailed-prompt gains
  (arXiv:2508.03678).

## Context / grounding
- Zhou et al. EMNLP 2023 Findings (arXiv:2303.11315): context-faithful prompting cut the
  memorization ratio 35.2% → 3.0%; unanswerable-question accuracy 30.6% → 87.8% (GPT-3.5).
- Weller et al. EACL 2024 ("According to…"): grounding directives improve grounding and
  often end-task performance (cite qualitatively — numeric range unverified).
- Omar et al., Communications Medicine 2025: models repeated/elaborated planted errors in
  up to 83% of cases — context is trusted even when wrong.

## Format / output contracts
- OpenAI Structured Outputs (Aug 6, 2024): schema compliance <40% (prompting alone,
  gpt-4-0613) → 100% (strict mode).
- ⚠ Tam et al. EMNLP 2024 Industry ("Let Me Speak Freely" — format restrictions degrade
  reasoning) did NOT survive replication: dottxt "Say What You Mean" (matched prompts —
  structured ≥ unstructured) and JSONSchemaBench (arXiv:2501.10868 — constrained decoding
  ≥ unconstrained on GSM8K/Last Letter/Shuffled Objects). Teach "reason first, format
  second" as a safe manual habit only; do not teach "JSON hurts reasoning" as fact.

## Structure / tags
- He et al. (arXiv:2411.10541): same content, different wrapper (plain/Markdown/JSON/YAML)
  → up to 40% swing on GPT-3.5; GPT-4-class more robust. Best format differs BY MODEL —
  the honest claim is "structure explicitly and standardize one tested template," not
  "XML is magic."

## The Out
- Omar et al. 2025 (Nature Communications Medicine): "acknowledge uncertainty instead of
  speculating" mitigation cut mean hallucination 66% → 44% across six models; GPT-4o
  53% → 23% (p<0.001).
- npj Digital Medicine 2026 follow-up: GPT-5 65% unprompted → ~7.7% with the mitigation
  (⚠ decimal from search summary — verify before quoting beyond "under 8%").
- Kalai et al. (OpenAI) 2025, arXiv:2509.04664: mechanism — binary-graded evals reward
  guessing; o4-mini 75% error / 1% abstention vs gpt-5-thinking-mini abstaining 52% with
  far fewer errors.

## Self-check
- Huang et al. ICLR 2024 (arXiv:2310.01798): intrinsic self-correction degrades — GPT-4
  GSM8K 95.5 → 89.0 over two review rounds; GPT-3.5 CommonSenseQA 75.8 → 38.1.
- Kamoi et al. TACL 2024: self-correction works only with reliable EXTERNAL feedback.
- CoVe (ACL Findings 2024, arXiv:2309.11495): planned verification questions — Wikidata
  list-QA precision 0.17 → 0.32; biography FactScore 55.9 → 71.4. Use these table numbers,
  not the secondhand "50–70% reduction" phrasing.

## Metaprompting
- OPRO (ICLR 2024, arXiv:2309.03409): optimizer prompts beat human prompts by up to 8%
  (GSM8K) and up to 50% (Big-Bench Hard).
- GEPA (arXiv:2507.19457, ICLR 2026 oral): reflective prompt evolution beats RL fine-tuning
  (up to +20%, 35× fewer rollouts) and MIPROv2 by >10% aggregate.

## Meta / replication layer
- No quantitative successor to The Prompt Report exists (latest v6, Feb 2025).
- Wharton Prompting Science Reports 1–4 (2025; 25–100 runs per question): politeness
  effects wash out (R1); CoT prompting value decreasing + adds variability (R2,
  arXiv:2506.07142); tips/threats don't help (R3); personas null (R4). The modern
  replication layer for the evidence-corner slide.

## PDCA connection (verified)
- Art Smalley (Toyota veteran), "Prompt, Do, Check, Act: The New PDCA," Lean Enterprise
  Institute Lean Post, May 27, 2026 — "Plan becomes Prompt… Check and Act are human work";
  "the people who get the most out of these tools… are the ones willing to run the loop a
  few more times" (lean.org/the-lean-post; mirrored at artoflean.com).

## UNVERIFIED (do not slide without re-checking)
Weller numeric range · GPT-5 7.67% decimal · dottxt publication date · He et al. corporate
affiliation · "DETAIL Matters" preprint (no numbers) · gpt-5-thinking-mini 26% companion
figure.
