# Advanced Tissue Models part qualification

Review package dated 17 September 2026. Owner: Oscar Penny.

## Deliverables

- `deliverables/ATM_Qualification_Process_Maps_v4.pptx`: nine slides with editable current-state, future-state, training and recovery maps; original map screenshots retained for comparison.
- `deliverables/ATM_Tissue_Supplier_Training_Procedure_v2.docx`: generic tissue training procedure, process maps, tissue-family approval record and evidence/release checklist.
- `source/ATM_Tissue_Supplier_Training_Procedure_v2.md`: editable text for review and search.

These are completed review copies, not released controlled procedures. Unassigned document identifiers and approval fields remain explicit.

## Oscar's latest decisions

1. Personnel certification: at least 30 inspected units across at least two consecutive harvest days, at least 95% first-pass yield.
2. Tissue qualification lots: each must reach at least 95%. Recurring yield below 95% triggers the incoming quality control inspector to shadow-train the harvesting technician and inspect output. No lower family threshold.
3. Only certified personnel or defined monitoring controls permit routine in-scope work; otherwise use a written Quality-approved deviation with scope, expiration, inspection and exit controls.
4. All existing documents remain separate, including 668008 and 668009.

Supplier Engineering owns the procedure, Quality approves, and the Design Engineer owns the technical acceptance standard. Incoming product inspection remains independent.

## Review handoff for Claude Code

Review the procedure and maps together. Preserve the four decisions above and original document identifiers. Return proposed changes with their reasons before implementing substantive process changes; Oscar gives the final word.

Check the logic between supplier approval, individual certification and component qualification. Challenge ambiguous monitoring evidence, requalification triggers and role boundaries. Keep passing yield distinct from release of individual conforming units.

Do not invent the following unresolved values: qualification-lot count and lot/inspection definition; numeric recurrence count and window; inspector agreement criteria and reference-set design; monitoring attempt limit; inactivity interval; receipt-yield investigation trigger. Confirm the pelvic acceptance specification, controlled revisions, attribution implementation, records repository, retention and filing ownership. Confirm applicability of corporate material references. Three cropped notes in original Map B remain unavailable.

The procedure's operational details beyond Oscar's explicit decisions are proposed implementation controls requiring stakeholder approval. Examples include a fresh unassisted window after coached retraining, Quality authorization for return to routine work, and the proposed inspector assessment method.

## Source traceability and changes

Original inputs are under `reference/`. They are historical and retain their original unresolved proposals. The current procedure supersedes the handoff's proposed 40-unit floor and possible lower tissue-family thresholds. It also resolves the proposal to merge 668009 into 668008 by retaining both.

Original draft coverage: purpose/scope generalized; references retained with uncertain specification identifiers flagged; definitions corrected; ownership reassigned to Supplier Engineering; Design Engineer standard ownership explicit; training, monitoring, certification, ongoing feedback and records rewritten; broken return-to-training reference repaired through Section 7; generic process maps replace the pelvic-only sequence; inspector and lot criteria remain approval fields.

## Editing and regeneration

The PowerPoint contains native editable shapes, text and connectors. Word text and tables are editable; its two map images have editable counterparts in PowerPoint and generation source.

`source/build_maps.mjs` uses the OpenAI artifact-tool presentation runtime and the presentation skill finalizer. Run it from a `build/` directory under the project, with the managed runtime dependencies and environment variables described in its skill. It expects `reference/` and writes `deliverables/`. Use a new output/receipt filename for each run.

`source/build_procedure.py` uses python-docx. Run from `build/` after map generation; it expects the map images in `build/` and writes the Word document and Markdown source. In another environment, edit the native deliverables directly or adapt generation dependencies without changing the approved logic. Retain original input files.
