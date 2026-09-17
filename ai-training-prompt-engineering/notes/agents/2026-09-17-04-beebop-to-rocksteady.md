# Beebop → Rocksteady — Review iteration 04

**Reviewed private course commit:** `ba57f77f722b86e4feb6889012dd580ed52723a8`

The bounded cleanup corrected the citation wording and dashboard range-label logic. Beebop independently verified the updated source logic, rendered the affected live-deck slides, inspected the regenerated course and field-guide citation pages, and checked the workbook citation cell.

Two narrow issues remain. Do not change anything else.

## Required repair

1. **Restore mixed text formatting on the detailed Role & Task reference slide.** The citation-normalization routine rewrote a whole mixed-format paragraph through its first text run. The resulting slide does not overflow, but the complete Task explanation is now bold and the prior hierarchy—including the distinct citation styling—was lost. Make the substitution at run level, or otherwise preserve the paragraph’s original typography while changing only the citation text. Compare the repaired slide directly with its pre-cleanup rendering.
2. **Finish the citation sweep.** One long-format-deck source note still uses the shorthand “Yang 41.1%.” Replace that remaining ambiguous form with the agreed canonical wording. Expand the verification search so it reviews every occurrence of “Yang,” including forms without a year, rather than checking only known year-bearing variants.

Preserve the approved course content, layout, five exercise families, requirements-writing integration, artifact sequence, dashboard behavior, workbook, timing, and package structure. No additional copy, design, or scope changes are authorized.

## Approval and stop condition

Before applying this repair, report your understanding and proposed artifact classes to Oscar and obtain his approval. Then complete exactly one repair iteration, regenerate only affected artifacts, render-check the repaired reference slide, run the presentation overflow test, report the resulting private commit and evidence in the communication repository, and **stop for Beebop review and Oscar’s final word**.

Keep private course files and detailed course data out of this public repository.
