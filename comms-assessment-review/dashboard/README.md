# Browser-reader dashboard (prototype)

`dashboard.html` is the self-contained field-mode dashboard from
TOOL_BLUEPRINT.md §1: open it in any browser, click **Load workbook** (or drag
the .xlsx onto it), and it renders the readout from the workbook's own cached
formula results. Nothing is uploaded anywhere. **Export snapshot** produces a
dated read-only copy with the data baked in, for emailing/SharePoint.

- `dashboard_shell.html` — the source page. `dashboard.html` is this file with
  SheetJS (xlsx-0.20.3, Apache-2.0, from cdn.sheetjs.com) spliced in at the
  `/*__SHEETJS__*/` marker.
- Rebuild: fetch `xlsx.full.min.js` and run
  `python3 -c "lib=open('xlsx.full.min.js').read(); s=open('dashboard_shell.html').read(); open('dashboard.html','w').write(s.replace('/*__SHEETJS__*/',lib))"`
- `test_dashboard.js` — Playwright end-to-end suite (32 checks): loads the real
  workbook AND a LibreOffice-rewritten copy, asserts every planted-story number
  (60% coverage, 6 defects, Gandalf→Frodo at 15, R9 double theater, …), tests
  the goal filter, the snapshot export/reload round trip, and dark mode.

Reads sheets by header name (not cell addresses), so it survives row growth.
Already understands an optional `goal_class` column on Goals (core /
aspirational badges + banding) for the v2 workbook.
