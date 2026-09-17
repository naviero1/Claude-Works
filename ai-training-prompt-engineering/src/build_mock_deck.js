// Supplier_Quality_Mock_Presentation.pptx — the prepared output for exercise 3.
// A fictional five-slide management deck. Distinct navy look so it never reads
// as part of the course deck. Every displayed number and chart value is COMPUTED
// HERE from references/exercise-data/Supplier_Data_Clean.csv at build time —
// one shared calculation, full precision retained until display formatting.
const pptxgen = require('pptxgenjs');
const path = require('path');
const fs = require('fs');

// ---- shared calculation (the only source of every number on the slides) ----
const csvPath = path.join(__dirname, '..', 'references', 'exercise-data', 'Supplier_Data_Clean.csv');
const lines = fs.readFileSync(csvPath, 'utf8').trim().split('\n');
const header = lines[0].split(',');
const col = (name) => header.indexOf(name);
const rows = lines.slice(1).map((l) => l.split(','));
if (rows.length !== 144) throw new Error(`expected 144 detail rows, got ${rows.length}`);

const sup = {}; // name -> {units, returns, defects}
const bravoMonth = {}; // month -> {units, returns}
let blanks = 0;
for (const r of rows) {
  const s = r[col('Supplier')];
  const u = Number(r[col('Units_Shipped')]);
  const ret = Number(r[col('Units_Returned')]);
  const d = Number(r[col('Defects_Found')]);
  if (r[col('Inspection_Hours')] === '') blanks += 1;
  const a = (sup[s] ||= { units: 0, returns: 0, defects: 0 });
  a.units += u; a.returns += ret; a.defects += d;
  if (s === 'Bravo Plastics') {
    const m = (bravoMonth[r[col('Month')]] ||= { units: 0, returns: 0 });
    m.units += u; m.returns += ret;
  }
}
const names = Object.keys(sup);
if (names.length !== 3) throw new Error(`expected 3 suppliers, got ${names.length}`);
if (blanks !== 1) throw new Error(`expected exactly 1 blank Inspection_Hours, got ${blanks}`);
const MONTHS = Object.keys(bravoMonth).sort();
if (MONTHS.length !== 12) throw new Error(`expected 12 months, got ${MONTHS.length}`);

const rate = (s) => sup[s].returns / sup[s].units; // fraction, full precision
const ranked = names.slice().sort((a, b) => rate(b) - rate(a)); // highest first
const [hi, mid, lo] = ranked; // Bravo, Cardinal, Alpha (derived, not assumed)
const totU = names.reduce((t, s) => t + sup[s].units, 0);
const totR = names.reduce((t, s) => t + sup[s].returns, 0);
const totD = names.reduce((t, s) => t + sup[s].defects, 0);

const TREND = MONTHS.map((m) => bravoMonth[m].returns / bravoMonth[m].units * 100);
const peakIdx = TREND.indexOf(Math.max(...TREND));
const lastIdx = MONTHS.length - 1;
const quiet = TREND.map((v, i) => [v, i]).sort((a, b) => a[0] - b[0]).slice(0, 2)
  .map(([, i]) => i).sort((a, b) => a - b);

// display formatting (full precision above, formatting only here)
const pct3 = (f) => `${(f * 100).toFixed(3)}%`;
const pct1 = (f) => `${(f * 100).toFixed(1)}%`;
const x1 = (r) => `${r.toFixed(1)}×`;
const num = (n) => n.toLocaleString('en-US');
const kk = (n) => `${(n / 1000).toFixed(1)}k`;
const MONTH_NAMES = { '01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December' };
const monthName = (m) => `${MONTH_NAMES[m.slice(5)]} ${m.slice(0, 4)}`;
const monthShort = (m) => MONTH_NAMES[m.slice(5)].slice(0, 3);

const rHiMid = rate(hi) / rate(mid);
const rHiLo = rate(hi) / rate(lo);
const peakVsLoYear = (TREND[peakIdx] / 100) / rate(lo);

const NAVY = '1E2761', ICE = 'CADCFC', INK = '232A31', SLATE = '46545F', MUTE = '7A8790',
      WHITE = 'FFFFFF', PANEL = 'F2F4F8', RED = 'AF3230';

const poss = (n) => n.endsWith('s') ? n + '’' : n + '’s';
const p = new pptxgen();
p.layout = 'LAYOUT_WIDE';

function footer(s, n) {
  s.addText(`Fictional training data · computed from Supplier_Data_Clean.csv (${rows.length} detail rows) · period ${MONTHS[0]} to ${MONTHS[lastIdx]}`, {
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
  { text: `12 months (${MONTHS[0]} to ${MONTHS[lastIdx]}) · 4 receiving sites · 3 suppliers · ${rows.length} delivery records. `, options: { color: 'E8EEF9' } },
  { text: 'Return rate = total units returned ÷ total units shipped, same scope for every comparison. ', options: { color: 'E8EEF9' } },
  { text: 'Decision this deck supports: is a supplier follow-up warranted?', options: { bold: true, color: WHITE } },
], { x: 0.8, y: 4.1, w: 11.0, h: 1.2, fontFace: 'Calibri', fontSize: 14, isTextBox: true, margin: 0, lineSpacingMultiple: 1.15 });
s.addText(`Fictional training data · computed from Supplier_Data_Clean.csv · period ${MONTHS[0]} to ${MONTHS[lastIdx]}`, {
  x: 0.8, y: 7.05, w: 10.5, h: 0.3, fontFace: 'Calibri', fontSize: 9.5, color: '9FB2D8', isTextBox: true, margin: 0 });
s.addNotes('PURPOSE: frame the decision, not the data.\nTALKING POINTS: one question, one period, one definition — every number later in the deck uses this same scope. The decision is only whether follow-up is warranted; this deck does not claim a cause.\nTRANSITION: "First, the comparison."');

// ---- 2 · supplier comparison (bar)
s = p.addSlide();
s.background = { color: WHITE };
s.addText(`${hi} returns at ${x1(rHiMid)} the next supplier's rate — and ${x1(rHiLo)} the lowest`, {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
s.addChart(p.ChartType.bar, [{
  name: 'Return rate (%)',
  labels: [lo, mid, hi], // ascending so the largest renders on top
  values: [rate(lo) * 100, rate(mid) * 100, rate(hi) * 100], // full precision; label format rounds
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
  { text: `${hi} — ${num(sup[hi].returns)} returns / ${num(sup[hi].units)} shipped = ${pct3(rate(hi))}\n`, options: { fontSize: 12.5, color: INK } },
  { text: `${mid} — ${num(sup[mid].returns)} / ${num(sup[mid].units)} = ${pct3(rate(mid))}\n`, options: { fontSize: 12.5, color: SLATE } },
  { text: `${lo} — ${num(sup[lo].returns)} / ${num(sup[lo].units)} = ${pct3(rate(lo))}\n\n`, options: { fontSize: 12.5, color: SLATE } },
  { text: 'All rates are totals ÷ totals over the same 12 months and 4 sites — never an average of monthly percentages.', options: { fontSize: 11.5, italic: true, color: SLATE } },
], { x: 8.75, y: 1.65, w: 3.8, h: 3.0, fontFace: 'Calibri', isTextBox: true, margin: 0, lineSpacingMultiple: 1.1 });
s.addText(`Shipment volumes are nearly equal (${kk(sup[lo].units)} / ${kk(sup[mid].units)} / ${kk(sup[hi].units)} units), so the rate gap is not a volume artifact.`, {
  x: 8.5, y: 5.0, w: 4.25, h: 0.9, fontFace: 'Calibri', fontSize: 12, color: SLATE, isTextBox: true, margin: 0 });
footer(s, 2);
s.addNotes(`PURPOSE: the comparison, on one honest scale.\nTALKING POINTS: same scope for all three; totals over totals; near-equal volumes make the comparison fair. ${num(totR)} total returns on ${num(totU)} units (${pct3(totR / totU)} overall). The headline ratios: ${x1(rHiMid)} ${mid}, ${x1(rHiLo)} ${lo} — computed from the full-period rates.\nTRANSITION: "Is this recent, or persistent? The trend."`);

// ---- 3 · the trend (line)
s = p.addSlide();
s.background = { color: WHITE };
s.addText(`${poss(hi)} return rate is elevated and volatile — no sign of steady improvement`, {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
s.addChart(p.ChartType.line, [{
  name: `${hi} monthly return rate (%)`, labels: MONTHS, values: TREND, // full precision
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
  { text: `Peak: ${TREND[peakIdx].toFixed(3)}% in ${monthName(MONTHS[peakIdx])} — about ${peakVsLoYear.toFixed(1)}× ${poss(lo)} full-year rate.\n\n`, options: { fontSize: 12.5, color: INK } },
  { text: `Quiet months exist (${monthShort(MONTHS[quiet[0]])}–${monthShort(MONTHS[quiet[1]])} ${MONTHS[quiet[1]].slice(0, 4)} near ${Math.min(TREND[quiet[0]], TREND[quiet[1]]).toFixed(2)}%), but the rate returns to elevated levels — most recently ${TREND[lastIdx].toFixed(3)}% in ${monthName(MONTHS[lastIdx]).split(' ')[0]}.\n\n`, options: { fontSize: 12.5, color: SLATE } },
  { text: 'Monthly rates use that month’s own shipments as the denominator; small months move more.', options: { fontSize: 11.5, italic: true, color: SLATE } },
], { x: 9.55, y: 1.7, w: 3.0, h: 4.4, fontFace: 'Calibri', isTextBox: true, margin: 0, lineSpacingMultiple: 1.1 });
footer(s, 3);
s.addNotes(`PURPOSE: the pattern over time, honestly framed.\nTALKING POINTS: volatile, not trending down; the ${monthName(MONTHS[peakIdx])} peak (${TREND[peakIdx].toFixed(3)}%) and the ${monthName(MONTHS[lastIdx]).split(' ')[0]} level (${TREND[lastIdx].toFixed(3)}%) both sit far above the other suppliers’ full-year rates. Do NOT claim seasonality or cause from 12 points.\nTRANSITION: "What we propose to do about it."`);

// ---- 4 · recommendation (clearly separated from findings)
const hiMonths = TREND.map((v, i) => [v, i]).sort((a, b) => b[0] - a[0]).slice(0, 5)
  .map(([, i]) => i).sort((a, b) => a - b);
const hiMonthsLabel = hiMonths.map((i) => `${monthShort(MONTHS[i])} ${MONTHS[i].slice(0, 4)}`).join(', ');
s = p.addSlide();
s.background = { color: WHITE };
s.addText(`Proposed follow-up: a focused quality review with ${hi}`, {
  x: 0.55, y: 0.35, w: 12.2, h: 0.75, fontFace: 'Cambria', fontSize: 26, bold: true, color: INK, isTextBox: true, margin: 0 });
s.addShape('roundRect', { x: 0.55, y: 1.45, w: 6.0, h: 4.9, rectRadius: 0.08, fill: { color: PANEL }, line: { type: 'none' } });
s.addText([
  { text: 'WHAT THE DATA SHOW (findings)\n', options: { bold: true, fontSize: 13, color: NAVY } },
  { text: `• ${poss(hi)} return rate (${pct3(rate(hi))}) is ${x1(rHiMid)} ${poss(mid)} and ${x1(rHiLo)} ${poss(lo)} over the same 12 months and sites.\n`, options: { fontSize: 13, color: INK, lineSpacingMultiple: 1.15 } },
  { text: `• The gap persists across the year and peaks in ${monthName(MONTHS[peakIdx])}.\n`, options: { fontSize: 13, color: INK, lineSpacingMultiple: 1.15 } },
  { text: `• ${hi} also drives ${num(sup[hi].defects)} of ${num(totD)} inspection defect occurrences — a separate measure, reported separately.\n`, options: { fontSize: 13, color: INK, lineSpacingMultiple: 1.15 } },
], { x: 0.85, y: 1.65, w: 5.4, h: 4.5, fontFace: 'Calibri', isTextBox: true, margin: 0, valign: 'top' });
s.addShape('roundRect', { x: 6.85, y: 1.45, w: 5.9, h: 4.9, rectRadius: 0.08, fill: { color: NAVY }, line: { type: 'none' } });
s.addText([
  { text: 'WHAT WE RECOMMEND (judgment)\n', options: { bold: true, fontSize: 13, color: ICE } },
  { text: `1. Ask ${hi} for a returns root-cause review on the highest-return months (${hiMonthsLabel}).\n`, options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.15 } },
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
  ['One missing value', `${blanks === 1 ? 'One inspection-hours record is missing' : blanks + ' inspection-hours records are missing'} (missing ≠ zero). It does not affect the return-rate figures.`],
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
  { text: `• Decision today: approve the ${hi.split(' ')[0]} review\n`, options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.2 } },
  { text: '• Owner + date for the root-cause session\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.2 } },
  { text: '• Re-run this analysis next quarter, same definitions, same scope\n', options: { fontSize: 13, color: WHITE, lineSpacingMultiple: 1.2 } },
], { x: 8.7, y: 1.7, w: 3.8, h: 3.6, fontFace: 'Calibri', isTextBox: true, margin: 0, valign: 'top' });
footer(s, 5);
s.addNotes('PURPOSE: earn trust by naming what the analysis cannot say.\nTALKING POINTS: every limitation is also an instruction for the next analysis. End on the single decision requested.\nTRANSITION: none — invite the decision.');

const out = path.join(__dirname, '..', 'references', 'exercise-data', 'Supplier_Quality_Mock_Presentation.pptx');
p.writeFile({ fileName: out }).then(() => {
  console.log('mock deck written:', out);
  console.log(`computed: ${hi} ${pct3(rate(hi))} (${num(sup[hi].returns)}/${num(sup[hi].units)}) | ratios ${x1(rHiMid)} ${mid}, ${x1(rHiLo)} ${lo} | peak ${TREND[peakIdx].toFixed(3)}% ${monthName(MONTHS[peakIdx])} | overall ${pct3(totR / totU)}`);
});
