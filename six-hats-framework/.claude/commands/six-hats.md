---
description: Run any topic through the Six Thinking Hats framework, one hat at a time.
argument-hint: <topic> [--modality auto|decisions|research|creative|technical] [--single-pass]
allowed-tools: Task, Read, Grep, Glob, Write
---

# /six-hats

Run a full **Six Thinking Hats** analysis on the topic below, following the
protocol in `spec/framework.md`. The core rule: **each hat is a separate,
isolated pass** so the modes don't contaminate each other.

**Topic (and any flags):**
$ARGUMENTS

## How to run it

1. **Blue (open) — framing.** State, in 2–3 sentences: what exactly is being
   thought about, what a good outcome looks like, and which modality this is.
   - Determine the **modality**: use an explicit `--modality` flag if given;
     otherwise classify the topic as one of `decisions`, `research`,
     `creative`, or `technical`. Read the matching file in
     `prompts/modalities/` and use its per-hat focus throughout.
   - Pick the hat **sequence** from `spec/sequences.md` for that modality
     (Blue always bookends).

2. **White — facts.** Produce the shared factual ground: what's known (with
   confidence), what's unknown, and what you'd need to find out. For a
   `technical` topic, read the relevant code/files first. Keep it neutral — no
   opinions. **This White output is the only thing shared with the other hats.**

3. **The middle hats — run each in isolation.** For every remaining hat in the
   sequence, launch a **separate subagent** via the Task tool so each thinks
   blind to the others. Use these agents:
   `hat-green`, `hat-yellow`, `hat-black`, `hat-red`.
   - Give each subagent: the **topic**, the **modality focus** (from the
     modality file), and the **White facts**. Do **not** give it the other
     hats' outputs.
   - You can dispatch the independent hats in parallel (send the Task calls in
     one turn). Red must be told to give **no** justifications.

4. **Blue (close) — synthesis.** Once every hat has reported, synthesize (this
   is the only step that sees all passes): a **bottom line**, the **key
   tensions** between hats (especially Yellow vs Black, and any strong Red gut
   read against the logic), **what tipped it**, **open questions**, and
   **next actions**.

5. **Deliver.** Assemble a Markdown report with one section per hat in sequence
   order, ending with the Blue synthesis. If the user included `--single-pass`,
   skip the subagents and do all hats yourself in one structured pass (cheaper,
   lower fidelity). Offer to save it to a file.

Stay strict about hat discipline: Black and Yellow back every point with a
reason; Green suspends judgment; Red gives feelings with no reasons; White stays
neutral. That discipline is the whole value.
