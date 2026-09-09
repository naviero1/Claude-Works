# r19 — Comparison-slide & big-number design patterns (researched 2026-09-09)

Owner request (round-3 audit): make S16 catch the eye per assistant; make S17's bill
stand out. Findings below; final specs adopted in PENDING_CHANGES.md Round 3.

## The load-bearing principles (sources)

- **Assertion-evidence** (Alley, Penn State; peer-reviewed ASEE 2011): one short
  assertion dominates (~28pt, 8–14 words); evidence sits smaller and visual, not
  bulleted. Tested better comprehension/recall than topic+bullets.
- **Duarte 3-second / Glance Test** (duarte.com; HBR Oct 2012): a slide (or card) must
  land its message in ~3 seconds — one focal point, size/color contrast, whitespace.
- **Knaflic single-accent rule** (Storytelling with Data): exactly ONE preattentive
  attribute for the hero element; gray down everything else.
- **F/Z scanning** (NNGroup eye-tracking; O'Reilly UX): sparse grids scan in a Z — put
  the most familiar item top-left; rows scan in an F — left edge and first words win.
- **Signal-to-noise** (Presentation Zen / Garr Reynolds): delete every element that
  doesn't carry the message (tiny vendor rows, borders, repeated labels).
- **Big numbers**: one number per slide, oversized, few words (Storydoc/Beautiful.ai);
  pair numerals with LENGTH-encoded bars so magnitude is felt, not just read; the
  multiplier as a badge/callout (Domo/Tabular Editor KPI practice).
- Card UI practice (UX Collective/Eleken): one dominant element per card, an icon/logo
  anchor, consistent header/body/footer zones, fixed card anatomy.
- Genre check: analyst 2×2s (Gartner MQ) read as rankings — wrong for six neutral
  peers; editorial AI "cheat sheets" are tables/prose — confirms card-with-one-big-
  keyword has room to outperform.

## ADOPTED SPEC — S16 "identity trading cards" (keep 2×3 grid)

Card anatomy (≈3.95×2.55", 0.25" gutters):
1. Header strip: logo chip (0.45") + name Calibri Bold ~16pt ink + vendor as 8pt gray
   suffix on the same line.
2. HERO: the 2–4 word identity phrase, Cambria ~26–28pt TEAL — the only teal and only
   large text on the card.
3. Evidence: ONE sentence, Calibri ~10.5–11pt slate (cut to the strongest clause; facts
   stay r13-backed).
4. Caveat as a footer PILL (rounded chip, 9pt, amber tint) — scannable badge, not an
   italic line.
Z-path order: ChatGPT (top-left) → Claude → Gemini / Copilot → Perplexity → Grok.
Slide title becomes an assertion: "Six assistants, six different jobs — pick by task,
not habit."
Variant B (if owner wants a bigger step): same anatomy as six F-pattern rows — faster
scan, weaker equal-peers feel.

## ADOPTED SPEC — S17 bill: "David vs Goliath" split + proportional bars

- Split versus block: "$2.19" (Cambria ~120pt+, TEAL) vs "$60" (same size, ink/charcoal
  — no second accent); "/M output tokens" once, small; vendor names 14–16pt above.
- Under the numerals: two bars at TRUE 1 : 27.4 lengths (teal stub vs near-full-width
  gray bar).
- Hero badge: filled teal circle/pill "27×" (Cambria ~54–72pt white) + "cheaper" 12pt,
  at the seam or the long bar's end.
- Sub-line: "a $100 job for $3.60."
- Eye path: badge → $2.19 → $60/bars. (Fits the slide alongside the MoE hospital
  drawing; the five-benchmark chart compresses or moves to notes-backed thumbnail if
  space demands — decide at layout time.)

Point sizes are calibration for the 13.33×7.5" deck, not source-quoted, except Alley's
~28pt/8–14-word assertion rule.

Key sources: peer.asee.org (assertion-evidence 2011) · duarte.com 3-second test · HBR
"Do Your Slides Pass the Glance Test?" (Oct 2012) · garrreynolds.com design tips ·
NNGroup F-pattern · shortform.com Knaflic preattentive summary · storydoc.com
big-number slides · tabulareditor.com KPI cards · uxdesign.cc card best practices ·
slidemodel.com comparison slides · storypitchdecks.com expert survey · techrepublic.com
AI cheat sheet. (Blog dates without timestamps unverified.)
