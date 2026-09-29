# Recommended topics to add — "From Prompts to Agents"

Prepared 2026-09-29 by the `topics` research agent. Read-only review of the owner-final deck (69 slides, text dump `deck_main.txt`), the Reference Deck (67 slides, `deck_ref.txt`), the book (`src/assets/course_content.json`, 9 chapters), the Template Creator (`src/builder_template.html`) and the taxonomy (`prompt-library/taxonomy/*.json`, 18 presets G1–G8, A1–A5, GX/AX).

Conventions: every dated fact carries its date. "Covered" cites deck positions (`pos N`, the slide's order in the file; `printed N` is the number on the slide) or book headings. "Secondhand" marks claims taken from a news or blog summary rather than the primary page. No model identifiers are used in this file; examples are fictional.

Audience reminder: analysts and managers using chat assistants and agentic tools for spreadsheets, dashboards, presentations, email and supplier quotes.

---

## Ranked list (summary)

| # | Topic | Priority | Effort | Slot |
|---|-------|----------|--------|------|
| 1 | Prompting reasoning-tier models: outcome, not procedure | must | S–M | Part 3 live (pos 35) + book ch. 3 + Template Creator toggle |
| 2 | Prompt injection for chat users: the email you summarize can carry orders | must | S | Part 4 live (pos 44) + Reference Deck + book ch. 4 |
| 3 | Where your words go: training defaults by account type | must | S | Part 2 (one live row) + Reference Deck 106 + book ch. 2 |
| 4 | Screenshots, charts and scanned PDFs: transcribe, check, then compute | should | M | Part 4 pos 46 divider + new Template Creator preset |
| 5 | Team-scale evaluation: a golden set, a scorecard, a different grader | should | M | Part 6 (ref 62) + workbook tab + book ch. 6 |
| 6 | Portability: one plain-text prompt, any assistant | should | S | Part 6 (ref 60/61) + Template Creator note line |
| 7 | Self-reports are not evidence: the model on itself, its confidence | should | S | Part 1 notes (pos 8–11) + Field Guide |
| 8 | Context engineering, the two missing sentences | should (residual) | S | Reference Deck pos 51 + book ch. 1/5 |
| 9 | Briefing a deep-research run | could | S | Template Creator G7 variant + book ch. 4 |
| 10 | Meeting recaps and transcripts as a play | could | M | Reference Deck 99 "more plays" + workbook |
| 11 | EU AI Act Article 4: the course as an AI-literacy record | could | S | pos 1–2 notes + book intro |
| 12 | The Prompt Report map: name the families once | could | S | Book ch. 7 + Reference Deck 108 |
| 13 | Prompting in more than one language | could | S | Field Guide + Template Creator language option |
| 14 | Structured output for office users (table / CSV / JSON) | could | S | Template Creator format option + book ch. 3 |

---

## 1 · Prompting reasoning-tier models: outcome, not procedure — MUST

**Plain description.** Newer "thinking" models plan their own steps. When you hand them a long recipe ("first do this, then that, then think step by step"), you can make the result worse, not better. What still helps is saying what a good result looks like, what must not happen, what evidence to use, and when to stop. The habit to teach: write the finish line, not the route.

**Evidence.**
- OpenAI, *Reasoning best practices* (developer guide; page undated; fetched 2026-09-29): "Keep prompts simple and direct: The models excel at understanding and responding to brief, clear instructions." · "Avoid chain-of-thought prompts: Since these models perform reasoning internally, prompting them to 'think step by step' or 'explain your reasoning' is unnecessary." · "Reasoning models often don't need few-shot examples to produce good results, so try to write prompts without examples first."
- OpenAI, current-model prompting guide (https://developers.openai.com/api/docs/guides/gpt-5.5; fetched 2026-09-29): "Reduce or remove detailed step-by-step process guidance. Let [the model] choose the path unless the product requires that path." · "Start with the smallest prompt that preserves the product contract." · Keep "success criteria," "stopping conditions," and "constraints."
- Anthropic, *Prompting best practices* (platform docs; fetched 2026-09-29): "Prefer general instructions over prescriptive steps. A prompt like 'think thoroughly' often produces better reasoning than a hand-written step-by-step plan." · "Remove over-prompting." · Also: "Providing context or motivation behind your instructions, such as explaining ... why such behavior is important, can help."

**Why it matters here.** The audience will meet thinking modes inside every office assistant. Today's course teaches a seven-element anatomy plus numbered steps and wait-gates; without this nuance, participants will over-script the model and blame it when the answer is mechanical.

**Already covered.** pos 35 (printed 32) EXPIRED column, row 1: "'Think step by step' → pick a reasoning model, set the effort dial"; NOT TO DO row 5: "smallest prompt that keeps the contract"; pos 61 (Template A1) notes: "DESIGN THICK, SHIP LEAN"; pos 56 (Reference toolkit) "The anatomy: the elements the task needs"; book ch. 3 "Prompt techniques to test" → "Was right — then the product absorbed it".

**Gap.** The course says what to unlearn but never states the positive rule for thinking tiers: keep outcome + success criteria + constraints + evidence + stop; drop process steps and example piles unless the path itself is the requirement. The live anatomy walk (pos 25–29) can be heard as "fill all seven, always."

**Where it slots.** Part 3 live: one added row on pos 35 ("TO DO 6: on a thinking tier, write the finish line, not the route") and one SAY line on pos 31 (improvement loop: "if you turned effort up, take process steps out"). Book ch. 3 "Prompt techniques to test": a short subsection. Template Creator: a "thinking tier" switch that hides the step-list block and keeps success/stop.

**Effort.** S for deck + book; M if the Template Creator switch is built. **Priority: must** — the prior review flagged it and three vendors now say the same thing.

---

## 2 · Prompt injection for chat users: the email you summarize can carry orders — MUST

**Plain description.** When you ask an assistant to summarize a thread or a document, everything in that thread goes into the model — including hidden text an outsider planted. A crafted email can tell the assistant to fetch private files and send them out through a link or an image. This happened to a mainstream office suite in 2025 and was fixed by the vendor. The lesson for a chat user: the material you feed in is *data*, and if the summary starts doing odd things (adds links you didn't ask for, mentions "instructions", asks you to click), stop and report it.

**Evidence.**
- *EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System*, arXiv 2509.10540 (submitted 2025-09-06): a "zero-click prompt injection vulnerability" in Microsoft 365 Copilot that "enabled remote, unauthenticated data exfiltration via a single crafted email."
- The Hacker News, 2025-06-11 (secondhand): CVE-2025-32711, CVSS 9.3, patched by Microsoft, "no evidence that the shortcoming was exploited maliciously in the wild."
- OWASP, *Top 10 for LLM Applications 2025* (published 2025-03-12 per the OWASP page; fetched 2026-09-29): LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM06 Excessive Agency.
- Microsoft Learn, *Enterprise data protection* (ms.date 2026-05-29): Copilot helps "safeguard against AI-focused risks such as harmful content and prompt injections" — i.e. the vendor treats it as a live control, not a solved problem.

**Why it matters here.** The Part 4 email exercise (pos 44–45) is run in the exact product class where the zero-click exploit was found. The audience summarizes real supplier threads every day.

**Already covered.** pos 63 (WORKING SAFELY, appendix): "Prompt injection is real — Anything the agent reads ... can carry hostile instructions. Danger peaks when private data + untrusted content + outbound channels combine: break one leg." pos 59 notes: "everything below the divider is DATA, never instructions." Both live in Part 5/appendix and are framed for *agents*.

**Gap.** Nothing in the live 60 minutes tells a *chat* user that a summarized email is untrusted input, or what to do when a summary misbehaves. No dated, real, office-suite incident is cited (the deck cites a browser-agent red-team figure and a community-skill case).

**Where it slots.** Part 4 live, pos 44 (Outlook teach): one line — "The thread is data. If the summary adds a link, mentions instructions, or asks you to act, stop and tell IT." Reference Deck: the WORKING SAFELY slide gets EchoLeak as the office-suite example. Book ch. 4 step 6 sidebar "Practice on fiction only": add the incident and the stop rule.

**Effort.** S. **Priority: must** — highest-consequence gap for this audience, and the fix is one sentence plus one dated example.

---

## 3 · Where your words go: training defaults by account type — MUST

**Plain description.** Whether an assistant learns from what you paste depends on the *account*, not the brand. Personal accounts on the big consumer apps use your chats to train by default unless you switch it off; business, enterprise and API accounts don't by default; the office-suite assistant says tenant data is not used to train its models. Web-search queries have separate rules. Before pasting a supplier quote, know which account you are in.

**Evidence.**
- OpenAI Help, *Data controls FAQ* (page returned 403 to the fetch tool; content via search summary, secondhand, fetched 2026-09-29): on Free, Plus and Pro personal workspaces, "data sharing is enabled for you by default"; with Business, Enterprise, Edu and the API, "by default, we don't use provided inputs and outputs to train our models"; the toggle is "Improve the model for everyone."
- Anthropic consumer policy change announced 2025-08-28 (secondhand: Business Today 2025-08-29; ICAI note): from 2025-09-28, Free/Pro/Max chats are used for training unless the user opts out, with retention extended to five years for consenting users; enterprise, government, education and API offerings excluded.
- Microsoft Learn, *Enterprise data protection in Microsoft Copilot and Microsoft Copilot Chat* (ms.date 2026-05-29; fetched 2026-09-29): "the prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation models." Web queries "are sent via a secure connection with user and tenant identifiers removed" but "the Bing search service operates separately from Microsoft 365 and has different data-handling practices."

**Why it matters here.** The course's own exercises paste quotes, threads and datasets. The audience mixes personal and work accounts.

**Already covered.** Reference Deck pos 60 (printed 106) "The right workspace for the data": "Approved account · Allowed material · Minimum access" — generic, relocated to self-study on 2026-09-18. pos 7 notes still say: "That is exactly what 'trains on your data by default' means on the trust slide in Part 2" — that slide no longer exists in the live deck (dangling reference). Book ch. 2 "The right workspace for the data" → "Before any upload".

**Gap.** No dated, concrete statement of defaults by account type; no mention that web-grounding queries are handled differently; the pos 7 note points at a removed slide.

**Where it slots.** Part 2 live: one row on pos 17 or a footer on pos 18 ("Personal account = training on by default; business account = off by default — check Settings before pasting"). Reference Deck 106: a three-row table (personal / business / office suite) with dates. Book ch. 2: same table. Fix the pos 7 note.

**Effort.** S. **Priority: must** — direct data-handling risk, cheap to add, and it repairs a broken cross-reference.

---

## 4 · Screenshots, charts and scanned PDFs: transcribe, check, then compute — SHOULD

**Plain description.** Assistants can read pictures now, but they misread them more often than people do — a "3" becomes an "8", a minus sign disappears, a dashed line is confused with a solid one. The safe habit: ask for a verbatim transcription into a table first, spot-check two or three values yourself against the picture, and only then let the assistant calculate.

**Evidence.**
- *ChatBCG: Can AI Read Your Slide Deck?*, arXiv 2407.12875 (submitted 2024-07-16): tested models could "read 7-8 out of 15 labeled charts perfectly end-to-end" and "underperform compared to humans", with worse results on "unlabeled charts (where data ... has to be inferred from the X and Y axis)." The HTML version reports error rates of 16% and 14% on labeled charts versus under 5% for humans (secondhand via search summary).
- OpenAI, *Images and vision* guide, "Limitations" (fetched 2026-09-29): "The model may misinterpret rotated or upside-down text and images." · struggles with "graphs or text where colors or styles—like solid, dashed, or dotted lines—vary." · "The model may give approximate counts for objects in images." · "may not perform optimally when handling images with text of non-Latin alphabets."
- *Unmasking Deceptive Visuals: Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering*, arXiv 2503.18172 (submitted 2025-03-23; EMNLP 2025): 24 models tested on 3,026 misleading-chart examples; the abstract frames misleading charts as a "critical vulnerability."

**Why it matters here.** Supplier quotes arrive as PDFs and photos; dashboards are shared as screenshots. The course's own Part 4 block "From DOC to data analysis · PDFs, graphs to data entry" (pos 46) promises exactly this and then teaches text-PDF extraction only.

**Already covered.** pos 47 (Quote-Extract): "Copy values exactly as stated ... Cite the source file and page for every extracted commercial value." pos 8: "use AI for language, software for characters." Reference Deck pos 67 (printed 113) prompt: "Using the supplied screenshot or copied text ... Mark anything the supplied information does not establish as needing verification."

**Gap.** No slide or book passage says that image/chart reading has a higher error rate than text, or gives the transcribe → spot-check → compute rule. The pos 46 divider's speaker notes are a copy of the data-block notes from pos 36 (they talk about uploading the supplier workbook), so the block has no teaching content of its own. No Template Creator preset for "picture or scan → table".

**Where it slots.** Part 4 pos 46: replace the copied notes with a 40-second teach: "pictures are read, not parsed — transcribe first, check two values, then compute." Template Creator: new preset "G9 · Image or scan → verbatim table" seeded from the Quote-Extract prompt. Book ch. 4 step 7: one sidebar.

**Effort.** M (preset + notes + book). **Priority: should.**

---

## 5 · Team-scale evaluation: a golden set, a scorecard, a different grader — SHOULD

**Plain description.** A shared prompt needs a small test kit: five to ten saved inputs with the answers you expect, a one-line pass/fail rule for each, and a habit of re-running the kit whenever the prompt or the model changes. If you let a model grade the results, use a *different* model from the one that wrote them and make it output a number, not an essay.

**Evidence.**
- Anthropic, *Create strong empirical evaluations* (platform docs; fetched 2026-09-29): "Be task-specific: Design evals that mirror your real-world task distribution, including edge cases." · "Automate when possible." · "Prioritize volume over quality: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals." Example rubric ends with "Output only the number."
- OpenAI, *Evaluating model performance* guide (fetched 2026-09-29): "Evaluations (often called evals) test model outputs to ensure they meet style and content criteria that you specify." Workflow: describe the task, run with a test dataset, analyze and iterate.
- Panickssery, Bowman, Feng, *LLM Evaluators Recognize and Favor Their Own Generations*, NeurIPS 2024 (arXiv 2404.13076, 2024-04): "self-preference" — "an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality."

**Why it matters here.** Part 6 asks participants to promote prompts to a team library; a team library without a test kit drifts silently at the next model upgrade (the deck's own "re-baseline on every upgrade" rule, pos 35).

**Already covered.** Reference Deck pos 16 (printed 62) "A small review process for shared prompts": typical / edge / unanswerable cases; "Record the version, owner, source assumptions, and review date." pos 56 CHECK quadrant: "Self-check on NAMED criteria." Reference Deck printed 109 (neutral rubric) and 110 (review checklist). Team-library fields on printed 57 include "models tested · last tested."

**Gap.** No "saved test set" object, no expected-output column, no pass/fail scorecard, no rule that the grading model differs from the writing model, no trigger ("re-run on model change").

**Where it slots.** Part 6: extend printed 62 with a fourth card "Keep the three cases as a saved test kit; re-run on every change." Workbook: a new tab "EVAL-Kit" (input · expected · pass rule · last run · model). Book ch. 6 "A small review process": one subsection. Template Creator: G3 evaluation preset gains an option "Grader is a different model from the author."

**Effort.** M. **Priority: should** — the prior review named it; the fix reuses existing slides.

---

## 6 · Portability: one plain-text prompt, any assistant — SHOULD

**Plain description.** The same prompt should work in any assistant. Keep the prompt as plain text with clear fill-in slots; keep product tricks (how you attach or point at a file) outside the template; test it in two tools before you share it; write down which tools you tested.

**Evidence.**
- Microsoft Support, *Refer to specific files and more in Microsoft 365 Copilot* (undated; via search summary, secondhand, 2026-09-29): "type '/' and begin typing the file you wish to link."
- Google Workspace blog, *5 tips for writing great prompts for Gemini in the Workspace side panel* (2024-07-29): "Use @ to give Gemini more information from other files."
- *The Prompt Report*, arXiv 2406.06608 (v6, 2025-02-26), §5.2.1: "Small Changes in the Prompt" can significantly change results — the reason a template must be re-tested per tool.

**Why it matters here.** The Part 4 email exercise is written for one office suite ("WHERE TO CLICK IN OUTLOOK", pos 44) with a paste fallback; participants will move between tools and licences ("admin flags mean colleagues get different capabilities", pos 17).

**Already covered.** pos 2: "every assistant, every vendor, every year"; pos 44: "If that feature is unavailable, paste the supplied fictional thread into an approved assistant — same prompts, same results"; Reference Deck printed 57 storage map with "models tested" field; pos 35 "re-baseline on every upgrade."

**Gap.** No stated portability rule; the file-reference syntax differs by product ("/" vs "@" vs attach) and nothing tells participants to keep that outside the template.

**Where it slots.** Part 6 live/ref (printed 60–61): one line "plain text + slots; product syntax stays outside; tested in two tools." Template Creator: an "attach / reference" helper line under Context → material ("Attached document") listing the three product conventions. Book ch. 6 "Tools change; the practice does not" (heading already exists — extend it).

**Effort.** S. **Priority: should.**

---

## 7 · Self-reports are not evidence: the model on itself, and its confidence — SHOULD

**Plain description.** A model's description of its own features, its own version, its own cutoff or how sure it is are just more generated text. Research finds no reliable "self-access", and human-feedback training pushes models to sound more confident than they should. So: check features in the vendor's help pages, and instead of asking "how confident are you?", ask for the evidence and the list of gaps.

**Evidence.**
- Song, Hu, Mahowald, *Language Models Fail to Introspect About Their Knowledge of Language*, arXiv 2503.07513 (submitted 2025-03-10): "we do not find evidence that LLMs have privileged 'self-access'" and "LLMs cannot introspect" (21 open models tested).
- *Taming Overconfidence in LLMs: Reward Calibration in RLHF*, arXiv 2410.09724 (2024-10-13, revised 2025-02-28): "RLHF tends to lead models to express verbalized overconfidence in their own responses."

**Why it matters here.** Four of the seven live exercises ask the assistant to explain its own tokens, context window, two speeds and architecture (Prompts 3, 4, 5, 7). The notes carry "recovery" lines for when answers disagree across the room, but no rule that these answers are illustrations, not facts.

**Already covered.** pos 35 NOT TO DO row 4: "'are you sure?' as verification"; pos 15 sycophancy countermeasures; Reference Deck printed 113 prompt: "Mark anything the supplied information does not establish as needing verification."

**Gap.** No explicit statement that self-descriptions and confidence ratings are ungrounded; "rate your confidence 1–10" is not on the myth list.

**Where it slots.** Part 1: one facilitator SAY line on pos 8 or pos 11 ("the model is explaining a concept, not reporting its own settings — check the help page"). Field Guide / book ch. 7 myth list: add "Confidence scores as verification". Adjust the WHY lines of Prompts 3/4/5/7 in the workbook.

**Effort.** S. **Priority: should.**

---

## 8 · Context engineering: the two missing sentences — SHOULD (residual)

**Plain description.** The course already names context engineering. Two ideas from the source article are still missing and are easy to say: keep the desk to "the smallest possible set of high-signal tokens", and remember that models get worse at finding things as the desk fills ("context rot").

**Evidence.** Anthropic, *Effective context engineering for AI agents* (2025-09-29): context engineering is "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference"; aim for "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome"; "context rot: as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases"; system prompts at the "right altitude": "specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics."

**Already covered.** pos 9 amber card: "Pros call this CONTEXT ENGINEERING: the prompt is the briefing; context is everything on the desk"; glossary entry; pos 21 four context failures (poisoning, drift, confusion, clash); pos 9 "lost in the middle".

**Gap.** "Minimum effective dose" and "context rot" are not stated; the link between "fewer, better tokens" and topic 1 (shorter prompts) is not drawn.

**Where it slots.** Reference Deck pos 51 (printed 49) and book ch. 1 "Context, saved history, and memory": two sentences. Book ch. 5 intro: one line tying it to the mission brief.

**Effort.** S. **Priority: should**, but most of the work is done — treat as a polish item.

---

## 9 · Briefing a deep-research run — COULD

**Plain description.** Research modes run for many minutes and ask a few questions before they start. A good brief names the question, the decision it serves, the sources to prefer or avoid, the output shape and the date range — and answers the clarifying questions fully, because a re-run is expensive.

**Evidence.** OpenAI, *Introducing deep research* (2025-02-02; via search summary, secondhand): the mode "will ask a few clarifying questions" before searching. OpenAI forum, *Exploring deep research: three tips* (2025-04-28; secondhand): state the objective clearly, answer the clarifying questions, give keywords and clear verbs.

**Already covered.** pos 4–5 mention "deep-research modes"; Reference Deck printed 113 "Capabilities to look for in an assistant"; Template Creator preset G7 "Research brief — cited"; book ch. 4 step 9 "Reference files become a research workbook."

**Gap.** G7 is a chat-turn brief; nothing addresses the long-running mode or its clarifying questions.

**Where it slots.** Template Creator: a G7 variant "deep-research mode" adding source rules, exclusions, date range and "answer the clarifying questions before it starts." Book ch. 4 step 9: one paragraph.

**Effort.** S. **Priority: could.**

---

## 10 · Meeting recaps and transcripts as a play — COULD

**Plain description.** Meeting recaps are among the most common office assistant tasks and share the email play's traps: a decision that changed mid-meeting, an approval with a condition, a question nobody answered. The same "Not stated + cite the speaker and time" discipline applies.

**Evidence.** Not researched this session (unknown). The recommendation rests on the course's own email-play design (pos 44, pos 59) transferring to a transcript.

**Already covered.** Main deck: zero mentions of "meeting"; Reference Deck printed 99 "MORE PLAYS WE CAN DRILL NEXT" (contents not itemised here); book ch. 4 mentions meetings four times.

**Gap.** No transcript exercise, no fictional transcript in the practice pack.

**Where it slots.** Reference Deck 99 + workbook tab "EX-Meeting" with a fictional 10-minute transcript and a key; a G8 preset variant.

**Effort.** M (needs a fictional transcript with planted traps). **Priority: could.**

---

## 11 · EU AI Act Article 4: the course as an AI-literacy record — COULD

**Plain description.** Since 2025-02-02, organisations in the EU that use AI systems must "take measures to support the development of AI literacy" of staff, taking account of their role and context. A role-specific course like this one is the kind of measure the rule expects; keeping the attendance list and the syllabus is the cheap part.

**Evidence.** Regulation (EU) 2024/1689, Article 4 (text at artificialintelligenceact.eu; fetched 2026-09-29): "Providers and deployers of AI systems shall take measures to support the development of AI literacy" of their staff and others operating AI on their behalf; applies from 2025-02-02 per Article 113(a).

**Why it matters here.** The exercise data uses euros and a Berlin site, which suggests an EU footprint — the organisation's actual jurisdiction is unknown.

**Already covered.** Nothing in deck or book mentions the Act or literacy obligations.

**Gap.** No statement of purpose linking the course to a compliance record.

**Where it slots.** pos 1–2 facilitator notes and the book introduction: one paragraph; keep attendance and version in the repo.

**Effort.** S. **Priority: could** (jurisdiction unknown).

---

## 12 · The Prompt Report map: name the families once — COULD

**Plain description.** The course already kills the famous tricks one by one. Naming the survey's families once ("examples in the prompt", "thought generation", "decomposition", "ensembling", "self-criticism") lets a reader see that the evidence table covers the whole map.

**Evidence.** *The Prompt Report: A Systematic Survey of Prompt Engineering Techniques*, arXiv 2406.06608 (submitted 2024-06-06; v6 2025-02-26): "a taxonomy of 58 LLM prompting techniques, and 40 techniques for other modalities." Section 2.2 families as read from the v6 HTML: In-Context Learning, Thought Generation, Decomposition, Ensembling, Self-Criticism (secondary blogs list six with Zero-Shot as a separate family — not confirmed from the paper text this session).

**Already covered.** pos 2 notes: "the Prompt Report counts 58 text + 40 other-modality techniques"; pos 35 evidence columns; book ch. 7 "The evidence box set: works, myth, expired."

**Gap.** The families are never named; readers cannot tell the table is complete.

**Where it slots.** Book ch. 7 intro sentence; Reference Deck printed 108.

**Effort.** S. **Priority: could.**

---

## 13 · Prompting in more than one language — COULD

**Plain description.** Write the prompt in the language you want the deliverable in. For tasks about local culture or wording, prompting in that language tends to work better than translating to English; non-English text also costs more tokens.

**Evidence.** *Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models*, arXiv 2403.10258 (submitted 2024-03-15): "translation into English can boost the performance of English-centric LLMs" on standard tasks, but for culture-related tasks "prompting in the native language proves more effective."

**Already covered.** pos 8: "non-English and dense technical text cost more tokens"; Template Creator Context → constraints option "Language/units house rules"; Role identity option "Translator / localizer."

**Gap.** No guidance on which language to prompt in. The audience's working languages are unknown.

**Where it slots.** Field Guide one paragraph; Template Creator Format → a "deliverable language" option.

**Effort.** S. **Priority: could.**

---

## 14 · Structured output for office users (table / CSV / JSON) — COULD

**Plain description.** When the answer will be pasted into a spreadsheet or read by another tool, ask for the exact column list, or for CSV in a code block; ask for JSON only when a program will consume it. The strictest version (schema-enforced output) exists in the developer products, not the chat apps.

**Evidence.** Deck's own citations at pos 28/54 (OpenAI Structured Outputs, 2024-08; JSONSchemaBench 2025). Anthropic prompting best practices (fetched 2026-09-29): "Try asking the model to conform to your output structure first, as newer models can reliably match complex schemas when told to."

**Already covered.** pos 28 Format: "A table with exactly: Site | Return rate | vs target | Trend"; taxonomy Format → output_type includes "Table", "Comparison matrix".

**Gap.** No "CSV in a code block" option and no note that chat apps do not enforce schemas.

**Where it slots.** Template Creator Format → output_type: add "CSV block (paste into a sheet)"; book ch. 3 Format paragraph: one sentence.

**Effort.** S. **Priority: could.**

---

## What I could not verify

- OpenAI *Data controls FAQ*: the help page returned HTTP 403 to the fetch tool; the defaults quoted in topic 3 come from search-result summaries (secondhand).
- Anthropic's 2025-08-28 consumer-data policy: news coverage only; the primary announcement was not fetched.
- EchoLeak CVSS score and "no evidence of exploitation": The Hacker News (secondhand); the arXiv abstract was verified.
- Microsoft "/" file-reference syntax: search-result summary of a Microsoft Support page, not the page itself.
- The Prompt Report's exact number of top-level families (five per the v6 HTML fetch; six per secondary blogs).
- ChatBCG's 16% / 14% chart error rates: from the HTML version via search summary; the abstract wording ("7-8 out of 15 labeled charts") was verified.
- IEEE VIS 2025 "Perils of Chart Deception": secondhand (university news page); not fetched.
- Deep-research clarifying-question behaviour and tips: secondhand.
- Google's "21 words" claim is Google's own internal figure (blog, 2024-07-29), not independently measured.
- The audience's jurisdiction and working languages: unknown.
- Whether Reference Deck printed 99 "MORE PLAYS" already lists meeting transcripts: not itemised this session.

## Side findings (not topics)

- pos 43 and pos 46 (the "Email summary exercise" and "From DOC to data analysis" dividers) carry speaker notes copied from pos 36 (the data-block divider): "Everything in this block runs on one workbook you upload at the start..." — the notes do not match the slide titles.
- pos 7 notes refer to "the trust slide in Part 2" which is no longer in the live deck (relocated to Reference Deck printed 106 on 2026-09-18).
- The live Context & Format slide (pos 28, printed 27, source-detail block) still states "cut memory-override errors 35%→3% and lifted accuracy on unanswerable questions 31%→88%", while the appendix copy of the same card (pos 54, printed 53) was softened to "source-grounding studies report improvements on specific tasks; those effect sizes are not universal" — the live and appendix wordings of one claim disagree. The same pair exists in the Reference Deck (lines 2220 vs 2262 of `deck_ref.txt`).
