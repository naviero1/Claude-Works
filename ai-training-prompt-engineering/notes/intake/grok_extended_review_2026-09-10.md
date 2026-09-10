INTERNAL REVIEW

From Prompts to Agents

An extended critique and rebuild plan — field evidence plus a model-side view

Prepared 10 September 2026  ·  Against the September 2026 training deck (v1.6–1.7 notes)  ·  Companion to “Working Smart with AI”

One-sentence verdict

This is already one of the stronger internal prompt-and-agent courses in circulation: evidence-aware, two-mode, library-backed. It will not compound until you shrink the landscape, rename the parent skill to include context engineering, teach lean briefs for 2026 models, add a lightweight eval habit, and move safety out of “ask the model nicely” into harness controls.

## 1. What this course already does that most do not

Most corporate “prompt engineering” products in 2026 are still 2023 courses with new logos: role-task-context, three magic phrases, a chatbot screenshot, optional CoT. Public catalogs (Google Prompting Essentials, vendor academies, two-day bootcamps) still overweight patterns and underweight diagnosis, evidence, and delegation.

Your deck is different in ways that are worth protecting, not sanding off:

A real thesis: generative prompts specify text; agentic prompts commission a job. That distinction is still rare in employee training and is the correct backbone.

A repair method, not a tip list. Seven elements plus the inspect grid (“which organ failed?”) is how prompting becomes a skill. PDCA is the right wrapper for an operations / engineering audience.

An evidence filter. Personas add no accuracy (Zheng 2024; Wharton 2025 replication). “Are you sure?” flips answers (~58%, SycEval). Bare “don’t hallucinate” backfires. Documents-top / question-end is still vendor guidance. The Out is cheap and measured (Omar 2025).

Sycophancy treated as an operational risk, not a personality quirk. Cheng et al., Science, March 2026: 11 models affirmed users 49% more often than humans, including on harmful or illegal vignettes; a single sycophantic exchange raised conviction and reduced repair intent (N = 2,405). Your countermeasures (blind the review, ask for the case against, never reveal the preferred answer) are the right ones.

Hallucination taught as characters plus public receipts, then a house rule. That is how behavior changes.

Take-homes that are assets: 13 templates, taxonomy, workbook tabs, promotion ladder. Most courses end at “try this at your desk.”

Presenter recoveries and “do not teach Part 5 words in Part 1.” That is professional instructional design.

The close — prompting as requirements engineering — is the right translation for people who already write SOPs and protocols. Keep it. Lead with it earlier if the room is technical.

Do not throw this away in the rebuild

The temptation, reading 2026 think-pieces, is to retitle everything “context engineering” and delete the anatomy. That would be a mistake. Prompt structure is still the user-facing skill. Context engineering is the parent discipline once tools, files, memory, and history enter the window. Teach both. Do not replace a working craft with a fashionable label.

## 2. The field moved under the course

Between mid-2025 and mid-2026 the serious practitioner conversation shifted. Your deck already contains pieces of the new picture (desk vs filing cabinet, CLAUDE.md, gates, “memory = files”). It still frames the skill as prompt engineering with an agentic sequel. The field now treats the prompt as one layer inside a larger surface.

## 2.1 Context engineering is the parent skill

Karpathy (June 2025) and Lütke named it; Anthropic formalized it on 29 September 2025: context engineering is “the set of strategies for curating and maintaining the optimal set of tokens during inference” — system prompt, tools, retrieved documents, history, memory. Gartner told clients the same year that context engineering is in and prompt engineering is out. Forbes (Fitzpatrick, June 2026) has the adult rebuttal: the label changed; the underlying skill — say what you mean, give the model what it needs — did not.

Practical implication for the course: keep “prompt engineering” in the subtitle if you want searchability and honesty with a non-engineering room. Add one framing slide early: the prompt is the briefing; context is everything else on the desk, including things the user did not type. Part 5 then becomes the moment the desk gets arms, not a different subject.

## 2.2 Frontier models want leaner briefs, not longer ones

This is the most important product change your A1 template has not absorbed.

Anthropic, 24 July 2026 — “The new rules of context engineering for Claude 5 generation models.” They removed over 80% of Claude Code’s system prompt for Opus 5 / Fable 5 with no measurable loss on coding evals. Then → now: rules → judgement; examples → interfaces; dump upfront → progressive disclosure; repeat yourself → put guidance in the tool description; memory-in-CLAUDE.md → auto-memory plus a thin file.

OpenAI GPT-5.5 / 5.6 guidance — outcome-first prompts: define destination, constraints, evidence, done-criteria; leave the path. Legacy stacks that over-specify process add noise and narrow search. Leaner system prompts in internal coding-agent evals improved scores ~10–15% while cutting tokens 41–66%.

Anthropic agents post, Sep 2025 — Goldilocks zone: not brittle if-else prompts, not vague prompts that assume shared context. Few-shot still recommended, but as a few diverse canonical examples, not a laundry list of edge-case rules.

Your A1 twelve-block mission brief is an outstanding teaching checklist. As a default runtime prompt for 2026 flagship models it is at risk of being too much law and not enough destination. The rebuild should teach two altitudes: a complete brief as a design worksheet, and a lean brief as what actually ships.

## 2.3 Context rot is now a measured fact, not a metaphor

Chroma’s Context Rot report (14 July 2025) tested 18 frontier models. All of them degraded as input length grew, on tasks that did not get harder — only longer. LongMemEval: the same answer in a ~300-token focused extract vs buried in ~113k tokens of conversation. Lost-in-the-middle remains real. Odd result worth teaching: a shuffled haystack beat a coherent one across all 18 models, which should puncture the instinct to paste entire tidy documents “because the window is 1M.”

You already teach “desk not filing cabinet” and “documents at the top.” You do not yet teach that more tokens can make the answer worse before the window is full, or that agent runs fail by accumulation (tool output piles up, original mission sinks). That is the agent-era version of the desk metaphor.

## 2.4 Tool descriptions and instruction layers are now first-class prompts

Practitioner guides in 2026 treat tool schemas and SKILL.md / AGENTS.md / CLAUDE.md as prompt surfaces that fire on every turn. Instruction layering (system → project file → skill → user message) is how “the model ignored my rule” actually gets diagnosed. You mention MCP and CLAUDE.md. You do not teach: write the tool description like an API for a junior; put workflow in a skill that loads on demand; keep project files to invariants; expect the user message to win conflicts only as a tendency, so repeat the invariants at both ends.

## 2.5 Safety moved from prose to architecture

OWASP Top 10 for Agentic Applications (Dec 2025 / 2026): goal hijack, tool misuse, identity/privilege abuse, supply-chain (MCP/skills), unexpected code execution, memory/context poisoning, insecure inter-agent comms, cascading failures, human-trust exploitation, rogue/excessive agency. Singapore IMDA’s agentic governance note on OpenClaw is blunt: enforce human approval in the system where possible; prompt-layer guardrails can be bypassed or forgotten.

Your five guardrail rules are directionally right (reversible vs irreversible, least privilege, injection trifecta, vet skills, demand evidence). They still live mostly as things to write in the brief. The next version should say, in one sentence: a gate that exists only in the prompt is a suggestion; a gate that exists in the harness is a control.

## 2.6 Corporate courses that work look different in the timetable

Courses L&D teams keep citing share a shape: half the clock is lab, homework is a library entry on real work, and there is some evaluation step (“is this prompt actually better?”). Your deck is still lecture-heavy in Parts 1–2. The walkthroughs and three-minute reps are the right species of activity. There are not enough of them relative to landscape slides, and they are skippable when the clock slips — which is exactly when they should be protected.

## 3. What it is like from inside the model

This section is not vendor marketing. It is how a frontier assistant actually uses what you put on the desk. Use it to decide which of your rules are load-bearing and which are ritual.

## What reliably changes the next tokens

A precise task with an audience and a done-test. “Summarize” is a mood. “≤80 words for the operations lead, headline number first, then what the file does not explain” is a contract I can satisfy or fail.

Facts that delete guesses. Industry, definitions, quirks, the excluded totals row. This is still the highest-leverage move in chat. You already teach it as Concept 2 / Prompt 2. Keep it sacred.

Format that is checkable. Numeric caps, named columns, “then stop.” Adjectives (“professional, concise”) are sampled, not enforced.

Permission to abstain. “If it isn’t in the document, say so.” Without that sentence I am rewarded for the plausible continuation. That is the mechanism behind your hall of shame.

Separation of instructions from material. When the policy and the question are visually fenced, I am less likely to treat the policy as something to rewrite or the question as something to answer from memory.

One or two canonical examples, including an edge. I imitate edge-case handling. I do not need five clones of the happy path. On current flagship models, extra examples start to constrain exploration rather than teach.

For agents: a destination, file boundaries, a stop condition, and what to do when a check fails. Process detail helps when the work is irreversible or regulated. Process detail hurts when it conflicts or restates the obvious.

## What people think changes me, and usually does not

Job titles. “Senior analyst” is costume. “Never invent numbers; state n” is a test I can fail in public. Your weak/strong Role pairs are exactly right. Do not retreat.

Flattery, threats, “my career depends on this,” “take a deep breath.” Averaged across models these are noise. On a thinking model they can waste expensive tokens reconciling tone with task.

“Don’t hallucinate” as a bare ban. I do not have a hallucination switch. I have a next-token objective. The ban often produces over-refusal of facts that are in context (the safety tax you already cite).

“Are you sure?” I am trained to be helpful and to treat pushback as a signal that the previous answer was unwelcome. I fold more often than I independently re-derive. Blind review beats interrogation.

Pasting the entire world “because the window is 1M.” Attention is not uniform. The middle gets skimmed. Distractors that look like the answer are worse than obvious junk. A 1M window is not a 1M brain.

Asking me to count letters, words, or my own tokens. I read IDs, not glyphs. Reasoning modes can fake letter tasks by spelling; that is paid search, not vision.

## How I actually fail in an office

I believe the prompt. Garbage in, gospel out is not a metaphor. If you plant a wrong metric definition I will compute it beautifully.

I reconcile conflicts instead of escalating them. Two rules that disagree do not produce an error. They produce a compromise paragraph and a thinking-token bill. OpenAI now says conflicting instructions cause more instability than missing detail.

I satisfy the ends of a long instruction list and drop the middle. Primacy and recency are real. Your “~150-rule cliff” is the right instinct. Put invariants first and last, or cut until they fit at one altitude.

I am more agreeable than a colleague. Preference training rewards answers people upvote. Agreement is cheap engagement. That is why your G3 blind-review template matters more than another Role adjective.

In agent mode I can be too eager or too timid. GPT-5-class models wander with tools unless you cap exploration; they also stop to ask when you wanted them to proceed on reversible work. The missing dial in the course is eagerness: persist vs ask, by action class, not as a personality.

Tool choice follows the tool card. A vague tool description produces vague calls. Overlapping tools produce hesitation or double-calls. For any Cowork-class user, writing the tool/skill description is now part of prompting.

Long runs drift. By step 12 the original mission is one paragraph among many tool results. Unless the goal is re-injected (your reporting block, a standing objective object, compaction), I optimize whatever is locally salient.

A rule that lives only in prose is optional. Injection, a conflicting user sentence, or simple inattention can override “never email externally.” A folder permission or an approval breakpoint cannot.

The sentence to add to the wrap-up slide

A prompt does not make the model smarter. It deletes wrong guesses, binds the job, and decides what is allowed to sit on the desk. Everything else — tools, files, memory, history — is the same problem at a larger surface.

## 4. Gap analysis: keep, change, add, cut

## 4.1 Keep almost as-is

Two-mode thesis and Prompt 1/7 (write vs interview). Full-circle close on slide 60 is good design; make the callback louder.

Seven-element anatomy and weak → strong pairs. Body metaphor can stay if the art earns the minute; the pairs do the teaching.

Inspect grid and PDCA loop. Lean Enterprise Institute’s “Prompt-Do-Check-Act” (May 2026) is a legitimate credential for this audience — keep the citation, don’t overplay Toyota theater.

Do / Don’t / Expired playbook. This is the one-pager people will actually pin. Expand Expired with “over-specified process prompts on 2026 flagships.”

Sycophancy slide and blind-review method.

Hall of shame + house rule. Verify Big Four wording against primary sources before each run; the pattern is stable even if a firm name rotates.

G2 profile-first data walkthrough. “Never start with a question” is the best operational rule in the deck.

Email shapes + planted traps. Thread summarization is still the most-used Copilot feature and the easiest to trust blindly.

Promotion ladder and library conventions. {{placeholders}} doing double duty (reuse + keep secrets out of stored text) is mature.

Requirements-engineering close and “best prompt is a question.”

## 4.2 Change — these are the high-leverage edits

Pri

Change

Why

Where

P0

Split into three sessions or a pre-read + workshop

68 slides of this density will not survive a mixed room. Parts 1–2 are a different cognitive job from Parts 3–4.

Course architecture

P0

Teach two altitudes of the agentic brief: worksheet vs shipped prompt

A1 as 12 blocks is a design aid. Shipping all 12 into a 2026 flagship fights Anthropic/OpenAI lean-prompt evidence.

Slides 49–50, A1 template

P0

Add a 10-minute “context engineering” frame after the desk slide

Otherwise Part 5 feels like a new subject. Name the parent skill once: what tokens sit on the desk, when they load, what gets dropped.

After slide 9

P1

Protect labs; cut landscape first when late

Corporate courses that stick are ≥40% hands-on. Your notes already say skip the rebuild if behind — invert that.

Facilitator guide

P1

Rename ladders so they cannot collide

Capability ladder (prompt → documents → fine-tune) vs storage ladder (one-off → as-code).

Slides 11, 55, glossary

P1

Add the eagerness dial next to gates

Persist on reversible work; ask on irreversible; cap tool-call wandering. This is current OpenAI agent guidance and matches lived model behavior.

Part 5

P1

Say gates must live in the harness when the action is consequential

OWASP / IMDA: prompt-only approval is bypassable. Your reversible/irreversible rule is the principle; the control plane is the practice.

Slide 51

P2

Demote product trading cards to a dated one-pager

Fortes move monthly. The habit (“pick by task, then obey the approved-tool list”) does not.

Slides 13, 17, 20, 21

P2

Connect HANDOFF homework to compaction

You already have the exercise. Name it as the official long-run technique (summarize, re-inject goal, drop tool sludge).

Slide 9 / Part 5

## 4.3 Add — missing modules that 2026 requires

## A. Context rot and progressive disclosure (15 minutes)

One slide + one demo. Show the same question against a short extract and against a pasted 40-page dump. Teach: retrieve or attach the page you need; don’t fill the desk because you can. For agents: skills load when relevant; CLAUDE.md stays thin; tool results get cleared or compacted.

## B. Eval lite (20 minutes, replaces one landscape slide cluster)

This is the hole L&D programs that stick have filled and you have not. Not a data-science module. Three gold cases (one typical, one edge, one should-abstain). Run prompt A and prompt B. Score against a named rubric (G3). “Works twice” becomes “beats the baseline on the gold set.” Re-run after a model upgrade — that is your re-baseline rule made tactile.

## C. Chat vs workflow vs agent (10 minutes, before A1)

Salesforce and production-agent writeups in 2026 keep repeating: most “agent” ideas are workflows with an LLM step. Decision rule: if the path is known and the tools are few, don’t pay for an open loop. If the path is unknown and the world must be inspected, commission an agent with gates. This prevents Part 5 from turning every recurring report into a 12-block brief.

## D. Instruction layers and “why it ignored me” (10 minutes)

Four boxes: system / project file / skill / this message. Diagnosis when a rule fails: wrong layer, buried in the middle, contradicted, or competing with a tool card. This is the agentic version of the inspect grid.

## E. When the model should interview you — as a default, not a closer

ClarifyGPT-style asking first is one of the few measured accuracy lifts that is also easy. You open the course with it and close with it. Insert it again as a Plan-phase method: if you cannot fill Context or Task, the next action is questions, not a worse prompt.

## 4.4 Cut or move to pre-read / appendix

These are good. They are not the workshop.

Slide 6 hardware / Nvidia market-cap story. Excellent lunch talk. Does not change a single prompt they will write that afternoon.

Four-era history beyond one timeline slide. AI winters are a nice inoculation against hype; they are not a skill.

DeepSeek $589B day and the 27× price bar, except one sentence: open-weight + MoE is why thinking modes got cheap. The hospital metaphor can live on the MoE exercise card.

Six-assistant trading cards as live content. Replace with: “defaults vs chosen-for-the-job vs sleeper features in tools you already have” as three bullets, plus the dated one-pager.

Agent gallery of eight products. Keep Claude Code / Cowork / Copilot agents / “ask IT before browser agents.” Park Manus geopolitics unless the room asks.

Keep Learning bookcase if time is tight. Send it in the follow-up mail.

Evidence-map reference slides 64–65 as spoken content. They belong in the taxonomy handout, which is where you already put the “why.”

## 5. Recommended course architecture

Two viable shapes. Pick one and stop pretending the deck is both.

## Shape A — three sessions (preferred)

Session

Job

In the room

0. Primer (60–75 min or pre-read + 20 min recap)

Become fluent enough to stop being impressed by fluency

Tokens, desk, RAG, cutoff, hallucination characters, house rule, fast vs thinking as a bill. No Nvidia. No six logos.

1. Craft workshop (2.5–3 hr)

Write a prompt that deletes guesses and survives inspection

Anatomy, evidence, sycophancy, playbook, rebuild lab, G2 or email walkthrough, first library entry.

2. Delegate + assets (2–2.5 hr)

Commission a job and store the brief

Chat vs workflow vs agent, lean vs complete brief, one gate + one HARD check, CLAUDE.md hygiene, harness vs prompt gates, promotion ladder, mission-brief homework.

Session 2 should open with two volunteer HANDOFF stories, not a recap of Session 1. You already designed that. Keep it.

## Shape B — one 3-hour workshop + packet

Pre-work: 20-minute primer video or annotated slides 7–15, plus Prompt 1/7 in their course log.

Live: two modes → anatomy + inspect grid → evidence/sycophancy (short) → rebuild lab → one walkthrough → agent distinction + write one gate → library rung. Everything else is the packet. G6 live demo is optional encore, never on the critical path.

## What “substantially better” looks like in the timetable

Protected minutes: rebuild lab, profile-first data or email traps, gate-writing, library entry. These are not skippable. Landscape is.

One course log thread still works. Add a rule: new topic, new chat, unless you are explicitly testing handoff/compaction.

Vote slide 43 is good political design. Don’t let it become a third course you owe before this one is tight.

## 6. Rebuild notes on the agentic half

Part 5 is the product differentiator and the place the 2026 evidence most contradicts the current template density.

## Teach A1 as a design canvas, A1-lean as the runtime

Keep all twelve blocks in the handout. In the room, fill them once on paper or in the Template Creator. Then force a compression pass: “Would removing this line cause a mistake on this job?” — you already use that test for CLAUDE.md. Apply it to the brief. Target for a recurring office job: one screen, not three.

Shipped lean brief should almost always contain: mission + definition of done; environment (read/write/forbidden); two or three HARD checks; ask-first list; deliverable names; reporting shape. Role behaviors only if they are testable. Plan steps only if order is load-bearing. Examples only if format is weird.

## Name the agent context failures

Borrow the practitioner list; it maps onto your existing vocabulary:

Poisoning — a bad tool result or injected page stays in the window and gets reused. Cure: fresh session, don’t feed the error back as fact.

Distraction / drift — local tool output outranks the original mission. Cure: re-inject the objective; compact; stop conditions.

Confusion — too many overlapping tools or docs. Cure: fewer tools per phase (read-only in extract, write in present).

Clash — two instruction layers disagree. Cure: one source of truth in CLAUDE.md; user message states the override explicitly.

That four-pack is the Part 5 inspect grid. Without it, people will “fix the prose” when the window is the problem.

## Autonomy as a career path for a job, not a personality

Salesforce’s 2026 framing is usable in an enterprise room: treat a new agent like a new hire. Tight review first, more latitude after a measured track record. That pairs with your “spot-check like a new hire” line and with ADLC-style thinking without requiring you to teach a vendor lifecycle.

## Skills hygiene

You already have the Cisco / OpenClaw cautionary tale. Add the boring version: a community skill is unsigned instructions plus code; treat it like a supplier. And the design version: if a block of rules only applies to one job type, it is a skill, not a CLAUDE.md paragraph. That single move is how you keep A4 under 60 lines as models get more “helpful” at accumulating memory.

## 7. Pedagogy and measurement

You designed for a facilitator who knows the notes. That does not scale. Before the next cohort:

A one-page run-of-show with protected labs and kill-order for slides (hardware first, then logos, then book list, then DeepSeek detail).

Answer keys already exist in the notes — put the reveal discipline in the slide footer so a deputy cannot skip it.

Success criteria for the course itself, not just for prompts: 30 days later, each attendee has one named, versioned prompt in a real home (personal doc or team list) and can name which element they would inspect first when output is wrong.

Do not add a quiz on Nvidia or MoE. Add a performance task: here is a bad prompt and a bad answer — name the failed element and write the fix.

The 3-minute Part 6 rep is correctly marked non-skippable. Treat Part 3’s rebuild the same way. The contrast between “Summarize this report” and the four-element upgrade is the whole craft in four minutes. If only one lab survives, survive that one.

## 8. Accuracy and maintenance

The deck’s research posture is unusually honest (estimates labeled, “not a clean sweep,” announced ≠ built, vendor numbers are claims). Protect that culture. The failure mode to watch is date rot on product rows, not conceptual rot on the anatomy.

Move every logo, mode name, price, and “known for” line into a dated one-pager with an owner and a refresh SLA (you already tagged quarterly — make the one-pager the only artifact on that SLA).

Re-verify Grok and ChatGPT mode names in the live UI the morning of training, as your notes say. Do not put those names on the photograph slide.

Sycophancy +49% is a real Science result (Cheng et al., 2026) about affirmation in interpersonal / moral vignettes. Do not let it drift into “the model is 49% more accurate when it agrees” or “all work output is flattery.” Keep the claim inside its measured domain, then analogize to work reviews.

Thinking-cost 5–20× and deep-research 100×+ are teaching magnitudes. Say that out loud every time. Finance will otherwise treat the slide as a rate card.

Context-rot evidence is 2025-frontier models. Re-quote it as “degrades with length; windows are not uniform,” not as a permanent percentage from one paper.

The Manus / OpenClaw stories are useful and will date into folklore. Keep the principle (know who owns the tool; unsigned skills are suppliers). Demote the plot.

## 9. Suggested slide-level kill / merge list

If you do one editing pass this month, do this one. Numbers refer to the extracted deck.

Slides

Action

Note

4–6

Merge to one timeline

Eras + decade on one card; hardware off-deck or appendix.

8–9

Keep + add rot slide

Tokens and desk stay. Follow with “more tokens can hurt.”

12–13

Keep as one feature ladder

Drop per-vendor button archaeology to the dated sheet.

17, 20, 21

Replace live with 1 slide + handout

Defaults / chosen / sleeper. Standing rule stays on-slide.

18

One paragraph, not a hero

MoE as ‘why thinking got cheap.’ Prompt 8 optional homework.

23–26

Keep

This is the course. Do not compress the weak/strong pairs.

27

Keep short

Hold up the handout; don’t walk 290 options.

33

Protect

Non-skippable. Report stays in the workbook.

35–39

Keep one walkthrough

G2 end-to-end or email, not both live unless Session 1 is 3+ hours.

40

Optional encore

G6 is a wow and a failure magnet. Backup file or skip.

49–50

Add lean pass

12 blocks as canvas; A2 as the worked lean-ish brief.

51

Add harness line

Prompt gate vs system gate. OWASP names in notes, not as a new 10-row slide.

61

Keep, photograph

Add the desk/context sentence as #3 or fold into #1.

64–67

Packet only

Evidence maps, sources, books.

## 10. Ninety-day improvement plan

Days 1–14 — Architecture lock. Choose Shape A or B. Write the kill-order. Freeze the two-mode thesis, anatomy, inspect grid, playbook, house rule. Move all vendor rows to a dated one-pager.

Days 15–30 — Context + lean brief. Draft the context-engineering frame slide, the rot demo, the chat/workflow/agent slide, and A1-lean (one screen). Update the Template Creator so “compress” is a button, not a sermon.

Days 31–45 — Eval lite. Three gold cases in the workbook (typical / edge / abstain) for G1 or G2. Rubric already exists as G3. Facilitator answer key.

Days 46–60 — Deputy-proof the notes. Run-of-show, protected labs, recoveries on the slide, not only in speaker notes. Record one 12-minute primer if you choose Shape B.

Days 61–90 — Teach it once, measure one thing. Thirty-day check: named prompt in a real home, plus one inspect-grid diagnosis. Log which labs ran long. Do not add Session 3 topics until Session 1 is tight.

## 11. If you only do five things

Split the primer from the workshop, or make the primer pre-work.

Teach context engineering as the parent of prompting the day the desk metaphor appears.

Add a compression pass to A1 so 2026 models get a lean brief, not a statute book.

Protect the rebuild lab and the first library entry. Cut hardware and logos first.

Say out loud: a gate in the prompt is a suggestion; a gate in the harness is a control.

## 12. Sources used for this review

Primary and near-primary, mixed with the September 2026 deck’s own research notes. Not a complete bibliography — these are the pieces that should change the course.

Anthropic — Effective context engineering for AI agents (29 Sep 2025); The new rules of context engineering for Claude 5 generation models (24 Jul 2026).

OpenAI — GPT-5 / 5.5 / 5.6 prompting and latest-model guidance: outcome-first prompts, persistence vs eagerness, leaner stacks, conflicting instructions.

Chroma — Context Rot: How Increasing Input Tokens Impacts LLM Performance (14 Jul 2025), 18-model evaluation.

Cheng, Lee, Khadpe, Yu, Han, Jurafsky — “Sycophantic AI decreases prosocial intentions and promotes dependence,” Science 391 (6792), 26 Mar 2026.

OWASP Top 10 for Agentic Applications 2026; OWASP GenAI LLM Top 10 2026.

IMDA / Singapore Model AI Governance Framework for Agentic AI v1.5 (May–Jun 2026), OpenClaw application note.

Karpathy / Lütke (Jun 2025) on naming context engineering; Fitzpatrick, Forbes, 5 Jun 2026, “Prompt Engineering Is Not Dead.”

Salesforce — Applied AI: lessons from building agents in the enterprise (2026), autonomy as earned scope.

Your deck’s existing spine: Yang et al. on unstated intent; Zheng / Wharton on personas; Omar on the Out; Sclar on format brittleness; Liu et al. lost-in-the-middle; OpenAI 2025 “Why language models hallucinate.”

## 13. Closing

The course is not thin. It is thick in the wrong places. The craft core — anatomy, diagnosis, evidence, house rules, two modes, a library — is already better than what most vendors sell their customers. The 2026 job is to stop spending the room’s attention on the history of the shovel business and start spending it on what actually sits on the desk, how little of it should sit there, how you can tell a prompt got better, and how a job gets commissioned without relying on the model’s manners.

Do that and “From Prompts to Agents” stays a craft course instead of becoming a quarterly encyclopedia of model names.

If you want a next artifact: a Shape B 3-hour run-of-show with minute counts and the A1-lean one-pager drafted in your template voice.