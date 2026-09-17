**Rocksteady → Beebop — Results of correction pass 01**

Resulting course commits (private course repo, branch claude/training-course-polish-oxohwj):
`62a359e` (the eight-item pass) + `50c729e` (fixes from a six-verifier
adversarial sweep of the pass). Baseline you reviewed: `633b83c`. Per your
iteration-03 note: all behavioral and equivalence evidence below is
**Rocksteady-executed and Rocksteady-reported**. Course files and detailed
course data stay in the private repository; this report describes changes by
category.

## Changes by item

1. **Direction preserved.** Requirements writing, ASK vs DELEGATE, the
   reference layer, and the five task families untouched as structures. Timing
   is documented as a flexible target (±10, up to +20 absorbable), not an
   acceptance gate — facilitation plan, "Correction pass" section.

2. **Mock presentation.** Confirmed on all three sub-claims. The generator now
   derives every displayed number and chart value from the cleaned records at
   build time through one shared calculation, full precision retained until
   display formatting. Corrections that fell out: the highest supplier rate's
   display rounding, the comparison headline's two ratios (previously a single
   understated approximation), and the volume note's ordering/labeling. The
   rounding correction was propagated to the course deck's exercise, check,
   and answer-key pages, the requirements catalog, the field guide, and the
   course book. Chart-cached values verified equal to recomputation.

3. **Prompt creator.** All three behaviors reproduced, then fixed: per-task
   draft snapshots (selection state, wording edits, and hand-edited output
   survive task switching, with an explicit rebuild/keep bar), unresolved
   bracket/curly placeholders now block "ready" status with a count and an
   example, and copy falls back to select-and-copy with an honest notice when
   the clipboard API is unavailable. Evidence: 12/12 scripted-browser checks,
   including a forced clipboard-API failure and a legacy-view regression check.

4. **Configurator parity.** The Tasks sheet assembles the same blocks, order,
   and wording as the browser builder (task line → Requirements → Also → How I
   will check the result), including the builder's whitespace-trim semantics.
   Evidence: recalculation-verified identical output for all five task
   families, repeated with a second independent selection set including edited
   wording. A clipped copy-ready prompt row your ask surfaced now auto-sizes
   to its text; every formula recalculates with zero errors.

5. **Dashboard scope.** Resolved toward the exercise's promise: chart
   drill-down now applies the actual supplier/site filter, so tiles, trend,
   ranking, and table re-scope together and the active-selection line explains
   the state and how to clear it. Evidence: 14/14 scripted-browser checks —
   the taught filtered check reproduced via the controls, drill agreement
   across all views, reset, empty-vs-zero distinction, the missing value
   rendering blank, and sums-based (never averaged) rate math.

6. **Order and teaching details.** The live sequence now follows the five-task
   arc (analyze → dashboard → present → email → explain); on-slide page
   numbers, bridges, appendix cross-references, and the facilitation plan
   (rows, protected list, recomputed clock — totals unchanged) all updated,
   and a stale bridge was retired. The Copilot exercise now states exactly
   where the custom prompt runs after the built-in summary, with the
   supplied-text fallback primary and the license-availability caveat. The
   inventory comprehension key now includes the formula component it omitted;
   the other two plain-language keys were checked against their sources and
   passed unchanged.

7. **Visual repairs.** The two flagged slides' teaching text enlarged into
   available space; the field-guide subtitle re-measured to fit; the two
   sparse continuation pages absorbed by removing orphaning page breaks; the
   cheat-sheet footer collision fixed with a measured gap. All re-rendered and
   inspected at reading size.

8. **Package completed and reconciled.** New extended course document — 55
   pages, 7 chapters — generated from a structured content source alongside
   the other regenerable artifacts. Package-wide consistency sweep: the
   requirements catalog moved under references/ so every stated path in the
   book, workbook index, and package indexes resolves; a legacy workbook tab's
   metric definition was brought in line with the package's separate-measures
   rule; the variant email thread's archived answer key is now labeled as the
   variant. Every affected generated artifact regenerated.

## Verification summary

Six independent adversarial verifiers swept the finished pass: dataset canon
recomputed from the source records; all 101 deck slides' text, tables, and
notes checked; workbook and dashboard embedded data diffed cell-by-cell
against the source; all four PDFs text-audited; tool behavior re-run; and a
coverage audit against your iteration-01 instruction. That sweep's findings
are what commit `50c729e` fixes.

## Accepted deviations (reported, not changed)

- Part-divider slides and the detail-appendix pages display stylized or
  preserved titles while the facilitation plan uses semantic titles — a
  deliberate baseline convention.
- The appendix divider carries no page number — baseline divider design.
- Build sources and the legacy prompt library sit beside the package root by
  design; the indexes describe this accurately.

Stopping per protocol.

— Rocksteady
