# Six-slide visual pilot — change report (v01)

Date: 2026-09-17. Built under [approvals.md](approvals.md) and [rocksteady-handoff.md](rocksteady-handoff.md) (owner approval confirmed in session). Builder: `src/build_visual_pilot.py` (deterministic; verifier: `src/verify_visual_pilot.py`).

## OWNER VERDICT (2026-09-17, in session — supersedes the six-slide state below)

Oscar reviewed the six before/after comparisons and the A/B pair and ruled per slide: **approved — 23, 28, 34 (version A), 53; declined — 37 and 87** ("don't make changes" / "no change"). The pilot deck was rebuilt to the verdict state: slides 37 and 87 restored to the untouched baseline, only the four approved treatments present, re-verified in full (99 slides pixel-identical to baseline; four approved slides changed; zero font-size changes — the two slide-37 increases fell away with the declined treatment, so the font log is empty). Version B is superseded by the choice of A and retained only as comparison evidence. The declined wireframe (37) and bars (87) remain documented in this report and the composites as what was piloted and not kept.

## Source and outputs

- Source verified before work: `deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx`, Git blob `e83fd87a8b3e8c868942bdeda668ce085a44c8e4`, SHA-256 `117f60b30c292527d1ac8444ab3efafdbb0ef8d0f3ff159b68149e5804bd24fa` — unchanged at branch head. The main deliverable is untouched by this pilot.
- Version A (the pilot): `notes/visual-polish/pilot/From_Prompts_to_Agents_Visual_Pilot_v01.pptx` — 103 slides, only 23/28/34/37/53/87 modified.
- Version B (slide-34 alternative): `notes/visual-polish/pilot/From_Prompts_to_Agents_Visual_Pilot_v01_S34B.pptx` — differs from A only on slide 34.
- Evidence: `notes/visual-polish/review-evidence/pilot/` (six before/after composites + `s34-comparison-A-vs-B.png`); [font-change-log.md](font-change-log.md); [crop-provenance.md](crop-provenance.md).

## What changed, per slide (all with the approved `#F7F8F6` background, per-slide property only)

| Slide | sid | Treatment as built |
|---|---|---|
| 23 | 278 | Prompt paragraphs kept verbatim (24 pt) on a white specification panel, regrouped right (x2.75); left annotation labels "Audience + source" / "method" / "format + tone + check" (new 18 pt objects) with teal brackets; the linked phrases carry pale-teal native character underlays (editable highlights, exact to the glyph). |
| 28 | 283 | The four PLAN/DO/CHECK/ACT rows became a 2×2 clockwise cycle of white cards (labels 21.75 pt, bodies 22.5 pt, all verbatim) with teal arrows PLAN→DO→CHECK→ACT and the mandatory ACT→PLAN return. Card height 1.70″ (spec envelope 1.58″ adjusted for substitute-font wrap; text sizes untouched). |
| 34 | 291 | Version A, formatting only: file instruction line, then each complete prompt on its own full-width white panel with a clear gap; "then wait" boundary intact; prompt text retained at its baseline 17 pt (the 18 pt trial did not pass the conservative substitute-font fit check — see the font log). Version B: same wording, also at baseline 17 pt, plus an authentic crop of `Supplier_Data_Exercise.xlsx` (header + first 8 detail rows, all columns, aspect preserved) with a filename caption. |
| 37 | 294 | Anchor prompt row moved up into empty masthead space (title box empty-height reduced; wording untouched), requirements and teaching line reflowed into a left block, and a white wireframe panel added at the specified envelope: "Schematic" (17 pt), empty selector chips (Date-range selector / metric selector / reset control; supplier and site filters with two empty selector boxes), a return-arc on reset, three parallel connectors from the selector row into summary values, trend chart, and sortable detail table. No values, traces, or invented results anywhere. |
| 53 | 308 | Left column framed by a thin paper outline with a folded corner; right column framed by a stronger 2.5 pt boundary outline; a small outlined amber checkpoint diamond sits in the boundary margin aligned with "Configure available approvals." — covering no text. All six statements and both headings untouched. |
| 87 | 342 | Three editable teal rectangles beside the existing return-rate percentages at the exact specified geometry (common zero baseline x = 11.12″; 0.004 rate fraction ↦ 1.10″; widths 0.27111644 / 0.95831560 / 0.35361247 from the full-precision fractions 74/75,060 · 262/75,184 · 96/74,658). No TOTAL bar; all 20 table cells and the caveat untouched. |

## Font changes (full detail in [font-change-log.md](font-change-log.md))

The only applied increases are the two slide-37 changes (anchor prompt 17→18 pt; teaching line 17→18 pt), under the approved standing exception (baseline < 20 pt, wording/family/emphasis unchanged). Not applied (reported per handoff §4): slide 34 in **both** versions — the 18 pt trial for the prompt labels and bodies did not pass the conservative substitute-font fit check in A, and in B the workbook crop consumes the space the increase needs, so baseline 17 pt is retained throughout slide 34; slide 37 requirements body — an 18 pt trial crowded the teaching line beside the approved wireframe, so baseline 17 pt is retained. Nothing was reduced; nothing at ≥ 20 pt changed. (An earlier draft of this report incorrectly described slide 34-A as raised to 18 pt; corrected 2026-09-17 in the evidence-accuracy repair — the decks and the machine-generated font log were always consistent at 17 pt.)

## Slide 34 recommendation

Version A is recommended for the course: it improves prompt grouping and separation while retaining the baseline 17 pt prompt text. Version B is faithful and authentic, but at the space available the crop's cell text is small — it communicates the upload's tabular structure at a glance rather than readable values. If that recognition cue matters more than the cleaner full-width layout, B is usable; the A/B composite shows the trade-off directly. Beebop's independent review concurs: A preferable, B's crop too small to be useful beyond recognition.

## Verification results

- Renders: all 103 slides of baseline, A, and B rendered at identical resolution (110 DPI, LibreOffice; Calibri/Cambria render as substitutes, as with all prior renders — no native PowerPoint check was available, disclosed per handoff §8).
- Collateral: all 97 non-target slides of A are **pixel-identical** to the baseline render; B is pixel-identical to A everywhere except slide 34.
- Structure (see `src/verify_visual_pilot.py`, all checks passing): 103 slides; native slide ID order identical; only the six pilot slide parts differ from baseline (canonical XML); **all notes parts byte-identical**; theme/master/layout parts **byte-identical**; every baseline visible string present verbatim on the six modified slides with no unapproved additions (approved labels only); every size delta is a logged <20 pt increase with emphasis preserved; slide-87 bar geometry matches the spec to <0.002″; all 20 table cells unchanged; crop provenance hashes verified.
- Adversarial visual round (completed 2026-09-17): seven independent inspectors re-checked the six slides and the A/B pair against the acceptance checks, plus a completeness critic against handoff §8. **Zero blockers.** One geometry finding was fixed and re-verified (slide 23's third bracket overshot the white panel when the substitute font wrapped that group to three lines; the panel now sizes to measured content). Remaining known cosmetics, disclosed and left as-is: slide 23's two method-phrase underlays sit ~2 px apart across wrapped lines and can read as one block at distance; slide 53's checkpoint diamond floats ~2 px from the heavy boundary border; slide 28's CHECK card has tighter bottom padding than its three siblings (three-line body); slide 34 shows a pre-existing underscore-descender artifact of the substitute font, present in the baseline render too.
- Render evidence for independent inspection: full-size renders of the six slides (baseline + A) and slide 34-B under `review-evidence/pilot/renders/`, and a SHA-256 manifest of all three complete 103-render sets with the pixel-diff statement in `review-evidence/pilot/render-manifest.json`.
- Companion blobs confirmed unchanged at branch head (handoff §8): `Course_Workbook.xlsx` `5a6ca157da0f57821c5d43652041285ed8eae9c3`, `From_Prompts_to_Agents_Cheat_Sheet.pdf` `2379ff285a42d6b35e0a93020767fe2eff68d8c7`, `From_Prompts_to_Agents_Course.pdf` `00cc627572877aeca3588521a943a31d15ab2b9f`, `From_Prompts_to_Agents_Facilitated_60_Minute.pptx` `e83fd87a8b3e8c868942bdeda668ce085a44c8e4`, `Prompt_Template_Creator.html` `8ba21181efe79206d6b76e9a53109f1f2f0328df`; builder, prepared outputs, and exercise sources under `references/` and `src/` untouched by this pass.

## Timing statement (TIME-PLAN)

Per [pilot-facilitation-plan.md](pilot-facilitation-plan.md): the operating target remains approximately 60 minutes with the owner's flexibility of roughly ten minutes either way and up to twenty additional minutes available; the current full active-note allocation measures **72:50**, including 45:00 of DO practice. This pilot changes no notes, durations, modes, or order.

## Out of scope, unchanged

Main deliverable and the other four core artifacts; extended PDF; all notes; companion C01–C05 and the queued note/transition/content proposals; full-deck expansion (blocked until pilot review).
