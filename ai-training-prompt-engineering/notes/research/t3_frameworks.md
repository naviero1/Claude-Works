# T3 — The "Alphabet Soup" Prompt Frameworks: Slots, Origins, and a Merged Slot Inventory

Research date: 2026-08-23. Purpose: every named fill-in-the-slots prompt framework, slot-by-slot, as raw material for the ATTRIBUTE layer of a prompt-template-creator ontology.

**Reliability warning (important for the ontology):** These acronym frameworks are folklore-grade. Only a few have a verifiable primary source (CO-STAR, SPEAR, CLEAR, Google PTCF, Microsoft GCSE, Prompt Canvas). Many others (APE, RACE, CARE, COAST, TAG, TRACE, CRISPE, RISEN...) circulate in listicles with **conflicting expansions** — variants are recorded below because each variant surfaces a distinct candidate attribute.

---

## 1. Core frameworks (slot-by-slot)

### 1.1 CO-STAR — Context, Objective, Style, Tone, Audience, Response
- **Origin:** Created by **GovTech Singapore's Data Science & AI Division** (not by Sheila Teo personally); popularized worldwide by Sheila Teo's article "How I Won Singapore's GPT-4 Prompt Engineering Competition" (Towards Data Science, Dec 2023) after she won GovTech's first GPT-4 Prompt Engineering competition. Source: https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41 ; competition context: https://govinsider.asia/intl-en/article/can-a-prompting-competition-unlock-public-sector-ai-literacy-govtech-shows-how ; GovTech Empower article: https://www.tech.gov.sg/technews/mastering-the-art-of-prompt-engineering-with-empower/
- **Slots (from Teo's article, near-verbatim):**
  - **C — Context:** "Provide background information on the task" — helps the LLM understand the specific scenario.
  - **O — Objective:** "Define what the task is that you want the LLM to perform" — a clear task focuses the response.
  - **S — Style:** "Specify the writing style you want the LLM to use" — e.g. the style of a named expert or profession.
  - **T — Tone:** "Set the attitude of the response" — formal, humorous, empathetic, etc.
  - **A — Audience:** "Identify who the response is intended for" — tailors the response to the reader's level/needs.
  - **R — Response:** "Provide the response format" — list, JSON, professional report, etc., for downstream use.
- **The same article also teaches:** delimiters (`===` or XML tags) to separate prompt sections — "XML tags prove effective since LLMs train extensively on structured web content"; consistent tag naming matching instructions. (Same TDS URL.)
- **What it adds vs. others:** the only mnemonic that separates **Style vs. Tone vs. Audience** as three distinct audience-facing slots; strong on communication/copy tasks.

### 1.2 CRISPE — Capacity & Role, Insight, Statement, Personality, Experiment
- **Origin:** Matt Nigh's GitHub repo "ChatGPT3-Free-Prompt-List" (early 2023): https://github.com/mattnigh/ChatGPT3-Free-Prompt-List (NOTE: the repo README has since been repurposed for his PromptBin tool — the original CRISPE text is no longer on the live README; definition corroborated via secondary sources below).
- **Slots (canonical, per https://www.knowledgehut.com/blog/artificial-intelligence/prompt-engineering-frameworks-rtf-crispe-costar and https://godofprompt.ai/blog/prompt-structures-for-chatgpt-basics/):**
  - **CR — Capacity and Role:** what role/expertise the AI should act as ("senior marketing strategist with 15 years of experience...").
  - **I — Insight:** background information and context behind your request.
  - **S — Statement:** what you are actually asking the model to do.
  - **P — Personality:** the style, tone, personality or manner it should respond in.
  - **E — Experiment:** ask for multiple examples/variations ("give me three subject line options").
- **Variant expansions seen in the wild** (evidence of drift, each a distinct attribute idea):
  - Context, Role, Input, Steps, Parameters, Example — https://promptbuilder.cc/blog/prompt-frameworks-2025 (adds **Parameters** and **Steps** slots)
  - Clarity, Relevance, Iteration, Specificity, Parameters, Examples — https://juuzt.ai/knowledge-base/prompt-frameworks/
- **What it adds:** **Personality** as a slot, and **Experiment** — the only classic framework with a built-in "generate N variations" slot (divergence/sampling as an attribute).

### 1.3 RTF — Role, Task, Format
- **Origin:** no attributed creator (community folklore; among the earliest ChatGPT-era mnemonics). Definitions: https://www.knowledgehut.com/blog/artificial-intelligence/prompt-engineering-frameworks-rtf-crispe-costar ; https://www.thepromptwarrior.com/p/5-prompt-frameworks-level-prompts
- **Slots:**
  - **R — Role:** the persona/expertise the AI should adopt ("Act like a life coach with 30 years of experience").
  - **T — Task:** the specific work to complete.
  - **F — Format:** how the output should be structured (table, list, report...).
- **What it adds:** the minimal 3-slot floor; "the fastest way to stop the model from wandering" (promptbuilder.cc). Every larger framework is a superset of RTF.

### 1.4 TAG — Task, Action, Goal
- **Origin:** unattributed listicle framework. Definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi
- **Slots:** **T — Task:** "Define the specific task." **A — Action:** "Describe what needs to be done." **G — Goal:** "Explain the end goal."
- **Variant:** Task, Audience, Guardrails — https://aipromptsx.com/prompts/frameworks (adds a **Guardrails/constraints** slot).
- **What it adds:** separates the *task label* from the *action verb* from the *end goal* — i.e., what/how/why decomposition.

### 1.5 RACE — Role, Action, Context, Expectation
- **Origin:** unattributed. Definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi (also https://promplify.ai/blog/prompt-engineering-frameworks-compared/ as Role/Action/Context/Expect)
- **Slots:** **R — Role:** specify the AI's role. **A — Action:** detail what action is needed. **C — Context:** relevant details of the situation. **E — Expectation:** describe the expected outcome.
- **What it adds:** an explicit **Expectation** (desired-outcome) slot on top of RTF's trio; "minimalist four-component structure prioritizing speed" (promplify.ai).
- (Unrelated marketing acronym RACE = Reach, Act, Convert, Engage also appears on https://juuzt.ai/knowledge-base/prompt-frameworks/ — not a prompt-slot framework.)

### 1.6 APE — Action, Purpose, Expectation
- **Origin:** unattributed; the standard beginner triad. Definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi ; also "a simple 3-step structure that works for 80% of tasks" per https://aipromptsx.com/prompts/frameworks
- **Slots:** **A — Action:** "Define the job or activity to be done." **P — Purpose:** "Discuss the intention or goal." **E — Expectation:** "State the desired outcome."
- **Variants:** Action/Parameter/Example (https://www.promptquorum.com/blog/prompt-frameworks); Audience/Purpose/Execution (juuzt.ai); Ask/Plan/Execute (promptbuilder.cc). Not to be confused with APE = Automatic Prompt Engineer (Zhou et al., arXiv 2211.01910), a research method.
- **What it adds:** **Purpose** ("why") as its own slot, distinct from the task and the expected result.

### 1.7 CARE — Context, Action, Result, Example
- **Origin:** unattributed. Definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi
- **Slots:** **C — Context:** set the stage for the discussion. **A — Action:** what you want done. **R — Result:** the desired outcome. **E — Example:** give an example to illustrate.
- **What it adds:** the first small framework with a dedicated **Example (few-shot)** slot.

### 1.8 COAST — Context, Objective, Actions, Scenario, Task
- **Origin:** unattributed. Definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi
- **Slots:** **C — Context:** set the stage. **O — Objective:** describe the goal. **A — Actions:** explain the actions needed. **S — Scenario:** describe the scenario. **T — Task:** describe the task.
- **Variant:** Context, Objective, Audience, Style, Tone — https://aipromptsx.com/prompts/frameworks (a CO-STAR-like audience/communication variant).
- **What it adds:** **Scenario** as a slot distinct from Context (situational narrative vs. background facts).

### 1.9 ROSES — Role, Objective, Scenario, Expected Solution, Steps
- **Origin:** unattributed. Definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi
- **Slots:** **R — Role:** specify the AI's role. **O — Objective:** state the goal. **S — Scenario:** describe the situation. **E — Expected Solution:** define the desired outcome. **S — Steps:** ask for the actions needed to reach the solution.
- **Variant:** Role, Objective, Style, Example, Scenario — https://aipromptsx.com/prompts/frameworks
- **What it adds:** **Expected Solution** (a solution-shaped success spec) + **Steps** (procedure elicitation) in one mnemonic.

### 1.10 RISE — Role, Input, Steps, Expectation / RISEN — Role, Instructions, Steps, End goal, Narrowing
- **RISE** definition: https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi — **R** role; **I — Input:** "Describe the information or resources"; **S — Steps:** ask for detailed steps; **E — Expectation:** desired result.
- **RISEN** (described as an evolution of RISE) definition: https://www.thepromptwarrior.com/p/5-prompt-frameworks-level-prompts — **R — Role:** desired AI persona. **I — Instructions:** main task assignment. **S — Steps:** numbered sequence for completion. **E — End goal:** desired output objective. **N — Narrowing:** constraints and limitations. (RISEN is commonly credited to prompt educator Kyle Balmer in secondary sources; no primary page retrieved.)
- **Variant:** RISEN = Role, Intention, Scenario, Expectation, Notation — https://www.promptquorum.com/blog/prompt-frameworks
- **What they add:** **Input** (source material) as a slot (RISE); **Narrowing** — the clearest named **constraints** slot in the soup (RISEN).

### 1.11 RODES — Role, Objective, Details, Examples, Sense Check
- **Origin:** unattributed. Definition: https://www.thepromptwarrior.com/p/5-prompt-frameworks-level-prompts
- **Slots:** **R — Role:** AI's professional identity. **O — Objective:** primary goal. **D — Details:** context and constraints. **E — Examples:** model outputs demonstrating desired style. **S — Sense Check:** confirmation question ensuring the AI understood ("Do you understand the task?").
- **What it adds:** **Sense Check** — the only classic framework with a built-in comprehension-verification slot (a dialogue/verification attribute).

### 1.12 SPEAR — Start, Provide, Explain, Ask, Rinse & Repeat
- **Origin:** **Britney Muller** (AI consultant, ex-Moz; taught in her "LLM Prompt Engineering for Beginners" course). Sources: https://juuzt.ai/knowledge-base/prompt-frameworks/the-spear-framework/ ; https://www.seo-bytes.com/post/llm-prompt-engineering-for-beginners-webinar-recap ; https://maven.com/p/fe9c2f/llm-prompt-engineering-for-beginners
- **Slots (process steps, not content slots):** **S — Start:** define the problem/task. **P — Provide:** provide examples/formatting guidance. **E — Explain:** explain the situation like you would to a person. **A — Ask:** clarify your request/pose the question. **R — Rinse & Repeat:** iterate on your prompts.
- **What it adds:** frames prompting as a **workflow** rather than a form; the explicit **iteration** slot.

### 1.13 Google PTCF — Persona, Task, Context, Format
- **Origin (primary):** Google, "Gemini for Google Workspace: Prompting guide 101 — A quick-start handbook for effective prompts", October 2024 edition. PDF: https://services.google.com/fh/files/misc/gemini_for_workspace_prompt_guide_october_2024_digital_final.pdf (also https://services.google.com/fh/files/misc/workspace_with_gemini_prompting_guide.pdf)
- **Verbatim (p.2):** "The four main areas to consider when writing an effective prompt are: **Persona, Task, Context, Format**." Example prompt with all four: "You are a program manager in [industry]. Draft an executive summary email to [persona] based on [details about relevant program docs]. Limit to bullet points." — "You don't need to use all four in every prompt, but using a few will help! Always remember to include a verb or command as part of your task; this is the most important component of a prompt."
- **Quick tips (p.3, verbatim headings):** 1. Use natural language. 2. Be specific and iterate. 3. Be concise and avoid complexity. 4. Make it a conversation ("fine-tune your prompts if the results don't meet your expectations"). 5. Use your documents (personalize with your own Drive files). 6. Make Gemini your prompt editor ("Make this a power prompt: [original prompt text here]"). Plus the empirical note: "the most fruitful prompts average around **21 words** with relevant context, yet the prompts people try are usually less than nine words."
- **What it adds:** vendor-endorsed 4-slot minimum; the "task verb is mandatory, everything else optional" rule; prompt-length telemetry; grounding-in-own-documents tip; meta-prompting ("prompt editor") tip.

### 1.14 Microsoft GCSE — Goal, Context, Source, Expectations
- **Origin (primary):** Microsoft Support, "Learn about Copilot prompts": https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5 (the four "elements of a good prompt"; echoed across Microsoft 365 Copilot docs, e.g. https://learn.microsoft.com/en-us/copilot/security/prompting-tips)
- **Slots:**
  - **Goal:** what you want Copilot to do — the primary instruction/question. "All that's required is a clear goal. If you want to be more specific, add the other parts."
  - **Context:** background about the situation, audience, or environment — why you need it, how it will be used.
  - **Source:** which data/documents Copilot should use — e.g. "based on all emails from Sam in the past two weeks" (grounding scope; reduces hallucination).
  - **Expectations:** how the output should look and feel — tone, format, length, style, e.g. "The tone of the document will be friendly and suggestive."
- **Additional Microsoft tips on the same page:** start minimal and expand; expect iteration ("Most likely, you'll follow up on the results with another prompt"); verify accuracy; expect run-to-run variation.
- **What it adds:** **Source** — the only vendor mnemonic with a dedicated slot for *which corpus/data to ground on*; bundles tone+format+length into one "Expectations" super-slot.

---

## 2. Other seriously-circulated frameworks (briefer)

All slot lists below are as printed at the cited URL; treat unattributed ones as folklore.

| Framework | Expansion (slot-by-slot) | Source | Distinct contribution |
|---|---|---|---|
| **TRACE** | Task, Request, Action, Context, Example | https://www.linkedin.com/pulse/9-frameworks-master-chatgpt-prompt-engineering-edi-hezri-hairi | Request vs. Action split. Variant: Task, Requirements, Audience, Context, Evaluation (https://aipromptsx.com/prompts/frameworks) adds **Evaluation** slot |
| **ERA** | Expectation, Role, Action | same LinkedIn 9-frameworks URL | outcome-first ordering |
| **CREATE** | Character, Request, Examples, Adjustments, Type of output, Extras | https://promplify.ai/blog/prompt-engineering-frameworks-compared/ | **Adjustments** (revision instructions) + **Extras** (catch-all) slots |
| **STOKE** | Situation, Task, Objective, Knowledge, Examples | https://promplify.ai/blog/prompt-engineering-frameworks-compared/ | **Knowledge** = injected domain expertise slot |
| **CRAFT** | Context, Role, Action, Format, Target(audience) | https://www.promptquorum.com/blog/prompt-frameworks | RTF + context + audience. Variant: Capability, Role, Action, Format, Tone (https://latitude.so/blog/guide-to-standardized-prompt-frameworks) |
| **ICIO** | Instruction, Context, Input Data, Output Indicator | https://www.myframework.net/icio-ai-prompt-framework/ ; matches the canonical "Elements of a Prompt" in DAIR.AI's Prompt Engineering Guide (https://www.promptingguide.ai/introduction/elements) | cleanest instruction-vs-input-data separation; closest to research vocabulary |
| **CLEAR** (Lo) | Concise, Logical, Explicit, Adaptive, Reflective | **Primary source:** Leo S. Lo, "The CLEAR path: A framework for enhancing information literacy through prompt engineering," *Journal of Academic Librarianship* 49(4), July 2023 — https://www.sciencedirect.com/science/article/abs/pii/S0099133323000599 ; open copy: https://digitalrepository.unm.edu/ulls_fsp/211/ | not slots but **quality criteria** for prompt text + iteration (Adaptive = revise drafts; Reflective = evaluate approach) — peer-reviewed |
| **ICE** | Instruction, Context, Examples | https://latitude.so/blog/guide-to-standardized-prompt-frameworks | minimal instruction+grounding+few-shot |
| **SPECS** | Setting, Problem, Expectation, Constraints, Success Criteria | https://www.promptquorum.com/blog/prompt-frameworks | explicit **Success Criteria** slot |
| **SCOPE** | Situation, Constraints, Objectives, (+2 more, unenumerated at source) | https://aipromptsx.com/prompts/frameworks | constraints-forward |
| **CIDI** | Context, Instructions, Details, Input | https://juuzt.ai/knowledge-base/prompt-frameworks/the-cidi-framework/ | Details as its own slot |
| **BAB** | Before, After, Bridge | https://juuzt.ai/knowledge-base/prompt-frameworks/ | copywriting arc: current state → desired state → how to get there (state-transition attributes) |
| **STAR** | Situation, Task, Action, Result | https://juuzt.ai/knowledge-base/prompt-frameworks/ (borrowed from behavioral interviewing) | narrative decomposition; CAR/PAR (Context/Problem, Action, Result) are 3-slot cousins, same URL |
| **PECRA** | Purpose, Expectation, Context, Request, Action | https://aipromptsx.com/prompts/frameworks | purpose-first ordering |
| **RASCEF** | Role, Action, Steps, Context, Examples, Format | https://aipromptsx.com/prompts/frameworks | six-slot union of RTF+steps+examples |
| **GRADE** | Goal, Request, Action, Details, Example | https://aipromptsx.com/prompts/frameworks | goal-oriented + few-shot |
| **ROLE** | Role, Objectives, Limits, Evaluation | https://promptbuilder.cc/blog/prompt-frameworks-2025 | **Limits** + **Evaluation** (scoring rubric) slots |
| **ACE** | Audience, Context, Execution | https://aipromptsx.com/prompts/frameworks | audience-first minimal |
| **AIM** | Audience, Input, Method | https://aipromptsx.com/prompts/frameworks | method slot |
| **CHAIN** | Context, Hypothesis, Analysis, Inference, Narration | https://aipromptsx.com/prompts/frameworks | reasoning-stage slots |
| **RELIC** | Role, Emphasis, Limitation, Information, Challenge | https://juuzt.ai/knowledge-base/prompt-frameworks/ | Emphasis (priority) slot |
| **SPEAR (juuzt listing)**, **RACEF** (Rephrase, Append, Contextualize, Examples, Follow-Up), **4S** (Structure, Style, Substance, Speed) | see https://juuzt.ai/knowledge-base/prompt-frameworks/ | long-tail |
| **CREO / PAIN** | covered in VamshiBandaru's Medium comparative overview of RACE, CARE, APE, CREATE, TAG, CREO, RISE, PAIN, COAST, ROSES — **could not retrieve (HTTP 403)**: https://medium.com/@vamsiparasar1992/prompt-engineering-frameworks-a-comparative-research-overview-of-race-care-ape-create-tag-354082db86b3 | expansions unverified |

Adjacent non-slot mnemonics sometimes listed as "prompt frameworks" (exclude from attribute layer or tag as method-patterns): SCAMPER, ELI5, SMART (Specific, Measurable, Achievable, Relevant, Time-bound), Six Thinking Hats, Chain-of-Thought ("Let's think step-by-step"), Chain of Density (iterative densification) — https://juuzt.ai/knowledge-base/prompt-frameworks/ ; https://www.thepromptwarrior.com/p/5-prompt-frameworks-level-prompts

---

## 3. The Prompt Canvas (arXiv 2412.05127)

- **Paper:** Michael Hewing, Vincent Leinhos, "The Prompt Canvas: A Literature-Based Practitioner Guide for Creating Effective Prompts in Large Language Models," submitted 6 Dec 2024. https://arxiv.org/abs/2412.05127 (HTML: https://arxiv.org/html/2412.05127v1)
- **Purpose (abstract):** prompt-engineering knowledge is "fragmented across academic papers, blog posts and anecdotal experimentation"; the canvas consolidates conceptual foundations + practical strategies into a single learning resource "for pupils, students and employees" — modeled on the Business Model Canvas idea of one-page structured capture.

### 3.1 Canvas structure — four primary field-categories (with the paper's justification per field)

1. **Persona/Role and Target Audience** — "Defining a specific persona or role helps in tailoring the language model's perspective, ensuring that the response aligns with the expected expertise or viewpoint." Mapped techniques: role-based prompting, style prompting.
2. **Task/Intent and Step-by-Step** — "Clearly articulating the goal provides the language model with a specific objective, enhancing the focus and purpose of the response"; break complex tasks into sequential instructions. Mapped techniques: Chain-of-Thought (incl. zero-shot CoT), Plan-and-Solve, Thread-of-Thought.
3. **Context and References** — "Providing context and relevant references equips the language model with necessary background information, reducing ambiguity" and enhancing accuracy. Mapped techniques: zero/one/few-shot learning, provision of external information.
4. **Output/Format and Tonality** — "Specifying the desired format and tone ensures that the response meets stylistic and structural expectations." Mapped techniques: output/format directives (tables, markdown, code), tonality customization.

### 3.2 Canvas supporting boxes

- **Recommended Techniques** (8 items): Iterative Optimization; Placeholders and Delimiters; Prompt Generator; Chain-of-Thought Reasoning; Tree-of-Thoughts Exploration; Emotion Prompting; Rephrase and Respond / Re-Reading; Adjusting Hyperparameters.
- **Tooling** (8 items): LLM Apps; Prompting Platforms; Prompt Libraries; Browser Extensions; LLM Arenas; Custom GPTs for specific purposes; Customized LLMs and company-wide use; Integration of LLMs via API into application systems.

### 3.3 Element taxonomies the paper synthesizes (useful attribute sources)

- **White et al. 2023 prompt-pattern elements** (as tabulated in the paper): Scope (boundary definition), Task/Goal, Context (background + constraints), Procedure (step-by-step), Role (persona), Output (format specs), **Termination Condition** (success/completion criteria).
- **Braun et al. 2024 nine prompt dimensions** under three meta-dimensions: *Interaction* (Human-in-the-Loop; Computer-in-the-Loop; Input/Output types), *Context* (Learning: zero/one/few-shot; Role/Style; Information space internal/external), *Outcome* (Chain-of-Thought; Result goals: learn, lookup, investigate, monitor/extract, decide, create).
- **Sasson Lazovsky et al. 2024 prompt-engineering skills:** creativity, clarity/precision, adaptability, critical thinking, empathy, cognitive flexibility, goal orientation.
- **Not retrieved verbatim:** the exact guiding questions printed inside each canvas box on the one-page PDF figure (the arXiv HTML render summarizes them; the downloadable canvas PDF at the paper's companion site was not fetched).

---

## 4. MERGED DEDUPLICATED SLOT INVENTORY

Every distinct slot concept appearing across the frameworks above, with the frameworks that include it. **Bold** = appears in ≥5 frameworks (core attribute candidates). Framework name in (parens) = variant expansion only.

| # | Slot concept (candidate ATTRIBUTE) | Definition distilled | Frameworks containing it |
|---|---|---|---|
| 1 | **Role / Persona (of the AI)** | expertise, identity or perspective the model adopts | RTF, RACE, RISE, RISEN, RODES, ROSES, CRISPE (Capacity&Role), CRAFT, CREATE (Character), ERA, RASCEF, RELIC, ROLE, Google PTCF (Persona), Prompt Canvas (Persona/Role) |
| 2 | **Task / Action / Instruction** | the verb — what to do | RTF (Task), TAG (Task+Action), RACE, APE (Action), CARE (Action), COAST (Actions+Task), TRACE, ERA, CREATE (Request), GRADE (Request+Action), PECRA (Request+Action), RASCEF, ICIO (Instruction), ICE, CIDI (Instructions), Google PTCF (Task — "most important component"), Microsoft GCSE (Goal), CRISPE (Statement), Prompt Canvas (Task/Intent), STAR (Task), AIM/ACE (Execution/Method) |
| 3 | **Objective / Goal / Purpose (the why)** | intended outcome or motivation behind the task | CO-STAR (Objective), COAST, ROSES, RODES, TAG (Goal), APE (Purpose), PECRA (Purpose), RISEN (End goal), GRADE (Goal), ROLE (Objectives), SPECS/SCOPE (Objectives), Microsoft GCSE (Goal overlaps), White et al. (Task/Goal) |
| 4 | **Context / Background / Situation** | facts of the situation reducing ambiguity | CO-STAR, RACE, CARE, COAST, CRAFT, CRISPE (Insight), TRACE, PECRA, RASCEF, CIDI, ICIO, ICE, STOKE (Situation), SPECS (Setting), STAR/CAR (Situation/Context), Google PTCF, Microsoft GCSE, Prompt Canvas (Context) |
| 5 | Scenario (narrative situation) | story-form setting distinct from background facts | COAST, ROSES, (RISEN promptquorum variant) |
| 6 | **Input data / Source / References** | the material to operate on / ground in | ICIO (Input Data), RISE (Input), CIDI (Input), AIM (Input), Microsoft GCSE (**Source** — named grounding corpus), STOKE (Knowledge), Google tip "Use your documents", Prompt Canvas (References), Braun (Information space internal/external) |
| 7 | **Audience** | who the output is for | CO-STAR, (COAST variant), (TRACE variant), (APE juuzt variant), CRAFT (Target), ACE, AIM, Prompt Canvas (Target Audience), Microsoft GCSE (inside Context), Google PTCF example ("email to [persona]") |
| 8 | **Style** | writing style / voice | CO-STAR, (ROSES variant), (COAST variant), 4S, Prompt Canvas (inside Output/Format & Tonality) |
| 9 | **Tone / Personality** | attitude/emotional register | CO-STAR (Tone), CRISPE (Personality), CRAFT-latitude (Tone), (COAST variant), Microsoft GCSE (inside Expectations), Prompt Canvas (Tonality) |
| 10 | **Response format / Output structure** | shape of the deliverable: table, JSON, list, code... | RTF (Format), CO-STAR (Response), CREATE (Type of output), RASCEF (Format), CRAFT (Format), ICIO (Output Indicator), Google PTCF (Format), Microsoft GCSE (inside Expectations), White et al. (Output), Prompt Canvas (Output/Format) |
| 11 | Length / detail level | word/size bound on output | CO-STAR (inside Response — "200-word email"), Microsoft GCSE (inside Expectations), Google PTCF example ("Limit to bullet points") |
| 12 | **Expected outcome / Result / Expectations** | what success looks like | APE, RACE, RISE, ERA (Expectation), CARE (Result), ROSES (Expected Solution), PECRA (Expectation), STAR/CAR/PAR (Result), Microsoft GCSE (Expectations), SPECS (Expectation) |
| 13 | Success criteria / Evaluation rubric | measurable acceptance test | SPECS (Success Criteria), ROLE (Evaluation), (TRACE variant Evaluation), White et al. (Termination Condition), SMART (Measurable) |
| 14 | **Examples (few-shot)** | sample inputs/outputs to imitate | CARE, RODES, TRACE, CREATE, RASCEF, GRADE, STOKE, ICE, (ROSES variant), (CRISPE variants), SPEAR (Provide), Prompt Canvas (few-shot under Context/References) |
| 15 | Variations / divergence request | ask for N alternatives to choose from | CRISPE (Experiment), SxS (promptbuilder.cc), CREATE (Adjustments, partially) |
| 16 | **Steps / Procedure / Process** | decompose into ordered sub-steps | RISE, RISEN, ROSES (Steps), RASCEF, (CRISPE promptbuilder variant), APE-promptbuilder (Plan), White et al. (Procedure), Prompt Canvas (Step-by-Step), CHAIN (reasoning stages) |
| 17 | **Constraints / Limits / Guardrails / Narrowing** | what to avoid, boundaries, rules | RISEN (Narrowing), ROLE (Limits), RELIC (Limitation), (TAG variant Guardrails), SPECS/SCOPE (Constraints), RODES (Details, partly), White et al. (Scope; Context-constraints), CREATE (Adjustments) |
| 18 | Details / Specifics / Parameters | fine-grained requirement values | RODES (Details), CIDI (Details), GRADE (Details), (CRISPE variants: Parameters), APE-promptquorum (Parameter) |
| 19 | Emphasis / Priority | what matters most | RELIC (Emphasis) |
| 20 | Sense check / comprehension confirmation | model confirms understanding before executing | RODES (Sense Check) — unique |
| 21 | **Iteration / Refinement loop** | treat prompt as draft; follow-up and refine | SPEAR (Rinse & Repeat), CLEAR (Adaptive + Reflective), RACEF (Follow-Up), Google tip 4 ("Make it a conversation"), Microsoft ("expect iteration"), Prompt Canvas (Iterative Optimization) |
| 22 | Prompt-text quality criteria | conciseness, natural language, logical order, explicitness | CLEAR (Concise, Logical, Explicit), Google tips 1–3 (natural language; specific; concise, ~21-word sweet spot), 4S |
| 23 | Delimiters / structural markup | ===, XML tags, placeholders separating sections | CO-STAR article (delimiters/XML), Prompt Canvas (Placeholders and Delimiters) |
| 24 | Model/system parameters | temperature etc. | Prompt Canvas (Adjusting Hyperparameters), (CRISPE variants: Parameters) |
| 25 | Before/After state transition | current state vs. desired state framing | BAB (Before, After, Bridge); SPECS (Setting vs. Expectation) |
| 26 | Extras / catch-all | anything else | CREATE (Extras) |

**Frequency takeaway for the attribute layer:** the universal core across ~30 frameworks is a 6-attribute skeleton — **Role/Persona, Task/Action, Context (+Input/Source), Objective/Purpose, Output Format (+Style/Tone/Audience/Length), Expected outcome/Examples** — with **Steps, Constraints, Success criteria, Sense-check, and Iteration** as the differentiating "power" attributes that only the richer frameworks include. Vendor frameworks (Google PTCF, Microsoft GCSE) confirm the same core with only 4 slots and uniquely contribute **Source/grounding** (Microsoft) and **mandatory task-verb + prompt-length guidance** (Google).

---

## 5. Retrieval gaps / caveats

- **Matt Nigh's original CRISPE README** could not be fetched directly (live repo README now hosts his PromptBin tool; web.archive.org fetch blocked by tooling). CRISPE definition corroborated via knowledgehut.com and godofprompt.ai; canonical expansion (Capacity&Role, Insight, Statement, Personality, Experiment) also matches the first search-result summary of promptbuilder-adjacent sources.
- **Medium articles 403'd:** VamshiBandaru comparative overview (CREO and PAIN expansions unverified) and Giuliano Lemes information-literacy article. prompt-maven.com DNS failed.
- **Prompt Canvas one-page PDF figure** (exact in-box guiding questions) not extracted — only the arXiv HTML description of each category.
- Several frameworks have **multiple circulating expansions** (APE ×4, CRISPE ×3, RISEN ×2, TRACE ×2, CRAFT ×2, COAST ×2, ROSES ×2, TAG ×2, RACE ×2); the ontology should model expansions as *variants of a named framework*, not assume one canonical form.
- CO-STAR's authoritative in-Teo's-article phrasing was retrieved; the separate GovTech "Empower/Prompt Royale" page content was not fetched (search-result summary only): https://www.tech.gov.sg/technews/mastering-the-art-of-prompt-engineering-with-empower/
