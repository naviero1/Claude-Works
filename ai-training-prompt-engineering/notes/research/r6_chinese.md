# R6 — Chinese LLMs: What They Brought, State of Play (Aug 2026), and Governance Caveats

Research notes for corporate AI training (supplier/quality engineers + business professionals, medical-device company). All facts carry inline source URLs and "as of" dates. Items that could not be confirmed in a primary or reputable secondary source are marked **UNVERIFIED** or **[secondary sources only]**. Research date: 2026-08-21.

---

## 1. The headline story in one paragraph

In January 2025 a little-known Chinese lab (DeepSeek) released an open-weights reasoning model that roughly matched OpenAI's best at a claimed fraction of the training cost, wiping a record ~$589B off Nvidia's market value in one day. Over the following 18 months, Chinese labs (DeepSeek, Alibaba Qwen, Moonshot Kimi, Zhipu GLM, MiniMax, Baidu, Tencent) became the dominant force in *open-weight* AI — permissively licensed models anyone can download, self-host, and fine-tune — while US labs kept a narrow lead at the closed frontier. Stanford's AI Index 2026 puts the US-China top-model performance gap at ~2.7% (Elo), down from 17.5–31.6 percentage points on major benchmarks in 2023 (source: https://thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap). For a regulated company the key teaching distinction is: **the consumer apps (chat.deepseek.com, Kimi app) send data to China and are widely banned on government devices; the open weights are files you can run entirely on your own infrastructure — two very different risk profiles.**

---

## 2. DeepSeek

### 2.1 The "DeepSeek moment" (January 2025)
- DeepSeek-R1 released **Jan 20, 2025** under an **MIT license**: a reasoning model that matched or exceeded OpenAI o1 on core reasoning benchmarks at release — the first open-weight model to do so (sources: https://fireworks.ai/blog/deepseek-r1-deepdive; https://openrouter.ai/deepseek/deepseek-r1).
- **Jan 27, 2025**: Nvidia lost **$589 billion in market cap in one day — the largest single-day value loss of any company in history at that time**; the stock fell 17%, Nasdaq 100 fell ~3% (sources: https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html; https://www.forbes.com/sites/dereksaul/2025/01/27/biggest-market-loss-in-history-nvidia-stock-sheds-nearly-600-billion-as-deepseek-shakes-ai-darling/).
- Trigger: DeepSeek's claim that its V3 base model cost ~$5.6M to train vs >$100M for GPT-4, plus R1 matching o1 (source: https://finance.yahoo.com/news/nvidia-stock-plummets-loses-record-589-billion-as-deepseek-prompts-questions-over-ai-spending-135105824.html). Marc Andreessen called it "one of the most amazing and impressive breakthroughs I've ever seen" (same Yahoo/CNBC coverage).

### 2.2 Architecture (V3/R1) — the teachable mechanics
- DeepSeek-V3 and R1: **Mixture-of-Experts (MoE), 671B total parameters, only ~37B active per token** — i.e., the model is a large "team of specialists" but consults only a few per word, so inference cost tracks the 37B, not the 671B (sources: https://arxiv.org/html/2412.19437v1 (V3 technical report); https://fireworks.ai/blog/deepseek-r1-deepdive).
- R1 also shipped **six distilled dense models (1.5B–70B, built on Qwen2.5 and Llama bases)** — "reasoning taught to small models" — small enough to run on a laptop/single GPU (source: https://fireworks.ai/blog/deepseek-r1-deepdive).

### 2.3 The training-cost claim — always teach the caveat
- The $5.576M figure = **final pre-training run only**: 2.788M H800 GPU-hours at an assumed $2/GPU-hour rental, per DeepSeek's own paper, which explicitly excludes "prior research and ablation experiments" (source: https://arxiv.org/html/2412.19437v1).
- SemiAnalysis estimated DeepSeek's total hardware spend at **well over $500M** (some coverage cites ~$1.6B TCO across its GPU fleet) — the $5.6M is a real efficiency signal but not the cost of building the lab (sources: https://tech.slashdot.org/story/25/01/28/1315215/deepseek-has-spent-over-500-million-on-nvidia-chips-despite-low-cost-ai-claims-semianalysis-says; https://techstrong.ai/agentic-ai/early-critic-of-deepseek-says-model-cost-was-1-6-billion-not-5-6-million/; context: https://stratechery.com/2025/deepseek-faq/).
- Analogy (defensible): "$5.6M was the fuel for the winning race lap, not the cost of building the car, the garage, and all the practice laps."

### 2.4 Current status — V4 (as of Aug 2026)
- **Apr 24, 2026**: DeepSeek unveiled preview versions of its new flagship **V4-Flash and V4-Pro** series, "a year after upending Silicon Valley," touting top-tier coding benchmarks and a "Hybrid Attention Architecture" for long-conversation memory (source: Bloomberg, https://www.bloomberg.com/news/articles/2026-04-24/deepseek-unveils-newest-flagship-a-year-after-ai-breakthrough).
- Reported specs at preview: v4-pro ~1.6T total / 49B active; v4-flash ~284B / 13B active, both open-weight MoE (Bloomberg summary above; secondary sources give slightly different totals).
- V4's earlier delay was attributed (by a CCTV-affiliated account) to a strategic shift toward **domestic Chinese chips** (source: Bloomberg, https://www.bloomberg.com/news/articles/2026-04-26/deepseek-v4-delay-shows-shift-to-china-chips-cctv-account-says).
- **Confirmed on Hugging Face as of Aug 21, 2026**: `DeepSeek-V4-Pro-0813` (~1.7T params, updated ~Aug 13, 2026) and `DeepSeek-V4-Flash-0731` (304B params, 2.83M downloads) are published open-weight on the official deepseek-ai org (source: https://huggingface.co/deepseek-ai).
- **[secondary sources only]**: MIT licensing for V4 weights, GA dates (Flash Jul 31 / Pro Aug 12–13, 2026), and a claimed 75% V4-Pro price cut on May 31, 2026 come from SEO-grade sites (e.g., https://www.sitepoint.com/deepseek-v4-released-whats-new-in-the-latest-model-2026/) — treat exact pricing/license details as UNVERIFIED until checked against api-docs.deepseek.com.

### 2.5 Consumer-app privacy problems (the cautionary half of the story)
- DeepSeek's own privacy policy stated user data is stored **on servers in China** (source: https://therecord.media/italy-blocks-chinese-ai-tool-deepseek-over-privacy-concerns).
- **Italy (Garante), Jan 2025**: first Western regulator to block the DeepSeek app after answers on data practices it called "completely insufficient"; DeepSeek claimed EU law didn't apply to it; app removed from Italian app stores (sources: https://therecord.media/italy-blocks-chinese-ai-tool-deepseek-over-privacy-concerns; https://www.euronews.com/next/2025/01/31/deepseek-ai-blocked-by-italian-authorities-as-others-member-states-open-probes).
- **Australia, Feb 2025**: banned DeepSeek from **all government devices** as "an unacceptable level of security risk" (source: https://www.malaymail.com/news/world/2025/02/05/australia-bans-chinas-deepseek-ai-program-from-govt-devices-oversecurity-concerns/165528).
- Additional bans/restrictions through 2025: South Korea (new downloads suspended), Taiwan, US federal bodies (Congress, Navy, NASA) and multiple US states for government devices (roundups: https://redact.dev/blog/deepseek-ai-ban-privacy-concerns/; https://www.malaymail.com/news/tech-gadgets/2025/06/29/global-scrutiny-grows-as-nations-curb-access-to-deepseek-amid-surveillance-and-misinformation-concerns/182027).
- Key teaching point: these bans target the **hosted app/API**, not the open weights. A US company running DeepSeek weights on its own AWS/on-prem GPUs sends nothing to China — that is an architectural fact of self-hosting, though model-behavior concerns (Section 8.2) still apply.

---

## 3. Alibaba Qwen — the open-weight ecosystem leader

### 3.1 Family history
- **Qwen2.5** (Sept 2024): dense models ~0.5B–72B, most under Apache 2.0 — became the favorite base for fine-tuners; DeepSeek chose Qwen2.5 as the base for most R1 distills (source: https://fireworks.ai/blog/deepseek-r1-deepdive; family overview: https://en.wikipedia.org/wiki/Qwen).
- **Qwen3** (Apr 28–29, 2025): full open-weight family under **Apache 2.0** — MoE flagship **Qwen3-235B-A22B** (235B total / 22B active), MoE Qwen3-30B-A3B, plus six dense models 0.6B/1.7B/4B/8B/14B/32B; hybrid "thinking / non-thinking" modes (sources: https://qwenlm.github.io/blog/qwen3/; https://simonwillison.net/2025/Apr/29/qwen-3/).
- **Qwen3-Coder-480B-A35B-Instruct** (Jul 22–23, 2025): open agentic-coding MoE, 480B total / 35B active, 256K context extrapolating to 1M (sources: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct; https://x.com/Alibaba_Qwen/status/1947766835023335516).
- **Qwen3-Max-Preview** (Sept 5, 2025): Alibaba's first **>1-trillion-parameter** model — notably **closed** (API-only), showing Alibaba runs a dual open/closed strategy (sources: https://x.com/Alibaba_Qwen/status/1963991502440562976; https://www.opensourceforu.com/2025/09/alibabas-qwen3-max-hits-1-trillion-parameters-but-drops-open-source-access/).

### 3.2 Current (Aug 2026)
- **Aug 3, 2026**: Alibaba released **Qwen3.8-Max** — reported as a 2.4-trillion-parameter MoE with ~95B active, 1M-token context, native text/image/video input; the first time Alibaba open-sources a Max-class flagship; Alibaba shares rallied (sources: https://www.cnbc.com/2026/08/03/alibaba-ai-model-qwen-rival-anthropic.html; https://www.marktechpost.com/2026/08/03/alibaba-qwen-releases-qwen3-8-max/; https://dataconomy.com/2026/08/03/qwen3-8-max-ai-model/).
- Open weights landed **Aug 12, 2026** as `Qwen/Qwen3.8-2.4T-A95B` on Hugging Face — but note: the downloadable release is reported as **text-only, no 1M context, custom license**, distinct from the fuller multimodal qwen3.8-max API; a companion **Qwen3.8-27B** dense model shipped under Apache 2.0 (sources: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B; https://llm-stats.com/blog/research/qwen3-8-max-open-weights — the license nuance is [secondary sources only], verify the HF model card before quoting).

### 3.3 Ecosystem dominance numbers
- Qwen overtook Meta's Llama as the **most-downloaded open-model family on Hugging Face by Oct 2025**; ~2.045B Hub downloads counted in the 2026 reporting year vs ~418M for Google and ~227M for Meta; **151,448 Qwen-derivative models** on the Hub (Alibaba claims >300,000 derivatives — counts differ by methodology) (source: https://thenextweb.com/news/alibaba-qwen-downloads-hugging-face-open-models).
- Alibaba says cumulative Qwen downloads passed **3 billion** across platforms (source: Fortune, Aug 15, 2026, https://fortune.com/2026/08/15/alibaba-qwen-open-ai-models-3-billion-downloads-meta-google/); Xinhua reported 700M on Hugging Face alone by Jan 2026 (https://english.news.cn/20260113/004b0522f987475cbf83ffc3a8d009aa/c.html — Chinese state outlet, use the HF-counted numbers for the slide).

---

## 4. Moonshot AI — Kimi

- **Kimi K2** (Jul 11, 2025): **1.04T-parameter MoE, 32B active**, open weights under a **Modified MIT license** (standard MIT plus a clause: very large deployments — >100M MAU or >$20M/month revenue — must display "Kimi K2" in their product UI); designed explicitly for **agentic** work (tool use, multi-step tasks) (sources: https://arxiv.org/pdf/2507.20534 (Kimi K2 technical report); https://www.marktechpost.com/2025/07/11/moonshot-ai-releases-kimi-k2-a-trillion-parameter-moe-model-focused-on-long-context-code-reasoning-and-agentic-behavior/; https://www.hpcwire.com/2025/07/16/chinas-moonshot-ai-releases-trillion-parameter-model-kimi-k2/). License-clause detail: verify wording at https://huggingface.co/moonshotai/Kimi-K2-Instruct before quoting.
- **Kimi K2 Thinking** (Nov 6, 2025): open reasoning/agentic version; can chain 200–300 tool calls autonomously; ranked #3 on Artificial Analysis' Agentic Index at release — top open model on several agentic benchmarks; CNBC reported a **$4.6M training cost**, which Moonshot's CEO said "is not an official number" (sources: https://www.cnbc.com/2025/11/06/alibaba-backed-moonshot-releases-new-ai-model-kimi-k2-thinking.html; https://www.yicaiglobal.com/news/kimi-k2-thinkings-reported-usd46-million-training-cost-isnt-official-moonshot-ceo-says; https://www.deeplearning.ai/the-batch/kimi-k2-thinking-outperforms-proprietary-models-with-new-techniques-for-agentic-tool-use).
- **Current (Aug 2026)**: **Kimi K2.5** (Jan 2026) then **Kimi K2.6** (Apr 20–21, 2026): same 1T/32B-active MoE architecture, open weights, now **natively multimodal (text/image/video)**, 256K context, INT4-native; claims open-source SOTA on SWE-Bench Pro (58.6) and long-horizon agent runs (4,000+ tool calls, 300 parallel sub-agents) (source: https://www.latent.space/p/ainews-moonshot-kimi-k26-the-worlds — an AI-newsletter roundup; benchmark claims are Moonshot's own, treat comparative rankings vs Claude/GPT as vendor-claimed).
- Rumored **K3** (2.8T params): **UNVERIFIED** — appears only on SEO sites as of Aug 21, 2026.

---

## 5. Zhipu AI / Z.ai — GLM

- **GLM-4.5** (Jul 2025): 355B total / 32B active MoE, open weights, MIT license, agent-focused (referenced in the GLM-5 write-up: https://huggingface.co/blog/mlabonne/glm-5).
- **US Entity List**: **Jan 15, 2025** — the US Commerce Department added Zhipu (Beijing Zhipu Huazhang Technology) and subsidiaries to the Entity List for allegedly supporting China's military modernization — **the first Chinese LLM company blacklisted**; Zhipu "strongly opposes" and said impact would be minimal. Listed companies cannot buy US technology without special license — note this restricts *exports to* Zhipu; it does not by itself make *using* GLM weights illegal for a US company, but it is a major procurement red flag (sources: https://www.usnews.com/news/technology/articles/2025-01-15/chinese-ai-related-firm-zhipu-says-strongly-opposes-inclusion-in-us-export-control-entity-list; https://www.scmp.com/tech/tech-war/article/3295002/tech-war-us-adds-chinese-ai-unicorn-zhipu-trade-blacklist-bidens-exit).
- **IPO**: Z.ai listed in Hong Kong **Jan 8, 2026** — described as the world's first publicly traded foundation-model company; raised $558M at ~$7.1B valuation (source: https://huggingface.co/blog/mlabonne/glm-5).
- **GLM-5** (Feb 11, 2026): 744B total / 40B active MoE, MIT license, 200K context (DeepSeek Sparse Attention), 77.8% SWE-bench Verified; per Reuters (as cited in the HF write-up) trained **entirely on Huawei Ascend chips with MindSpore** — a milestone for non-Nvidia frontier training (source: https://huggingface.co/blog/mlabonne/glm-5).
- **Mid-2026**: GLM-5.2 (Jun 13, 2026, open weights ~744B/40B, 1M context reported) and GLM-5.3 (Aug 14, 2026, via GLM Coding Plan, claimed strongest open-weights coder; weights lagging the service release) — **[secondary sources only]** (https://mlq.ai/news/zhipu-releases-glm-53-through-its-coding-service-with-weights-still-two-weeks-away/; https://datanorth.ai/news/zhipu-ai-releases-glm-5-2); GLM-5.5 rumors: **UNVERIFIED**.

---

## 6. The rest of the field (brief)

- **MiniMax** (Shanghai): **M1** (Jun 2025) — 456B/45.9B-active hybrid-attention MoE, **1M-token context** (8x R1), Apache 2.0; its RL phase reportedly cost only **$534,700** (512 H800s for 3 weeks) using its CISPO algorithm (source: https://arxiv.org/abs/2506.13585). **M2** (Oct 23, 2025) — 230B/10B active, agentic/coding focus; debuted as the top open-weight model on Artificial Analysis' intelligence index at ~8% of Claude Sonnet's per-token cost (source: https://venturebeat.com/ai/minimax-m2-is-the-new-king-of-open-source-llms-especially-for-agentic-tool). Successors M2.1/M2.5 exist on HF as of mid-2026 (https://huggingface.co/MiniMaxAI/MiniMax-M2.5).
- **Baidu Ernie**: earliest mover (Ernie Bot launched Mar 2023, first ChatGPT-style bot from Chinese big tech) but kept models closed; reversed course and **open-sourced the ERNIE 4.5 family on Jun 30, 2025 under Apache 2.0** — 10 variants, largest 424B total/47B active MoE (sources: https://ernie.baidu.com/blog/posts/ernie4.5/; https://venturebeat.com/ai/baidus-new-ernie-4-5-model-is-open-for-enterprise-use-with-apache-2-0). Teaching point: even the closed-model holdouts capitulated to open weights.
- **Tencent Hunyuan**: broad open-source portfolio (Hunyuan-Large Nov 2024; strong video/3D generation models); Hunyuan 2.0 (Dec 2025, ~406B/32B active) and an open-weight Hunyuan 3.0 flagship (Jul 2026, ~295B/21B active, Apache 2.0) — model details **[secondary sources only]** (https://presenc.ai/research/tencent-hunyuan-model-lineage-2026); Tencent publicly championed open source over closed mega-models at Davos, Jan 2026 (https://www.opensourceforu.com/2026/01/tencent-pushes-open-source-ai-over-closed-mega-models-at-davos/).
- **01.AI** (Kai-Fu Lee): early open-weight Yi models (2023–24); pivoted away from frontier-model training to enterprise AI/data infrastructure ("the Palantir of China," product "Boss AI"); targeting a 2027 Hong Kong IPO (sources: https://www.bloomberg.com/news/articles/2026-07-20/ai-pioneer-kai-fu-lee-s-startup-targets-hong-kong-ipo-next-year; https://thenextweb.com/news/01ai-kai-fu-lee-hong-kong-ipo-2027-palantir-china). Teaching point: not every 2023 "China LLM tiger" survived the price war as a model lab.

---

## 7. What they brought to the table (the teaching points)

1. **Credible open-weight frontier models with permissive licenses.** MIT (DeepSeek R1/V3, GLM-5), Apache 2.0 (Qwen3, ERNIE 4.5, MiniMax), Modified MIT (Kimi K2). Permissive license + downloadable weights = you can self-host on-prem or in your own VPC, fine-tune on proprietary data, and never send a byte to the vendor — the strongest possible data-privacy posture for AI, and directly relevant to regulated industries (licenses per sources in Sections 2–6).
2. **Radical cost efficiency as an engineering discipline.** MoE sparsity (activate ~5% of parameters per token: 671B/37B, 1T/32B, 2.4T/95B), distillation (R1's reasoning transplanted into 1.5B–70B models), INT4-native training (K2.6), efficient RL (MiniMax's $534K RL run). Teach the honest version: headline training-cost figures ($5.6M V3, $4.6M K2 Thinking) are final-run compute only and partly unofficial (Sections 2.3, 4).
3. **Price pressure on US labs.** R1 launched at roughly $0.55/$2.19 per million tokens vs o1's $15/$60 (~96% cheaper) (source: https://openrouter.ai/deepseek/deepseek-r1). Sam Altman conceded OpenAI had been "on the wrong side of history" on open models after DeepSeek; OpenAI shipped **gpt-oss-120b/20b (Aug 5, 2025)** — its first open-weight models since GPT-2 — thirteen days after the White House AI Action Plan (Jul 23, 2025) made US open-weight leadership a national priority (sources: https://openai.com/index/introducing-gpt-oss/; https://www.cnbc.com/2025/08/05/openai-open-weight-meta-mistral-deepseek-ai.html; https://fortune.com/2025/08/05/openai-launches-open-source-llm-ai-model-gpt-oss-120b-deepseek).
4. **Long context leadership in open models.** MiniMax M1's 1M-token window (Jun 2025), Qwen3-Coder 256K→1M, GLM-5.2's reported 1M (sources in Sections 3, 5, 6).
5. **Agentic capability in open models.** Kimi K2/K2 Thinking made "open-weights agent that orchestrates hundreds of tool calls" real (Section 4); MiniMax M2 topped open agentic tool-calling indices (Section 6).
6. **Global adoption — including US enterprises.** Qwen is the most-downloaded open model family on Hugging Face with ~151K derivative models (Section 3.3). Flagship example: **Airbnb** — CEO Brian Chesky said Airbnb "relies heavily" on Alibaba's Qwen for its customer-service agent ("very good... fast and cheap"), among 13 models used; resolution times fell from ~3 hours to seconds; House committees then investigated, and Chesky clarified Airbnb is not an Alibaba customer and "We are not providing data to any Chinese companies" — i.e., they self-host the open weights (sources: https://www.scmp.com/tech/tech-trends/article/3329921/airbnb-picks-alibabas-qwen-over-chatgpt-win-chinese-open-source-ai; https://www.bloomberg.com/news/articles/2026-05-20/airbnb-s-chesky-says-us-misunderstanding-use-of-chinese-open-source-ai-models; https://www.forbes.com/sites/anishasircar/2026/05/21/airbnb-ceo-brian-chesky-called-chinese-ai-fast-and-cheap-now-congress-wants-answers/). This one story teaches both the upside AND the governance scrutiny.
7. **Stanford HAI AI Index 2026 — the gap numbers** (report cited as of Mar/Apr 2026; coverage: https://thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap; https://www.artificialintelligence-news.com/news/ai-safety-benchmarks-stanford-hai-2026-report/):
   - Top-model performance gap: **~2.7%** (Claude Opus 4.6 Arena 1503 vs ByteDance Dola-Seed-2.0-Preview 1464), vs 17.5–31.6 pp gaps on MMLU/MATH/HumanEval in 2023.
   - Private AI investment: US **$285.9B** vs China **$12.4B** (23:1) in 2025 — near-parity performance at a fraction of visible spend.
   - Notable models 2025: US 50 vs China 30 (China doubled from 15).
   - Closed-vs-open frontier gap: top closed model leads top open model by ~3.3%.
   - Verify final wording against the primary report at https://hai.stanford.edu/ai-index before publishing slides.

---

## 8. Caveats for a regulated (medical-device) company

### 8.1 The one distinction to hammer home
- **Consumer app / hosted API from a Chinese vendor** = your prompt data goes to servers in China, under Chinese law (including data-access obligations to the state); this is what Italy's Garante blocked and governments banned (Section 2.5).
- **Self-hosted open weights** = a file of numbers running on your infrastructure; no network connection to the vendor exists unless you create one. Airbnb's "we are not providing data to any Chinese companies" defense rests exactly on this (Section 7.6).
- Policy implication: "Never put company data into DeepSeek/Kimi/Qwen consumer apps" and "IT may evaluate self-hosted open weights under our review process" are BOTH correct and not contradictory.

### 8.2 Censorship and alignment travel with the weights
- China's **Interim Measures for the Management of Generative AI Services** (CAC + 6 regulators, effective **Aug 15, 2023**) require public-facing generative AI to uphold "Core Socialist Values," avoid content subverting state power, pass security assessment, and file algorithms with the CAC (sources: https://www.chinalawtranslate.com/en/generative-ai-interim/; https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2023/07/china-issues-generative-ai-regulations).
- Consequence: R1 refused ~85% of 1,360 sensitive China-topic prompts in PromptFoo testing (source: https://techcrunch.com/2025/01/29/deepseeks-ai-avoids-answering-85-of-prompts-on-sensitive-topics-related-to-china); **running locally does not remove it** — a locally run R1 answered questions about Kent State but not Tiananmen (source: https://techcrunch.com/2025/05/29/deepseeks-updated-r1-ai-model-is-more-censored-test-finds); Enkrypt AI found 91.2% of R1's China-controversy answers leaned pro-government (source: https://futurism.com/artificial-intelligence/hack-deepseek-censorship-tiananmen-square and Enkrypt coverage via https://thedispatch.com/article/yes-deepseek-provides-censored-responses-to-questions-about-china/).
- For quality-engineering use (supplier docs, CAPA drafting) this rarely bites, but it is an alignment-provenance question your AI governance process should ask of ANY model: who trained it, to refuse or say what?

### 8.3 Export control / procurement context
- Zhipu on the US Entity List since Jan 15, 2025 (Section 5) — first LLM lab listed; Entity List restricts US exports TO the company, but many corporate procurement policies treat listed entities as blanket no-go counterparties.
- **No Adversarial AI Act** (S.2177 / H.R.4142, introduced Jun 25, 2025, bipartisan incl. Sens. Scott and Peters + House Select Committee on the CCP): would create a Federal Acquisition Security Council list of foreign-adversary AI and bar federal agencies from using it, with research/evaluation exceptions. **Status as of Aug 21, 2026: introduced, not enacted** — legislative trackers through Mar 2026 list it as pending; some AI provisions moving via NDAA conference (sources: https://www.congress.gov/bill/119th-congress/senate-bill/2177/text; https://www.congress.gov/bill/119th-congress/house-bill/4142; https://fedscoop.com/congress-seeks-ban-on-government-use-of-foreign-adversary-ai/; https://www.steptoe.com/a/web/fadAxzABgVZpz2TTyddTXB/steptoe-federal-ai-legislative-tracker_mar16-2026.pdf).
- Practical read for a med-device firm selling into government/defense-adjacent supply chains: even lawful internal use of Chinese-origin models may raise customer-flowdown and RFP questions (the Airbnb congressional letters are the template — Section 7.6).

### 8.4 The shadow-AI data-leak numbers (verifiable)
- Harmonic Security's index of **22M anonymized enterprise prompts (Jan 1–Dec 31, 2025)**: **~4% of enterprise AI prompts (900,000+) went to China-based AI apps** (DeepSeek, Kimi/Moonshot, Baidu, Qwen, Manus); nearly 8% of employees had used a China-based GenAI tool; DeepSeek showed particularly high source-code exposure; overall 6.7% of prompts potentially disclosed company data, with code the top exposed category (30%) (sources: https://www.harmonic.security/resources/what-22-million-enterprise-ai-prompts-reveal-about-shadow-ai-in-2025; https://cybernews.com/ai-news/1-in-25-enterprise-ai-prompts-china/). Slide-ready line: "1 in 25 enterprise AI prompts went to a China-based app — mostly without IT knowing."
- Policy takeaways to teach: (1) blocklists + approved-tool lists; (2) the ban is on the *apps*, driven by where data goes; (3) shadow AI is a people problem — give staff a sanctioned tool or they will find their own.

### 8.5 Quick governance checklist (derived from the above)
1. Consumer Chinese AI apps: prohibited for any company data (align with device-ban precedents, Garante findings, Harmonic stats).
2. Chinese open weights, self-hosted: possible with AI-governance review — check license (Apache/MIT/Modified-MIT), Entity-List status of the vendor, customer contract flowdowns, and validation like any other software of unknown provenance (for a med-device QMS: treat as SOUP with documented evaluation).
3. Model behavior: red-team for embedded alignment quirks before production use.
4. Track the No Adversarial AI Act and NDAA AI provisions if you sell to US government customers.

---

## 9. Analogies captured (with defensibility notes)

- **MoE = "a hospital, not a general practitioner":** 671B parameters is the whole hospital staff; each token only consults the ~37B-parameter specialists it needs. Technically defensible — routing networks select a few experts per token; total capacity ≠ per-token compute.
- **Open weights = "getting the compiled program, and a license to run it anywhere":** you can run/fine-tune it privately, but you don't get the training data or full recipe (so "open-source" is contested; "open-weight" is the precise term). Defensible; standard in the literature.
- **$5.6M = "the fuel bill for the record lap, not the cost of the racing team":** defensible; matches DeepSeek's own paper caveat + SemiAnalysis.
- **Distillation = "the professor writes the crib notes; the student carries them into the exam":** big reasoning model generates training data that teaches small models its reasoning style. Defensible at training-101 level.
- **Consumer app vs self-hosted = "restaurant vs buying the cookbook":** at the restaurant (app) you hand over your order and they see everything; with the cookbook (weights) you cook at home and nobody watches. Defensible for data-flow; note the cookbook still decides some "recipes it refuses to cook" (embedded censorship).

---

## 10. UNVERIFIED / handle-with-care list

- DeepSeek V4 exact licenses, GA dates, and the May 31, 2026 price cut — SEO-grade sources only; HF org page confirms V4-Pro-0813 and V4-Flash-0731 exist as open weights (Aug 2026) but licenses weren't visible. Verify at https://huggingface.co/deepseek-ai model cards / api-docs.deepseek.com.
- Qwen3.8-Max open-weight release being text-only/custom-license — plausible, from llm-stats/orcarouter; verify the HF model card https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B.
- Kimi K2.6 benchmark superiority over Claude Opus 4.6 / GPT-5.x — vendor-claimed numbers relayed by newsletters; label as "Moonshot-reported" on slides.
- Kimi "K3 2.8T" — UNVERIFIED rumor.
- GLM-5.2/5.3 details and GLM-5.5 — secondary sources only; GLM-5 (Feb 2026) facts are solid via the HF blog.
- Tencent Hunyuan 2.0/3.0 parameter details — secondary sources only.
- Alibaba "300,000+ Qwen derivatives" — Alibaba's own claim; HF-counted figure is 151,448 (use the latter).
- Stanford AI Index 2026 numbers — consistent across several outlets but pull the primary PDF at hai.stanford.edu before printing exact figures.
- Nvidia loss "$589B": consistent across CNBC/Forbes/Bloomberg — solid.
