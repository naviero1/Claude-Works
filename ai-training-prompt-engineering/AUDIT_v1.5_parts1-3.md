# AUDIT — v1.5 deck, slides 1–32 (Parts 1–3) · 2026-09-09

Full factual-integrity + visual audit of everything through the end of Part 3.
**Nothing is applied** — this is the findings ledger; fixes execute on the owner's
"update". Method: every on-slide claim and speaker note cross-checked against
notes/research/ (r1–r16, t1–t6, research-notes.md) and the taxonomy JSON; all 32 slides
visually rendered and inspected; mechanical checks (prompt numbering, concept labels,
relative references, house rules) run on source.

**Headline: 22 findings — 3 HIGH · 6 MED · 13 LOW. Nothing structurally wrong; the HIGHs
are provenance/verification gaps, not wrong teaching. Everything else on the slides
checked out (the SUPPORTED list at the bottom).**

## HIGH

H1. **Slide 12 mode-name rows lack a repo paper trail, and the notes overstate it.**
   The rows WERE verified on 2026-09-09 by a live web check (OpenAI/Google/Anthropic/
   Microsoft/Perplexity help pages — ChatGPT "deep research" still a live paid feature
   with the legacy version removed Mar 2026; Gemini "Deep Research" all tiers (free ~5
   reports/mo) vs "Deep Think" (Ultra); claude.ai "Research" (paid); Copilot "Quick
   response / Think Deeper / Smart (GPT-5)" + Researcher agent, consumer Deep Research
   retired; Perplexity "Search / Research / Create files and apps"; Haiku $1/$5 from
   anthropic.com) — but that verification never landed in notes/research/, so the note
   line "Mode names verified Sep 9, 2026 (notes/research/ + vendor help pages)" is
   half-false and r5's older UNVERIFIED flags still stand un-superseded.
   FIX AT UPDATE: write the verification into a research file (r17_mode_names.md with
   the URLs from the Sep-9 check), correct the provenance line, and note the ChatGPT
   caveat (help-page content came via search index, not a direct page load — re-confirm
   in the live app before the training day).

H2. **Slide 12 "Smart (GPT-5)" row can read as clashing with slide 16's "GPT-5.6
   preferred".** Both are true — "Smart (GPT-5)" is the CONSUMER Copilot mode label
   (Microsoft's page wording); "GPT-5.6 preferred" is the M365 Copilot model policy —
   but the deck never says they're different surfaces.
   FIX: one clause in slide-12 notes ("consumer app labels; M365 Copilot adds
   Auto/Quick/Think deeper with GPT-5.6 preferred").

H3. **Slide 16 Perplexity card leads with "~94% of answers carry inline citations" —
   a secondary-source stat r13 explicitly lists as not anchored.** The anchored claim is
   CJR/Tow: lowest citation-error rate (37% vs 67% for ChatGPT Search).
   FIX: drop ~94%; lead with the CJR result.

## MED

M1. **Slide 20 Sora row: "shut down 14 months after launch" — the duration is
   unsupported and almost certainly wrong** (app launched Sep 2025, shut Apr 2026 ≈ 7
   months; r12 verifies only the shutdown date). FIX: "shut down in April 2026, months
   after launch" — drop the number.
M2. **Slide 13 kind-1 example says "(The Bard telescope flub, next slide)" but Bard is
   NOT on slide 14** (owner locked four incidents; Bard is notes-reserve). FIX: cue it
   as "presenter story" or swap the example to an on-slide incident.
M3. **Slide 7 notes: "pricing (two slides ahead)" points at slide 9 (RAG); the bill is
   slides 11–12.** FIX: "later this part."
M4. **Slide 28: metaprompting "productized by every vendor"** — r3's table has Copilot
   n/a; it's three of four. FIX: "the major vendors."
M5. **Slide 27 technique 1: "stated reasons MEASURABLY improve compliance"** — source is
   vendor guidance, no measurement. FIX: drop "measurably."
M6. **Slide 14 Big Four card compresses two facts too far**: Deloitte repaid PART of the
   fee; EY's 16/27 were "fabricated, misattributed, or dead," not all "fake."
   FIX: "partially refunded" · "16 of 27 references didn't check out."

## LOW

L1. Slide 22 title wraps to two lines (visual) → trim subtitle to "what good looks like"
    form that fits one line.
L2. Slide 18 yellow tier: "370K Grok chats" → "~300K+" (r11 gives a 300–370K range).
L3. Slide 8: "(~30% better answers)" → "up to ~30%" (Anthropic's own phrasing).
L4. Slide 8: "≈1,500 pages" for 1M tokens is derivable but unsourced → footnote
    "≈750K words" or add the derivation to notes.
L5. Slide 16 ACRONYMS: GDPval "across 44 occupations" → repo supports "220 real
    knowledge-work tasks" (44-occupations figure not in r13).
L6. Slide 28 notes: attribute the 75.8→38.1 collapse to GPT-3.5 (reads as GPT-4), and
    phrase Huang as "criteria-free re-review," not literally the words "are you sure?"
    (that phrase's backdown evidence is Sharma, qualitative).
L7. Slides 29/31: "phrased differently… 76 points" → "FORMATTED differently" (Sclar is
    formatting brittleness, not paraphrase).
L8. Slide 19 notes: OpenClaw maintainer quote is lightly paraphrased inside quotation
    marks → use the verbatim sentence or unquote.
L9. Slide 20 Firefly: "trained only on licensed content… ships with indemnification" →
    "licensed/openly-licensed content; PAID plans include indemnification."
L10. Slide 2 notes: "Parts 3, 5 and 6 carry the hands-on moments; the eight PROMPT
    exercises run throughout" — chips actually live on slides 2–17 (Parts 1–2) →
    reword.
L11. Slide 10 BRIDGE: "two concepts left — and they're BOTH about the bill" — Concept 6
    isn't → "the next one is all about the bill."
L12. Slide 12 cost ladder: "100×+" for deep research is an illustration, not a sourced
    multiplier → keep, but mark as order-of-magnitude in notes (5–20× is the sourced
    one).
L13. Slides 19–20: Manus saga and Sora shutdown carry no on-slide dates (dates are in
    notes) — the deck's own rule wants dated claims → add "(Dec 2025 / Apr 2026)"
    parentheticals.

## Passed clean (checked, no findings)

- r14's mandatory incident phrasings honored (Bard $100B caveat, Air Canada small-amount
  framing, Hood threatened-not-filed, Cohen not-sanctioned — all in notes as required).
- r13's don't-print rules honored ("ChatGPT writes better," "Cowork slightly better,"
  SWE-bench Pro numbers, Perplexity MAU — none on slides).
- r15's do-not-slide list honored (GPT-5 hallucination decimal, invented Lu percentages,
  CoVe "50–70%," Weller numbers — all avoided).
- No real company/person names in examples; fictional names only.
- No absolute slide-number cross-references anywhere.
- PROMPT chips 1/8–8/8: exactly once each, in slide order (2, 6, 7, 8, 10, 11, 12, 17),
  each with a TRY IT notes section (debrief + recovery).
- Concepts 1–6 coherent; splits labeled 1-of-2/2-of-2; divider promises match.
- All other bridges and relative references resolve to the right slides.
- All 32 slides visually inspected post-build; layouts clean except L1.
- P6 scheduling puzzle re-proved unique (Ben Mon · Chloe Tue · Ema Wed · Ana Thu ·
  Dev Fri); quotation normalization arithmetic in slide-37 notes re-computed and correct
  (out of audit scope, checked opportunistically).
- ~120 distinct claims verified SUPPORTED against their research files — the full list
  is preserved in the audit transcript; highlights: every Part-1 concept number, the
  R1-vs-o1 chart values and pricing, all nine server/residency rows, the four
  hall-of-shame incidents, all Part-3 element evidence numbers (41.1%, 35→3, <40→100,
  64→71, 80%, 53→23, 95.5→89, 0.17→0.32, +8%/+50%, up-to-40% wrapper, ~49% sycophancy,
  76-point Sclar), the LEI "Prompt, Do, Check, Act" citation, and the taxonomy counts
  (19/78/286/18 — recounted from the JSON).

## Scope notes for the NEXT audit (Parts 4–6, when the owner reviews them)

- Verify the practice-dataset answer key computationally (Bravo defect trend, negative
  inspection-vs-returns correlation, Osaka on-time lead, TOTAL-row reconciliation).
- Part-4 pointer notes still carry the old session-split language (frozen by owner
  mid-review).
- Slide 34's GPT-4 ~59% multiplication figure already spot-checked SUPPORTED.
