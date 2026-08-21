# R2 — Core Technical Concepts Every AI User Should Understand
**Research notes for "Prompt Engineering, Generative AI, and Agentic AI" training (medical-device supplier/quality engineers + business professionals).**
Prepared 2026-08-21. All product/model claims verified against sources on this date unless marked UNVERIFIED or "reported by third party."

---

## 1. Tokens & Tokenization

**Definition.** LLMs don't read letters or whole words — they read *tokens*: chunks of text (word pieces, whole common words, punctuation, spaces) mapped to numeric IDs from a fixed vocabulary. The model's entire world is a sequence of these IDs; it predicts the next token ID, one at a time.

**Rules of thumb (English), per OpenAI's help article** (source: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them):
- 1 token ≈ **4 characters** of English text
- 1 token ≈ **0.75 words** (so 100 tokens ≈ 75 words)
- Common word = 1 token ("apple"); rarer words split ("hamburger" → "ham" + "bur" + "ger")
- Non-English languages and dense technical text usually cost **more** tokens per word.

**Why models are "bad at counting letters."** The model never sees individual letters — "strawberry" arrives as one or two token IDs, not as s-t-r-a-w-b-e-r-r-y. Asking it to count the r's is like asking someone to count the letters in a word they only ever heard spoken, never saw written. Mechanism grounded in the tokenization doc above (source: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them). Same reason models historically struggled with reversing strings, precise character-level edits, and arithmetic on long digit strings.

**Why pricing and limits are in tokens.** Compute cost scales with tokens processed (input) and generated (output), so every major API prices per million tokens — e.g., as of Aug 2026: Claude Fable 5 at $10 input / $50 output per million tokens (source: https://www.anthropic.com/news/claude-fable-5-mythos-5 via search summary; also https://openrouter.ai/anthropic/claude-fable-5), Claude Sonnet 5 at $2 / $10 introductory until Sept 1, 2026 (source: https://www.anthropic.com/news/claude-sonnet-5), GPT-5.6 Sol at $5 / $30 with a long-context surcharge ($10/$45) above 272K input tokens (source: https://openrouter.ai/openai/gpt-5.6-sol and https://www.requesty.ai/models/openai/gpt-5.6-sol — third-party trackers; vendor page not directly fetched). Output tokens cost ~5x input across most vendors because generation is serial and slower.

**Analogy (defensible).** Tokens are like LEGO bricks of text: common words are single pre-molded bricks; unusual words get built from smaller pieces. You pay by the brick, not by the sentence. Defensible — it accurately captures subword vocabulary and per-unit pricing.

**Practical implication.** Paste-heavy prompts (long SOPs, spec sheets) consume budget and context fast; a 50-page document is roughly 25,000–35,000 tokens. Don't ask a model to do character-exact work (letter counts, checksum-style validation) — use it for language, use software for characters.

---

## 2. Context Window

**Definition.** The context window is the model's working memory for one conversation/request: the maximum number of tokens the model can attend to at once. Everything must fit inside it: the **system prompt**, the **entire chat history (both sides)**, **attached files**, **tool/search results**, and the **response being generated** (source: Anthropic context-windows docs, https://platform.claude.com/docs/en/build-with-claude/context-windows — page family verified via platform.claude.com docs; and OpenAI key concepts, https://developers.openai.com/api/docs/concepts). It is working memory, not storage: nothing persists between fresh chats unless a separate memory feature re-inserts it.

**Context window sizes of major models — verified as of Aug 2026:**

| Model (latest flagship line) | Context window | Max output | Source |
|---|---|---|---|
| Claude Fable 5 (Anthropic, rel. Jun 9, 2026) | **1M tokens** (default, no long-context surcharge) | 128K | https://www.anthropic.com/news/claude-fable-5-mythos-5 ; https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 |
| Claude Sonnet 5 (Anthropic, rel. Jun 30, 2026) | **1M tokens** (default and max) | 128K | https://www.anthropic.com/news/claude-sonnet-5 ; https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5 |
| GPT-5.6 Sol (OpenAI frontier family Sol/Terra/Luna, rel. Jul 9, 2026) | **~1.05M tokens** | 128K | https://openrouter.ai/openai/gpt-5.6-sol (third-party tracker); family confirmed via https://help.openai.com/en/articles/9624314-model-release-notes (page exists; direct fetch blocked 403 — details via search snippets) |
| GPT-5.4 (OpenAI, rel. Mar 5, 2026) | 272K standard; **~1M experimental** (opt-in in API/Codex) | 128K | https://openai.com/index/introducing-gpt-5-4/ ; https://www.datacamp.com/blog/gpt-5-4 |
| Gemini 3.1 Pro (Google, rel. Feb 19, 2026; newest Pro tier — no 3.5 Pro released as of Aug 21, 2026) | **1,048,576 tokens** | 65,536 | https://ai.google.dev/gemini-api/docs/models (model list verified); https://www.marktechpost.com/2026/02/19/google-ai-releases-gemini-3-1-pro-with-1-million-token-context-and-77-1-percent-arc-agi-2-reasoning-for-ai-agents/ ; "no 3.5 Pro yet": https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/ |
| DeepSeek V4 (open-weight MoE, rel. Apr 24, 2026; V4-Pro & V4-Flash) | **1M tokens** | 384K reported | https://api-docs.deepseek.com/news/news260424/ ; https://huggingface.co/blog/deepseekv4 |
| Qwen3.5 family (Alibaba, rel. Feb 2026, Apache 2.0) / Qwen3.8-Max (rel. Aug 3, 2026, 2.4T MoE) | **1M tokens** (flagship variants; some mid-size variants 256K) | varies | https://openrouter.ai/qwen/qwen3.5-plus-20260420 ; https://alternativeto.net/news/2026/8/alibaba-launches-qwen3-8-max-with-2-4t-parameters-and-1m-token-context-window/ |
| Kimi K3 (Moonshot AI, rel. Jul 16, 2026, open weights Jul 26; 2.8T MoE) | **1,048,576 tokens** | ~975K reported | https://openrouter.ai/moonshotai/kimi-k3 ; https://en.wikipedia.org/wiki/Kimi_(chatbot) |

Headline: by Aug 2026 the ~1M-token context window is the de facto flagship standard across US and Chinese labs. Caveat for the audience: **consumer chat apps often enforce smaller effective limits than the API number** (e.g., reporting that Gemini's app tier limits are far below 1M: https://www.smithstephen.com/p/geminis-million-token-promise-you — third-party, illustrative).

**"Lost in the middle" / long-context degradation.** Liu et al. 2023 (Stanford et al., TACL) showed model accuracy is highest when relevant information sits at the **beginning or end** of a long context and drops significantly when it's **in the middle** — a U-shaped curve (source: https://arxiv.org/abs/2307.03172). Follow-on work shows degradation persists in modern long-context models when the task requires more than literal keyword matching — e.g., NoLiMa (2025) found sharp performance drops well below advertised context lengths (source: https://arxiv.org/abs/2502.05167 — paper identity verified from training knowledge; exact figures not re-fetched, treat specific percentages as UNVERIFIED). Net: "fits in the window" ≠ "used reliably."

**Analogy (defensible).** The context window is a desk, not a filing cabinet: everything you and the model are working from must be physically on the desk, and papers buried mid-pile get overlooked. Defensible — matches both the capacity limit and the positional-attention findings.

**Practical tips (vendor-verified).** Anthropic's long-context guidance: put long documents (~20K+ tokens) **at the top** of the prompt, put your **question/instructions at the end** (up to ~30% quality improvement in Anthropic's tests), wrap multiple documents in labeled tags, and ask the model to **quote relevant passages first** (source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips). Also: start a fresh chat when switching topics (stale history pollutes attention and costs tokens), and summarize long threads into a new chat instead of continuing forever.

---

## 3. Parameters vs Training Data, the Training Pipeline, and Knowledge Cutoff

**Parameters vs training data.** Training data is the text corpus the model learned from (trillions of tokens); parameters are the billions of learned numerical weights that store the *compressed statistical patterns* of that data — the data itself is not stored or retrievable verbatim. Analogy (defensible): parameters are to training data what a chef's skill is to every meal they ever tasted — the experience shaped the skill, but the meals aren't stored in the chef. Scale reference points, all open-weight and verified: DeepSeek V4-Pro = 1.6T total parameters (source: https://api-docs.deepseek.com/news/news260424/), Kimi K3 = 2.8T (source: https://openrouter.ai/moonshotai/kimi-k3), Qwen3.8-Max = 2.4T (source: https://datanorth.ai/news/alibaba-releases-qwen3-8-max). Frontier closed models (GPT-5.x, Claude 5, Gemini 3.x) do not disclose parameter counts — UNVERIFIED by design.

**Pipeline in 3 sentences.** (1) **Pretraining**: the model learns next-token prediction over a huge internet-scale corpus, acquiring language, facts, and reasoning patterns. (2) **Instruction tuning (SFT)**: it is then trained on curated example dialogues so it follows instructions instead of just continuing text. (3) **RLHF/RLAIF**: human (or AI) preference rankings train a reward signal that further tunes the model to be helpful, honest, and harmless. (Canonical source: InstructGPT, Ouyang et al. 2022, https://arxiv.org/abs/2203.02155 — stable, foundational paper.)

**Knowledge cutoff.** The date after which the training data contains ~nothing; the model's built-in knowledge freezes there (typically 6–12 months before release). Example: Claude Fable 5 (released June 2026) has a **January 2026** training cutoff (source: Anthropic model docs, https://platform.claude.com/docs/en/about-claude/models — cutoff value consistent with Anthropic's published model overview; specific page not re-fetched, treat exact month as high-confidence but verify on the docs page before slides). **Web search changes this in practice, not in principle**: search/RAG injects fresh documents into the context window at question time, so the model can answer about yesterday — but the retrieved text, not the model's weights, is the source, which is exactly why search-grounded answers can cite links. Practical implication: for anything regulatory, price, or standards-related (e.g., "current FDA guidance"), require the tool to search/cite, never trust built-in recall.

---

## 4. Embeddings & Vector Similarity

**Definition.** An embedding turns a piece of text into a long list of numbers (a vector — commonly 1,536 or 3,072 dimensions in OpenAI's text-embedding-3 models; source: https://platform.openai.com/docs/guides/embeddings — stable documented values) positioned so that **texts with similar meaning get nearby vectors**, even with zero word overlap ("supplier audit finding" lands near "vendor inspection nonconformance"). Similarity is computed geometrically (cosine similarity: the angle between vectors).

**Analogy (defensible).** An embedding is a GPS coordinate for meaning: every sentence gets an address in a giant map of ideas, and "nearby addresses" mean "similar meaning." Defensible — it's literally a learned geometric space; the only simplification is that the map has thousands of dimensions, not two.

**Practical implication.** Embeddings are why "semantic search" in modern document tools finds relevant SOPs and CAPAs without exact keyword matches — and they're the retrieval engine inside RAG (next section). Users don't handle embeddings directly, but understanding them explains why search sometimes returns *conceptually* related but *wrong* documents.

---

## 5. RAG (Retrieval-Augmented Generation)

**Definition & loop.** RAG bolts a search step onto generation: (1) **Retrieve** — embed the user's question, find the most similar chunks in a vector index of your documents; (2) **Augment** — paste those chunks into the prompt as context; (3) **Generate** — the model answers *from the supplied text*, ideally with citations. Coined in Lewis et al. 2020 (source: https://arxiv.org/abs/2005.11401 — stable foundational paper); modern enterprise practice per Anthropic's contextual-retrieval work (source: https://www.anthropic.com/news/contextual-retrieval).

**Why enterprises use RAG vs alternatives (as of Aug 2026):**
- **vs fine-tuning:** RAG adds *knowledge* cheaply and updates instantly (re-index a document in minutes); fine-tuning bakes in *behavior/style*, is slow and per-model, and is poor at reliably adding facts.
- **vs long context (now 1M tokens):** stuffing everything into context works for tens of documents, but a QMS with millions of pages can't fit; per-query cost scales with tokens sent (and some vendors surcharge long context — e.g., GPT-5.6 Sol above 272K input, source: https://openrouter.ai/openai/gpt-5.6-sol), while RAG sends only the relevant few chunks.
- **Freshness:** index updates beat retraining.
- **Citations:** answers can point to the exact source paragraph — essential for audit trails in regulated industries.
- **Access control:** retrieval can enforce per-user document permissions; a fine-tuned model can't "un-know" restricted content for certain users.

**When RAG fails.** If retrieval brings back the wrong, outdated, or superseded chunk, the model will still fluently synthesize an answer from it — **bad retrieval = confident wrong answer**, delivered with citations that make it *look* trustworthy. Classic failure modes: wrong document version retrieved (rev B instead of rev D of an SOP), question phrased in terms not present in the corpus, answer that requires combining chunks that were never retrieved together. Anthropic reports traditional RAG can lose context when chunking; contextual retrieval reduced retrieval failure rates by 49% (67% with reranking) (source: https://www.anthropic.com/news/contextual-retrieval).

**Analogy (defensible).** RAG is an open-book exam: the student (model) still writes the answer, but from pages a librarian fetched. If the librarian pulls the wrong page, the student confidently writes a well-formatted wrong answer — and cites the wrong page. Defensible and captures the failure mode.

**Practical implication.** When a RAG-based tool (internal chatbot, Copilot over SharePoint) answers, **check the citations, not just the prose** — the citation being irrelevant or outdated is the tell.

---

## 6. Hallucination

**Mechanism.** LLMs are trained to predict the most *plausible* next token, not the most *true* one — fluency and truth usually coincide (that's why they're useful) but diverge exactly where the training data is thin: rare facts, precise citations, numbers, names. OpenAI's 2025 research paper formalizes this: hallucinations are a statistically expected outcome of standard training, and are sustained because mainstream benchmarks **reward confident guessing over saying "I don't know"** — models are optimized to be good test-takers (source: https://openai.com/index/why-language-models-hallucinate/ ; paper: https://arxiv.org/abs/2509.04664).

**Calibration.** A calibrated model's confidence matches its accuracy. Base models are reasonably calibrated on next-token probabilities; post-training for helpfulness tends to make expressed confidence *sound* uniformly high — the model's fluent, assertive tone carries no information about reliability (supported by the OpenAI paper above). Teachable line: **fluency is not evidence.**

**Why RAG + citations + verification mitigate.** RAG grounds generation in retrieved text (the model paraphrases sources instead of free-recalling); citations create a checkable trail; and human verification closes the loop because checking a quoted source is far easier than fact-checking free prose. None eliminates hallucination — see §5's "confident wrong answer" failure — they convert an unverifiable claim into a verifiable one.

**Analogy (defensible).** The model is an improv actor with encyclopedic experience: it never breaks character to say "I don't know" unless trained/prompted to — the show must go on, so it fills gaps with the most plausible-sounding line. Defensible as a description of plausibility-optimized decoding; note it's about the objective, not intent (models don't "lie").

**Practical implication (medical-device audience).** Treat every uncited factual claim — standards clauses (ISO 13485, 21 CFR 820), dates, numbers, supplier data — as a draft requiring verification. Ask for citations explicitly; prompt "if you are not sure, say so" (helps, doesn't cure).

---

## 7. Temperature & Sampling (one paragraph)

At each step the model produces a probability distribution over every possible next token; **sampling** picks one, and **temperature** controls how adventurous that pick is — low temperature (→0) almost always takes the top choice (consistent, repetitive), higher temperature spreads probability toward less likely tokens (varied, creative, riskier). Ranges as of Aug 2026: Claude API temperature 0–1.0, default 1.0 (source: https://platform.claude.com/docs/en/api/messages via https://platform.claude.com/docs/en/claude_api_primer); OpenAI API 0–2.0, and OpenAI's reasoning models lock temperature entirely; on the newest Claude models (4.7+), temperature is deprecated in favor of the default (source: search-verified via https://platform.claude.com/docs/en/claude_api_primer and community docs — flag as "check current API docs" before publishing). **Why the same prompt gives different answers:** sampling is deliberately random above temperature 0, and even *at* temperature 0 outputs aren't guaranteed identical because of floating-point/batching nondeterminism in inference servers (source: Thinking Machines, "Defeating Nondeterminism in LLM Inference," Sept 2025, https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ — cited from training knowledge; URL slug UNVERIFIED, finding widely reported). Analogy (defensible): temperature is a creativity dial on a word-by-word dice roll — cold dice always land on the likeliest word; hot dice sometimes land on surprising ones.

---

## 8. Reasoning / Extended-Thinking Models

**What they do differently.** Before answering, they generate internal chain-of-thought tokens — drafting, checking, and revising — spending more compute at answer time ("test-time compute") on harder problems (origin: OpenAI o1, https://openai.com/index/learning-to-reason-with-llms/ — stable). As of Aug 2026 this is mainstream and increasingly *adaptive* rather than a separate model: Claude Sonnet 5/Fable 5 use adaptive thinking with selectable effort levels (low/medium/high/max/x-high) (source: https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5); OpenAI's GPT-5.x routes between fast and thinking modes (source: https://openai.com/index/introducing-gpt-5-2/); DeepSeek/Qwen/Kimi flagships all ship thinking modes (sources in §2 table).

**Cost/latency tradeoff.** Thinking tokens are billed as **output tokens** (the expensive kind) even when you only see a summary of them, and they add seconds-to-minutes of latency (source: Anthropic extended-thinking docs, https://platform.claude.com/docs/en/build-with-claude/extended-thinking). A hard question can silently cost 5–20x a simple one.

**When to use.** Multi-step analysis, math, root-cause analysis, code, tricky tradeoff documents, anything where being wrong is expensive. Skip it for lookups, reformatting, summarization, and casual drafting — you pay in time and tokens for reasoning you don't need.

**Analogy (defensible).** Kahneman's System 1 vs System 2: fast intuitive answering vs slow deliberate working-through. Widely used (including by vendors) and defensible as a behavioral description — but note the model isn't literally "thinking"; it's generating intermediate tokens that improve the final prediction.

---

## 9. Mixture of Experts (two sentences)

A Mixture-of-Experts model splits its feed-forward layers into many specialized "expert" sub-networks and, for each token, a router activates only a few of them — so the model has a huge total parameter count but only a small fraction does work on any given token. Examples: Mixtral 8x7B uses 46.7B total parameters but only ~12.9B active per token (source: https://mistral.ai/news/mixtral-of-experts/ — stable, Dec 2023), and DeepSeek V4-Pro has 1.6T total with just **49B active per token** (V4-Flash: 284B total / 13B active) (source: https://api-docs.deepseek.com/news/news260424/ and https://huggingface.co/blog/deepseekv4), which is how trillion-parameter open models stay affordable to run. *Analogy (defensible): a hospital with many specialists where triage routes each patient to only the two or three relevant doctors — capacity of the whole hospital, cost of a small clinic per visit. Practical implication: this is why "bigger total parameters" no longer means proportionally slower or pricier.*

---

## 10. Fine-Tuning

**Definition.** Continuing training on your own examples so the model's *weights* change — producing a custom model variant that reliably reproduces a desired behavior, format, tone, or narrow skill. Current offerings (as of Aug 2026): OpenAI supports supervised fine-tuning (SFT) and preference tuning (DPO) on GPT-4.1/GPT-4.1-mini and reinforcement fine-tuning (RFT) on o4-mini — the GPT-5.4+ flagship family is **not** fine-tunable (source: https://developers.openai.com/api/docs/guides/supervised-fine-tuning and https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning); Anthropic offers Claude Haiku fine-tuning via Amazon Bedrock (source: https://aws.amazon.com/bedrock/anthropic/ — check current model list); open-weight models (Qwen, DeepSeek, Kimi) can be fine-tuned freely.

**When companies actually need it** (vendor guidance-aligned; see OpenAI fine-tuning docs above):
- Consistent **style/format/persona** at scale (e.g., always emit your exact report structure) that prompting can't hold reliably;
- **Distilling** a big model's behavior into a small, cheap, fast model for high-volume tasks;
- Narrow **classification/extraction** tasks with thousands of labeled examples;
- Domain **jargon/tone** the base model garbles.

**When they don't** (most of the time): adding company knowledge (→ RAG, §5), freshness (→ search/RAG), one-off or evolving tasks (→ prompting with examples), and anything achievable with a good system prompt — the order of escalation is **prompt → RAG → fine-tune**, cheapest and most reversible first. Fine-tuning does not reliably teach new *facts* and can degrade general ability; it also creates a maintenance burden (retune on every base-model upgrade).

**Analogy (defensible).** Prompting is giving instructions to a skilled temp; RAG is handing the temp your binder of procedures; fine-tuning is sending them to a training course that permanently changes how they work. Defensible — correctly places knowledge in the binder (context) vs habits in the training (weights).

**Practical implication.** If someone proposes "let's fine-tune a model on our QMS," the right first question is: "is this a *knowledge* problem (RAG) or a *behavior* problem (maybe fine-tune)?" Most enterprise cases are knowledge problems.

---

## Verification Notes & Gaps
- **Verified via primary/vendor sources:** OpenAI token rules of thumb; Claude Fable 5 & Sonnet 5 context/pricing/release dates; GPT-5.4 announcement & context; Gemini model lineup (3.1 Pro newest Pro tier, no 3.5 Pro as of Aug 21, 2026); DeepSeek V4 specs (vendor API docs); "Lost in the Middle" paper; Anthropic long-context tips (incl. the ~30% figure); Anthropic extended-thinking billing; OpenAI hallucination paper; OpenAI fine-tuning model availability; Lewis 2020 RAG paper; Mixtral MoE figures; contextual retrieval figures.
- **Verified via reputable third-party trackers only (vendor page not directly fetched):** GPT-5.6 Sol context (~1.05M) and pricing ($5/$30, long-context surcharge) — help.openai.com blocked direct fetch (HTTP 403); OpenRouter/Requesty agree. Kimi K3 and Qwen3.5/3.8-Max specs (OpenRouter/Wikipedia/news).
- **UNVERIFIED / flag before slide use:** exact month of Claude Fable 5 knowledge cutoff (Jan 2026 — high confidence, confirm on platform.claude.com model page); NoLiMa's specific percentage drops; Thinking Machines nondeterminism blog exact URL; DeepSeek V4 exact per-token pricing ($0.87/M output figure is from morphllm.com, third party); claim that Claude 4.7+ deprecates the temperature parameter (from docs-adjacent sources — confirm in current API reference).
- **Landscape note:** OpenAI's model line moved fast in 2026 (GPT-5.2 → 5.3 → 5.4 → 5.5 → 5.6 Sol/Terra/Luna family, flagship as of Aug 2026); slides should say "GPT-5.x family" and date every number.
