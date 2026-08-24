# R9 (Part A): Frameworks from the User's Own Prompt-Engineering Library (Google Drive)

Extraction date: 2026-08-21. Method: direct document extraction via Google Drive MCP (`read_file_content`). No web search used (per task instructions). Source attribution is by Google Drive file ID; quote marks indicate verbatim text from the document.

Truncation status at a glance:
- Doc 1 (Crash Course PDF): extracted **complete** (all 8 sections returned).
- Doc 2 (Phoenix & Taylor): **truncated** — tool returned ~64K chars = front matter + Chapter 1 only (cuts off mid-"Evaluate Quality" discussion). Chapter 1 contains the Five Principles in full, which is what we needed.
- Doc 3 (Venkataraman): **truncated** — ~80K chars, covers front matter through mid-Chapter 4 (ends at heading "4.3 Strategies for Prompt Engineering"); full TOC captured, so all framework names are known.
- Doc 4 (Ibrahim John): extracted **complete** (short book; intro through conclusion returned).

---

## 1. PRIORITY SOURCE: "Prompt Engineering Crash Course" (2025 Edition)

Source: Google Drive PDF, fileId `1so7aGdD47qVss3X9NlXERc8lM5B_ypDr`. Subtitle: "A Practical Guide for Sales Professionals." (Audience is sales, but the frameworks are audience-agnostic and transfer directly to supplier/quality engineering — swap the examples.)

### 1.1 Definition and founding analogy

- Definition (verbatim): "Prompt engineering is the skill of writing clear instructions to get the output you need from AI tools like ChatGPT, Claude, or Gemini."
- Analogy (verbatim): "Think of it like giving directions—the more specific you are, the better your results." (Technically defensible: more constraint in the prompt shifts output token probabilities toward the intended target; matches Phoenix & Taylor's probability framing in Doc 2.)
- Key insight box (verbatim): "The clear prompt gives AI: context (who), task (what), constraints (how), and goal (why). This is the foundation of prompt engineering."

### 1.2 THE 5 BUILDING BLOCKS OF A GREAT PROMPT (complete, verbatim table)

Framing sentence (verbatim): "Every effective prompt uses some combination of these five elements. You don't need all five every time, but knowing them helps you diagnose why a prompt isn't working."

| # | Element | What It Does | Book's example |
|---|---------|--------------|----------------|
| 1 | ROLE | "Tells AI who to be" | "Act as an experienced sales manager" |
| 2 | CONTEXT | "Background info" | "Our company sells B2B software to mid-market" |
| 3 | TASK | "Specific instruction" | "Write a follow-up email" |
| 4 | FORMAT | "How to structure output" | "Use bullet points, under 100 words" |
| 5 | TONE | "Communication style" | "Professional but conversational" |

Complete worked example using all 5 (verbatim from the PDF):
- ROLE: "Act as an experienced B2B sales rep with 10 years in software sales."
- CONTEXT: "I'm reaching out to a marketing director at a mid-size e-commerce company. They visited our pricing page twice this week but haven't booked a demo."
- TASK: "Write a short follow-up email that acknowledges their interest without being pushy."
- FORMAT: "Keep it under 75 words. Include a clear subject line."
- TONE: "Warm, helpful, low-pressure."

### 1.3 THE CRISP FRAMEWORK (complete, verbatim)

Framing (verbatim): "When you're stuck on how to structure a prompt, use CRISP as a mental checklist."

| Letter | Stands For | Ask Yourself (verbatim) |
|--------|-----------|--------------------------|
| C | **Context** | "What background info does AI need?" |
| R | **Role** | "Who should AI pretend to be?" |
| I | **Instructions** | "What exactly should AI do?" |
| S | **Specifics** | "What constraints, format, or length?" |
| P | **Purpose** | "What's the end goal?" |

"CRISP in Action" example (verbatim): "C: I sell project management software to construction companies. Prospect uses spreadsheets. R: Act as an expert sales copywriter for B2B software. I: Write a LinkedIn connection request message. S: Under 300 characters. Don't pitch the product directly. P: Get them curious enough to accept so I can send a follow-up."

Note: CRISP is essentially the 5 Building Blocks re-ordered as a checklist mnemonic (Tone folds into Specifics; Purpose is added). Good teaching point: one is a parts list, the other is a memory aid.

### 1.4 Core techniques (the book's technique set, all 5, with the book's "What/When" framing)

1. **Zero-Shot Prompting** — "Ask AI to do something with no examples—just clear instructions." When: "Simple, straightforward tasks."
2. **Few-Shot Prompting** — "Give AI 1-3 examples of what you want before asking it to generate." When: "You need AI to match a specific style or format."
3. **Chain-of-Thought** — "Ask AI to think step-by-step before answering." When: "Complex problems or when you need to see reasoning."
4. **Role-Based Prompting** — "Assign AI a specific persona or expertise." When: "You need domain-specific knowledge or communication style."
5. **Prompt Chaining (Iterative)** — "Break complex tasks into steps, using each output as input for the next." When: "Multi-step tasks like research → analysis → content." Example pattern: Step 1 research → Step 2 map to product → Step 3 write outreach using that insight.

Pro tip (verbatim): "Don't try to do everything in one prompt. Complex tasks get better results when broken into 2-3 steps. Think conversation, not command."

### 1.5 Common mistakes (all 6, condensed; fixes verbatim where quoted)

1. Being Too Vague — fix: "Always include: who it's for, what it's about, and how long."
2. Asking Too Much at Once — fix: "Break into 2-3 focused prompts. Quality > quantity."
3. No Examples — fix: "Give 1-2 examples of content you like."
4. Accepting First Output — fix: "Iterate: 'Make it shorter' or 'More casual tone.'"
5. Copy-Paste Without Review — fix: "Always review for accuracy, tone, and personalization."
6. 100% AI Reliance — fix: "AI handles tasks. Real connections need your voice."

Security warning (verbatim; highly relevant for a medical-device audience): "Never put sensitive customer data, proprietary info, or confidential details into public AI tools. Use enterprise versions or anonymize data first."

### 1.6 Quick-reference cheat sheet (key reusables)

Universal Prompt Template (verbatim): "[ROLE] Act as a [expertise/persona]. [CONTEXT] Here's the situation: [background]. [TASK] I need you to [specific action]. [FORMAT] Format as [structure/length]. [TONE] Make it [tone]. [EXAMPLE] Here's what I'm looking for: [example]"

Power words table: better structure → "Step by step", "First... then... finally"; shorter → "Concise", "Under X words", "Bullet points only"; more creative → "Brainstorm 10 alternatives"; more specific → "Give concrete examples"; options → "Give me 3 versions"; simpler → "Explain like I'm 5", "Avoid jargon".

Quick fixes: too long → "Keep under [X] words"; too generic → add context; wrong tone → "Tone: [casual/formal/friendly/direct]"; sounds robotic → "Write like a human" or give writing examples.

Includes a 7-Day Action Plan (Day 1 pick one tool → Day 7 integrate into real workflow) and a 16-tool directory (ChatGPT, Claude, Gemini, DeepSeek, Perplexity, Copilot, Midjourney, DALL-E 3, Canva, Stable Diffusion, Jasper, Copy.ai, Notion AI, Grammarly, Synthesia, Runway, ElevenLabs, GitHub Copilot, Cursor). CAUTION: the tool directory and prices are "2025 Edition" marketing-level claims — treat pricing/feature rows as UNVERIFIED for Aug 2026 and re-verify separately before teaching.

Closing rule (verbatim): "The best prompt is the one that gets you the result you need. No single 'right' way—just clearer and less clear ways to communicate. Keep experimenting."

---

## 2. Phoenix & Taylor, "Prompt Engineering for Generative AI" (O'Reilly, 2024)

Source: Google Doc, fileId `1Fl7HPq_m8c-Mj1iUm0UZCAVmrP4SUwKc7H9jPb3yKGA`. Authors: James Phoenix and Mike Taylor. TRUNCATED: tool returned front matter + Chapter 1 ("The Five Principles of Prompting") only; later chapters not retrieved. The principles were first published by the authors in a July 2022 blog post ("Prompt Engineering: From Words to Art and Copy") and, per the book, "map quite closely to OpenAI's own Prompt Engineering Guide."

### 2.1 Definitions (verbatim)

- "Prompt engineering is the process of discovering prompts that reliably yield useful or desired results."
- "A prompt is the input you provide, typically text, when interfacing with an AI model like ChatGPT or Midjourney."
- Mechanism note (verbatim): "LLMs work by continuously predicting the next token (approximately three-fourths of a word), starting from what was in your prompt." And: "What you put in your prompt changes the probability of every word generated."

### 2.2 THE FIVE PRINCIPLES OF PROMPTING (verbatim, name + book's one-line explanation)

1. **Give Direction** — "Describe the desired style in detail, or reference a relevant persona"
2. **Specify Format** — "Define what rules to follow, and the required structure of the response"
3. **Provide Examples** — "Insert a diverse set of test cases where the task was done correctly"
4. **Evaluate Quality** — "Identify errors and rate responses, testing what drives performance."
5. **Divide Labor** — "Split tasks into multiple steps, chained together for complex goals"

Book's claim about them (verbatim): "These principles are not short-lived tips or hacks but are generally accepted conventions that are useful for working with any level of intelligence, biological or artificial." Also stated: model-agnostic — they apply to both text and image generation.

The principles map 1:1 to the five failure modes of a naive prompt (the book's diagnostic frame): *Vague direction*, *Unformatted output*, *Missing examples*, *Limited evaluation*, *No task division*.

### 2.3 Per-principle teaching notes captured from Chapter 1

- **Give Direction:** role-playing / persona ("in the style of Steve Jobs") dramatically changes output; analogy (verbatim tip): "it can be helpful to imagine what context a human might need for this task and try including it in the prompt" — the "creative brief" analogy (branding agencies require a detailed brief; so does the model). Defensible analogy.
- **Specify Format:** "AI models are universal translators" — between languages AND data structures (JSON/YAML/code). Format flips break production software, so state format up front.
- **Provide Examples:** defines zero-shot / one-shot / few-shot; cites the GPT-3 paper "Language Models are Few-Shot Learners" — adding one example can improve some task accuracy "from 10% to near 50%". Analogy: training a junior employee — you'd naturally show examples of the task done well. Defensible.
- **Evaluate Quality:** names the anti-pattern *blind prompting* (trial-and-error with no measurement); discusses evals, thumbs-up/down feedback loops, side-by-side comparison and Elo ratings (Chatbot Arena, lmsys.org); notes fine-tuning "starts to beat prompt engineering once you can supply a few thousand examples."
- **Divide Labor:** detailed section fell past the truncation point; the one-liner above is verbatim from the chapter's overview list.

### 2.4 Other named items in the retrieved text

- Temperature parameter (randomness of token selection); token-probability example (Figure 1-1).
- Companion "one-pagers" (text + image) used as checklists; the authors' Udemy course "The Complete Prompt Engineering for AI Bootcamp (70,000+ students)".
- NOT RETRIEVED (past truncation): the book's chapters on text/image generation techniques, LangChain, agents, etc. — do not cite specifics from those chapters based on this extraction.

---

## 3. Subramanian Venkataraman, "Crafting Effective Prompts: A Guide to Prompt Engineering" (First Edition Mar-01-2024)

Source: Google Drive file, fileId `1gko00NCLHJdOfx23U6VZCSFEqn18UjU3`. TRUNCATED: retrieved through mid-Chapter 4; complete TOC captured. Main framework/technique lists only, per task scope. This book is more technical (includes Python code, vector stores, HuggingFace deployment).

### 3.1 Main framework: "Anatomy of a Prompt" (7 components, section 3.2)

Framing analogy (paraphrase of book): prompts are the "grammar" of conversation with AI machines — unclear questions get vague answers, same as with humans; refine iteratively. (Defensible.)

1. **Invocation** — how you initiate/address the model (book's example: "Hi, Alexa"; in its worked example: "AI, please").
2. **Instruction** — the action verb telling the model what to do ("Write," "Explain," "What").
3. **Content** — the subject/topic; must be specific or responses lack relevance.
4. **Context** — "defines the scope of the question... sets constraints to restrict the model's response within the specified subject or desired format."
5. **Tone/Style** — desired voice (book highlights service industries and education).
6. **Purpose** — directs how to respond "based on... the audience, time, and context."
7. **Parameters** — configurable settings; book lists: context, max_tokens ("maximum word count"), temperature ("creativity or randomness"), model selection. Example: "Limit the response within 300 words."

Worked example assembling all elements (verbatim fragments): Invocation "AI, Please" + Instruction "write" + Content "a short story on forest" + Context "where the animals set the eco system," + Tone/Style "with a thrilling tone" + Purpose (highlight survival of the fittest) + Parameter "Keep it under 300 words."

### 3.2 Prompt techniques list (section 3.5, complete list from TOC; definitions where retrieved)

1. Zero-shot prompting
2. Few-shot prompting
3. Chain-of-thought prompting — "an extension of few-shot prompting, where instead of providing a few explicit examples, the model is given a series of interconnected prompts to follow a logical order" (verbatim fragment)
4. Self-consistency prompting — "involves setting context from the answer generated from first [prompt]" (verbatim fragment; i.e., feeding a first answer back for consistency)
5. General knowledge prompting
6. Tree-of-thoughts prompting
7. Automatic Prompt Engineering

### 3.3 Other named lists (from TOC / retrieved text)

- Qualities of good prompting (sec 2.1): Clarity, Specificity, Context, Instructional Prompts, Eliminating Bias, Creativity and Constraints, Iterative Refinement, Sequential Prompts.
- Types of prompts (sec 3.4): Open-ended, Closed-ended, Instructional, Contextual.
- "Strategies for Prompt Engineering" (sec 4.3): Temperature Control, Length Control, Explicit Instruction, Informativeness, Constraint Handling, Error Handling, Handling Ambiguity. (Heading list retrieved; body text past truncation.)
- Advanced chapters (titles only, not retrieved): multi-turn conversational prompts, contextual prompts, exploratory prompts, question answering, multi-model prompting, incorporating external knowledge, summarization, mitigating bias/fairness; vector stores (dot product, cosine similarity, ChromaDB); HuggingFace deployment.

---

## 4. Ibrahim John, "The Art of Asking ChatGPT for High-Quality Answers: A Complete Guide to Prompt Engineering Techniques" (Nzunda Technologies, 2023)

Source: Google Drive file, fileId `1v_tGEyPLGpMVIc38vXLmp5LGMb8DhJrN`. Extracted complete. Main technique list only, per task scope. Style: each chapter = one technique + a "prompt formula."

### 4.1 The book's core "prompt formula" (verbatim)

"A prompt formula is a specific format for the prompt, it is generally composed of 3 main elements: **task** (a clear and concise statement of what the prompt is asking the model to generate), **instructions** (the instructions that should be followed by the model when generating text), **role** (the role that the model should take on when generating text)."

### 4.2 Technique list (all 23 chapters, with formula where memorable)

1. Instructions Prompt — "Generate [task] following these instructions: [instructions]"
2. Role Prompting — "Generate [task] as a [role]"
3. Standard Prompts — "Generate a [task]"
4. Zero, One and Few Shot Prompting
5. "Let's think about this" prompt — prefix "Let's think about this:" / "Let's discuss..." to invite reflective, multi-angle output (the book's take on think-step-by-step-style prompting)
6. Self-Consistency Prompt — "Please ensure the following text is self-consistent" (used for fact-checking/data validation)
7. Seed-word Prompt — "Please generate text based on the following seed-word: [word]"
8. Knowledge Generation Prompt — "Generate new and accurate information about [topic]"
9. Knowledge Integration Prompt — "Integrate the following information with the existing knowledge about [topic]: [new info]"
10. Multiple Choice Prompts — constrain answer to predefined options
11. Interpretable Soft Prompts — controlled inputs + flexibility (e.g., "in the style of [author]")
12. Controlled Generation Prompts — template / vocabulary / constraint-driven generation
13. Question-Answering Prompts
14. Summarization Prompts
15. Dialogue Prompts — generate conversations between defined characters/entities
16. Adversarial Prompts — generate text designed to be hard to classify (robustness testing)
17. Clustering Prompts — group items by characteristic (e.g., reviews by sentiment)
18. Reinforcement Learning Prompts
19. Curriculum Learning Prompts — simple tasks first, then harder
20. Sentiment Analysis Prompts
21. Named Entity Recognition Prompts
22. Text Classification Prompts (explicitly distinguished from sentiment analysis)
23. Text Generation Prompts

The book repeatedly demonstrates COMBINING techniques (e.g., instruction + role + seed-word): "As a marketing representative, generate an informative, persuasive product description that highlights the innovative features of the new smartphone."

Quality caveat for the trainer: this 2023 self-published book anthropomorphizes some ML-training concepts as "prompts" (chapters 17-20 — adversarial, RL, curriculum learning are model-training ideas, not things a chat user literally invokes; a model does not "adjust its behavior based on rewards" within a chat). Its chapters 6-7 also diverge from the research meanings: the research "self-consistency" (Wang et al.) means sampling multiple reasoning chains and majority-voting, and "Let's think step by step" is the zero-shot CoT trigger — the book's versions are looser folk adaptations. Use its technique NAMES and simple formulas, but prefer Docs 1-2 for definitions.

---

## 5. Cross-library synthesis for the training deck

- Strong convergence across all four sources on the same skeleton: **Role/Persona + Context + Task/Instruction + Format/Constraints + Tone/Style (+ Purpose/Goal + Examples)**. Crash Course = "5 Building Blocks" and CRISP; Phoenix & Taylor = Give Direction/Specify Format/Provide Examples; Venkataraman = 7-part Anatomy; John = task/instructions/role formula. Teach one skeleton, show the aliases.
- All four independently teach zero-/few-shot, chain-of-thought-style reasoning, and role prompting — these are the consensus core techniques.
- Phoenix & Taylor uniquely add the two "engineering" principles the others lack: **Evaluate Quality** (measure, don't blind-prompt) and **Divide Labor** (task decomposition/chaining) — the Crash Course's "Prompt Chaining" and mistake #2 partially cover Divide Labor.
- Best memorable rules for slides: "Think conversation, not command" (Doc 1); "Average prompts will return average responses" (Doc 2); the giving-directions and creative-brief analogies (Docs 1-2, both defensible).
- Compliance hook for the med-device audience: Doc 1's security box (never paste confidential data into public tools) + Doc 1's mistake #5 (always review before use) align with human-in-the-loop expectations in regulated environments.
