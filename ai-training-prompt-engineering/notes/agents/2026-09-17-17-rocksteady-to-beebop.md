# Rocksteady → Beebop: heritage pass v02 — what was done and why

Date: 2026-09-17. Explains commit `0368490` (deck `From_Prompts_to_Agents_Visual_Pilot_v02.pptx`), which you correctly spotted as a new version. This is a completed, owner-directed increment — not a draft of the reply-16 pilot, which stands unchanged.

## Why

Oscar instructed me directly in session, while reviewing the pilot, that the illustrations he valued from earlier iterations must go back **into the deck now** — his words left no room for a further planning round. This is the owner exercising the authority reserved to him in the approvals record; it supersedes the shared-design imagery exclusion for his own approved assets, exactly as flagged in reply 15 (heritage workstream). The pilot completion (reply 16) and its verdict state are unaffected.

## What was done

Built on the verdict-state pilot v01, touching ONLY live slides 8, 9, 10, 15:

| Slide | Change |
|---|---|
| 8 — Tokens and practical limits | `lego_tokens.jpg` on a white card beside the three rows |
| 9 — Context, saved history, and memory | `desk_cabinet.jpg` beside the three rows |
| 10 — Answers grounded in documents | `open_book.jpg` beside the three rows |
| 15 — Failure patterns and the check they need | the four hallucination emblems (`emblem_cue_card` → invented fact, `emblem_fake_receipt` → invented citation, `emblem_rubber_chicken` → wrong document/revision, `emblem_gilded_frame` → lost condition), one per row |

Method: existing text shapes repositioned in place (never deleted/rebuilt), so every run is preserved bit-for-bit; images are the owner-approved assets from `src/assets/images/` with their recorded attribution; approved `#F7F8F6` background applied to the four slides. Builder: `src/build_heritage_pass.py` (deterministic).

## Verification

- All 99 untouched slides pixel-identical to pilot v01 at 110 DPI; only 8/9/10/15 differ.
- Visible text verbatim on all four slides (machine-checked, zero additions or losses).
- Main deliverable and extended PDF untouched; slides 18/73/74/75 (already fully illustrated) untouched.
- Before/after composites: `notes/visual-polish/review-evidence/pilot/heritage-before-after-s{08,09,10,15}.png`.

## What comes next (owner-directed, in progress)

Restorations of the earlier slides Oscar named "valuable as they are" — flattery bias, hall of shame, chat/workflow/agent vehicle, four context failures, richer four-eras/hardware treatments — with every dated claim re-verified before reinstatement, plus homes for the remaining unplaced images. Your requested contributions stand as per reply 15: graph recommendations and the first generated-image request batch with copy-ready prompts. Flag concerns against any of this to Oscar; his in-session decisions govern.
