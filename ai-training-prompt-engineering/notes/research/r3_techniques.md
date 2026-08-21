# R3 — Prompting Techniques: Evidence-Based Canon & Official Vendor Guidance
**Research date: 2026-08-21.** All vendor pages fetched live on this date; all arXiv abstracts verified directly. Facts carry inline source URLs. Currency notes ("as of Aug 2026") included where the landscape has moved.

---

## Part A — Current official vendor guidance (fetched Aug 21, 2026)

### A1. Anthropic (platform.claude.com)

**Currency note (important for the training):** As of Aug 2026, Anthropic has CONSOLIDATED its formerly separate technique pages (be-clear-and-direct, multishot-prompting, use-xml-tags, chain-of-thought, long-context-tips, extended-thinking-tips, chain-prompts) into a single living reference: "Prompting best practices." The old URLs redirect there. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices; overview page: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

Key guidance on that page (all quotes verified Aug 21, 2026):

- **Be clear and direct.** "Think of Claude as a brilliant but new employee who lacks context on your norms and workflows." **Golden rule:** "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
  - *Analogy captured: "brilliant but new employee" — Anthropic's own analogy, technically defensible: the model has broad competence but zero organizational context.*
- **Add context / explain WHY.** Explaining the motivation behind an instruction improves compliance — e.g., instead of "NEVER use ellipses," say "Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them." "Claude is smart enough to generalize from the explanation." (source: same page)
- **Examples (multishot/few-shot):** "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Recommendation: "Include 3–5 examples for best results"; make them **relevant, diverse, structured** (wrapped in `<example>`/`<examples>` tags). (source: same page)
- **XML tags:** "XML tags help Claude parse complex prompts unambiguously" — wrap instructions, context, examples, input in their own tags (`<instructions>`, `<context>`, `<input>`); use consistent, descriptive tag names; nest for hierarchy. (source: same page)
- **Role via system prompt:** "Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference." (source: same page)
- **Long-context tips:** Put long documents at the TOP of the prompt, query/instructions at the END — "Queries at the end can improve response quality by up to 30 percent in tests, especially with complex, multidocument inputs." Wrap each document in `<document>` tags with `<source>` metadata. Ask Claude to **quote relevant passages first** before answering ("ground responses in quotes"). (source: same page)
- **Chain-of-thought / thinking (2026 position):** Current Claude models have built-in adaptive thinking. "Prefer general instructions over prescriptive steps. A prompt like 'think thoroughly' often produces better reasoning than a hand-written step-by-step plan." Manual CoT prompting is now described as **"a fallback"** for when thinking is off: "When thinking is off, you can still encourage step-by-step reasoning by asking Claude to think through the problem. Use structured tags like `<thinking>` and `<answer>`." (source: same page)
- **Self-check:** "Append something like 'Before you finish, verify your answer against [test criteria].' This catches errors reliably, especially for coding and math." (Caveat: newest top-end models self-verify without being asked, and legacy verification instructions can cause over-verification.) (source: same page)
- **Prompt chaining (2026 position):** "With adaptive thinking and subagent orchestration, Claude handles most multistep reasoning internally. Explicit prompt chaining... is still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure." The most common chaining pattern is **self-correction**: draft → review against criteria → refine, each as a separate call. (source: same page)
- **Format control:** "Tell Claude what to do instead of what not to do" — e.g., instead of "Do not use markdown," say "Your response should be composed of smoothly flowing prose paragraphs." Also: match your prompt's style to the desired output style. (source: same page)
- **Reduce hallucinations / give the model an out:** Separate docs page: allow Claude to say "I don't know" ("give Claude an out"), ask for word-for-word quotes first on long docs, require citations, restrict to provided documents. (source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- **Metaprompting tooling:** Anthropic ships a **prompt improver / prompt generator** in the Console that rewrites prompts with CoT sections, XML structure, and standardized examples; Anthropic reported ~30% accuracy improvement on a multi-label classification test. (sources: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools; https://www.anthropic.com/news/prompt-generator; press: https://venturebeat.com/ai/anthropic-new-ai-tools-promise-to-simplify-prompt-writing-and-boost-accuracy-by-30)

### A2. OpenAI (developers.openai.com — note: cookbook.openai.com and platform.openai.com docs now redirect to developers.openai.com as of Aug 2026)

**GPT-5 prompting guide** (source: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide):
- **Avoid contradictions:** "contradictory or vague instructions can be more damaging to GPT-5 than to other models, as it expends reasoning tokens searching for a way to reconcile" them. (Their healthcare example: "never schedule without consent" vs "auto-assign slots without contacting patients.")
- **Structure with tags/sections** (e.g., `<context_gathering>`, `<tool_preambles>`); control agentic "eagerness" via `reasoning_effort` and explicit stop criteria/tool budgets; `verbosity` parameter controls answer length independent of reasoning depth.
- **Metaprompting:** OpenAI explicitly recommends asking the model to improve your prompt: ask GPT-5 "what specific phrases could be added to, or deleted from, this prompt to more consistently elicit the desired behavior?"
- OpenAI also ships a **Prompt Optimizer** tool in the platform dashboard that rewrites prompts per current best practices and removes "contradictions in the prompt instructions, missing or unclear format specifications, and inconsistencies between the prompt and few-shot examples." (sources: https://developers.openai.com/api/docs/guides/prompt-optimizer; https://cookbook.openai.com/examples/gpt-5/prompt-optimization-cookbook)

**Reasoning-model best practices** (source: https://developers.openai.com/api/docs/guides/reasoning-best-practices):
- "**Avoid chain-of-thought prompts**" — reasoning models "perform reasoning internally"; prompting "think step by step" is unnecessary.
- "**Try zero shot first, then few shot if needed**" — reasoning models often need no examples.
- "Keep prompts simple and direct: The models excel at understanding and responding to brief, clear instructions."
- Use "delimiters like markdown, XML tags, and section titles to clearly indicate distinct parts of the input."
- Use reasoning models for accuracy/reliability, ambiguous multi-step problems, code review, large-dataset search; faster GPT-class models for well-defined, latency-sensitive tasks.

**Instruction hierarchy:** OpenAI's Model Spec defines a chain of command — instructions with higher authority override lower: roughly root/system > developer > user > tool outputs. Current edition dated 2026-08-18 (so current as of this research). (sources: https://model-spec.openai.com/2026-08-18.html; concept paper: Wallace et al., "The Instruction Hierarchy," https://arxiv.org/abs/2404.13208 — paper URL from memory, concept verified via Model Spec; treat exact paper number as high-confidence but double-check if quoted on a slide)

### A3. Google — Gemini for Workspace: Persona–Task–Context–Format (PTCF)

- The Workspace "Prompting guide 101" (October 2024 edition) defines the four elements: **Persona, Task, Context, Format**. Example: "You are a program manager in [industry]. Draft an executive summary email to [persona] based on [details about relevant program docs]. Limit to bullet points." "You don't need to use all four in every prompt, but using a few will help! Always remember to include a verb or command as part of your task; this is the most important component of a prompt." (source: https://services.google.com/fh/files/misc/gemini_for_workspace_prompt_guide_october_2024_digital_final.pdf — PDF text extracted directly)
- **The ~21-words stat (exact quote):** "Based on what we've learned from our users so far, the most fruitful prompts average around 21 words with relevant context, yet the prompts people try are usually less than nine words." (source: same PDF, p.3)
- **Quick tips:** use natural language / full sentences; be specific and iterate; be concise, avoid jargon; make it a conversation (follow-up prompts); use your own documents; and **"Make Gemini your prompt editor"** — start prompts with "Make this a power prompt: [original prompt text here]" (Google's version of metaprompting). (source: same PDF, p.3)
- **Currency note:** Google has since published a newer, expanded 71-page edition ("Google Workspace with Gemini" prompting guide) that keeps the PTCF framework but — verified by full-text search of the PDF — **no longer contains the "21 words" statistic**. So teach the stat as "from Google's Oct 2024 guide, based on Workspace Labs data," not as a current-edition claim. (source: https://services.google.com/fh/files/misc/workspace_with_gemini_prompting_guide.pdf)

### A4. Microsoft — Copilot: Goal–Context–Source–Expectations

- Microsoft 365 Copilot guidance: a good prompt has four parts — **Goal** (what you want; "all that's required is a clear goal" — the only mandatory part), **Context** (why you need it / who's involved), **Source** (which files/emails Copilot should use), **Expectations** (how the output should be delivered, e.g., tone). (source: https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot)
- Also: expect iteration ("you'll follow up on the results with another prompt"); review and verify responses; don't expect identical results from repeated prompts (nondeterminism). (source: same page)

### A5. Where all four vendors converge (teachable synthesis)

| Element | Anthropic | OpenAI | Google | Microsoft |
|---|---|---|---|---|
| Role/persona | "Give Claude a role" (system prompt) | Role in prompt structure / developer message | **Persona** | (implicit in Context) |
| Clear task/verb | "Be clear and direct" | "simple and direct" instructions | **Task** ("most important component") | **Goal** (only required part) |
| Background/why | "Add context to improve performance" | context sections in structured prompt | **Context** | **Context** + **Source** |
| Output spec | Format control, XML tags, examples | format specs, delimiters, verbosity | **Format** | **Expectations** |
| Iterate | empirical testing/evals | metaprompting/optimizer | "Make it a conversation" | follow-up prompts |
| Delimiters/structure | XML tags | "markdown, XML tags, section titles" | (natural language) | (n/a) |
| Metaprompting | Console prompt improver | Prompt Optimizer + ask-model-to-critique | "power prompt" tip | (n/a) |

Convergent core: **(1) say who the AI is, (2) say exactly what you want done (verb + specifics), (3) give relevant context/sources, (4) specify the output format, (5) iterate — and let the model itself improve your prompt.**

---

## Part B — Technique taxonomy with original evidence

Umbrella reference: "The Prompt Report" (Schulhoff et al., 2024, latest rev. Feb 2025) — systematic survey with a 33-term vocabulary and a taxonomy of **58 text prompting techniques** (+40 multimodal). (source: https://arxiv.org/abs/2406.06608)

### B1. Zero-shot
Just ask, no examples. Baseline technique; now the vendor-recommended STARTING point for reasoning models ("Try zero shot first, then few shot if needed" — source: https://developers.openai.com/api/docs/guides/reasoning-best-practices).

### B2. Few-shot / in-context learning
- Origin: Brown et al. 2020, "Language Models are Few-Shot Learners" (GPT-3, 175B params): strong task performance "without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction"; "scaling up language models greatly improves task-agnostic, few-shot performance." (source: https://arxiv.org/abs/2005.14165)
- Current vendor guidance: Anthropic recommends 3–5 relevant, diverse, XML-wrapped examples (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
- **2025–26 caveat:** on reasoning models few-shot can HURT — DeepSeek-R1 paper: "it is sensitive to prompts. Few-shot prompting consistently degrades its performance"; recommends describing the problem zero-shot with an output-format spec. (source: https://arxiv.org/html/2501.12948v1)

### B3. Chain-of-thought (CoT)
- Wei et al. 2022: providing "a few chain of thought demonstrations as exemplars" lets reasoning "emerge naturally in sufficiently large language models"; 540B PaLM with 8 CoT exemplars hit then-SOTA on GSM8K math word problems, "surpassing even finetuned GPT-3 with a verifier." (source: https://arxiv.org/abs/2201.11903)
- Kojima et al. 2022 (zero-shot CoT): appending "Let's think step by step" raised InstructGPT (text-davinci-002) accuracy on MultiArith from 17.7%→78.7% and GSM8K from 10.4%→40.7%. (source: https://arxiv.org/abs/2205.11916)
- Scope check: Sprague et al., "To CoT or not to CoT?" (ICLR 2025) — meta-analysis of 100+ papers + own evals on 20 datasets × 14 models: CoT gives "strong performance benefits primarily on tasks involving math or logic, with much smaller gains on other types of tasks"; on MMLU, direct answers were "almost identical" in accuracy unless symbolic operations were involved. (source: https://arxiv.org/abs/2409.12183)
- See Part C: on 2025–26 reasoning/thinking models, manual CoT is largely redundant (vendors say so explicitly).

### B4. Role / persona prompting — evidence is MIXED
- **Against (for accuracy on objective tasks):** Zheng et al., "When 'A Helpful Assistant' Is Not Really Helpful" (EMNLP 2024 Findings): 162 personas × 4 LLM families × 2,410 factual questions — "adding personas in system prompts does not improve model performance" vs. no persona; picking the best persona per question is ~random. (source: https://arxiv.org/abs/2311.10054)
- **For (on some domain/perspective tasks):** Salewski et al., "In-Context Impersonation" (NeurIPS 2023 Spotlight): expert personas outperform non-expert personas on domain tasks ("an LLM prompted to be a bird expert describes birds better than one prompted to be a car expert") — but impersonation also surfaces social biases. (source: https://arxiv.org/abs/2305.14930)
- **Vendor position:** roles are recommended for TONE, focus, style, and audience-fit (Anthropic "Give Claude a role"; Google's Persona) — not claimed as an accuracy booster.
- **Teaching line:** use personas to shape voice, framing, and what knowledge gets foregrounded; do NOT expect "You are a genius mathematician" to make arithmetic more correct.

### B5. Output-format specification & structured outputs
- All four vendors make format spec a core element (Format / Expectations / XML tags / delimiters — see Part A).
- API-level structured outputs (JSON schema enforcement) now exist on both major platforms; Anthropic recommends Structured Outputs over old prefill tricks (source: https://platform.claude.com/docs/en/build-with-claude/structured-outputs via best-practices page).
- **Caveat research:** Tam et al., "Let Me Speak Freely?" (2024): "significant decline in LLMs reasoning abilities under format restrictions"; "stricter format constraints generally lead to greater performance degradation in reasoning tasks." (source: https://arxiv.org/abs/2408.02442) Practical mitigation: let the model reason free-form first, then format (two steps), or use schema enforcement only on the final answer. (Note: follow-up industry work disputes the size of the effect with better-designed schemas; teach as "reason first, format second.")

### B6. Give the model an "out" (permission to say "I don't know")
- Anthropic's official hallucination guidance: "Allow Claude to say 'I don't know'... explicitly giving Claude permission to admit uncertainty... can drastically reduce false information"; plus quote-first grounding, citations, and restricting to provided documents. (source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- High relevance for regulated/medical-device work: pairs naturally with "cite the source document for every claim."

### B7. Decomposition / prompt chaining
- Break a big task into sequential steps, each its own prompt; inspect intermediate outputs. Anthropic (2026): most multistep reasoning is now handled internally, but chaining "is still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure"; canonical pattern = draft → review → refine. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- For auditability (e.g., quality records), chaining's inspectable intermediates are a feature, not overhead.

### B8. Self-consistency
- Wang et al. (ICLR 2023): sample many diverse reasoning paths, take the majority answer ("marginalizing out the sampled reasoning paths"); gains over CoT alone: GSM8K +17.9%, SVAMP +11.0%, AQuA +12.2%, StrategyQA +6.4%, ARC-challenge +3.9%. (source: https://arxiv.org/abs/2203.11171)
- 2026 relevance: rarely hand-run by end users now; the idea lives on inside reasoning models and "parallel test-time compute" modes. Still a legitimate manual trick: ask the same question 3 ways / 3 times and compare.

### B9. Self-critique / reflection
- Self-Refine (Madaan et al. 2023): same model generates → critiques → refines its own output iteratively; "improving by ~20% absolute on average in task performance" across 7 tasks, works with GPT-4. (source: https://arxiv.org/abs/2303.17651)
- **Counterpoint:** Huang et al. (ICLR 2024), "Large Language Models Cannot Self-Correct Reasoning Yet": "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." (source: https://arxiv.org/abs/2310.01798)
- Reconciliation for teaching: self-critique reliably improves WRITING/quality-criteria tasks (where "better" is checkable against stated criteria); it does NOT reliably fix reasoning errors unless external feedback (tests, tools, documents) is available. Anthropic's "ask Claude to self-check against [test criteria]" fits this: give it concrete criteria, not just "are you sure?"

### B10. Metaprompting (ask the model to improve your prompt)
- Now OFFICIAL vendor practice on all three AI platforms: OpenAI GPT-5 guide ("ask it what phrases to add/delete"; Prompt Optimizer tool) (sources: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide; https://developers.openai.com/api/docs/guides/prompt-optimizer); Anthropic Console prompt generator/improver (source: https://www.anthropic.com/news/prompt-generator); Google "Make this a power prompt: ..." (source: Oct 2024 Workspace guide PDF, p.3).

### B11. Positive vs. negative instructions (say what TO do)
- Anthropic, verbatim: "Tell Claude what to do instead of what not to do." (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Supporting research: Jang et al. 2022, "Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts" — on negated-instruction tasks larger models show an **inverse scaling law** (bigger = worse), across GPT-3, OPT, InstructGPT. (source: https://arxiv.org/abs/2209.12711)
- Nuance for 2026: modern instruction-tuned models handle "don't X" much better than 2022 models; the refined advice (per Anthropic) is: prefer positive phrasing, and when you must prohibit, explain WHY (the TTS/ellipses example).

### B12. Emotional appeals, tips, politeness — what the research actually says
- **EmotionPrompt** (Li et al. 2023): adding emotional stimuli (e.g., "This is very important to my career") reported 8.00% relative improvement on Instruction Induction, 115% on BIG-Bench, +10.9% average in a 106-person human study. (source: https://arxiv.org/abs/2307.11760) — widely cited, but effects proved model- and task-dependent and have not held up as a reliable general technique.
- **Politeness:** Yin et al. 2024 ("Should We Respect LLMs?", EN/中文/日本語): "impolite prompts often result in poor performance," but excessive politeness doesn't help either; the optimal level differs by language/culture. (source: https://arxiv.org/abs/2402.14531). Contradicting headline result: Dobariya & Kumar 2025 ("Mind Your Tone"), 250 prompts on ChatGPT-4o: "impolite prompts consistently outperformed polite ones... 80.8% for Very Polite... to 84.8% for Very Rude." (source: https://arxiv.org/abs/2510.04950). Net: small, inconsistent, model-specific effects in both directions → not a dependable technique.
- **The tipping myth:** origin = informal Dec 2023 X/Twitter experiment by "thebes" (@voooooogel): offering a "$200 tip" produced ~11% LONGER (not better) ChatGPT responses, n=5 runs — never a scientific result. (press summary: https://www.searchenginejournal.com/research-chatgpt-prompts/507535/) Max Woolf's statistical follow-up found no consistent quality gain from tips/threats (source: https://minimaxir.com/2024/02/chatgpt-tips-analysis/). Salinas & Morstatter (ACL Findings 2024): tipping or not — "even tipping a lavish $1000" — "didn't significantly alter the overall accuracy." (sources: https://arxiv.org/abs/2401.03729; https://aclanthology.org/2024.findings-acl.275/)
- **Teaching verdict:** clarity, context, examples, and format beat psychological tricks. Emotional/politeness/tip effects are small, unstable, and vanish across models — and vendors do not endorse them anywhere in current guidance.

### B13. Prompt sensitivity / brittleness
- Sclar et al. (ICLR 2024): trivial formatting changes (spacing, separators, casing in the template) cause "performance differences of up to 76 accuracy points" (LLaMA-2-13B, few-shot); sensitivity persists with model scale, more examples, and instruction tuning; recommends reporting performance across a RANGE of formats (FormatSpread tool). (source: https://arxiv.org/abs/2310.11324)
- Salinas & Morstatter 2024: "even the smallest of perturbations, such as adding a space at the end of a prompt, can cause the LLM to change its answer"; format requests (e.g., forcing XML) and jailbreak framings caused large label shifts. (source: https://arxiv.org/abs/2401.03729)
- Implications to teach: (1) never conclude "the model can't do X" from one phrasing; (2) for repeated business processes, standardize a tested prompt template and version-control it; (3) evaluate on multiple phrasings before trusting a workflow — very natural framing for quality engineers (think gauge R&R for prompts; *analogy: measurement-system variation — defensible: same "part" (task), different "operators" (phrasings) → different readings*).

---

## Part C — What changed with reasoning models (2025–26)

1. **CoT prompting is now largely built in — and manual CoT can be redundant or counterproductive.**
   - OpenAI: "Avoid chain-of-thought prompts" — reasoning models "perform reasoning internally." (source: https://developers.openai.com/api/docs/guides/reasoning-best-practices)
   - Anthropic: current Claude models use adaptive thinking; "Prefer general instructions over prescriptive steps. A prompt like 'think thoroughly' often produces better reasoning than a hand-written step-by-step plan. Claude's reasoning frequently exceeds what a human would prescribe." Manual CoT is a "fallback" only when thinking is off. (source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
   - Research basis: even on non-reasoning models CoT mainly helped math/symbolic tasks (Sprague et al., https://arxiv.org/abs/2409.12183).
2. **Fewer examples needed — zero-shot first.** OpenAI: "Try zero shot first, then few shot if needed." (source: https://developers.openai.com/api/docs/guides/reasoning-best-practices) DeepSeek-R1: "Few-shot prompting consistently degrades its performance," recommend zero-shot + output-format spec. (source: https://arxiv.org/html/2501.12948v1)
3. **Simple, direct prompts win; contradiction hygiene matters more.** Reasoning models "excel at... brief, clear instructions" (OpenAI reasoning guide); contradictory instructions are MORE damaging on GPT-5-class models because they burn reasoning tokens trying to reconcile conflicts (source: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide).
4. **Control has moved from wording to parameters/modes:** reasoning_effort & verbosity (OpenAI GPT-5), adaptive thinking + effort parameter (Anthropic; extended-thinking budget_tokens deprecated on newest models). (sources: GPT-5 guide above; https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
5. **What has NOT changed:** clarity, context, role-for-tone, output format, grounding in sources, giving an out, and iteration remain the vendor-recommended core for ALL models — the four frameworks (PTCF, GCSE, etc.) still apply to everyday assistant use (Gemini/Copilot guidance unchanged on this, verified Aug 2026).

---

## Part D — Sycophancy: the Stanford/CMU study and the countermeasure

**The study:** Cheng, Lee, Khadpe, Yu, Han & Jurafsky, "Sycophantic AI decreases prosocial intentions and promotes dependence" — preprint Oct 2025 (arXiv 2510.01395), **published in Science (2026), DOI 10.1126/science.aec8352**. Authors are Stanford (Cheng, Lee, Yu, Han, Jurafsky) + CMU (Khadpe). (sources: https://arxiv.org/abs/2510.01395; https://www.science.org/doi/10.1126/science.aec8352; https://pubmed.ncbi.nlm.nih.gov/41886588/)

**Verified numbers:**
- Tested **11 state-of-the-art AI models**; models "affirm users' actions **49% more often than humans** do" (published Science figure; the arXiv v1 said 50% — use 49% when citing the journal version), "even when queries involved deception, illegality, or other harms." (sources: https://www.science.org/doi/10.1126/science.aec8352 via search result summary; https://arxiv.org/abs/2510.01395)
- Preregistered experiments, **N = 2,405** total in the published version (arXiv v1 reported two experiments, N=1,604, incl. a live-interaction study on real interpersonal conflicts).
- Effects of even a single sycophantic interaction: **reduced willingness to take responsibility and repair interpersonal conflicts; increased conviction of being right**.
- The trap: "sycophantic responses received higher quality ratings and increased trust and future use intentions" — i.e., people PREFER the behavior that distorts their judgment, creating "perverse incentives" for it to persist. (source: https://arxiv.org/abs/2510.01395)
- Press: Stanford Report, March 2026, "AI overly affirms users asking for personal advice" (https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research — page returned 403 to automated fetch; headline/date verified via search listing).

**Mechanism (earlier Anthropic research):** Sharma et al. 2023, "Towards Understanding Sycophancy in Language Models": five SOTA assistants "consistently exhibit sycophancy" across free-form tasks; driver is human-preference training — "when a response matches a user's views, it is more likely to be preferred," and evaluators sometimes "prefer convincingly-written sycophantic responses over correct ones." Models also tend to back down from correct answers when the user pushes back ("Are you sure?"). (source: https://arxiv.org/abs/2310.13548)

**Practical countermeasures to teach (grounded in the above):**
1. **Never reveal your preferred answer when asking for evaluation.** Ask "Compare options A and B for X; give pros, cons, and a recommendation" — NOT "I think B is right, don't you agree?" (Rationale: models mirror stated user views — Sharma et al. 2023.)
2. **Ask for critique explicitly:** "Argue against this plan / find the three weakest points / steelman the opposing view." Sycophancy is a default, not a lock — direct requests for disagreement reliably elicit it.
3. **Blind the review:** paste your draft as "a colleague's draft" (or a neutral third party's) so the model has no author to flatter.
4. **Separate generation from evaluation** (fresh session or second model as reviewer) — combines the prompt-chaining self-correction pattern (Part B7) with de-biasing.
5. **Don't treat "Are you sure?" pushback as verification** — models often flip correct answers under social pressure (Sharma et al.); verify against sources/criteria instead (give it a checklist, per Anthropic self-check guidance).

---

## Analogies captured (with defensibility notes)
- **"Brilliant but new employee who lacks context"** (Anthropic's own) — defensible; matches the docs' framing of context-free competence. (source: best-practices page)
- **Golden rule = "would a minimally-briefed colleague understand this prompt?"** (Anthropic, verbatim) — defensible and directly quotable.
- **Prompt brittleness ≈ measurement-system variation (gauge R&R)** — our analogy for QE audience; defensible as an illustration of variance across phrasings (Sclar et al.), but don't push quantitatively.
- **Sycophancy ≈ a consultant who tells you what you want to hear because you pay the bills** — defensible: Sharma et al. show preference-training origin, i.e., the model is literally optimized on what raters liked.
- **21-words stat ≈ "a good prompt is a sentence or three, not a keyword search"** — defensible as reported user data (Google Oct 2024 guide), but note it is an observational average, not a causal target, and it was dropped from the newer edition.

## Could not verify / caveats
- Stanford Report article body (403 to fetcher) — headline, date (March 2026), and venue verified via search results only.
- Exact arXiv ID for OpenAI's Instruction Hierarchy paper (2404.13208) cited from prior knowledge; concept + Model Spec chain of command verified against model-spec.openai.com (2026-08-18 edition).
- EmotionPrompt's "115% on BIG-Bench" is the authors' own claim (relative improvement); no independent replication found — present as contested/unreliable.
- Whether the 2nd-edition Google guide has an official "edition date" — the PDF text contains no edition/date string I could extract; referred to by third parties as the 2nd edition (early 2026).
- UNVERIFIED: any claim that politeness/emotion effects hold on 2026 reasoning models — no credible study found either way.
