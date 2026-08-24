# Dashboard Evaluation — What's Missing

Five independent evaluation lenses (method coverage, analyst workflow,
executive pitch, engineering robustness, model fidelity) read the dashboard
source, the rendered views, and the framework's own documentation; every
claimed gap was then adversarially verified against the actual code. 41
candidates → 33 confirmed, organized below by what they mean, with the
verified fix location. Date: 2026-08-24.

## A · The framework's own promises the tool doesn't render yet
*(all verified small, all in this HTML file)*

1. **WhiteSpace matrix** — the third canonical view ("where do hand-offs break
   *between functions*?") doesn't exist. The map has every ingredient
   (edges + actor functions); group them into the Rummler function×function
   grid with "n req · n ok · n DEFECT" cells.
2. **SPOF findings list** — the manual's reading order step 4 dead-ends at a
   map badge. Needed: the at-risk *flows* themselves (topic, producer →
   consumer, criticality, carriers, and the mitigation line "no
   system-of-record carrier — publish to a durable channel").
3. **Channels are invisible** — the Channels sheet is never parsed. No venue
   inventory, no persistence/synchrony surface, no "does any system of record
   back this goal?" check — so the standard SPOF fix has no ground to point at.
4. **Extra (unrequired) flows** — only a "+n" footnote. The waste/undocumented-
   value conversation (interview Q8's harvest) needs the actual list: sender →
   receiver, topic, carrier, evidence; plus the manual's promised light-dotted
   map edges.
5. **Consolidation candidates** — the reading order's final step: NVA meetings
   with zero cargo, cost-sorted, with the "cut as an experiment: skip two
   occurrences" framing.
6. **GoalLens parity in Decompose** — the verdict *sentence* ("in words"), the
   goal's affected-stakeholder list (⚠ marks), and stakeholder-presence % on
   meeting lines (parsed but currently dropped).

## B · The pitch to B — findings never become a decision
*(the Time-Talent-Energy argument the course names as "what wins your pitch")*

7. **Minutes never become money.** No total meeting cost headline, no
   NVA/recoverable-cost figure, meetings not even sorted by cost. Fix: an 8th
   KPI (total person-hours/week, annualized), a "recoverable" line (cost of
   NVA meetings), cost-sorted meetings with a total row. Loaded-rate € stays a
   user-entered number, never hardcoded.
8. **No executive Readout view** — the snapshot B opens lands on an analyst
   instrument. Build a sixth view (default when booting from a snapshot):
   what we found per goal (verdict sentences), what it costs, the survey
   symptoms it explains, and —
9. **No recommended-actions list** — the method's fixes-by-defect-type exists
   per flow but is never aggregated into "what we recommend": cut experiments
   with savings, carrier fixes, decision one-liners.
10. **Survey symptoms have no home** — B's trigger was the employee survey;
    a "you told us → we found" strip needs a small optional Symptoms sheet
    (workbook generators first).

## C · Honesty fixes — places the tool currently overclaims
*(small; mostly copy — do these first, they cost credibility every day they stand)*

11. **VA tooltip describes the carries-based test; the cached verdict is
    claims-based.** Say what's true today ("claims a goal — note: claims, not
    carries; see theater") until the workbook's t3 fix lands.
12. **"SPOF" badge on a person from a flow-level single-path flag** — the
    workbook computes single-delivery-path, not sole-producer. Re-badge as
    "fragile ×n" (or disclose the predicate in the tooltip) until v2 unifies.
13. **"aligned" decision chip for channel/ad_hoc venues where no
    owner-presence check ran** — render "not checked" instead.
14. **"covered" hides the one-side-only caveat** — soften the tooltip now;
    implement the claimed-only flag in the workbook later (already a §4.4
    dictionary decision).
15. **People ranking reads as centrality** — copy fix: "how much the goals
    depend on this person — not a network-science measure; the pipeline's ONA
    only ever corroborates."
16. **Footer honesty line** — distinguish cached workbook verdicts from the
    dashboard's own aggregations (isolated badge, per-person sums, min/topic).

## D · Robustness
*(small, this HTML)*

17. Missing/renamed sheets currently render a healthy-looking empty dashboard
    — add a required-sheet manifest check with a loud banner.
18. Unknown verdict tokens fall through to green chips / invisible map edges —
    add an explicit neutral "unknown" branch to every chip/edge renderer.
19. Reload contract: drop/input loads leave a stale Chromium file handle —
    one reset point in parseArrayBuffer; also rebuild both filter dropdowns
    on every load (today they keep the first file's goals/actors).
20. Provenance: show "saved ⟨file date⟩ · read ⟨date⟩" (File.lastModified),
    name snapshots by data date; staleness insurance note in help.
21. Same-(from,to) flows draw on identical map paths — only the topmost is
    hoverable; fan or bundle pair edges.
22. Print stylesheet — per-goal handout and map printing (Decompose printed
    is already the one-page-per-topic readout).
23. Data-health panel: add referential-integrity check (dangling IDs), jump
    links, and an explicit all-green "dashboard-ready" state (the blueprint's
    own gate).
24. Accessibility (scoped): tooltips on keyboard focus; visible-text fallback
    for tooltip-only definitions; map remains mouse-first with a table
    equivalent (People/defects tables already are one).

## E · Deferred deliberately (post-pilot or upstream first)

- **Baseline comparison** (the sustain phase's "visible dividend"): build when
  the first re-audit is scheduled. The snapshot's embedded JSON is already the
  perfect baseline artifact — "Load baseline snapshot" → deltas.
- **Findings triage state** (reviewed/actioned/dismissed): belongs in the
  workbook (a Findings-log sheet), not browser storage.
- **Overload verdict**: cache it in the workbook first (one-place computation,
  per the dictionary), then badge it here. Until then the tool honestly shows
  raw minutes only.
- **Catchball sign-off visibility**: needs the blueprint's sign-off column in
  the generators first; then Decompose shows signed/pending per need.
- **Search**: native find-in-page suffices at pilot scale; typeahead is a v3
  app feature.

## Recommended build waves

- **Wave 1 (honesty + safety, hours):** C11–C16, D17–D19 — nothing new, just
  stop overclaiming and fail loudly.
- **Wave 2 (complete the method, ~a day):** A1–A6 — WhiteSpace matrix, SPOF
  list, Channels table, extra-flows table, consolidation candidates, GoalLens
  parity.
- **Wave 3 (the pitch, ~a day):** B7–B9 — money KPIs, Readout view,
  recommended actions. CSV export of findings rides along.
- **Wave 4 (polish):** D20–D24.
- **Upstream queue (generators):** overload flag, sign-off column, Symptoms
  sheet, claimed-only flag, t3 carries fix, SPOF predicate unification — all
  already tracked in MODEL_DICTIONARY.md / TOOL_BLUEPRINT.md.
