# Visual heritage proposal — owner-valued visuals from earlier iterations

Date: 2026-09-17. Status: DRAFT for Oscar's decision bundle; not yet sent to
Beebop; authorizes nothing by itself. Context: during pilot review Oscar
cited earlier illustrated slides he found valuable (tokens/LEGO, context
desk, RAG librarian, four eras, hardware story, hallucination emblems, hall
of shame, assistant comparison, DeepSeek/MoE hospital, prompt anatomy). The
22 owner-approved illustrations from those iterations survive in
`src/assets/images/`. The summarized 103-deck kept the metaphors as text —
so most images plug back into an existing slide.

## Category A — direct image reattachment (concept survives on a matching slide)

The slide already teaches the metaphor; the treatment is layout + the
existing owner-approved image. No new wording needed beyond optional captions.

| Asset | Current slide | Title |
|---|---|---|
| `lego_tokens.jpg` | 8 | Tokens and practical limits |
| `desk_cabinet.jpg` | 9 and/or 73 | Context, saved history, and memory / A desk, not a filing cabinet |
| `open_book.jpg` | 10 and/or 74 | Answers grounded in documents / An open-book exam — audit the librarian |
| `body_anatomy.jpg` | 75 (echo on 49) | Seven parts, one body — what good looks like |
| `hospital_night.jpg` | 18 | January 2025: frontier ability, ~27× cheaper (MoE "specialist hospital") |
| `emblem_cue_card.jpg`, `emblem_fake_receipt.jpg`, `emblem_rubber_chicken.jpg`, `emblem_gilded_frame.jpg` | 15 | Failure patterns and the check they need (the four hallucination emblems) |
| `blueprint_loop.jpg` | 28 ref twin 79 | The toolkit is a loop |
| `deming_portrait.jpg` | 79 or 28 notes-adjacent reference | improvement-loop lineage |
| `courier_work_order.jpg` | 50 or 84 | mission brief / bounded work order |
| `dashboard_laptop.jpg` | 93 or 98 | dashboard requirement/exercise pages |
| `question_bench.jpg`, `office_scene.jpg` | 64/70 region | closing sequence (bench + office scenes) |
| `robot_graduate.jpg`, `mirror_reflection.jpg`, `map_world.jpg`, `memory_ladder.jpg`, `guardrails_road.jpg`, `hare_tortoise.jpg`, `shame_gallery.jpg`, `hospital_night.jpg` | audit pass | map each against parts 1–2 and the reference layer; attach only where the slide genuinely teaches the metaphor, otherwise leave archived |

## Category B — content restoration candidates (need Oscar's explicit call + currency re-verification)

These earlier slides carried substance the summarization dropped, not just
artwork. Restoring them adds content back and every dated claim must be
re-verified before reinstatement (currency-sensitive facts rule):

1. **Hallucination, measured** — the "confident guess" bar comparison and the
   four-mode taxonomy behind slide 14/15's summary.
2. **Hall of shame** — the named public cases (glue-on-pizza, Air Canada
   chatbot, Mata v. Avianca, Big Four citations arc) behind slide 15.
3. **Assistant comparison, vendor-named** — the "Pick by task, not habit"
   six-assistant cards behind slides 13/16/17 (heavily date-stamped; highest
   staleness risk, needs a maintenance note if restored).
4. **Four eras / hardware story richness** — the era cards and Moore's-pace
   chart behind slides 4–6.

5. **The flattery bias — measured, and all over the news** (owner: "value
   added as it is"): the +49% measured comparison, the news timeline, the
   countermeasures, and the SEE-IT-YOURSELF two-chat exercise, with
   `mirror_reflection.jpg`. No direct descendant in the current deck; nearest
   home is the failure-patterns region (slide 15) or a new reference-layer
   page. Every dated claim (study, news items) re-verified before
   reinstatement.
6. **Chat, workflow, or agent — the path decides** (owner: "value added as
   it is"): the three-vehicle cards, decision rule, and wrong-vehicle cost,
   with `courier_work_order.jpg`. Descendants: slides 46 ("What makes a
   workflow agentic?") and 48 (discussion). Restore as an enrichment of that
   block or a reference twin.
7. **Four context failures — name it, then cure it** (owner: "value added as
   it is"): the poisoning/drift/confusion/clash taxonomy plus the
   "why did it ignore me" instruction-layer stack. Direct descendant: slide
   54 ("Diagnosing a failed run"). Restore as an enrichment of 54 or a
   reference twin.

Category B could live in the deck's reference layer, in the extended course
PDF only, or both — Oscar chooses per item. Items 5–7 are slides the owner
explicitly called valuable in their complete form, so the default proposal
for them is faithful restoration (updated dates where needed) rather than
image-only reattachment.

## Constraint to reconcile with Beebop

Beebop's current shared-design rule for treated slides excludes
photographic/illustrative imagery ("no texture, stock photography, robots").
These are not stock images — they are owner-approved instructional metaphors
with recorded attribution (asset register). Adding them to the full pass
requires an explicit recorded decision superseding that rule for the listed
assets, plus per-slide fit specs from Beebop as with the pilot treatments.

## Owner-directed workstreams added 2026-09-17 (in-session instruction)

**C — Graphs where they help.** Oscar wants data graphs in the deck, with
Beebop recommending where a chart genuinely aids comprehension. Constraints:
native editable construction (like the slide-87 bars), driven only by
recorded, verifiable numbers — canon dataset values, or externally sourced
figures re-verified and dated at build time. No fabricated or decorative
charts; that rule stands.

**D — Generated illustrations via Oscar (Nano Banana).** Oscar has activated
the illustration pipeline recorded in
`notes/visual-polish/gemini-image-requests.md`: Beebop submits complete
requests — stable asset code, exact slide, instructional purpose, measured
box/aspect/pixels, palette/background (compatible with the approved #F7F8F6
surfaces and the existing 22-asset flat-illustration style), composition,
required and forbidden elements, filename, a copy-ready generation prompt,
and acceptance criteria. Rocksteady relays each batch to Oscar in session;
Oscar generates with Nano Banana (Gemini image generation) and returns
candidates; candidates are inspected against acceptance criteria before any
slide placement, and uploading a candidate does not approve its slide
treatment.

## Proposed sequencing

Bundle with the pilot verdict: (1) Oscar verifies the pilot; (2) completion
reply 15 goes to Beebop with the pilot results AND this proposal as the
owner's direction for full-pass planning; (3) Beebop specs the reattachments
per slide (Category A) and the restoration decisions (Category B) come back
as itemized approvals before any build.
