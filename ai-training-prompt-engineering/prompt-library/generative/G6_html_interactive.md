# G6 · Interactive HTML (dashboards, calculators, trackers)

**Type:** Generative · **Version:** 1.0 · **Use when:** the deliverable should be *used*, not read — filter, sort, what-if, self-serve lookup. One self-contained HTML file beats a deck or spreadsheet when the audience will explore.
**Works in:** Claude (Artifacts — interactive HTML/React in-chat), ChatGPT (Canvas), Gemini (Canvas), Copilot Pages; any tool that outputs an .html file you can open in a browser.

> **When HTML wins:** the reader asks their own questions (filter by site, change an
> assumption, look up a code). **When it loses:** formal records, print, regulated
> documents — those stay xlsx/pptx/pdf.

---

## Template A — Interactive dashboard from data

```text
<task>
Build a single-file interactive HTML dashboard: {{one line — for whom and what question it answers}}.
</task>

<data>
{{paste the table or attach the file}} — one row = {{grain}}. Columns: {{exact names + meaning + units}}.
Embed the data IN the file (no external calls, no server); it must work opened from disk,
offline, on a work laptop.
</data>

<views>
1. Headline row: {{3-4 KPI tiles — metric, current value, vs target, trend arrow}}.
2. Main chart: {{type, x, y, series}} — filterable by {{site | period | category}}.
3. Table view: sortable, searchable, with {{n}} visible; export-to-CSV button.
[optional] 4. Detail drill-down when a bar/row is clicked.
</views>

<design>
Clean and legible: readable fonts, units on axes, target lines where targets exist,
color-blind-safe palette, {{our colors: {{...}}}}. Mobile-tolerant. No login, no tracking.
State the as-of date and data source visibly in the footer.
</design>

<rules>
All numbers computed from the embedded data — no hard-coded results I can't trace.
If a value can't be computed from the data, show "—", never a guess.
</rules>
```

## Template B — Calculator / what-if tool

```text
Build a single-file HTML calculator for {{decision — e.g., "volume/pricing scenarios"}}.
Inputs (sliders/fields with sensible ranges and defaults): {{list, with units and defaults}}.
Logic: {{the formulas, exactly — or "derive from the attached sheet and SHOW me the formulas
you extracted for my confirmation before finishing"}}.
Outputs: {{the result numbers + one chart updating live}}.
Show the formula used, on screen, so users can audit it. Handle divide-by-zero and blank
inputs gracefully. Works offline from a single file.
```

## Template C — Team tracker / lookup

```text
Build a single-file HTML {{tracker | reference}} for {{e.g., "our defect-code atlas"}}:
searchable, filterable by {{fields}}, printable. Data embedded from the attached {{csv}}.
Include a "last updated {{date}} — owner {{name}}" banner. If data changes {{weekly}},
make regeneration easy: keep data in one clearly-marked block I can re-paste.
```

---

## What makes this work
- **"Single file, offline, no external calls"** — the constraint that makes the artifact shareable on a locked-down corporate laptop (email it, drop it on SharePoint; it just opens).
- **Exact columns + grain**, same as any data prompt: the dashboard is only as honest as its schema.
- **"Show the formula on screen"** turns a black-box calculator into an auditable tool colleagues will actually trust.
- **KPI-tiles + chart + table** is the layout that satisfies both the skimmer and the digger.

## Pitfalls
- Confidential data is *embedded in the file* — classify and share it like the spreadsheet it came from.
- In-chat "publish/share" buttons create **public links** (and some canvas-style shared apps use a public database). A share link is publication: for internal data, download the file and share it through normal channels instead.
- Nobody maintains it: name an owner and an update cadence in the banner, or it becomes stale-but-credible.
- Over-scoping: a dashboard with 12 views is a website project. 1 headline row + 1-2 views is the sweet spot per file.
- Assuming it updates itself — it's a snapshot. For live data you need a real BI tool (Tableau/Power BI), not an HTML file.
