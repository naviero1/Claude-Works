# PENDING CHANGES — v1.5 ledger (brainstorm phase, NOT yet applied)

**Status:** the owner is reviewing the deck slide by slide. Nothing below is applied to any
deliverable — this file is the complete, detailed holding pen. When the owner says
**"update"**, execute the checklist at the bottom. Owner review completed through Part 2
(physical slides 1–20) as of 2026-09-09; Part 3 review is in progress and will append here.

**Owner's standing rules gathered during this review (bind every change below):**
- R1. No edits to deck/deliverables until the owner says "update". This ledger is the record.
- R2. **Teach-first prompts** (owner's words): each guiding prompt "has to be simple and
  well explained… can either instruct more or inform and give a didactic example — don't
  push it on didactic examples testing capabilities if it will confuse the trainee more
  than teach."
- R3. **Every example, joke, and analogy must be understandable** to a non-technical room —
  each one below carries a "say it plainly" line; presenter notes must include it.
- R4. Speaker notes must be well-spaced for reading accuracy: one item per line, blank
  lines between sections. Template: HOW TO PRESENT / BRIDGE / TRY IT (where a prompt
  exists) / ACRONYMS / CONTENT.
- R5. No durations printed on slides.
- R6. Guiding-prompt layer is **capped at eight** ("enough with the prompt guiding
  questions"). No new prompts beyond the roster below.
- R7. Every new fact is dated and traceable to notes/research/ (new files r11–r14).
  Anything on an UNVERIFIED list must be re-checked before it touches a slide.
- R8. Session shape: three training blocks, 80 minutes core each, expandable to 120 with
  priced expansion modules. (Supersedes the two 1-hour-session copy currently on slides.)
- R9. Trainees keep ONE chat thread all course — their "course log" — so the prompts double
  as a take-home repository of the course.

---

## A. THE GUIDING-PROMPT ROSTER (final texts, capped at 8)

On-slide treatment, identical everywhere: a teal band with a chip reading **PROMPT n/8**
plus a small robot/AI icon; prompt text in Consolas. Numbering is provisional until the
owner finishes reviewing (assign final n/8 at update). Each slide's notes carry the
TRY IT section with the debrief and recovery lines below.

**P1 — slide 2 (Welcome) · "Two prompting modes" — opens the course log**
> This chat is my course log. Entry 1, same request two ways: a farewell card for a
> coworker. First, just write it. Then don't write it — draft the job brief instead:
> goal, inputs you need from me, checks, when to stop and ask.
- Debrief: the card ran on guesses (invented names, bracketed blanks); the brief asked YOU.
- Recovery (model asks questions both times): "guessing and bracketing are generative
  mode; asking is the agentic move — the brief just makes it happen on purpose."

**P2 — slide 6 (Under the hood) · "Narrowing the guesses" — two separate sends**
> Send 1: Finish this sentence 5 different ways: "We should move the launch date because"
> Send 2: Now 5 more ways, knowing: B2B software firm, competitor launches May 3, our
> beta ends April 20. What changed?
- Debrief: "Grade the directions, not the sentences — your facts didn't add intelligence,
  they deleted wrong guesses."

**P3 — slide 7 (Tokens) · "Bricks, not letters" (judged rewrite under R2)**
> Prompt — Tokens: bricks, not letters.
> You don't read letters — you read tokens: chunks of text, like LEGO bricks. Teach me
> this in under 150 words, like I'm a new office colleague.
> 1. Chop this sentence into token-style chunks, putting | between chunks (a rough split
> is fine — exact cuts vary): "Our quarterly onboarding checklist is ready."
> 2. Then one short sentence each: (a) why counting letters or making exact letter edits
> can go wrong for you; (b) what I should ask you to do FIRST when I need letter-perfect
> work; (c) why tokens are what I pay for and what fills up your memory of our chat.
> Plain language, no jargon.
- Debrief: point at the | marks — that is what the AI actually sees.
- Recovery (splits differ across the room / model hedges): "that IS the lesson — every
  vendor has its own brick set; the bricks are always there, the letters never are."
- NOTE: the old reversal demo is DEAD (2026 models pass it, teaching the opposite).
  Strawberry stays as a told story only.

**P4 — slide 8 (Context window) · "The handoff note" (judged rewrite under R2 — one
window; the old two-window choreography is DEAD)**
> Exercise — the handoff note. One day this chat gets too long, or I close it — and your
> desk is swept clean. Let's prepare now. Boil our course thread so far into a handoff
> note titled HANDOFF 4/8, under 80 words (shorter is fine): everything a brand-new chat
> would need to continue my training — what course this is, which numbered exercises
> I've done, and what comes next.
> Under the note, add two plain sentences explaining why I need it: what happens to
> everything in this chat the moment it closes.
> Then one last sentence: what would you need to remember me across chats? Just name
> it — we get there in Part 5.
- Debrief/homework: "tonight, paste your HANDOFF into a brand-new chat, ask 'Where was
  I?', and watch it pick up your course mid-stream."
- Recovery (note runs long / skips an exercise): "you just watched a long thread sag in
  the middle — the very reason we write handoff notes before we need them; reply 'add
  Exercise X and trim to 80 words'."

**P5 — slide 10 (Escalation ladder) · "Triage drill" (two sends; trainee commits before
the model grades — learning is model-proof). Owner has NOT trimmed it; default six
problems.**
> Course log — The Escalation Ladder: triage drill.
> Run a fast sorting drill for me, working only from the text below. Show me the six
> workplace AI problems as a numbered list, then STOP and wait for my answer. Your first
> reply is the numbered list and nothing else — no rungs, no hints, no reasoning.
> I'll reply with one letter per problem: P (fix with a better prompt — instructions,
> examples, tone, format), R (fix with retrieval — hand the AI the right documents), or
> F (fix with fine-tuning — retrain its habits; slow, costly, rarely the answer).
> The problems:
> 1. The assistant writes good product descriptions, but they never match our brand
> voice — even though the voice guide is three bullet points long.
> 2. The assistant confidently answers questions about our vacation policy — using last
> year's rules.
> 3. Support replies come out friendly and accurate, but twice as long as any customer
> will read.
> 4. The assistant can't answer "what did we decide in the March pricing review?" — it's
> all in our meeting notes.
> 5. A hospital's dictation tool keeps garbling that specialty's spoken shorthand,
> thousands of times a day; no document you hand it would change how it hears.
> 6. Our contract reviewers' AI must apply the firm's 40-page internal risk rubric to
> every contract. Pasting the rubric in works, but it crowds out the room the contract
> itself needs.
> After I answer, grade me in under 150 words. For each problem give your rung and ONE
> sentence of reasoning built on this diagnostic: is it a knowledge problem (the AI is
> missing or holding outdated information → retrieve), a behavior problem (it has what it
> needs but acts wrong → prompt), or a deep-habit problem that must hold across huge
> volume with no room for pasted instructions (→ fine-tune)? If one of my answers is
> defensible either way, say so and count it correct instead of marking it wrong. End
> with: my score out of 6, and the single question I should ask myself before choosing a
> rung next time.
- Debrief: "Who put F on number 6? Defend it — notice every argument comes down to one
  question: does the AI lack knowledge, or is it misbehaving with knowledge it already
  has. That question is the whole ladder."
- Recovery (model blurts answers past the STOP): "cover the screen, sort the six on paper,
  then scroll back and argue with it — a grader that can't wait for your diagnosis is
  exactly why the diagnosis has to live in your head."

**P6 — new slide 11A (Fast vs thinking) · "Fast answers vs careful answers" (verified
unique solution: Ben Mon · Chloe Tue · Ema Wed · Ana Thu · Dev Fri — trainer can check 20
screens at a glance; designed NOT to need the fast answer to be wrong)**
> Course log — next entry: Fast answers vs. careful answers.
> A small scheduling puzzle. Five colleagues — Ana, Ben, Chloe, Dev, and Ema — each
> present on a different day, Monday to Friday, one person per day.
> - Ana does not present on Monday.
> - Dev presents the day immediately after Ana.
> - Ema presents on Tuesday or Wednesday.
> - Ben presents earlier in the week than Chloe.
> - Chloe presents the day immediately before Ema.
> Do all three parts in one reply:
> PART 1 — FAST: Your instant answer: the five names with their days, on one line.
> Nothing else — no workings, no commentary.
> PART 2 — CAREFUL: Now solve it as if it really mattered: work through the possibilities
> step by step, check your final schedule against every one of the five rules, then state
> your final answer. Under 250 words.
> PART 3 — THE BILL: Estimate the word count of Part 1 and of Part 2 (rough is fine). If
> every word cost the same small amount, how many times more expensive was the careful
> version? Did your two answers agree? End with one sentence: when is the fast version
> enough, and when is it not?
- Debrief: "Shout your multiple — most of you paid 10–20x for the careful pass; that is
  exactly how the thinking tier bills you. Turn it on when stakes demand it, not by
  default."
- Recovery (fast answer already right): "you didn't beat the exercise — you caught the
  pricing: modern models often deliberate quietly even before the 'instant' line."

**P7 — new slide 11B (Feature menu) · meta-prompt; self-updating as vendors rename modes**
> Course log — next entry: The feature menu.
> You are the product I'm typing into right now. List the answer modes and major features
> this product offers me as a user — a quick answer, a deeper-thinking or
> extended-reasoning mode, web search, a deep-research mode that browses many sources for
> minutes, and any agent mode that takes multi-step actions for me. Only include what
> this product really has today. Give me a tight table, max 6 rows: (1) what the mode is
> called here, (2) what it actually does differently behind the scenes, (3) rough effort
> vs. a quick answer — 1x, 5–20x, or 100x+, (4) one everyday work task where it's the
> smallest mode that can succeed, (5) one task where it would be wasteful overkill,
> (6) where I switch it on in this interface — say "unsure" rather than guessing. Finish
> with a one-sentence rule of thumb for picking the smallest mode that can succeed.
- Debrief: "Read your column 1 aloud around the room — four different menus, one identical
  1x/20x/100x ladder. You didn't memorize this chart; you asked for it — ask again the
  day the menu changes."
- Recovery (model misstates its own UI/toggles): "meta-prompting's fine print: it knows
  what its modes DO far better than where the buttons live — keep the ladder, verify the
  toggles with your own eyes."

**P8 — slide 16 (DeepSeek moment) · "The specialist hospital" (owner-requested; drafted
under R2, informally judged — flag to owner it did not go through the full adversarial
round like P1–P7)**
> Course log — the specialist hospital.
> Explain Mixture of Experts to me like a colleague: a model built as a huge specialist
> hospital where only a few departments wake up for each question. Then, in plain
> language: why did this make powerful AI dramatically cheaper in 2025 — and what does
> that have to do with the deep-research and thinking modes I now get in my own AI app?
> Under 120 words.
- Debrief: "671 billion parameters on the books, ~37 billion awake per question — you pay
  for the specialists consulted, not the whole hospital."

**Removed/duplicate prompt ideas (do NOT resurrect):** metaprompting-as-its-own-prompt,
a Part 5 prompt, the migrated "Analyze the returns data" opener as a chip (see slide 13
entry), the strawberry test, the two-window handoff, the reversal demo.

---

## B. PART 1 CHANGES (physical slides 1–13)

### Slide 2 — Welcome
1. Title B chosen: **"Ask, or delegate — prompting does both"** (replaces "One skill, two
   modes — and a library you keep").
2. Keep both mode definitions and the 10-second-version teal card.
3. Map card: keep the six-part outline; **delete durations/session-split copy** (R5, R8) —
   replace "The map — two one-hour sessions / SESSION 1 / SESSION 2" with the three-block
   shape, no minutes printed.
4. Multimodal aside (one line + notes): "This course teaches the text wing. Image, video
   and audio prompting have their own dials — same discipline, different controls — and
   if there's enough interest, that can become its own training." Supporting fact for
   notes: the Prompt Report counts 58 text techniques plus 40 for other modalities
   (t1_prompt_report.md).
5. Add P1 chip (course log opens here).
6. Notes: rewrite in R4 spaced template; update the rep-pattern sentence (see slide 13).

### Slide 4 — Four eras
1. Thread the named technologies through the cards: Rules era → symbolic AI, expert
   systems (MYCIN, XCON). Learning era → machine learning, neural networks, deep learning
   + GPUs (AlexNet 2012, 15.3% vs 26.2% error). Generative era → transformers, LLMs.
   Agentic era → reasoning models, tool use.
2. Add one **schematic mini-diagram per era card** (owner chose schematics over data
   charts): tiny decision tree · tiny neural net · attention-lines sketch · agent loop
   (plan→act→check). House palette, small, inside each card.
3. No guiding prompt on this slide (owner). Scaling-laws amber band stays as text.

### Slide 5 — The decade
1. Timeline entries each carry their named method: 2017 Transformer · 2020 scaling laws +
   few-shot (GPT-3) · 2022 instruction tuning + RLHF (the 1.3B-beats-175B fact) · 2024
   reasoning / test-time compute (o1) · 2025 MoE + distillation + open weights (R1) ·
   2026 agentic harnesses.
2. Replace the "Adoption, in numbers" card with a single **time-to-100M-users bar chart**:
   ChatGPT 2 months · TikTok ~9 months · Instagram ~2.5 years (UBS/Reuters 2023 — single
   consistent source). Owner explicitly does not care about user counts beyond one honest
   graphic.
3. Agent-gap stat ("agent deployment still single-digit % — the gap is the opportunity")
   moves to speaker notes only.
4. NEVER build a multi-company user-growth line: verified metrics don't mix (WAU vs MAU vs
   downloads; only ChatGPT has 3 same-metric points; zero verified counts for
   Claude/Copilot/Perplexity/Grok).

### Slide 6 — Under the hood
1. Add the thesis line to the "Why prompting exists" callout: **"A complete prompt doesn't
   make the model smarter — it deletes wrong guesses."** (Prediction runs on plausibility;
   every fact you add narrows what counts as plausible.)
2. Add P2 chip (two sends).

### Slide 7 — Tokens
1. Upgrade the token-chip strip to **LEGO-brick styling** (studs on top, same house
   palette, same eight chunks). Keep slide structure otherwise.
2. Replace the "Try it once (tokenizer)" card with the P3 chip.
3. Strawberry stays in notes as a story, told WITH its mechanism; not a live demo.

### Slide 8 — Context window
1. Add P4 chip (replaces habit ④'s passive mention — summarize-and-carry becomes a taught,
   performed move).
2. Add a small teaser card: "A desk with a filing cabinet? Persistent files, notes and
   standing instructions are exactly what agentic tools bolt onto the desk — Part 5."
   (Nothing concrete; a seed. The prompt's last line makes the AI name it.)

### Slide 9 — RAG
1. Add a small teal strip: **"You already use this. Our internal company assistant — the
   one where you upload documentation and 'talk' to it — is RAG in production. Every step
   on this slide happens each time you ask it a question."**
   HARD RULE: no product name, no vendor name, no person named (repo hard rule 1).
2. Notes: presenter points at the four step cards — "you've been running this loop all
   along."

### Slide 10 — Escalation ladder
1. Add the generic diagnostic on-slide (this is what makes the ladder a reusable
   framework): **"One question triages everything: is the AI missing knowledge, or
   misbehaving with knowledge it already has? Missing → retrieve. Misbehaving → prompt.
   Deep habit at huge volume with no room to paste instructions → fine-tune (rare)."**
2. Add P5 chip (triage drill).
3. Disambiguate the two ladders (metaphor collision found in review): qualify bare "the
   ladder" phrases — slide 9's bridge line becomes "…the escalation ladder"; Part 6's
   kicker becomes "PART 6 · THE PROMOTION LADDER"; Part 6 rep bullet "which rung of the
   promotion ladder…". Glossary (closing part): add one-line entries for both ladders.

### Slide 11 — Reasoning models → SPLIT INTO TWO SLIDES (both labeled Concept 5)
Owner: "I don't want them to think in terms of a particular AI spending modality… use two
slides if you want to explain this right." Facts below are already verified in
r2_concepts.md §8, t4_choice_enums.md §5, r6_chinese.md; consumer research-mode NAMES need
the fresh-research pass (see Section E, item 3).

**11A — "Concept 5 · Fast models vs thinking models (1 of 2)"**
- Every vendor ships a fast tier (one pass, instant, cheap) and a thinking tier (drafts,
  checks and revises internally before answering — spending compute at answer time).
  System 1 / System 2 analogy stays.
- The bill: thinking tokens are billed like output tokens (~5x input price); a hard
  question can quietly cost 5–20x a simple one; by 2026 the dial is adaptive with
  selectable effort.
- Why the fast tier got good (one line, generic — the DeepSeek STORY stays on slide 16):
  MoE + distillation — models built huge but waking only a fraction per question, and big
  models teaching small ones.
- Keep the ON/OFF lists (green/amber cards) from the current slide.
- P6 chip.
**11B — "Concept 5 · The feature menu — where your tokens go (2 of 2)"**
- The cost ladder as a graphic: quick answer 1x → extended thinking 5–20x → web search →
  Deep Research 100x+ → agent modes (most of all).
- Deep Research explained honestly: a reasoning model given a browser and time — it plans,
  reads sources for minutes, and synthesizes a cited report. MoE is WHY this became
  affordable, not HOW it works (owner's "MoA/deep-research" wiring corrected; owner
  acknowledged).
- Discipline line: pick the smallest mode that can succeed; escalate deliberately.
- Copilot named as the everyday instance of the menu (modes verified: Researcher, Analyst,
  Think Deeper — r5_tools.md; consumer mode names across vendors pending Section E.3).
- Notes: the scaling anecdote, generic phrasing — one prompt to a fast model vs an
  orchestrated multi-agent deep run = hundreds of quick answers' worth of tokens (the
  sessions that built this course are the live example).
- P7 chip.
**Split mechanics:** the "(Part 3 preview) think-step-by-step is now often redundant" hook
and the notes bridge "last concept — the one everyone asks about first" move to 11B (the
second half). Divider copy "six concepts" stays true — both halves are Concept 5.

### Slide 12 — Hallucination → EXPAND INTO TWO SLIDES (both labeled Concept 6)
**12A — "Concept 6 · Hallucination — what it is, and the four kinds (1 of 2)"**
- Keep: mechanism bullet (most PLAUSIBLE next token, not most true), the OpenAI 2025 bold
  bullet, "fluency is not evidence".
- Add vocabulary gem: the closest human analog is **confabulation** — the model isn't
  seeing things; it fills gaps with plausible material, in-format (fake citations LOOK
  like citations, fake URLs look like URLs) (r10_library_b.md).
- Add the four kinds (teaching frame, not claimed as academic taxonomy — r14): invented
  facts · invented sources · confidently-wrong-from-a-bad-source (the RAG failure) ·
  running-with-your-false-premise (truth bias).
- The improv-actor analogy stays (say it plainly — see Section F).
**12B — "Concept 6 · The hall of shame — and the cure (2 of 2)"**
- OWNER LOCKED: **four incidents on-slide** — glue-on-pizza/eat-a-rock · the ChatGPT
  lawyer · Air Canada's bereavement chatbot · the Big Four arc (Deloitte→EY→KPMG as one
  row). Full verified texts, dates, sources and MANDATORY phrasing caveats in
  notes/research/r14_hallucination_incidents.md. Closer stat: ~1,500 court decisions
  worldwide involving AI-fabricated citations by mid-2026.
- The other nine verified incidents go in speaker notes (with the Bard-$100B phrasing
  caveat, Hood threatened-not-filed, Cohen not-sanctioned).
- Keep Ground it / Cite it / Verify it cards and the red house-rule band EXACTLY as they
  are (owner: "which you already have in this slide"). New framing line: "here's how you
  avoid being slide material."
**Expansion mechanics:** the closing bridge "that closes the concepts — …then the tool
landscape" moves to 12B and DROPS the rep mention (see next).

### Slide 13 — Three-minute rep → DELETE
- Owner: "We don't need this slide." The freed slot funds the 11A/11B split; the 12A/12B
  expansion adds one net slide.
- The vague-prompt exercise does NOT migrate as a slide or chip (owner capped prompt
  moments). Its content survives two ways only:
  a. Part 3's anatomy slide is already the corrected version of the same returns-data
     prompt (deck_pt3.js), and the elements slide re-runs "Analyze the returns data." as
     the weak Task example — the diagnosis is re-taught there.
  b. OPTIONAL spoken cold-open, notes-only, on the Part 3 divider: read "Analyze the
     returns data and make it look good for leadership" aloud, deadpan, and say "hold
     that thought — every gap you can feel in it has a name on the next slide." No slide,
     no chip, skippable.
- WORDING SYNC: "Analyze the returns data" also lives in ELEMENTS.md, taxonomy
  generative.json, build_elements_guide.py — do not reword anywhere without regenerating
  from the taxonomy (hard rule 3).
- Required note patches when deleting (found by structural sweep — these fail silently):
  1. deck_pt1.js welcome notes: rewrite "Parts 1, 3, 5, and 6 end with a skippable
     three-minute rep…" to the new truth (P1's rep removed; P2's died with slide 20; 3, 5,
     6 pending owner review).
  2. Hallucination slide's HOW-TO-PRESENT bridge: "…a three-minute rep, then the tool
     landscape" → "…then the tool landscape" (and it moves to 12B).
  3. Keep six "Concept n" labels intact (divider promises "six concepts").
  4. H.slide second-arg literals are stale/cosmetic (auto-numbering is live) — correct or
     delete them while editing these files so nobody miscounts later.

---

## C. PART 2 CHANGES (physical slides 14–20)

### Slide 15 — The assistants: add the "known for" layer
Evidence: notes/research/r13_reputations_r1.md. Rewrite each card's forte line to the
defensible versions (owner's impressions corrected where evidence disagreed):
- **ChatGPT**: "The everything assistant — fastest at drafts, options and marketing copy;
  largest user base." (Owner's "ChatGPT writes better than Claude" is REFUTED by LMArena
  creative-writing June 2026 and EQ-Bench Aug 2026 — both put Claude #1. Do not print the
  claim; notes may carry the correction.)
- **Claude**: "Best-in-class coding & agentic work — tops SWE-bench AND OpenAI's own
  real-work eval (GDPval); 1M-token documents; 2026 writing evals put it #1 for careful
  prose."
- **Gemini**: "Multimodal breadth + deepest Google integration — 1B+ monthly users;
  default AI inside Gmail/Docs/Meet."
- **Copilot**: "Ubiquity and governance — 30M+ paid seats (Jul 2026) inside the M365
  compliance boundary IT already audits. Licenses others' models — including Claude:
  Copilot Cowork runs on Claude Cowork's agent technology." (This replaces the owner's
  unbenchmarkable "Cowork slightly better than Copilot" with the stronger licensing fact.)
- **Perplexity**: "Research with receipts — ~94% of answers carry inline citations; lowest
  citation-error rate in CJR's AI-search testing."
- **Grok**: "Blunt on purpose — 'Unhinged' is a literal voice mode; real-time X data;
  aggressive price-performance. Caveat: fewer guardrails has meant real incidents (Jul
  2025 apology) — care for brand-sensitive work."
- Trust: NO per-vendor badges here (evidence says trust tracks the TIER, not the vendor —
  r11). One pointer line: "Which of these can see company data? Two slides ahead."
- Salvaged from deleted slide 20 into these notes: "vendor benchmark numbers are marketing
  until independently reproduced."
- Keep [REFRESH QUARTERLY]; re-date the footer at update.

### Slide 16 — The DeepSeek moment: define MoE, add the graph, link forward
1. Define MoE ON-SLIDE (currently acronyms-notes only), with the analogy written plainly
   (see Section F): built like a giant hospital of specialist departments — 671B
   parameters on the books, only ~37B wake up for any one question; you pay for the
   specialists consulted, not the whole building.
2. Add the **R1 vs o1 chart** (data verified, r13): five benchmark pairs — AIME 79.8/79.2,
   MATH-500 97.3/96.4, SWE-bench Verified 49.2/48.9, GPQA Diamond 71.5/75.7, Codeforces
   percentile 96.3/96.6 — plus the price bar $2.19 vs $60 per M output tokens (27x).
   HONESTY RULES: keep the two benchmarks o1 won; headline "matched on most, ~27x
   cheaper"; label Codeforces as human percentile, not accuracy. Source on slide:
   "DeepSeek-R1 paper, Jan 2025".
3. Link lines to the new 11A/11B pair: "This is why thinking tiers and deep-research
   modes didn't stay luxury-priced" (and 11B says "the mechanism behind this cheapness —
   Part 2, the DeepSeek moment").
4. Add P8 chip (specialist hospital).
5. Notes add the honest 2026 status line: NIST CAISI (May 2026) put DeepSeek ~8 months
   behind the frontier; still the open-weight value leader.
6. Keep the fuel-bill/racing-team caveat (say it plainly — Section F).

### Slide 17 — Who's who → becomes the servers & trust slide
Evidence: notes/research/r11_vendor_trust.md. Redesign:
1. LEFT — the server map (one row per vendor, verified): Anthropic (stored in US; EU via
   Bedrock/Vertex/Foundry) · OpenAI (EU residency Feb 2025; in-region inference Jan 2026 —
   business tiers only) · Google (enterprise residency by region; consumer reviewed-chats
   kept up to 3 years) · Microsoft (EU Data Boundary; footnote: the Claude models inside
   Copilot sit OUTSIDE it) · xAI (own Memphis/Southaven data centers; no residency
   options) · Perplexity (AWS worldwide; none published) · DeepSeek ("stored in the
   People's Republic of China" — its own policy, Feb 2026) · Kimi (PRC storage) · Z.ai
   (Singapore; parent on US Entity List).
2. RIGHT — the three-tier traffic light, badging the TIER not the vendor:
   GREEN company tenant (no training by default, SOC 2 — all vendors) · YELLOW personal
   account (trains by default, leak history, never client/regulated data) · RED
   China-hosted consumer apps (no company data, ever).
3. KEEP: the title-rule sentence, the red/green China cards' substance (restaurant vs
   cookbook), and the "one question decides: does company data leave your network?"
   callout as the closer.
4. Notes: green ≠ invulnerable (EchoLeak CVE-2025-32711, zero-click Copilot exfiltration,
   patched Jun 2025) · Grok's 370K Google-indexed chats (Aug 2025) · DeepSeek's exposed
   chat-log database (Jan 2025) · defaults drift — re-verify quarterly · if the Italy
   €15M OpenAI fine is ever cited, cite the Mar 2026 annulment with it.

### Slide 18 — Agent gallery → SPLIT INTO TWO SLIDES
Evidence: notes/research/r12_tool_landscape.md. Sixteen entries don't fit one slide.
**18A — "The agent gallery" (the doers):** Claude Code · Claude Cowork · ChatGPT Work ·
Copilot agents · **Manus** (new — general agent; one-line story: "famous enough that Meta
bought it for $2B and Beijing forced the deal apart; now independent in Singapore — try it
personally, don't feed it company data") · **Notion Agents** (new — agents living inside
the workspace you already use; run 24/7 on triggers) · Browser agents (Comet · Claude in
Chrome) · Automation platforms (n8n · Zapier) · OpenClaw (amber cautionary card stays).
Coding IDEs row may compress to one line to make room.
**18B — "The specialist shelf" (the makers):**
- **NotebookLM — renamed Gemini Notebook, Jul 2026** (say both names): answers grounded in
  YOUR uploaded documents, with citations; audio overviews. Best new tool for this room.
- **Meeting notes**: check Teams/Zoom native first (IT-sanctioned); Granola if
  best-in-class is wanted — bot-free, but flag the recording-consent policy.
- **Decks & design**: Gamma (decks from a prompt; $100M ARR) + Canva AI (the suite
  marketing already licenses).
- **Images**: Adobe Firefly headline — trained on licensed content, comes with legal
  indemnification ("the commercially safe one"); ChatGPT Images 2.0 / Nano Banana 2 =
  "already inside your chatbot"; one caveat line: Midjourney (active studio lawsuit) and
  Stable Diffusion ("the open-source option your IT department might run privately") are
  not office tools. [OWNER'S Stable Diffusion suggestion demoted with this rationale —
  flagged to owner, accepted direction.]
- **Apps without code**: Lovable (describe an app, get a working one; Adidas/NVIDIA use
  it; security review before real data).
- **Voice & language**: ElevenLabs (narrated training modules; consent required for voice
  cloning) + DeepL (real-time spoken translation; agent used for report/legal work —
  directly relevant to regulated multilingual documents).
- **Video one-liner**: Veo 3.1 for internal video — and the volatility lesson: OpenAI's
  Sora app shut down Apr 2026; don't build processes on consumer apps.
- FOOTER (find-more, owner-approved shape "a link or prompt… without being overbearing"):
  "Tools change monthly — ask your approved AI assistant: 'Search the web: what are the
  current best tools for [my task], and which are enterprise-safe?'" (Not chip-formatted;
  not one of the 8 prompts.) Backup link in notes only: There's An AI For That, captioned
  "browse by task, verify with IT before use."
- Both slides keep [REFRESH QUARTERLY].

### Slide 19 — The matrix → RETIRE (recommended; owner called it redundant and voted
"eliminate/no one cares" in this neighborhood — see Open Questions #2 for the residual
ambiguity)
- Fold into the gallery slides: the amber policy band ("your organization's AI policy and
  approved-tool list outrank everything here") moves to 18B's footer area; each gallery
  card gets an implicit "start here" job description (already in the card texts).
- Documented alternative if the owner prefers keeping a slide: a decision flow ("What's
  the job? → smallest tool and mode that can succeed"), which would also carry the
  token-economy echo into Part 2.
- If retired: the "touch the token economy again in Part 2" duty is carried by 16's link
  lines and 18B's mode-aware card texts.

### Slide 20 — "Picking tools when rankings churn" → DELETE (owner: eliminate)
- The 60-second write-your-three-tasks exercise dies with it (owner: "enough with the
  prompt guiding questions").
- Salvage exactly one line, into slide 15's notes: "vendor benchmark numbers are marketing
  until independently reproduced."
- This was also Part 2's folded rep — welcome-notes rep sentence must be rewritten
  accordingly (see slide 13 patches).

### Part 2 resulting shape (if matrix retires): divider → assistants → DeepSeek →
servers/trust → gallery 18A → gallery 18B. Seven slides → six.

---

## D. SLIDE-COUNT ARITHMETIC (for docs & QA at update time)

Part 1: 13 − 1 (rep) + 1 (11 split) + 1 (12 expand) = **14**.
Part 2: 7 − 1 (slide 20) − 1 (matrix, if retired) + 1 (gallery split) = **6**.
Parts 3–6 + close: unchanged so far (owner reviewing Part 3 now).
Deck total: 59 → **59** (net zero, if matrix retires; 60 if it stays as decision-flow).
README.md "59 slides" line and PROJECT_STATE absolute numbers (slides 20/22/23–26/55/56,
"S1 = 1–36") must be refreshed at update; the two evidence-map reference slides and
glossary shift by Part-1's +1.

---

## E. FRESH RESEARCH REQUIRED AT UPDATE TIME (blockers for specific lines)

1. Consumer deep-research feature names for OpenAI / Google / Anthropic apps (r5 flags
   "ChatGPT deep research in Aug 2026" UNVERIFIED; Gemini's Deep Research feature and
   claude.ai's Research mode are absent from notes). Needed for 11B's examples; also fixes
   the old matrix cell that overstated them (moot if matrix retires, but notes inherit).
2. Claude Haiku 4.5 pricing ($1/$5 is secondary-sourced) — only if pricing goes on 11A.
3. LMArena creative-writing leader — re-check the live board the week the deck ships.
4. All UNVERIFIED lists in r11–r14 stand as no-go lists.
5. Re-date every "as of Aug 2026" to the rebuild month across dated slides (15, 16, 17,
   18A/B) — [REFRESH QUARTERLY] discipline.

---

## F. PLAIN-LANGUAGE REGISTER (owner rule R3: every example and joke understandable)

Presenter notes must include these spelled-out versions — never assume the room knows the
reference:
- **LEGO bricks (tokens)**: "The AI reads text as chunks, like LEGO bricks. Common words
  are one pre-molded brick; rare words get built from smaller pieces. It has never seen
  inside a brick — that's why it can't reliably count letters."
- **Desk, not filing cabinet (context window)**: "Everything in your chat sits on one
  desk. Close the chat, the desk is swept clean. A filing cabinet — stored memory — is
  what agentic tools add later."
- **Open-book exam with a librarian (RAG)**: "You ask; a librarian fetches the most
  relevant pages from your documents; the AI writes the answer from those pages. If the
  librarian grabs the wrong page, the answer is fluent, cited — and wrong."
- **Skilled temp worker (escalation ladder)**: "Prompting = giving a temp clear
  instructions. Retrieval = handing the temp your binder. Fine-tuning = sending them to a
  training course that changes their habits."
- **Specialist hospital (MoE)**: "The model is built like a huge hospital: hundreds of
  specialist departments exist, but only the few relevant ones wake up for your question.
  You pay for the specialists consulted, not the whole building."
- **Fuel bill vs racing team (DeepSeek $5.6M)**: "The famous $5.6M was the fuel for the
  final winning race — not the cost of building the team, the cars and the practice
  seasons. Real efficiency, oversold headline."
- **Restaurant vs cookbook (China apps vs open weights)**: "Using the app is eating at
  their restaurant — they see your order. Downloading the open weights is taking the
  cookbook home — you cook, nothing is sent anywhere."
- **Improv actor (hallucination)**: "An improv actor never breaks character — the show
  must go on, so gaps get filled with the most plausible line. The AI is the same: it
  would rather invent a confident answer than stop the show."
- **Glue on pizza (the joke, explained)**: "Someone once posted a JOKE on a forum saying
  glue keeps cheese on pizza. Google's AI read that joke as advice and served it as a real
  answer. Funny — and exactly kind 3: confidently wrong from a bad source."
- **"MechaHitler" (Grok caveat — say carefully)**: "A bad settings update once had Grok
  praising Hitler for sixteen hours before an apology. That's the trade-off of a
  deliberately less-filtered assistant."
- **"Unhinged" mode**: "Not a nickname — an actual personality setting in Grok's voice
  app, by that name."
- **Sora shutdown lesson**: "A world-famous video app shut down fourteen months after
  launch. Rule: never build a business process on a consumer app."
- **The specialist-hospital P8, System 1/System 2, brick chips, handoff note**: already
  self-explaining in their prompt texts; presenter reads them verbatim.

---

## G. OPEN QUESTIONS (waiting on the owner — do not resolve unilaterally)

1. **Reps in Parts 3, 5, 6** ("Rebuild one line" · "Write one gate" · "Pick your rung"):
   owner judges each on its slide during the ongoing review. Part 6's is flagged
   PROTECTED in current notes ("the training cashing out").
2. **Matrix (slide 19)**: retire (recommended, assumed) vs rebuild as a decision flow —
   owner's last words were "redundant" + an "eliminate" vote whose numbering was
   ambiguous; confirm at update if not clarified sooner.
3. **Triage drill (P5)**: six problems (current default) or trimmed to four.
4. **Final prompt numbering** n/8 once Part 3–6 review is complete.
5. **Part 3+ intake**: owner reviewing now; comments will append to this ledger.
6. Earlier parked items: same-day vs separate-day blocks; breaks inside or outside the
   80-minute cores; Aug-2026 dating currency pass if the training date moves.

---

## H. EXECUTION CHECKLIST when the owner says "update"

1. Re-run Section E research items 1–3; resolve or drop any line still UNVERIFIED.
2. Edit deck sources only (deck_pt1.js, deck_pt2.js, deck_lib.js for the chip helper +
   brick styling; deck_pt3/4/close for ladder-name qualifiers and rep-pattern notes).
   Add an H.promptChip helper (PROMPT n/8 + robot icon, teal band, Consolas body) used by
   all eight chips identically.
3. Apply Part 1 changes (Section B), Part 2 changes (Section C), note patches (B/slide 13
   list), R4 note re-spacing on every touched slide, R5 duration removal.
4. Rebuild: `node deck_main.js`; visual QA every changed slide via soffice → pdftoppm
   render-check; verify chip consistency and chart honesty rules.
5. Update README.md (slide count, session-shape line) and PROJECT_STATE.md (v1.5 entry;
   refresh stale absolute numbers).
6. Commit with a clear message; push to `claude/training-course-polish-oxohwj` only.
7. Keep this file: mark applied sections ✅ and leave Section G open items visible.
