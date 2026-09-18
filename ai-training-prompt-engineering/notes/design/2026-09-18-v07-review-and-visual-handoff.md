# Beebop: v07 review and bounded visual handoff

Date: 18 September 2026. Reviewed material commit: `bc54dc5f1b94d6c37eed38fe7dc6371881b1fb11` on `claude/training-course-polish-oxohwj`.

## Authority and baseline

Read public instructions 14–16, public reply 18, private reply 18, `notes/visual-polish/integration-v06.md`, `notes/visual-polish/curriculum-v07.md`, the v07 builder and verifier, and the actual deck. The newer explicit owner direction recorded in curriculum-v07 governs over the older placement anchors. Instruction 13 already authorized verification and proposed repairs; it did not authorize implementing those repairs.

Do not repeat the completed model insertion or restore the removed summaries. The three illustrated risk slides remain together at v07 positions 14–16, the model-selection pair at 18–19, and the old baseline slide 11 is deleted by owner direction. Keep the revised prompt-to-exercise sequence. Accepting this as the working baseline does not mean every remaining quality issue is resolved.

## Independent checks performed by Beebop

- Downloaded the actual branch through git. Local and remote heads matched the reviewed commit immediately before handoff preparation.
- Actual presentation has 113 slides. Main deliverable and pilot v07 are byte-identical. SHA-256 (Secure Hash Algorithm, 256-bit): `dc3408ab3aa4ae56cc276a509824e1e4a9f62e31053c9674db35e3af6eb18462`.
- Ran the repository verifier: it reported `ALL CLEAN - 113 slides`. Its checks are limited to slide count, populated page-number shapes, selected stale-footer strings and a historical-quote substring. This is not comprehensive reference, factual or visual validation.
- Read actual slide text, order and notes. Confirmed the removed summary titles are absent and the five relocated slides occupy 109–113.
- Compared model tables against the supplied two-slide source: cell text identical, tables native/editable, original notes retained before appended facilitation fields.
- Compared embedded image bytes against v05: the three restored risk slides retain all their pictures (4, 7 and 2 respectively).
- Compared visible content and geometry for the accepted/protected pilot slides against v05, excluding page-number and reference-footer changes: preserved. Correct current mapping is baseline 23 -> 27, 28 -> 33, 34A -> 39, 53 -> 58, protected 37 -> 42, protected 87 -> 92. Match titles, not an assumed uniform offset.
- Independently rendered the current main presentation with LibreOffice to a 113-page slide PDF (Portable Document Format). Inspected individual 1600-pixel renders of 14, 15, 16, 18, 19, 31, 34, 35, 36 and 37, plus the committed first-40-slides contact sheet. No gross clipping or overlap in those selected renders. This is not a claim to have visually inspected every slide, checked in PowerPoint, or revalidated all dated facts. Some monospace text renders with uneven spacing locally (16, 35, 37); check the intended delivery renderer before changing fonts.

Rocksteady separately reports full-deck visual inspection and 44 reference remaps. The count of 44 was not independently reproduced. Do not conflate a successful machine check with complete instructional coherence.

## Remaining issues observed, not silently repaired

1. Notes are empty on 4, 6, 14, 15, 16, 20, 21, 22, 34, 35, 36 and 37. Sources and facilitation guidance need proposed restoration, as already requested by instruction 13. Original model-slide notes are intact.
2. The integrated risk slides still carry `REFERENCE STUDY` chrome despite their teaching placement. Self-study 109–110 retain `TEACH` chrome. Record a proposed classification correction rather than moving slides or assuming owner approval of a restyle.
3. Restored playbook slide 34 says `next slide's loop`, but slide 35 is the keepsake exercise and the loop is now 33. The reference remapper handles numeric references, not this relative reference.
4. Slide 35 calls itself the closing exercise and assumes a course log opened with Prompt 1, yet now precedes the main exercises. Check the prerequisite, workbook-tab links and intended demonstration against the actual course files. Preserve the owner's placement; propose a bridge or qualified usage note, not an automatic relocation.
5. Slide 36 still labels Part 4 as Playbook, followed by another Part 4 Application divider at 38. Preserve restored content and propose a navigation-label repair for review.
6. Slide 31's absolute wording `You are not in the loop while it works` should be qualified so it does not contradict approval gates and human review taught elsewhere. Propose wording such as `The agent can work between your review checkpoints; specify the deliverable, checks and approval gates up front.` Do not silently replace the owner-requested definition.
7. Extended written course PDF and companion maps/facilitation documents remain stale, as reply 18 reports. This pass does not authorize rebuilding them. A rendered slide PDF is not the extended written course.

## Actual inputs now supplied

- `notes/design/visual-production-inputs/Course_Visual_Prompts.md`: complete original 11-prompt pack, unchanged for traceability. This handoff overrides its old numbering, authorization status and outdated instruction to ask Oscar to generate/upload the first image.
- `notes/design/visual-production-inputs/S02_Ask_Delegate_v01.png`: Oscar's accepted original image, copied unchanged from his attachment. Use it; do not ask for another upload or regenerate it.

The image was inspected. Its two scenes and human review are clear. Preserve its aspect ratio and both scenes. Exact pixel dimensions need not match the requested dimensions if it remains sharp at the proposed size.

## One bounded next deliverable

Oscar authorized delegation of the remaining visual work after reviewing completed corrections. Prepare one **visual-candidate review package**, with finished target-slide treatments in a separate review deck, editable sources, full-size previews and a source/provenance register. Do not overwrite/promote the current main presentation or expand to unrelated slides. Oscar retains final review of the finished treatments; do not require another approval merely to prepare these already-requested candidates.

Use the original prompts with this authoritative mapping:

| Pack prompt | v07 target/title | Disposition |
|---|---|---|
| 1 | 2: One skill, two ways to work | Image already supplied and accepted. Prepare placement preview under ASK/DELEGATE; retain editable headings. |
| 2 | 7: How a language model produces an answer | Prepare editable inputs/model/response/external-check diagram. |
| 3 | Deleted: Verification belongs in the task | RETIRE. Do not recreate the deleted slide or insert its example elsewhere. |
| 4 | 110: One task through the improvement loop | Prepare workbook crop only for self-study. Do not return it to the live sequence. |
| 5 | 41: Add the Charts and Return the Excel File | Real editable charts plus large demonstration/capture. |
| 6 | 43: Build and Test the Dashboard | Actual filtered dashboard capture, reconciled to source. Preserve protected slide 42. |
| 7 | 44: Turn the Findings into a Five-Slide Management Mock-up | Actual five-slide renders, ordered contact sheet and full-size example. |
| 8 | 46: Outlook Exercise: Decisions, Actions, and Open Questions | Actual fictional thread excerpt and editable decision/action table. Reveal after attempt. |
| 9 | 47: Extract Supplier Quotes into Excel | Authentic quote crop to matching extracted row; keep source page identity. |
| 10 | 48: Normalize and Compare the Supplier Quotes | Native formula-bearing comparison; missing terms visible; no unsupported ranking. |
| 11 | 49: Turn Reference Files into a Research Spreadsheet | Actual source passage to evidence row to synthesis/source register. |

Thus: supplied image placement plus **eight live production treatments and one self-study treatment**. No further image-generation work from Oscar. Use meaningful slide-title-based asset names; old prompt filenames are historical identifiers, not current slide positions.

Preserve accepted 27/33/39/58 and protected 42/92 by title; preserve the restored artwork, both model tables, complete prompts, supporting reference depth and owner's chosen sequence. Answer-bearing examples appear after an attempt or as clearly identified prepared demonstrations. No exact-60-minute gate, rollback, further summary deletions or full-deck redesign.

## Source availability and provenance

Confirmed files exist in `references/exercise-data/`: `Supplier_Data_Exercise.xlsx`, `Supplier_Data_Analyzed.xlsx`, `Supplier_Quality_Dashboard.html`, `Supplier_Quality_Mock_Presentation.pptx`, `Packaging_Change_Thread.txt`, `Quote_Alpha_Components.pdf`, `Quote_Bravo_Plastics.pdf`, `Quote_Cardinal_Metals.pdf`, `Quote_Comparison_Workbook.xlsx`, `Research_Workbook.xlsx`, `research-pack/`, and the supplied instructor keys. Existence is not numerical validation. Use the packaging thread and its corresponding key, not similarly named alternate email material without checking identity.

For each produced visual record the actual source file/version, sheet/range or page, filter state, displayed units, calculation checks and reveal timing. Preserve source files. Exclude TOTAL from detail calculations, distinguish returns from defects, use supported denominators, preserve missing information and conditional commitments. Do not fabricate application interfaces, source excerpts, numbers or missing evidence. If a source proves insufficient, identify the exact missing field/file and continue the unblocked candidates.

## Return and stop

Return one indexed package in the private repository with: current baseline commit, title-to-position map, candidate deck, full-size previews, editable originals, source register, validation results and a concise discrepancy/proposed-repair log for the issues above and outstanding instruction-13 checks. Do not apply unrelated notes, citation or companion repairs as part of visual production.

In the public channel post coordination only: private package location/commit, completed and blocked items, and separate statuses for presentation, slide-render PDF and extended written course PDF. No private training content, data, screenshots or assets in Agents_Link. Beebop reviews candidate clarity and fidelity; Oscar has the final decision on finished slides. Stop after this bounded handoff result. No recurring monitoring is requested.
