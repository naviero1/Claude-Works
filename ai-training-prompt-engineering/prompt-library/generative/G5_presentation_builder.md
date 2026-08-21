# G5 · Presentations (outline → deck)

**Type:** Generative · **Version:** 1.0 · **Use when:** turning a report, analysis, or notes into slides.
**Works in:** Claude (pptx creation, Claude for PowerPoint), ChatGPT, Copilot in PowerPoint, Gemini in Slides, Gamma.

> The reliable flow is **content → outline → approval → deck**, not "make me a presentation
> about X." Approving headlines as plain text costs 2 minutes; re-thinking a rendered deck
> costs an afternoon.

---

## The template

```text
<role>
You are a presentation writer for executives. Titles state findings, not topics. Every claim
carries its number. You cut without mercy.
</role>

<mission>
Deck for {{audience}} · {{N}} minutes of their time · Their question: {{what they need decided
or understood}}. My raw material is attached/pasted below — use nothing beyond it.
</mission>

<structure>
- {{N}} slides max. Slide 1 answers the question; the rest support it; appendix for depth.
- Every slide title = the takeaway in ≤ 12 words, with the number
  ("Scrap fell 40% after the fixture change", never "Scrap update").
- Per slide: ≤ 3 bullets, each a fact with a number, plus [VISUAL: what the chart/image
  shows and what it must prove].
- Speaker notes per slide: 3-5 lines — what to say, the caveat, the ask.
- Footer on data slides: source file + as-of date.
</structure>

<continuity>
Match {{our template / the previous deck}}: fonts, colors, metric names, chart colors per
{{site/product}} exactly as before. [If building the file: use template {{file}}.]
</continuity>

<process>
Step 1: give me ONLY the slide titles + bullets + visual notes as plain text. STOP for my
approval — do not render.
Step 2 (after my OK): build the .pptx.
</process>

"""
{{raw material: the report, analysis output, notes}}
"""
```

## Quick variant — one slide from an analysis

```text
One slide for {{meeting}}, from the analysis below. Title = the answer with the number
(≤ 12 words). One chart [describe: type, x, y, sort, target line, n labels]. ≤ 3 bullets,
each with a number. Speaker notes: 3 lines + the one caveat I must say out loud.
Footer: source + as-of date. Text first for approval; render after my OK.
"""{{analysis output}}"""
```

---

## What makes this work
- **Message titles (assertion-evidence)**: decks read as an argument, not a table of contents; leadership can skim titles alone and get the story.
- **Time budget in the prompt** forces the right altitude — a "3 minutes on this slide" deck is a different artifact than a 30-minute deep-dive.
- **Text-before-render gate** is the single biggest time-saver in AI deck work.
- **"Use nothing beyond the material"** blocks invented context, the deck-generator failure mode.
- **Continuity block** because AI decks default to generic styling; template fidelity is what makes it look like *your* org's work.

## Pitfalls
- Asking for the deck before the analysis is settled — garbage in, confident garbage out.
- Letting the tool pick chart types for proportions/trends: specify, or you'll get 3-D pies.
- Skipping speaker notes — the deck walks without you and gets misread.
- Formatting fidelity: AI-generated pptx still needs a human pass on your corporate template (vendors admit this); budget 10 minutes for polish.
