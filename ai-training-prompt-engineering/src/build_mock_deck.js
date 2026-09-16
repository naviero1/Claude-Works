// Supplier_Quality_Mock_Presentation.pptx — the prepared output for exercise 3.
// A fictional five-slide management deck built ONLY from the verified supplier
// analysis (notes/design/round17_sequence.md). Distinct navy look so it never
// reads as part of the course deck. All numbers recomputed from the workbook.
const pptxgen = require('pptxgenjs');
const path = require('path');

const NAVY = '1E2761', ICE = 'CADCFC', INK = '232A31', SLATE = '46545F', MUTE = '7A8790',
      WHITE = 'FFFFFF', PANEL = 'F2F4F8', RED = 'AF3230';
const MONTHS = ['2025-09','2025-10','2025-11','2025-12','2026-01','2026-02','2026-03','2026-04','2026-05','2026-06','2026-07','2026-08'];
const BRAVO_TREND = [0.343,0.329,0.176,0.245,0.462,0.456,0.208,0.737,0.469,0.140,0.145,0.465];

const p = new pptxgen();
p.layout = 'LAYOUT_WIDE';

function footer(s, n) {
  s.addText('Fictional training data · verified against Course_Workbook.xlsx (144 detail rows) · period 2025-09 to 2026-08', {
    x: 0.55, y: 7.08, w: 10.5, h: 0.3, fontFace: 'Calibri', fontSize: 9.5, color: MUTE, isTextBox: true, margin: 0 });
  s.addText(String(n), { x: 12.5, y: 7.08, w: 0.5, h: 0.3, fontFace: 'Calibri', fontSize: 9.5, color: MUTE, align: 'right', isTextBox: true, margin: 0 });
}

// ---- 1 · question & scope (dark title slide)
let s = p.addSlide();
s.background = { color: NAVY };
s.addText('Should we investigate a supplier?', { x: 0.8, y: 2.0, w: 11.7, h: 1.0, fontFace: 'Cambria', fontSize: 40, bold: true, color: WHITE, isTextBox: true, margin: 0 });
s.addText('Which supplier has the highest return rate, and what should we investigate next?', {
  x: 0.8, y: 3.1, w: 11.0, h: 0.5, fontFace: 'Calibri', fontSize: 20, color: ICE, isTextBox: true, margin: 0 });
s.addText([
  { text: 'Scope — ', options: { bold: true, color: ICE } },
  { text: '12 months (2025-09 to 2026-08) · 4 receiving sites · 3 suppliers · 144 delivery records. ', options: { color: 'E8EEF9' } },
  { text: 'Return rate = total units returned ÷ total units shipped, same scope for every comparison. ', options: { color: 'E8EEF9' } },
  { text: 'Decision this deck supports: is a supplier follow-up warranted?', options: { bold: true, color: WHITE } },
], { x: 0.8, y: 4.1, w: 11.0, h: 1.2, fontFace: 'Calibri', fontSize: 14, isTextBox: true, margin: 0, lineSpacingMultiple: 1.15 });
s.addText('Fictional training data · verified against Course_Workbook.xlsx · period 2025-09 to 2026-08', {
  x: 0.8, y: 7.05, w: 10.5, h: 0.3, fontFace: 'Calibri', fontSize: 9.5, color: '9FB2D8', isTextBox: true, margin: 0 });
s.addNotes('PURPOSE: frame the decision, not the data.\nTALKING POINTS: one question, one period, one definition — every number later in the deck uses this same scope. The decision is only whether follow-up is warranted; this deck does not claim a cause.\nTRANSITION: "First, the comparison."');

// ---- 2 · supplier comparison (bar)
s = p.addSlide();
s.background = { color: WHITE };
s.addText('Bravo Plastics returns at almost 3× the rate of either other supplier', {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
s.addChart(p.ChartType.bar, [{
  name: 'Return rate (%)',
  labels: ['Alpha Components', 'Cardinal Metals', 'Bravo Plastics'],
  values: [0.099, 0.129, 0.349],
}], {
  x: 0.7, y: 1.45, w: 7.4, h: 4.9, barDir: 'bar',
  chartColors: [NAVY], showLegend: false, showTitle: false,
  showValue: true, dataLabelPosition: 'outEnd', dataLabelFormatCode: '0.000"%"', dataLabelFontSize: 12, dataLabelColor: INK,
  valAxisLabelFormatCode: '0.00"%"', valAxisLabelFontSize: 10, valAxisLabelColor: SLATE,
  catAxisLabelFontSize: 12, catAxisLabelColor: INK,
  valGridLine: { color: 'DCE3E6', size: 0.5 }, catGridLine: { style: 'none' },
});
s.addShape('roundRect', { x: 8.5, y: 1.45, w: 4.25, h: 3.3, rectRadius: 0.08, fill: { color: PANEL }, line: { type: 'none' } });
s.addText([
  { text: 'The numbers\n', options: { bold: true, fontSize: 14, color: NAVY } },
  { text: 'Bravo Plastics — 262 returns / 75,184 shipped = 0.349%\n', options: { fontSize: 12.5, color: INK } },
  { text: 'Cardinal Metals — 96 / 74,658 = 0.129%\n', options: { fontSize: 12.5, color: SLATE } },
  { text: 'Alpha Components — 74 / 75,060 = 0.099%\n\n', options: { fontSize: 12.5, color: SLATE } },
  { text: 'All rates are totals ÷ totals over the same 12 months and 4 sites — never an average of monthly percentages.', options: { fontSize: 11.5, italic: true, color: SLATE } },
], { x: 8.75, y: 1.65, w: 3.8, h: 3.0, fontFace: 'Calibri', isTextBox: true, margin: 0, lineSpacingMultiple: 1.1 });
s.addText('Shipment volumes are nearly equal (75.1k / 74.7k / 75.1k units), so the rate gap is not a volume artifact.', {
  x: 8.5, y: 5.0, w: 4.25, h: 0.9, fontFace: 'Calibri', fontSize: 12, color: SLATE, isTextBox: true, margin: 0 });
footer(s, 2);
s.addNotes('PURPOSE: the comparison, on one honest scale.\nTALKING POINTS: same scope for all three; totals over totals; near-equal volumes make the comparison fair. 432 total returns on 224,902 units (0.192% overall).\nTRANSITION: "Is this recent, or persistent? The trend."');

// ---- 3 · the trend (line)
s = p.addSlide();
s.background = { color: WHITE };
s.addText('Bravo’s return rate is elevated and volatile — no sign of steady improvement', {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
s.addChart(p.ChartType.line, [{
  name: 'Bravo Plastics monthly return rate (%)', labels: MONTHS, values: BRAVO_TREND,
}], {
  x: 0.7, y: 1.5, w: 8.3, h: 4.8,
  chartColors: [NAVY], lineSize: 2.5, lineSmooth: false, showLegend: false, showTitle: false,
  valAxisLabelFormatCode: '0.0"%"', valAxisLabelFontSize: 10, valAxisLabelColor: SLATE, valAxisMinVal: 0,
  catAxisLabelFontSize: 9, catAxisLabelColor: SLATE, catAxisLabelRotate: 45,
  valGridLine: { color: 'DCE3E6', size: 0.5 }, catGridLine: { style: 'none' },
});
s.addShape('roundRect', { x: 9.3, y: 1.5, w: 3.45, h: 4.8, rectRadius: 0.08, fill: { color: PANEL }, line: { type: 'none' } });
s.addText([
  { text: 'How to read it\n', options: { bold: true, fontSize: 14, color: NAVY } },
  { text: 'Peak: 0.737% in April 2026 — about 7× Alpha’s full-year rate.\n\n', options: { fontSize: 12.5, color: INK } },
  { text: 'Quiet months exist (Jun–Jul 2026 near 0.14%), but the rate returns to elevated levels — most recently 0.465% in August.\n\n', options: { fontSize: 12.5, color: SLATE } },
  { text: 'Monthly rates use that month’s own shipments as the denominator; small months move more.', options: { fontSize: 11.5, italic: true, color: SLATE } },
], { x: 9.55, y: 1.7, w: 3.0, h: 4.4, fontFace: 'Calibri', isTextBox: true, margin: 0, lineSpacingMultiple: 1.1 });
footer(s, 3);
s.addNotes('PURPOSE: the pattern over time, honestly framed.\nTALKING POINTS: volatile, not trending down; the April peak and the August level both sit far above the other suppliers’ full-year rates. Do NOT claim seasonality or cause from 12 points.\nTRANSITION: "What we propose to do about it."');

// ---- 4 · recommendation (clearly separated from findings)
s = p.addSlide();
s.background = { color: WHITE };
s.addText('Proposed follow-up: a focused quality review with Bravo Plastics', {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
s.addShape('roundRect', { x: 0.55, y: 1.45, w: 6.0, h: 4.9, rectRadius: 0.08, fill: { color: PANEL }, line: { type: 'none' } });
s.addText([
  { text: 'WHAT THE DATA SHOW (findings)\n', options: { bold: true, fontSize: 13, color: NAVY } },
  { text: '• Bravo’s return rate (0.349%) is ~2.7× Cardinal’s and ~3.5× Alpha’s over the same 12 months and sites.\n', options: { fontSize: 13, color: INK, lineSpacingMultiple: 1.15 } },
  { text: '• The gap persists across the year and peaks in April 2026.\n', options: { fontSize: 13, color: INK, lineSpacingMultiple: 1.15 } },
  { text: '• Bravo also drives 1,157 of 2,207 inspection defect occurrences — a separate measure, reported separately.\n', options: { fontSize: 13, color: INK, lineSpacingMultiple: 1.15 } },
], { x: 0.85, y: 1.65, w: 5.4, h: 4.5, fontFace: 'Calibri', isTextBox: true, margin: 0, valign: 'top' });
s.addShape('roundRect', { x: 6.85, y: 1.45, w: 5.9, h: 4.9, rectRadius: 0.08, fill: { color: NAVY }, line: { type: 'none' } });
s.addText([
  { text: 'WHAT WE RECOMMEND (judgment)\n', options: { bold: true, fontSize: 13, color: ICE } },
  { text: '1. Ask Bravo for a returns root-cause review on the highest-return months (Jan–Feb, Apr–May, Aug 2026).\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.15 } },
  { text: '2. Pull the return records behind those months for shared inspection.\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.15 } },
  { text: '3. Agree a target return rate and re-measure next quarter on the same definition.\n\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.15 } },
  { text: 'The data show an association, not a cause — the review is how we find the cause.', options: { fontSize: 12, italic: true, color: ICE } },
], { x: 7.15, y: 1.65, w: 5.3, h: 4.5, fontFace: 'Calibri', isTextBox: true, margin: 0, valign: 'top' });
footer(s, 4);
s.addNotes('PURPOSE: keep findings and judgment visibly separate.\nTALKING POINTS: left panel is what the workbook supports; right panel is our proposal. No cost claims, no committed savings — nothing here the data cannot back.\nTRANSITION: "What this analysis cannot tell you."');

// ---- 5 · limitations & next steps
s = p.addSlide();
s.background = { color: WHITE };
s.addText('Limits of this analysis — and the next checkpoints', {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
const lim = [
  ['Descriptive, not causal', 'The comparison ranks suppliers; it does not explain the difference. Causes come from the proposed review, not this dataset.'],
  ['No delivery counts', 'On-time percentages exist per month, but delivery counts do not — so no true overall delivery rate is claimed anywhere in this deck.'],
  ['One missing value', 'One inspection-hours record is missing (missing ≠ zero). It does not affect the return-rate figures.'],
  ['Two separate measures', 'Inspection defects (caught internally) and customer returns (escaped) are never added together.'],
];
lim.forEach((t, i) => {
  const y = 1.45 + i * 1.02;
  s.addShape('roundRect', { x: 0.55, y, w: 7.6, h: 0.9, rectRadius: 0.06, fill: { color: PANEL }, line: { type: 'none' } });
  s.addText([
    { text: t[0] + '  —  ', options: { bold: true, color: NAVY, fontSize: 13 } },
    { text: t[1], options: { color: SLATE, fontSize: 12 } },
  ], { x: 0.8, y: y + 0.07, w: 7.15, h: 0.78, fontFace: 'Calibri', isTextBox: true, margin: 0, valign: 'middle', lineSpacingMultiple: 1.05 });
});
s.addShape('roundRect', { x: 8.4, y: 1.45, w: 4.35, h: 4.0, rectRadius: 0.08, fill: { color: NAVY }, line: { type: 'none' } });
s.addText([
  { text: 'NEXT STEPS\n', options: { bold: true, fontSize: 13, color: ICE } },
  { text: '• Decision today: approve the Bravo review\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.2 } },
  { text: '• Owner + date for the root-cause session\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.2 } },
  { text: '• Re-run this analysis next quarter, same definitions, same scope\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.2 } },
], { x: 8.7, y: 1.7, w: 3.8, h: 3.6, fontFace: 'Calibri', isTextBox: true, margin: 0, valign: 'top' });
footer(s, 5);
s.addNotes('PURPOSE: earn trust by naming what the analysis cannot say.\nTALKING POINTS: every limitation is also an instruction for the next analysis. End on the single decision requested.\nTRANSITION: none — invite the decision.');

const out = path.join(__dirname, '..', 'deliverables', 'exercise-data', 'Supplier_Quality_Mock_Presentation.pptx');
p.writeFile({ fileName: out }).then(() => console.log('mock deck written:', out));
