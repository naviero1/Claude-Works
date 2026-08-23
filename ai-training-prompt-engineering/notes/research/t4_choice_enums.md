# T4 — Enumerable OPTION SETS for prompt attributes

Research date: 2026-08-23. Goal: concrete, defensible pick-lists a prompt-template-creator tool can offer for each attribute, sourced from shipped product UIs, vendor docs, style guides, and research. Verbatim enumerations preferred; gaps noted at the end of each section.

---

## 1. TONE

### 1.1 Product tone pickers (verbatim option sets)

**Microsoft Outlook — "Draft with Copilot" tone dropdown**
- Options: **Direct, Neutral, Casual, Formal** (4-value picker).
- Post-draft adjustment menu: **shorter, longer, more direct, more casual, more formal** — plus free-text "tell Copilot what to change" (e.g. "make this sound more casual and direct").
- Usage guidance published with the feature: *Formal* → major announcements, formal requests, external communications, documenting issues; *Casual* → internal team communication, friendly updates, networking, invites; *Neutral* → general inquiries, routine communication, reporting, meeting minutes.
- Sources: https://techwisegroup.com/weekly-tech-tips/copilot-microsoft-outlook/ ; https://www.howtogeek.com/use-copilot-in-outlook-to-craft-the-perfect-emails/ ; Microsoft Support "Draft an email message with Copilot in Outlook" (https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b — confirms the tone dropdown defaulting to **Neutral** and length defaulting to **Short**, but the support page itself does not enumerate every value; the 4-value list comes from the secondary walkthroughs above).

**Grammarly — tone detector**
- Detects **40+ tones**; officially confirmed names (with UI emoji) include: **Formal** (button-up shirt), **Confident** (handshake), **Appreciative** (raised hands), **Disapproving** (squint/frown), **Joyful** (smiley), plus **Informal, Optimistic, Friendly, Neutral**, and examples "excited," "accusatory/angry."
  - Sources: https://builtin.com/artificial-intelligence/grammarly-tone-detector ; https://www.grammarly.com/blog/product/tone-detector/ ; https://www.xda-developers.com/grammarly-tone-detector-available-keyboard-app/
- Grammarly's editorial taxonomy, "10 Types of Tone in Writing" (verbatim list + definitions):
  1. **Formal** — objective, authoritative, official
  2. **Informal** — relaxed, friendly, approachable, conversational
  3. **Optimistic** — confidence, encouragement, positive outlook
  4. **Worried** — concern, uncertainty, potential risk
  5. **Friendly** — rapport, trust, warmth
  6. **Curious** — inviting exploration, asking questions
  7. **Assertive** — clear opinions, boundaries, persuasion
  8. **Encouraging** — motivating, reassurance, supporting action
  9. **Surprised** — unexpected outcomes, discoveries
  10. **Cooperative** — collaboration, problem-solving, shared decisions
  - Source: https://www.grammarly.com/blog/writing-techniques/types-of-tone/
- NOT RETRIEVED: Grammarly's complete 40+-tone internal list — no primary page enumerates all of them.

**Anthropic Claude — Styles presets (claude.ai)**
- Presets: **Normal** (default), **Concise** ("shorter and more direct responses"), **Explanatory** ("educational responses for learning new concepts"), **Formal** ("clear and polished responses"); some coverage also lists a **Learning** preset. Custom styles can be generated from uploaded writing samples.
- Sources: https://www.maginative.com/article/anthropic-introduces-custom-writing-styles-for-claude-ai/ ; https://www.howtogeek.com/claude-ai-now-can-sample-and-mimic-your-writing-style/ ; https://promptoptimizer.tools/blog/how-to-use-claude-styles (support.claude.com article 10181068 returned 404 at fetch time — NOT RETRIEVED as primary).

**Notion AI — "Change tone" menu**
- Options: **Professional, Casual, Straightforward, Confident, Friendly** (5-value picker). Adjacent commands: Improve writing, Fix spelling & grammar, **Make shorter, Make longer, Simplify language**.
- Sources: https://www.xray.tech/post/how-to-use-notion-ai ; https://guides.ai/how-to-change-tone-notion-ai/ ; https://www.notion.com/help/guides/notion-ai-for-docs

**Apple Intelligence — Writing Tools (iOS 18.1+/macOS Sequoia 15.1+)**
- Rewrite tones: **Friendly, Professional, Concise** (plus base **Rewrite** and **Proofread**).
- Sources: https://support.apple.com/en-us/121582 ; https://macmost.com/using-apple-intelligence-rewriting-tools.html

**Google Gemini for Workspace — Prompting Guide 101 (Oct 2024 PDF, p.58, verbatim)**
- "Ask for outputs to have a specific tone, such as **formal, informal, technical, creative, or casual**."
- Source: https://services.google.com/fh/files/misc/gemini_for_workspace_prompt_guide_october_2024_digital_final.pdf

### 1.2 Synthesized practical tone menu (for the template tool)

Grouped on three axes (every option below traces to at least one shipped picker above):

| Axis | Options | Seen in |
|---|---|---|
| **Formality** | Formal · Professional · Neutral · Casual · Informal/Conversational | Outlook Copilot, Notion, Grammarly, Gemini guide |
| **Warmth** | Friendly · Warm/Empathetic · Appreciative · Encouraging · Optimistic · Enthusiastic/Joyful | Notion, Apple, Grammarly |
| **Directness / force** | Direct · Straightforward · Assertive · Confident · Diplomatic/Cooperative · Cautious/Worried | Outlook Copilot, Notion, Grammarly |
| **Register extras** | Technical · Creative/Playful · Authoritative · Urgent · Humorous · Academic | Gemini guide (technical, creative); Grammarly detector family |

A defensible compact picker (12): Formal, Professional, Neutral, Casual, Friendly, Warm, Encouraging, Confident, Direct, Diplomatic, Technical, Playful.

---

## 2. AUDIENCE

### 2.1 Reading-level scales

**ChatGPT Canvas — "Reading level" slider**
- Slider runs **Kindergarten → Graduate School** (endpoints verbatim in OpenAI's descriptions; multiple walkthroughs describe intermediate stops at school stages, e.g. Middle School, High School, College).
- Sources: https://zapier.com/blog/chatgpt-canvas/ ("adjust the reading level anywhere from Kindergarten to Graduate school") ; https://learnprompting.org/blog/how-to-use-openai-canvas-chatgpt ; https://godofprompt.ai/blog/10-secret-tips-for-chatgpt-4o-with-canvas-ultimate-guide/ (OpenAI's own pages openai.com/index/introducing-canvas and help.openai.com/en/articles/9930697 returned 403 — exact intermediate tick labels NOT RETRIEVED from primary).

**Federal plain language guidance**
- First rule: "**Write for your audience** … Take your audience's current level of knowledge into account. Don't write for an 8th-grade class if your readers are PhD candidates, small business owners, or working parents."
- Reading-grade conventions: general-public material at **6th–8th grade** ("To communicate with the average reader, we need to write at the 6th to the 8th grade reading level"); some agencies target 6th grade or below.
- Sources: https://digital.gov/guides/plain-language/principles ; Federal Plain Language Guidelines (https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf) ; https://portal.ct.gov/ctcontentstyleguide/create-my-content/plain-language ; https://www.dol.gov/agencies/eta/ui-modernization/use-plain-language/our-approach

**Flesch Reading Ease bands (readability slider anchor points)**
- 90–100 very easy (~5th grade); 60–70 ≈ **8th–9th grade** (plain-English target); 30–59 difficult (college); 0–29 very difficult (college graduate/academic).
- Source: https://readable.com/readability/flesch-reading-ease-flesch-kincaid-grade-level/

### 2.2 Expertise-level ladders

**WIRED "5 Levels" format** (a widely recognized 5-step expertise ladder):
- **child → teenager → undergrad (majoring in the subject) → grad student → expert colleague/peer**.
- Source: https://www.formatsunpacked.com/p/formats-unpacked-wireds-5-levels (describing WIRED's series, https://www.youtube.com/playlist?list=PLibNZv5Zd0dyCoQ6f4pdXUFnpAIlKgm3N)

**Role-based audience (executive vs technical)**
- Gemini Prompting Guide models audience via persona slots: "Draft an **executive summary email to [persona]** … Limit to bullet points" — audience is parameterized as a role, and its persona chapters double as audience categories (see §6). Source: Gemini guide PDF p.2.
- Microsoft's prompt-element model treats audience as part of **Context** ("Our audience is professionals who work in a hybrid environment..."). Source: https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5

### 2.3 Synthesized audience menu

- **Expertise**: Novice / General public / Practitioner / Expert-specialist (compact 4-step), or the WIRED 5-step (child, teen, undergrad, grad, peer expert).
- **Reading level** (slider): Kindergarten · Elementary · Middle School (6–8th grade = plain-language default) · High School · College · Graduate School (Canvas endpoints + plain-language anchor).
- **Reader role**: Executive / Manager / Technical peer / Frontline staff / Customer / New hire / Regulator (from Gemini guide + Copilot job-type filters, §6).
- **Familiarity with context**: knows the project / knows the domain only / knows neither (Microsoft "Context" element pattern).

---

## 3. OUTPUT FORMAT / RESPONSE TYPES

### 3.1 Vendor prompt-guide format vocabularies

**Google Gemini Prompting Guide 101** (primary PDF):
- Defines **Format** as one of the four prompt areas; examples given verbatim: "**Bullet points, talking points, specifying character count limits**"; in-guide format commands include "**Limit to bullet points**", "**Organize this agenda in a table format**", "**Create a sample agenda**", "Draft an **executive summary email**", "generate a **summary**", "Suggest **three different icebreaker activities**" (enumerated-options format), and Export to **Docs/Slides**.
- Source: https://services.google.com/fh/files/misc/gemini_for_workspace_prompt_guide_october_2024_digital_final.pdf (pp. 2, 7–8, 58)

**Microsoft 365 Copilot — prompt anatomy & gallery**
- Prompt parts: **Goal, Context, Expectations, Source** — "Expectations" is the format/output slot ("the format or output you want from Copilot"). Source: https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5
- Copilot Prompt Gallery filters prompts by **Task** (e.g. create, edit, …), **Job type** (e.g. Sales, Finance, HR), **App**, and **Copilot Agent**. Sources: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery (architecture; catalog at https://m365.cloud.microsoft/copilot-prompts) ; https://www.hubsite365.com/en-ww/crm-pages/how-to-use-the-prompts-gallery-in-copilot.htm ; https://onlycopilotfans.com/copilot-prompt-gallery — NOT RETRIEVED: the complete verbatim Task-filter list (the gallery is a login-gated SPA).

**Apple Intelligence Writing Tools — output transforms** (a shipped minimal "deliverable shape" menu):
- **Summary · Key Points (bulleted) · List · Table** (applied to existing text). Source: https://support.apple.com/en-us/121582

**ChatGPT Canvas — document/code shortcut menus** (shipped response-type operations):
- Writing: **Suggest edits · Adjust the length · Reading level · Add final polish · Add emojis**. Coding: **Code review · Add logs · Add comments · Fix bugs · Port to a language** (languages offered: **PHP, C++, Python, JavaScript, TypeScript, Java**).
- Sources: https://zapier.com/blog/chatgpt-canvas/ ; https://learnprompting.org/blog/how-to-use-openai-canvas-chatgpt

**API-level structured formats**
- OpenAI `response_format` values: **text · json_object · json_schema** (Structured Outputs; `strict: true` guarantees schema match; Responses API moves this under `text.format`). Sources: https://openai.com/index/introducing-structured-outputs-in-the-api/ ; https://developers.openai.com/api/docs/guides/structured-outputs ; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs

### 3.2 Synthesized deliverable-shape menu (grouped)

- **Micro formats**: one-liner / TL;DR · bullet summary · key points · talking points (Apple Key Points; Gemini "bullet points/talking points")
- **Prose documents**: memo · email (formal/casual) · executive summary · report with headed sections · blog post · press release (Gemini guide use cases; Copilot gallery "create" tasks)
- **Structured/tabular**: table · comparison matrix · agenda · checklist · step-by-step numbered instructions · FAQ · pros/cons list (Gemini "table format"/"sample agenda"; Apple List/Table)
- **Presentation**: slide outline / deck section (Gemini export-to-Slides flow)
- **Machine-readable**: JSON (schema-strict) · JSON object · Markdown · CSV · code in language X (OpenAI response_format; Canvas port-to-language list; Anthropic library "CSV converter" — §6)
- **Meta-shapes**: N options to choose from ("Suggest three…" — Gemini guide) · draft + rationale · annotated edits (Canvas "Suggest edits")

---

## 4. LENGTH / VERBOSITY

**OpenAI `verbosity` parameter (GPT-5 family)**
- Values: **low · medium · high**; default **medium**. Controls output length/detail; explicit prompt instructions override it ("write a 5 paragraph essay" wins regardless of setting).
- Sources: https://openai.com/index/introducing-gpt-5-for-developers/ ; https://developers.openai.com/api/docs/guides/latest-model ; https://docs.ag2.ai/latest/docs/use-cases/notebooks/notebooks/agentchat_gpt-5_verbosity_example/

**ChatGPT Canvas — "Adjust the length" slider**
- Slider from **Shortest → Longest** (5-ish stops; endpoints verbatim in walkthroughs). Source: https://godofprompt.ai/blog/10-secret-tips-for-chatgpt-4o-with-canvas-ultimate-guide/ ; https://zapier.com/blog/chatgpt-canvas/

**Outlook Copilot** — length option (default **Short**; dropdown offers longer/shorter variants: short/medium/long) alongside tone; adjust menu has **shorter / longer**. Sources: https://support.microsoft.com/en-us/office/draft-an-email-message-with-copilot-in-outlook-3eb1d053-89b8-491c-8a6e-746015238d9b ; https://techwisegroup.com/weekly-tech-tips/copilot-microsoft-outlook/

**Notion AI** — **Make shorter / Make longer** commands. Source: https://www.xray.tech/post/how-to-use-notion-ai

**Cap conventions (from vendor prompt guides)**
- Gemini guide: "Give constraints… include details in your prompt such as **character count limits** or the **number of options** you'd like to generate" (PDF p.58); example "completed by a group of 25 people in 30 minutes or less" shows numeric constraint phrasing (p.8).
- Common defensible cap types for a template tool: word cap ("under 150 words"), sentence cap ("in 2–3 sentences"), paragraph cap ("one paragraph"), bullet cap ("exactly 5 bullets"), character cap (social posts), page cap ("one-pager"), time-to-read cap. (Convention synthesis; the character-count and option-count forms are verbatim from the Gemini guide.)

**Synthesized length attribute** = *preset* (XS one-liner / S paragraph / M half-page / L full doc / XL exhaustive — mirrors low·medium·high + Shortest→Longest sliders) + *hard cap* (unit: words | sentences | paragraphs | bullets | characters | pages, value: N) + *override rule* (explicit caps beat presets, per OpenAI verbosity docs).

---

## 5. REASONING EFFORT (as of Aug 2026)

**OpenAI — `reasoning_effort` / `reasoning.effort`**
- Full value space (model-dependent): **none · minimal · low · medium · high · xhigh · max** — "Supported values are model-dependent… Lower effort favors speed and lower token usage" (primary: https://developers.openai.com/api/docs/guides/reasoning).
- Per-model notes: GPT-5 introduced **minimal**; **gpt-5.1** supports none/low/medium/high with default **none**; **gpt-5.1-codex-max** added **xhigh**; GPT-5.5 and GPT-5.6 default to **medium**. Sources: https://developers.openai.com/api/docs/guides/reasoning ; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/reasoning ; https://community.openai.com/t/request-for-compatibility-matrix-reasoning-effort-sampling-parameters-across-gpt-5-series/1371738

**Anthropic — `effort` parameter + thinking**
- Effort levels: **low · medium · high (default) · xhigh ("extra high") · max**. Claude.ai help (primary, fetched): Low/Medium "work well for routine tasks and stretch your usage further"; High is the "recommended effort level… best overall balance of quality and speed"; **Extra high (xhigh)** "designed for long-running coding and agentic tasks, offering deeper reasoning than high without the full token cost of max" (Opus 4.7 and newer); **Max** is "the most thorough option… deepest possible reasoning." Available on Opus 5, Sonnet 5, Fable 5, Opus 4.8/4.7/4.6, Sonnet 4.6.
- **Thinking and effort are separate, independently combinable settings**; extended thinking is a toggle (cannot be disabled on Opus 5). Effort governs token eagerness "across all output: text responses, tool calls, and extended thinking"; with adaptive thinking Claude decides when to think deeply.
- Sources: https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings (primary, fetched) ; https://www.anthropic.com/news/claude-opus-4-6 ; https://docs.litellm.ai/docs/providers/anthropic_effort ; https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-adaptive-thinking.html
- Template-tool enum: OpenAI {none, minimal, low, medium, high, xhigh, max}; Anthropic {low, medium, high, xhigh, max} × thinking {on, off, adaptive}.

---

## 6. PERSONA / ROLE LIBRARIES

### 6.1 Awesome ChatGPT Prompts (github.com/f/awesome-chatgpt-prompts) — 2,134 prompts in prompts.csv (fetched raw)

First ~160 canonical persona names, verbatim from the `act` column: Ethereum Developer; Linux Terminal; English Translator and Improver; Job Interviewer; JavaScript Console; Excel Sheet; English Pronunciation Helper; Spoken English Teacher and Improver; Travel Guide; Plagiarism Checker; Character; Advertiser; Storyteller; Football Commentator; Stand-up Comedian; Motivational Coach; Composer; Debater; Debate Coach; Screenwriter; Novelist; Movie Critic; Relationship Coach; Poet; Rapper; Motivational Speaker; Philosophy Teacher; Philosopher; Math Teacher; AI Writing Tutor; UX/UI Developer; Cyber Security Specialist; Recruiter; Life Coach; Etymologist; Commentariat; Magician; Career Counselor; Pet Behaviorist; Personal Trainer; Mental Health Adviser; Real Estate Agent; Logistician; Dentist; Web Design Consultant; AI Assisted Doctor; Doctor; Accountant; Chef; Automobile Mechanic; Artist Advisor; Financial Analyst; Investment Manager; Tea-Taster; Interior Decorator; Florist; Self-Help Book; Gnomist; Aphorism Book; Text Based Adventure Game; AI Trying to Escape the Box; Fancy Title Generator; Statistician; Prompt Generator; Instructor in a School; SQL Terminal; Dietitian; Psychologist; Smart Domain Name Generator; Tech Reviewer; Developer Relations Consultant; Academician; IT Architect; Lunatic; Gaslighter; Fallacy Finder; Journal Reviewer; DIY Expert; Social Media Influencer; Socrat; Socratic Method; Educational Content Creator; Yogi; Essay Writer; Social Media Manager; Elocutionist; Scientific Data Visualizer; Car Navigation System; Hypnotherapist; Historian; Astrologer; Film Critic; Classical Music Composer; Journalist; Digital Art Gallery Guide; Public Speaking Coach; Makeup Artist; Babysitter; Tech Writer; Ascii Artist; Python Interpreter; Synonym Finder; Personal Shopper; Food Critic; Virtual Doctor; Personal Chef; Legal Advisor; Personal Stylist; Machine Learning Engineer; Biblical Translator; SVG designer; IT Expert; Chess Player; Midjourney Prompt Generator; Fullstack Software Developer; Mathematician; RegEx Generator; Time Travel Guide; Dream Interpreter; Talent Coach; R Programming Interpreter; StackOverflow Post; Emoji Translator; PHP Interpreter; Emergency Response Professional; Fill in the Blank Worksheets Generator; Software Quality Assurance Tester; Tic-Tac-Toe Game; Password Generator; New Language Creator; Web Browser; Senior Frontend Developer; Code Reviewer; Accessibility Auditor; Solr Search Engine; Startup Idea Generator; Spongebob's Magic Conch Shell; Language Detector; Salesperson; Commit Message Generator; Conventional Commit Message Generator; Chief Executive Officer; Diagram Generator; Speech-Language Pathologist (SLP); Startup Tech Lawyer; Title Generator for written pieces; Product Manager; Project Manager; Drunk Person; Mathematical History Teacher; Song Recommender; Cover Letter; Technology Transferer; Unconstrained AI model DAN; Gomoku player; Proofreader; Buddha; Muslim Imam; Chemical Reactor; Friend.
- Source: https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv (repo: https://github.com/f/awesome-chatgpt-prompts)

### 6.2 Anthropic Prompt Library (docs.anthropic.com/en/resources/prompt-library/library)

Named prompt personas/tasks include (per library index): Cosmic keystrokes; **Corporate clairvoyant**; **Website wizard**; Excel formula expert; Google apps scripter; Python bug buster; Time travel consultant; Storytelling sidekick; **Cite your sources**; SQL sorcerer; Dream interpreter; Pun-dit; Culinary creator; Portmanteau poet; Hal the humorous helper; LaTeX legend; Mood colorizer; Git gud; Simile savant; Ethical dilemma navigator; **Meeting scribe**; Idiom illuminator; **Code consultant**; Function fabricator; Neologism creator; **CSV converter**; Emoji encoder; **Prose polisher**; Perspectives ponderer; Trivia generator; Mindfulness mentor; **Second-grade simplifier**; VR fitness innovator; **PII purifier**; **Memo maestro**; **Career coach**; **Grading guru**; Tongue twister; **Interview question crafter**; Grammar genie; Riddle me this; Code clarifier; Alien anthropologist; Data organizer; Brand builder; Efficiency estimator; **Review classifier**; Direction decoder; Motivational muse; Email extractor; Master moderator; Lesson planner; **Socratic sage**; Alliteration alchemist; Futuristic fashion advisor; Polyglot superpowers; Product naming pro; Philosophical musings; Spreadsheet sorcerer; Sci-fi scenario simulator; **Adaptive editor**.
- Sources: https://docs.anthropic.com/en/resources/prompt-library/library (mirror: https://anthropic.mintlify.app/en/resources/prompt-library/library) ; https://www.tomsguide.com/ai/anthropic-just-released-a-claude-3-prompt-library-heres-the-best-ones-to-try-now

### 6.3 Google Gemini Prompting Guide — role chapters (verbatim TOC, primary PDF)

**Administrative support · Communications · Customer service · Executives · Frontline management · Human resources · Marketing · Project management · Sales · Small business owners and entrepreneurs · Startup leaders** — the guide's entire structure is a persona library ("use the role-specific suggested prompts"), with sub-personas like "executive administrators and executive business partners." Source: Gemini guide PDF pp.4–7.

### 6.4 Microsoft Copilot Prompt Gallery — Job type filter
Job types include **Sales, Finance, HR** (and other functions); combined with Task and App filters. Source: https://www.hubsite365.com/en-ww/crm-pages/how-to-use-the-prompts-gallery-in-copilot.htm — full verbatim job-type list NOT RETRIEVED (gated SPA at https://m365.cloud.microsoft/copilot-prompts).

### 6.5 Synthesized persona-category menu for a template tool

- **Analyst**: Financial Analyst, Statistician, Data organizer, Efficiency estimator (ACP/Anthropic)
- **Editor/Writer**: Proofreader, Prose polisher, Adaptive editor, Tech Writer, Essay Writer, AI Writing Tutor
- **Coach/Mentor**: Motivational Coach, Career Counselor/Career coach, Life Coach, Debate Coach, Public Speaking Coach, Mindfulness mentor
- **Critic/Devil's advocate**: Debater, Movie/Film/Food Critic, Fallacy Finder, Perspectives ponderer, Ethical dilemma navigator
- **Examiner/Reviewer**: Job Interviewer, Interview question crafter, Journal Reviewer, Code Reviewer, Grading guru, Software QA Tester, Accessibility Auditor, Plagiarism Checker
- **Teacher/Explainer**: Math/Philosophy Teacher, Socratic sage/Socratic Method, Lesson planner, Second-grade simplifier, Instructor in a School
- **Domain expert/Consultant**: Legal Advisor, Accountant, IT Architect, Cyber Security Specialist, Web Design Consultant, Code consultant
- **Simulator/Tool**: Linux Terminal, SQL Terminal, JavaScript Console, Excel Sheet, Web Browser, Text Based Adventure Game
- **Business function** (audience-as-role): the 11 Gemini chapters + Copilot job types (Sales, Finance, HR, Marketing, …)

---

## 7. VERIFICATION / REVIEW MODES

### 7.1 Judge-mode taxonomies (published menus)

**LLMs-as-Judges survey (arXiv:2412.05579)** — three comparison modes:
- **Pointwise** (score each candidate alone against criteria), **Pairwise** (pick the better of two), **Listwise** (rank a whole candidate list). Source: https://arxiv.org/pdf/2412.05579 (summarized via https://www.emergentmind.com/topics/llm-as-a-judge-evaluation)

**Evidently AI — LLM-as-a-judge guide** (practitioner menu):
- **Pairwise comparison**; **Evaluation by criteria (reference-free direct scoring)**; **Reference-based** with context variants: *Answer + Reference Answer*, *Answer + Question*, *Answer + Retrieved Context*. Recommends **binary classification** (e.g. helpful/unhelpful) over wide scales. Example criteria enumerated: politeness, bias, tone, sentiment, hallucinations, relevance, completeness, accuracy, clarity, conciseness, PII presence, denials, repetitions, user frustration, issue resolution, context relevance, faithfulness to source. Source: https://www.evidentlyai.com/llm-guide/llm-as-a-judge

**OpenAI Evals templates (primary, evals repo docs/eval-templates.md)**
- Basic (deterministic): **Match** (startswith), **Includes**, **FuzzyMatch**, **JsonMatch**.
- Model-graded: **fact.yaml** — 5-way verdict A/B/C/D/E (submission ⊆ expert & consistent; ⊇ & consistent; = same details; ≠ disagreement; ≈ differences immaterial to factuality); **closedqa.yaml** — checks *relevant, concise, correct* (Y/N); **battle.yaml** — head-to-head comparison of two completions.
- Judge response formats (`eval_type`): **cot_classify** (reason→answer, recommended), **classify_cot** (answer→reason), **classify** (choice only). `choice_scores` maps choices to scores.
- Source: https://github.com/openai/evals/blob/main/docs/eval-templates.md

**Azure AI Foundry / Microsoft Foundry built-in evaluators (primary, full enumeration)**
- General purpose: **Coherence, Fluency**
- Textual similarity: **Similarity, F1 Score, BLEU, GLEU, ROUGE, METEOR**
- RAG: **Retrieval, Document Retrieval, Groundedness (1–5), Groundedness Pro (binary pass/fail), Relevance, Response Completeness**
- Risk & safety: **Hate and Unfairness, Sexual, Violence, Self-Harm, Protected Materials, Indirect Attack (XPIA), Code Vulnerability, Ungrounded Attributes, Prohibited Actions, Sensitive Data Leakage**
- Agent: **Task Adherence, Task Completion, Customer Satisfaction** (six dimensions: helpfulness, completeness, clarity, tone, resolution, adaptability), **Intent Resolution, Task Navigation Efficiency, Tool Call Accuracy, Tool Selection, Tool Input Accuracy, Tool Output Utilization, Tool Call Success, Quality Grader**
- **Rubric** evaluator: "Scores a response or multi-turn conversation against custom, weighted criteria using an LLM as the judge… weighted average score normalized to 0–1 with per-dimension reasoning."
- Custom: **Model Labeler, String Checker, Text Similarity, Model Scorer**; evaluation levels: **turn** vs **conversation**.
- Source: https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/concepts/built-in-evaluators.md (rendered: https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators)

### 7.2 Self-check / self-critique procedures (research)

- **Chain-of-Verification (CoVe)**, arXiv:2309.11495 — 4 steps: (1) draft **baseline response**; (2) **plan verification questions**; (3) **execute verifications** independently (answers not biased by the draft); (4) generate **final verified response**. Source: https://arxiv.org/abs/2309.11495
- **Self-Refine**, arXiv:2303.17651 — same model alternates **FEEDBACK → REFINE** iterations on its own output; no extra training; ~20% average human-preference improvement across 7 tasks. Source: https://arxiv.org/abs/2303.17651
- Related (cited for completeness, not fetched this session): **Reflexion** (arXiv:2303.11366, verbal self-reflection memory across attempts); **Constitutional AI critique→revision loop** (arXiv:2212.08073); **multi-agent debate** for factuality (arXiv:2305.14325).

### 7.3 Grounding/citation modes (vendor)

**Anthropic "Reduce hallucinations" guardrail menu** (docs): **allow "I don't know"** ("Explicitly give Claude permission to admit uncertainty"); **direct-quote extraction first** for long docs (>20K tokens) to ground answers; **verify with citations** ("make Claude's response auditable by having it cite quotes and sources for each of its claims"); **restrict to provided documents** (no general knowledge). Source: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations (confirmed via search snippets; page fetch redirected — mirror content verified at https://github.com/anthropics/courses prompt-engineering tutorial 08_Avoiding_Hallucinations)

### 7.4 Synthesized review-mode menu for the template tool

1. **Self-check / verify-then-answer** (CoVe 4-step) — arXiv:2309.11495
2. **Critique-and-revise loop** (Self-Refine FEEDBACK→REFINE; N iterations) — arXiv:2303.17651
3. **Rubric grade** (custom weighted criteria, 0–1 or 1–5, per-dimension reasoning) — Azure Rubric evaluator
4. **Binary pass/fail per criterion** (relevant/concise/correct Y-N) — OpenAI closedqa; Evidently binary guidance
5. **Pairwise compare / battle** (A vs B, optionally position-swapped) — OpenAI battle; survey pairwise mode
6. **Rank a list** (listwise) — arXiv:2412.05579
7. **Reference-based factuality verdict** (subset/superset/equal/contradiction/immaterial) — OpenAI fact template
8. **Cite-and-quote grounding** (quotes first, citations per claim, allow "I don't know") — Anthropic guardrails
9. **Steelman/devil's advocate critique** — NO formal published picker found; supported indirectly by persona libraries (Debater, Fallacy Finder, Perspectives ponderer) and multi-agent debate research (arXiv:2305.14325)
10. **Safety/compliance screen** (PII, harmful content, prompt-injection) — Azure risk & safety evaluators; Evidently PII criterion

---

## Retrieval gaps (explicit)

- OpenAI primary pages openai.com/index/introducing-canvas and help.openai.com (403) — Canvas slider intermediate tick labels sourced from secondary walkthroughs only.
- Grammarly's full 40+-tone detector list — no page enumerates all; ~11 tones confirmed by name.
- support.claude.com styles article 10181068 — 404 at fetch time; Claude styles presets sourced from press coverage.
- Copilot Prompt Gallery complete Task/Job-type filter lists — login-gated SPA; partial lists from secondary sources.
- Vertex AI metric-prompt-template page relocated (docs.cloud.google.com restructure to "Gemini Enterprise Agent Platform"); its pointwise_/pairwise_ metric name list not captured — Azure evaluator list used as the cloud-vendor enumeration instead.
