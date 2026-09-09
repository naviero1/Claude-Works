# r21 — Requirements ↔ prompts, and the craft of asking questions (researched 2026-09-09)

Powers the two v1.6 closing slides (owner: "emphasize how important for prompt
engineering it is to know how to write requirements, and how these compare in
structure to prompts… The importance of asking good questions as well.").

## Topic 1 — Requirements writing IS the sister skill

### The thesis, from mainstream sources (verbatim, verified)
- Andrew Stellman, "Prompt Engineering Is Requirements Engineering," O'Reilly
  Radar, Sep 17, 2025: "Prompt engineering and requirements engineering are
  literally the same skill—using clarity, context, and intentionality to
  communicate your intent." And: "AI raises the stakes on this core
  communication problem. Unlike your teammates, the AI won't push back or ask
  questions—it just generates something that looks plausible."
- Sean Grove (OpenAI), "The New Code," AI Engineer World's Fair, June 2025
  (verified against full transcript): "in the near future, the person who
  communicates most effectively is the most valuable programmer." · "Code is
  sort of 10% to 20% of the value that you bring. The other 80% to 90% is in
  structured communication." · on vibe coding: "we keep the generated code and
  we delete the prompt… a little bit like you shred the source and then you
  very carefully version control the binary." · "whoever writes the spec, be
  it a PM, a lawmaker, an engineer, a marketer, is now the programmer."
- GitHub Spec Kit (open-sourced Sep 2, 2025; GitHub Blog, Den Delimarsky): the
  spec "is a contract for how your code should behave and becomes the source
  of truth"; "a vague prompt like 'add photo sharing to my app' forces the
  model to guess at potentially thousands of unstated requirements." Works
  with 30+ agents incl. Copilot and Claude Code.
- Academic corroboration the field is real: "Requirements are All You Need"
  (arXiv:2406.10101, Jun 2024); "Prompts Are Programs Too!" (ACM FSE 2025,
  arXiv:2409.12447); Queen's University Belfast runs a PhD topic on the
  requirements↔prompting relationship (2025/26 listing).
- Practitioner line: "The same skills that make for great requirements —
  clarity, structure, and intent — make for great prompts." (Maria Santos,
  ModernAnalyst.com, Oct 26, 2025.)

### The five structural parallels (all verified to origin)
| Requirements form (origin) | Maps to our anatomy |
|---|---|
| User story: "As a [role], I want [goal], so that [benefit]" — Connextra/Rachel Davies, 2001 | ROLE + TASK (the *so that* = the Task's purpose clause) |
| Given-When-Then acceptance criteria — Dan North, BDD, mid-2000s | Given=CONTEXT · When=TASK · Then=FORMAT + verifiable checks (the Stop) |
| INVEST — Bill Wake, xp123.com, Aug 17 2003: Independent Negotiable Valuable Estimable **Small Testable** | Small → one task per prompt (the Stop); Testable → checkable Format contract; Negotiable → PDCA iteration |
| ISO/IEC/IEEE 29148:2018 — nine characteristics: necessary, appropriate, **unambiguous, complete, singular, feasible, verifiable**, correct, conforming | Unambiguous→Task (41.1%!); Complete→Context; Singular→the Stop; Verifiable→Format+self-check |
| Formal clarification step — ClarifyGPT (FSE 2024) | → Topic 2: elicitation = the question move |

### Evidence that requirement-style prompting wins
- ClarifyGPT (Mu et al., ACM FSE 2024, arXiv:2310.10996): a
  requirements-clarification loop lifts GPT-4 average Pass@1 across five
  benchmarks 62.43% → 69.60% (ChatGPT 54.32 → 62.37); with real human answers
  +13.87 pts on MBPP-sanitized (70.96 → 80.80).
- Already in the deck: Yang 2025 (41.1% unstated-requirement guesses; +4.8%
  requirements-aware optimization, arXiv:2505.13360); explicit I/O specs
  drive detailed-prompt gains (arXiv:2508.03678).
- NO direct study found showing requirements-TRAINED PEOPLE prompt better —
  frame as "the transfer is structural, and clarified-requirement prompts
  measurably win," never as a people study.

## Topic 2 — Asking good questions

- The flip (make the AI ask YOU): the community "ask me clarifying questions
  until you're 95% confident" meta-prompt now has an academic counterpart —
  ClarifyGPT's entire gain comes from asking before answering. CLAM
  (arXiv:2212.07769, Dec 2022): ambiguity-detect + clarify "significantly
  improves" accuracy (no headline number in abstract — cite qualitatively).
- Logic chain for the slide: AI guesses unstated requirements right 41.1% of
  the time → letting it ask instead recovers ~7–14 points (ClarifyGPT) → so
  "answer its questions" is quality control, not politeness.
- Five Whys — Taiichi Ohno, Toyota Production System (1988 Engl. ed.): "by
  repeating why five times, the nature of the problem as well as its solution
  becomes clear." Same factory, same habit as the PDCA slide.
- Socratic questioning, six types (Richard Paul taxonomy; U-Michigan
  summary): clarification · probe assumptions · probe evidence · other
  viewpoints · implications · question the question.
- HBR, "The Art of Asking Smarter Questions" (Chevallier, Dalsace & Barsoux,
  May–Jun 2024): investigative (what's known?) · speculative (what if?) ·
  productive (now what?) · interpretive (so what?) · subjective (what's
  unsaid?).
- Open→closed funnel: open to explore, closed to verify (common knowledge, no
  citation needed).

### Quotable authority — attribution checked
- VERIFIED — Sam Altman: "Figuring out what questions to ask will be more
  important than figuring out the answer." — ReThinking with Adam Grant, Jan
  2025; CNBC Jan 13 2025 covered it as "the No. 1 ability you need to succeed"
  in the AI age.
- VERIFIED w/ wording caveat — Picasso, 1964 (Fifield interview, The Paris
  Review 32): "But they are useless. They can only give you answers." (The
  "Computers are useless…" wording is a 1980s smoothing — quote the 1964 form
  or flag "as popularly rendered"; quoteinvestigator.com/2011/11/05.)

## Bridge sentence (for notes)
"The seven elements — Role, Task, Context, Format, Examples, the Out, the
Stop — are a requirements document in miniature: fill them in and you've
written a spec; notice which one you CAN'T fill in yet, and you've found the
exact question to ask — or to let the AI ask you."

## UNVERIFIED / DO NOT USE (R7)
- Einstein "55 minutes defining the problem" — APOCRYPHAL (QI: 1966 unnamed
  Yale professor; attached to Einstein 1973). Never with Einstein's name.
- Voltaire "judge a man by his questions" — MISATTRIBUTED; actual origin
  Pierre-Marc-Gaston de Lévis, Maximes et réflexions, 1808. Only with de
  Lévis credit.
- "200 business analysts / 34% more requirements" (eltegra.ai) — vendor
  marketing, no traceable study. Do not use.
- "The best coder will soon be the best communicator" — paraphrase; use
  Grove's verbatim line instead.
- CLAM's effect size (no number in abstract) · Grove exact calendar date
  ("2025" is safe) · the 95%-meta-prompt upvote count (see r16).

Key sources: oreilly.com/radar/prompt-engineering-is-requirements-engineering ·
youtube.com/watch?v=8rABwKRsec4 (+ transcript lawwu.github.io) · github.blog
spec-driven-development post + github.com/github/spec-kit ·
modernrequirements.com/blogs/iso-29148-explained · xp123.com INVEST ·
agilealliance.org user-story template · cucumber.io/docs/bdd/history ·
dl.acm.org/doi/10.1145/3660810 (ClarifyGPT) · arXiv 2212.07769 · 2406.10101 ·
2409.12447 · cnbc.com/2025/01/13 (Altman) · quoteinvestigator.com (Picasso,
Einstein) · hbr.org/2024/05/the-art-of-asking-smarter-questions ·
en.wikipedia.org/wiki/Five_whys.
