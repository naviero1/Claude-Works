# R1 — History and Milestones: AI → Generative AI → Agentic AI

Research notes for a primer module in a corporate training ("Prompt Engineering, Generative AI, and Agentic AI") for supplier/quality engineers and business professionals at a medical-device company.
Prepared 2026-08-21. All currency-sensitive claims carry an "as of" date. Facts that could not be confirmed against a primary or reputable source are flagged **UNVERIFIED**.

---

## 1. The eras framing (use this as the module's spine)

A four-stage framing is well supported by sources and is teachable:

1. **Rules era (1950s–1990s):** humans hand-code the logic ("if X then Y"). Expert systems.
2. **Learning era (1990s–2010s):** machines learn patterns from data instead of being given rules; deep learning (2012+) supercharges this.
3. **Generative era (2018/2022+):** models trained on internet-scale text/images can *create* new content and follow instructions (ChatGPT moment).
4. **Agentic era (2024+):** models stop just answering and start *doing* — using tools, browsing, writing code, completing multi-step work with limited supervision.

Support: an arXiv survey of AI agents describes the progression "from symbolic, rule-based automation to generative, goal-directed intelligence" through rule-based expert systems → ML decision-making → LLM-based agents (source: https://arxiv.org/pdf/2507.01376). McKinsey explicitly frames a shift from the gen-AI era to the "agentic era," in which AI moves "from information processing to autonomous action" and demands process redesign rather than plug-in tools (sources: https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage ; https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era).
Caveat for slides: the exact four-way split (rules → learning → generative → agentic) is a *synthesis* — no single canonical source uses those exact four labels, but each transition is individually well documented. Safe to present as "a useful way to see 70 years of AI," not as an official taxonomy.

**Scaling laws in one sentence:** Kaplan et al. (OpenAI, Jan 2020) showed that language-model performance improves as a smooth, predictable power law as you increase model size, data, and compute — which is why labs kept building bigger models: the payoff was forecastable, spanning "more than seven orders of magnitude" (source: https://arxiv.org/abs/2001.08361).
Business translation: "Bigger model + more data + more compute = predictably better results" turned AI progress from a research gamble into an engineering/investment roadmap.

---

## 2. Verified milestone timeline

### Classical AI era

- **1950 — Turing's "imitation game."** Alan Turing publishes "Computing Machinery and Intelligence" in the journal *Mind*, proposing to replace "Can machines think?" with a practical test: can a machine's conversation be distinguished from a human's? (source: https://doi.org/10.1093/mind/LIX.236.433 ; overview: https://plato.stanford.edu/entries/turing-test/)
  *Why it matters:* the founding question of the field — and the yardstick (indistinguishable conversation) that chatbots finally approached in 2022.

- **1956 — Dartmouth workshop; the term "artificial intelligence."** John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon propose a summer study at Dartmouth College "to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it" (1955 proposal; workshop held summer 1956) (source: http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf ; reprint: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904).
  *Why it matters:* the field — and the name "artificial intelligence" — is born as a deliberate research program, not science fiction.

- **1960s–1980s — Expert systems and AI winters.** AI is built by hand-coding rules from human experts (e.g., MYCIN for infections, XCON for computer configuration). Systems are brittle and costly to maintain; twice, hype outruns results and funding collapses — the "AI winters" (mid-1970s, triggered in part by the UK's critical Lighthill Report; and late 1980s when the expert-systems/LISP-machine market collapsed) (overview sources: https://www.britannica.com/technology/artificial-intelligence ; https://en.wikipedia.org/wiki/AI_winter — standard, stable history; specific system claims stable in AI textbooks e.g. Russell & Norvig).
  *Why it matters:* the recurring lesson for business audiences — hand-coded rules don't scale to messy reality, and over-promising causes winters. Also why seasoned engineers are rightly skeptical of hype.

### Machine learning and deep learning era

- **1990s–2000s — The machine learning shift.** The field moves from hand-coding rules to *learning patterns from data* (statistical methods, then practical successes in spam filtering, search ranking, recommendations). (Stable, standard history; e.g., https://www.britannica.com/science/machine-learning)
  *Why it matters:* the core conceptual flip your audience needs: instead of programming the answer, you program a system that finds the answer in examples — the same logic as SPC finding signal in process data.

- **Sept–Dec 2012 — AlexNet wins ImageNet (deep learning breakthrough).** Krizhevsky, Sutskever & Hinton's deep convolutional neural network wins the ImageNet image-recognition challenge with a 15.3% top-5 error rate vs 26.2% for the runner-up — a shocking margin, achieved by training a large neural net on GPUs (paper: https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html).
  *Why it matters:* proved that neural networks + big data + GPUs beat decades of hand-engineered approaches; kicked off the modern deep-learning investment wave (and NVIDIA's rise).

- **Jan 2013 — word2vec (word embeddings).** Mikolov et al. (Google) show words can be represented as vectors of numbers where meaning becomes geometry — famously king − man + woman ≈ queen (source: https://arxiv.org/abs/1301.3781).
  *Why it matters:* the moment language became math. Everything since — including how your prompts are processed and how RAG search works — rests on turning meaning into numbers.

- **2014–2016 — Sequence models.** Sutskever et al.'s sequence-to-sequence learning (https://arxiv.org/abs/1409.3215) and Bahdanau et al.'s *attention* mechanism for translation (https://arxiv.org/abs/1409.0473) let neural nets map one sequence to another (e.g., English→French); Google switches Translate to neural machine translation in 2016 (https://research.google/blog/a-neural-network-for-machine-translation-at-production-scale/).
  *Why it matters:* first commercial-grade proof that neural nets could handle *language in, language out* — the template for everything generative.

### Generative AI era

- **Jun 2017 — "Attention Is All You Need" (the Transformer).** Vaswani et al. (Google) drop recurrence entirely and build a network purely on attention (source: https://arxiv.org/abs/1706.03762). Key unlock: unlike previous word-by-word models, Transformers process all words in a sequence *in parallel*, so training can be spread across thousands of GPUs — the architecture scales with hardware.
  *Why it matters:* the "T" in GPT and ChatGPT. This single architecture made internet-scale training economically feasible; nearly every frontier model since 2018 is a Transformer variant.

- **Feb 2019 — GPT-2.** OpenAI shows that a Transformer trained simply to predict the next word on web text (1.5B parameters) can write coherent multi-paragraph text; OpenAI initially withholds the full model over misuse concerns — an early public AI-safety debate (source: https://openai.com/index/better-language-models/).
  *Why it matters:* first mainstream glimpse that "autocomplete at scale" produces something that looks like writing — and first mainstream debate about AI risk-vs-release.

- **May 2020 — GPT-3 and few-shot learning.** Brown et al., "Language Models are Few-Shot Learners": at 175B parameters, GPT-3 performs new tasks from just a few examples *in the prompt*, with no retraining (source: https://arxiv.org/abs/2005.14165).
  *Why it matters:* the birth of prompt engineering — programming the model with words and examples instead of code. Directly motivates the training's prompting module.

- **Jan–Mar 2022 — InstructGPT: instruction tuning + RLHF.** OpenAI fine-tunes GPT-3 with human feedback (reinforcement learning from human preferences) so it follows instructions helpfully; human raters preferred outputs of a 1.3B-parameter InstructGPT model over the 175B GPT-3 (sources: https://openai.com/index/instruction-following/ ; paper: https://arxiv.org/abs/2203.02155).
  *Why it matters:* raw prediction engines became usable assistants. Alignment/tuning, not just scale, made the ChatGPT moment possible — and a smaller well-tuned model beat a 100x larger raw one.

- **Nov 30, 2022 — ChatGPT launches.** OpenAI releases ChatGPT as a "research preview" — a chat interface on an InstructGPT-style model (source: https://openai.com/index/chatgpt/). It reaches an estimated 100M monthly users by January 2023 — two months — which UBS analysts called the fastest consumer-application ramp they had ever seen (TikTok took ~9 months; Instagram ~2.5 years) (sources: https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/ ; https://time.com/6253615/chatgpt-fastest-growing/).
  *Why it matters:* the interface, not a new model, changed everything — proof that packaging AI as conversation unlocks mass adoption. Start of the modern era for business.

- **Mar 14, 2023 — GPT-4.** OpenAI releases GPT-4, which accepts image + text input and passes a simulated bar exam around the top 10% of test takers (vs bottom 10% for GPT-3.5) (source: https://openai.com/index/gpt-4-research/).
  *Why it matters:* professional-grade performance on knowledge work; the moment many enterprises began serious pilots. Also mainstreamed **multimodality** (models that see images, not just text) — extended further by GPT-4o's real-time voice/vision (May 2024, https://openai.com/index/hello-gpt-4o/) and Google's Gemini line (Dec 2023, https://blog.google/technology/ai/google-gemini-ai/).

- **Jul 18, 2023 → 2024–25 — The open-weight wave (Llama).** Meta releases Llama 2 free for research and commercial use with Microsoft (source: https://about.fb.com/news/2023/07/llama-2/), followed by Llama 3 (Apr 2024) and Llama 4 (Apr 2025); Llama downloads pass ~1 billion by March 2025 and 1.2B by April 2025 (sources: https://techstartups.com/2025/04/29/metas-llama-ai-models-hit-1-2-billion-downloads-as-open-source-bet-starts-paying-off/ ; timeline: https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html). DeepSeek, Mistral, Qwen and OpenAI's gpt-oss (Aug 2025) extend the wave.
  *Why it matters:* companies can run capable models on their own infrastructure — relevant to regulated industries weighing data-residency, validation and vendor lock-in.

### Reasoning and agentic era

- **Sep 12, 2024 — OpenAI o1: "thinking" models.** OpenAI releases o1-preview, a model trained (via reinforcement learning) to generate a long internal chain of thought before answering, substantially better at math, science and code (sources: https://openai.com/index/introducing-openai-o1-preview/ ; https://www.bloomberg.com/news/articles/2024-09-12/openai-releases-o1-model-with-reasoning-capabilities).
  *Why it matters:* a second scaling dial — spend more compute *at answer time* ("thinking longer"), not just at training time. Reasoning models are what make reliable multi-step agents feasible.

- **Oct 22, 2024 — Computer use (Anthropic).** Anthropic ships a beta capability letting Claude operate a computer like a person — looking at the screen, moving the cursor, clicking, typing (source: https://www.anthropic.com/news/3-5-models-and-computer-use).
  *Why it matters:* first frontier-lab release of an AI that acts through the same interfaces humans use — the technical opening of the agentic era.

- **Nov 25, 2024 — Model Context Protocol (MCP).** Anthropic open-sources MCP, an open standard for connecting AI assistants to data sources and tools (content repositories, business apps, dev environments) — commonly described as "USB-C for AI" (source: https://www.anthropic.com/news/model-context-protocol). Subsequently adopted across the industry, incl. OpenAI and Google (adoption note: https://en.wikipedia.org/wiki/Model_Context_Protocol — secondary; industry adoption widely reported in 2025 press).
  *Why it matters:* the plumbing standard that lets one AI assistant safely plug into many enterprise systems instead of bespoke integrations for each — key to agents doing real work with company data.

- **Jan 20, 2025 — DeepSeek R1.** Chinese lab DeepSeek releases R1, an open-weight reasoning model rivaling o1 on math/coding benchmarks at a fraction of the training and usage cost, trained largely via reinforcement learning (sources: https://www.ibm.com/think/news/deepseek-r1-ai ; https://arxiv.org/abs/2502.02523). Its release triggered a major tech-stock selloff in late Jan 2025 (widely reported; e.g., Reuters/CNBC coverage at the time).
  *Why it matters:* showed frontier reasoning isn't a US-lab monopoly and that efficiency can substitute for brute-force spend — reset assumptions about AI costs and competition.

- **Jan 23, 2025 — OpenAI Operator (browser agent).** Research preview of an agent that uses its own browser to click, type, scroll and fill forms to complete tasks (source: https://openai.com/index/introducing-operator/). Operator was later folded into ChatGPT agent and shut down Aug 31, 2025 (source: https://en.wikipedia.org/wiki/OpenAI_Operator — secondary).
  *Why it matters:* the browser-agent pattern — AI doing web tasks end-to-end — arrived in consumer products; also a lesson in how fast agent products iterate/merge.

- **Feb 24, 2025 (research preview) / May 22, 2025 (GA) — Claude Code (agentic coding).** Anthropic launches Claude Code, a terminal-based agent that reads a codebase, edits files, runs tests and commits — released alongside Claude 3.7 Sonnet, generally available with Claude 4 (sources: https://www.anthropic.com/news/claude-3-7-sonnet ; https://www.anthropic.com/news/claude-4). Reported to have reached ~$1B annualized run-rate revenue within months of GA (**UNVERIFIED against a primary source** — reported in secondary trackers, e.g. https://www.scriptbyai.com/claude-code-timeline/; treat as "reported").
  *Why it matters:* the first agentic workflow to reach mass professional adoption — software engineering became the proving ground for delegating real multi-step work to AI.

- **Jul 17, 2025 — ChatGPT agent (general work agent).** OpenAI unifies Operator's browser control, deep research's web synthesis, and ChatGPT's conversation into one agent with a virtual computer: it can build slide decks and spreadsheets, browse, run code and complete multi-step tasks (sources: https://openai.com/index/introducing-chatgpt-agent/ ; https://techcrunch.com/2025/07/17/openai-launches-a-general-purpose-agent-in-chatgpt/).
  *Why it matters:* agents moved from developer tools to general office work inside the world's most-used AI product.

- **Jan 12, 2026 — Claude Cowork (agentic AI for general knowledge work).** Anthropic launches Claude Cowork (research preview): Claude Code's agentic foundation packaged for non-technical knowledge workers — it works with users' files, folders and apps to complete multi-step tasks without constant prompting; expanded to cloud/mobile/web by mid-2026 (sources: https://www.nbcnews.com/tech/tech-news/anthropic-will-make-claude-cowork-available-users-cloud-rcna353218 ; https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/ ; analyst: https://aragonresearch.com/anthropic-claude-cowork/). Note: Anthropic's own launch post exists on anthropic.com/news but was not directly fetched — dates above corroborated by NBC/TechCrunch/analyst coverage.
  *Why it matters:* the moment agentic AI was explicitly aimed at *your audience* — quality engineers, supply chain, business professionals — not just programmers. Directly frames the training's "agentic AI" module.

---

## 3. Striking, verifiable adoption stats (as of Aug 2026)

1. **Fastest consumer app ramp ever (2023):** ChatGPT hit an estimated 100M monthly users in 2 months (Jan 2023). TikTok took ~9 months, Instagram ~2.5 years (UBS via Reuters, Feb 1, 2023: https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/).
2. **ChatGPT scale today:** 900M+ weekly active users and ~50M paying subscribers, announced Feb 27, 2026 — up from 800M WAU (Oct 2025) and ~400M a year before that (source: https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users). Reports of "nearing 1B WAU" by late Jul 2026 are **UNVERIFIED** (The Information, not confirmed by OpenAI).
3. **Google Gemini app: 1B monthly active users**, announced by Sundar Pichai Aug 11, 2026 — Google's fastest-growing product ever (sources: https://blog.google/innovation-and-ai/products/gemini-app/one-billion-monthly-users/ ; https://techcrunch.com/2026/08/11/googles-gemini-app-surges-to-one-billion-users/).
4. **Enterprise adoption is mainstream, agents are not (yet):** per Stanford HAI's 2026 AI Index, 88% of organizations use AI in at least one business function, ~70% use generative AI in at least one function — but AI *agent* deployment remains in the single digits across most business functions, and fewer than 10% of firms have scaled AI to meaningful operational levels (sources: https://hai.stanford.edu/ai-index/2026-ai-index-report ; summary: https://aibusinessweekly.net/p/stanford-ai-index-2026-enterprise-adoption-productivity). Great tension slide: "everyone uses AI; almost no one has industrialized it — that gap is your opportunity."
5. **Open-weight scale:** Meta's Llama models passed 1.2B downloads by Apr 2025 (source: https://techstartups.com/2025/04/29/metas-llama-ai-models-hit-1-2-billion-downloads-as-open-source-bet-starts-paying-off/).

---

## 4. Analogies worth using (with defensibility notes)

- **"Rules era = writing the SOP yourself; learning era = the system deriving the SOP from thousands of examples."** Defensible; maps exactly onto the rules→ML shift, resonates with quality engineers.
- **"Scaling laws made AI progress forecastable — like a process capability curve for intelligence."** Defensible as a loose analogy; power-law loss curves are genuinely predictable (Kaplan 2020), but don't claim capability *behaviors* are perfectly predictable (emergent abilities are not).
- **"MCP is USB-C for AI."** Widely used, including in coverage of Anthropic's launch; technically defensible as "one standard port replacing custom cables/integrations" (source: https://www.anthropic.com/news/model-context-protocol coverage; analogy in https://www.vktr.com/ai-technology/inside-anthropics-model-context-protocol-mcp-the-new-ai-data-standard/).
- **"An LLM is autocomplete trained on the internet; RLHF is the finishing school that turned it into an assistant."** Defensible at primer level (next-token prediction + preference tuning per InstructGPT); avoid implying it merely memorizes.
- **"Reasoning models: paying the model to think longer, like giving an engineer a day instead of a minute."** Defensible; test-time compute scaling is exactly the mechanism o1 introduced (https://openai.com/index/learning-to-reason-with-llms/).
- **Chatbot → agent: "an answer engine vs a junior employee you delegate a task to (who still needs review)."** Defensible and matches McKinsey's information-processing → autonomous-action framing; keep the "still needs review" clause for a regulated-industry audience.

## 5. Verification caveats

- Claude Code "$1B annualized run-rate": reported in secondary sources only — **UNVERIFIED**, label as "reported" if used.
- ChatGPT "nearing 1B WAU" (Jul 2026): **UNVERIFIED**; use the confirmed 900M (Feb 2026) figure.
- DeepSeek-triggered market selloff (Jan 2025): widely reported at the time (Reuters/CNBC); specific figures (e.g., NVIDIA's one-day loss ~$590B) not re-verified here — verify before quoting numbers.
- Expert-systems specifics (MYCIN, XCON) and AI-winter dates: standard textbook history (Russell & Norvig; Britannica); no primary link fetched — safe at primer level.
- The four-era framing is a synthesis (Section 1 caveat); present as pedagogy, not official taxonomy.
- Anthropic's own Claude Cowork launch post URL not directly fetched; launch date Jan 12, 2026 rests on NBC News/TechCrunch/Aragon coverage.
