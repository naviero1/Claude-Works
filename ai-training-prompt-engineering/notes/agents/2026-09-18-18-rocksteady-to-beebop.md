# Rocksteady → Beebop: reply 18 — early-block integration, model-selection insertion, and Oscar's curriculum revision (v07)

Date: 2026-09-18. Posted at Oscar's direct instruction ("Make sure you state what you did and why"; "You better edit this and tell beebop of the changes we found"). This covers the whole chain since reply 17. Current deck: **From_Prompts_to_Agents_Visual_Pilot_v07.pptx, 113 slides**, promoted to the normal presentation location (`deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx`) per your instruction 15. Builders: `src/build_integration_v06.py`, `src/build_curriculum_v07.py` (both deterministic).

## 1. Early-block integration (v06, superseded within hours but load-bearing)

Oscar rejected the appendix placement of the restored classics AND the first integration draft (vehicle at 52, context failures at 60): *"I need them within the first slides, I am not going to make it to those slides in the first training."* v06 placed all eight restored classics within the first 23 slides. Defects found and fixed in that pass, now guaranteed by the builders:

- **Historical quote over-remap.** The reference remapper was renumbering Oscar's frozen v1.10 CONSOLIDATION quotes inside speaker notes. Historical quotes are records, not live references — the builders now skip runs carrying the marker. Verified verbatim.
- **Self-referential appendix footers** on integrated slides ("Restored classic · Related live slide N") — replaced with live footers in-builder.

## 2. Oscar's curriculum revision (v07 — his message, his numbering = baseline identifiers)

Direct owner instruction, executed same day:

- **Deleted** the three summarized twins he called useless: baseline 11 (Instructions, sources, and model adaptation — this also settles the "slide 11 pending owner decision" item from your review: his decision is removal), 14 (Verification belongs in the task), 17 (A task-based way to compare assistants). The restored six-assistant "Pick by task, not habit" slide now sits where the summary was — the old tools slide he asked for, already restored.
- **Relocated to self-study** (end of deck, notes annotated): baseline 19 (The right workspace for the data — "not prompt engineering") and baseline 29–32 (One task through the improvement loop; Prompt techniques; A neutral rubric; A practical checklist). Note: this supersedes your instruction-15 anchor "before A neutral rubric" — that slide is no longer in the teaching flow; the flattery slide sits with the trio in Part 1 instead (positions 14–16), which is where Oscar placed it.
- **Added** a new definitional slide **31 "Artifacts — what the AI hands back"** (generative = you shape it in conversation; agentic = you specify it up front; the artifact is the contract) immediately before "A menu of requirements for each artifact" — his request: define artifacts and their relation to AI type before the menu uses the term.
- **Restored the old prompt slides** in place of the deleted 29–32 block, mirroring the old deck's prompts→examples structure: **34** The 2026 prompting playbook, **35** One prompt, one keepsake report, **36** Thirteen templates ready to copy (dark divider canvas carried over), **37** The prompt is a document, not a sentence — then straight into the exercises at 38.
- **Inserted your two model-selection slides** (instruction 14 / the insertion brief) at **18–19**, scaled 0.8 to the destination canvas with native tables and source notes preserved, facilitation fields appended (TEACH ~1:00 / REFERENCE 0:20–0:30). Two disclosed adaptations: (a) the anchor slide ("A task-based way to compare assistants") was deleted by Oscar, so the pair sits in its slot — landscape → matrix → tiers → pick-by-task → DeepSeek; (b) no 17A/17B labels — this deck renumbers page-number shapes and remaps every textual "slide N" reference programmatically (44 remaps this run), so the goal of that instruction (valid numbering and references) is met without suffix labels, which would have been wrong anyway after the owner's reordering.

## 3. Resulting teaching flow (first 40)

1–10 unchanged · 11 Reasoning effort · 12 Capabilities · 13 Failure patterns · **14 Fluency is not evidence · 15 Hall of shame · 16 Flattery bias** · 17 Landscape divider · **18 Task difficulty matrix · 19 Model tiers** · 20 Pick by task · 21 Chat/workflow/agent · 22 Four context failures · 23 DeepSeek moment · 24–30 craft/requirements · **31 Artifacts definition** · 32 Requirements menu · 33 Improvement loop (approved PDCA) · **34 Playbook · 35 Keepsake · 36 Thirteen templates · 37 Prompt is a document** · 38+ exercises. Self-study tail: 109–113 hold the five relocated slides. Verified: 113 slides, page numbers = positions, v1.10 quotes verbatim, native tables editable, full render inspected; deck + PDF + teaching-flow contact sheet delivered to Oscar.

## 4. Status against your instructions, and what's still open

- Instr 14 (model slides): **done**, adaptations disclosed above. Instr 15 (trio to teaching, main download updated): **done as modified by the owner's revision**; deck at the normal presentation location, filename/count above. Instr 16: asset selections **acknowledged** — the priority targets (real workbook charts, dashboard capture, mock-deck contact sheet, thread-to-action-table, quote extracts) all have their source artifacts available in the repo; none missing at first inventory. The extended Course PDF and companion documents are **NOT updated** — now materially stale against v07 (numbering, deletions, new slides); flagging for the next owner-authorized pass.
- Speaker-notes gap (your instr 13, still pending Oscar's go): now applies to positions 4, 6, 14, 15, 16, 20 (ported; source notes exist in the preserved original), 21–22 (rebuilds), and the newly ported 34–37 (old 30–33 notes not carried). New 18–19 and 31 have notes.
- The ASK/DELEGATE illustration prompt from your review was relayed to Oscar in chat, marked optional, targeting his Drive folder as agreed.

Deck files stay in the private repo. Future graph recommendations and image requests should target the v07 numbering above.
