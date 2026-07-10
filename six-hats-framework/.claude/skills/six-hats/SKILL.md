---
name: six-hats
description: Structured thinking with Edward de Bono's Six Thinking Hats — analyze any topic through six isolated modes (facts, feeling, caution, optimism, creativity, process) and synthesize. Use when the user wants to think a decision, question, design, or draft through systematically, asks for pros/cons or risks-and-benefits done rigorously, wants a decision framework applied, or mentions "six hats," "de Bono," "thinking hats," a pre-mortem-style critique, or a full-spectrum evaluation. Adapts to decisions, research, creative, and technical tasks.
---

# Six Thinking Hats

A protocol for **parallel thinking**: instead of one muddy "analyze this" pass,
you think in one distinct mode at a time and keep the modes from contaminating
each other. This produces sharper output in each mode — criticism doesn't
smother creativity, optimism doesn't paper over risk, and the modes people
usually skip (a pure optimism pass, a pure idea-generation pass) actually happen.

## The six hats

- **🔵 Blue** — process/meta. Frames the session (open) and synthesizes it
  (close). Bookends every run.
- **⚪ White** — facts & information. What's known (with confidence), what's
  unknown, what to find out. Neutral; no opinions.
- **🔴 Red** — emotion & intuition. Gut reactions, stated with **no**
  justification.
- **⚫ Black** — caution & critique. Why it might fail; every risk backed by a
  reason.
- **🟡 Yellow** — optimism & value. Why it might work; every benefit backed by a
  reason. (Harder than Black — protect this pass.)
- **🟢 Green** — creativity. Alternatives, reframes, provocations; judgment
  suspended.

## How to run it

1. **Blue (open):** frame the topic and the goal; pick the **modality** —
   `decisions`, `research`, `creative`, or `technical` — which tunes each hat's
   focus and the hat order. See `spec/modalities.md` and `spec/sequences.md`.
2. **White:** establish the shared facts and gaps. This is the **only** hat's
   output shared with the others.
3. **Each other hat, in isolation:** give each one the topic, the modality
   focus, and the White facts — never the other hats' outputs. If sub-agents are
   available (`hat-green`, `hat-yellow`, `hat-black`, `hat-red`), dispatch them
   in parallel; otherwise do each hat as a clearly-separated pass, resetting
   your frame between them.
4. **Blue (close):** the only step that reads everything. Synthesize a bottom
   line, the key tensions (Yellow vs Black; any strong Red read against the
   logic), what tipped it, open questions, and next actions.

## Discipline (the whole value)

- Black and Yellow **must** give reasons. Red **must not**.
- White stays neutral; Green suspends judgment.
- Don't let one hat leak into another — that isolation is what makes this better
  than an unstructured analysis.

## Modality quick reference

- **decisions** — surface the full option set before judging; weight
  reversibility. Order: White → Green → Yellow → Black → Red.
- **research** — White is the centerpiece; Black stress-tests the *evidence*.
  Order: White → Green → Black → Yellow → Red.
- **creative** — diverge first; Red ("does it land?") is primary. Order: Green →
  Yellow → Red → White → Black.
- **technical** — pin real constraints (White), run Black early and hard. Order:
  White → Black → Green → Yellow → Red.

## Deliverable

One Markdown section per hat in sequence order, ending with the Blue synthesis.
For a scripted/batch version outside Claude Code, use `cli/six_hats.py`. Full
rules live in `spec/framework.md`.
