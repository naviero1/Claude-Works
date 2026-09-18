# Curriculum revision v07 — owner-directed (2026-09-18)

Builder: `src/build_curriculum_v07.py` (deterministic, v06 → v07). Verifier: `src/verify_v07.py`.
Deck: `notes/visual-polish/pilot/From_Prompts_to_Agents_Visual_Pilot_v07.pptx` (113 slides),
promoted to `deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx`.

## Owner instruction (verbatim anchors, his numbers = baseline identifiers)

"You also have a bunch of useless slides, specifically 11, 14, 17, i'd like a slide where i
introduce all the tools from the old slide here. that was value added, not the crap you both
erased and added, we dont want to get into slide 19's topic, i am just teaching prompt
engineering, for slide 27 we first need to define artifacts and how they are related to the
type of ai, agentic vs generative, we don't need 29, we done need 30, 31 or 32, instead bring
the prompts that we were talking about here then let's jump into the examples"

Interpretation, verified against titles (the numbers only cohere as baseline identifiers —
under v07/v06 numbering "17" would be the restored hall of shame he just fought to keep):

| His # | Slide | Action |
|---|---|---|
| 11 | Instructions, sources, and model adaptation | DELETED (summary twin) |
| 14 | Verification belongs in the task | DELETED (summary twin; trio covers it) |
| 17 | A task-based way to compare assistants | DELETED (summary twin; the restored old six-assistant "Pick by task, not habit" = "the old slide introducing all the tools" now sits in its place) |
| 19 | The right workspace for the data | RELOCATED to self-study (not prompt engineering) |
| 27 | A menu of requirements for each artifact | NEW definitional slide inserted before it |
| 29–32 | Improvement-loop example / techniques / rubric / checklist | RELOCATED to self-study; old prompt slides restored in their place |

"The prompts that we were talking about" = the old deck's prompt slides (old 30–33: playbook,
keepsake report, thirteen templates, prompt-is-a-document) — the old deck ran exactly
prompts → examples at this point, which his "then let's jump into the examples" mirrors.

Plus the two supplied model-selection slides (owner commit 434ee0f + insertion brief +
channel instruction 14), scaled ×0.8 to the destination canvas, native tables and source
notes preserved, caveat lines kept visible as the footer band, facilitation fields appended.
17A/17B labels were not used: this deck renumbers and remaps references programmatically,
and the owner's reordering made the literal labels wrong; the instruction's goal (valid
numbering/references) is met by the remap (44 references this run).

## v07 teaching flow (first 40)

1–10 unchanged · 11 Reasoning effort · 12 Capabilities · 13 Failure patterns ·
14 Fluency is not evidence · 15 Hall of shame · 16 Flattery bias · 17 Landscape divider ·
18 Task difficulty matrix · 19 Model tiers · 20 Pick by task · 21 Chat/workflow/agent ·
22 Four context failures · 23 DeepSeek · 24–30 craft/requirements ·
31 Artifacts — what the AI hands back (NEW) · 32 Requirements menu ·
33 Improvement loop (approved PDCA) · 34 Playbook · 35 Keepsake · 36 Thirteen templates ·
37 Prompt is a document · 38+ exercises. Self-study tail 109–113 = relocated slides.

## Build guarantees

- v1.10 CONSOLIDATION historical quotes frozen against the remapper (verified verbatim).
- Page-number shapes renumbered; 44 textual references remapped in text and notes; footers
  pointing at relocated slides say "(self-study)" instead of "live".
- Ported old slides carry their slide-level background (the templates divider is dark
  #1C272E → light footer chrome) and drop old kicker-footers positionally.
- Relocated slides carry a RELOCATED annotation at the top of their notes.
- Deleted slides' rels dropped; everything recoverable in git history.

## Verification (2026-09-18)

113 slides; page numbers = positions; no stale footers; quotes verbatim; native tables on
18–19; full 113-page render inspected (new slides 18, 19, 31, 34–37 individually).
Contact sheet: `review-evidence/pilot/v07-teaching-flow-contact-sheet.png`.

## Known-stale after v07 (pending next owner-authorized pass)

- Extended Course PDF + companion documents (facilitation plan, slide maps, timing): built
  against the 103-slide baseline; numbering and content now differ materially.
- Speaker notes: ported slides 4, 6, 14, 15, 16, 20 (source notes exist in
  `references/From_Prompts_to_Agents_Training.pptx`), rebuilds 21–22, and new ports 34–37
  are notes-empty (Beebop instr 13 verification pass, awaiting Oscar's go).
- s1 timing notes still describe the pre-revision protected-application split.
