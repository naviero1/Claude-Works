// Shared palette + helpers for the training deck
const path = require('path');
const ICONS = path.join(__dirname, 'assets', 'icons');

const C = {
  INK: '232A31',
  SLATE: '46545F',
  MUTE: '7A8790',
  BG: 'FFFFFF',
  PANEL: 'F2F5F6',
  LINE: 'DCE3E6',
  TEAL: '0E7C7B',
  TEAL_DARK: '0A5B5A',
  TEAL_TINT: 'E4F0EF',
  AMBER: 'B96A1B',
  AMBER_TINT: 'FBF0E0',
  RED: 'AF3230',
  RED_TINT: 'F9E9E8',
  GREEN: '3B8560',
  GREEN_TINT: 'E7F2EC',
  DARK: '1C272E',
  DARK_CARD: '2A3842',
  ON_DARK: 'ECF2F4',
  ON_DARK_MUTE: 'A9BBC4',
  TEAL_LIGHT: '5FB8B0',
};

const F = { head: 'Cambria', body: 'Calibri' };

function makeHelpers(pres) {
  const H = {};
  let pageCounter = 0;

  H.icon = (name, v) => path.join(ICONS, `${name}_${v || 'w'}.png`);

  // Slide with standard white background + footer (page numbers auto-increment)
  H.slide = (moduleTag, pageNo, opts = {}) => {
    const s = pres.addSlide();
    pageCounter += 1;
    s.background = { color: opts.dark ? C.DARK : C.BG };
    const footCol = opts.dark ? C.ON_DARK_MUTE : C.MUTE;
    if (moduleTag) {
      s.addText(moduleTag, { x: 0.55, y: 7.12, w: 9.5, h: 0.3, fontFace: F.body, fontSize: 8.5, color: footCol, align: 'left', margin: 0 });
    }
    if (pageNo) {
      s.addText(String(pageCounter), { x: 12.35, y: 7.12, w: 0.45, h: 0.3, fontFace: F.body, fontSize: 8.5, color: footCol, align: 'right', margin: 0 });
    }
    return s;
  };

  // Kicker + title
  H.title = (s, kicker, title, opts = {}) => {
    const dark = !!opts.dark;
    if (kicker) s.addText(kicker.toUpperCase(), { x: 0.55, y: 0.3, w: 12.2, h: 0.3, fontFace: F.body, fontSize: 11, bold: true, charSpacing: 2, color: dark ? C.TEAL_LIGHT : C.TEAL, margin: 0 });
    s.addText(title, { x: 0.55, y: kicker ? 0.58 : 0.4, w: 12.2, h: 0.75, fontFace: F.head, fontSize: opts.size || 30, bold: true, color: dark ? C.ON_DARK : C.INK, margin: 0 });
  };

  // Icon inside a colored circle
  H.iconCircle = (s, x, y, d, name, fill, variant) => {
    s.addShape('ellipse', { x, y, w: d, h: d, fill: { color: fill }, line: { type: 'none' } });
    const inset = d * 0.26;
    s.addImage({ path: H.icon(name, variant || 'w'), x: x + inset, y: y + inset, w: d - 2 * inset, h: d - 2 * inset });
  };

  // Rounded card
  H.card = (s, x, y, w, h, fill, lineColor) => {
    s.addShape('roundRect', { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: lineColor ? { color: lineColor, width: 0.75 } : { type: 'none' } });
  };

  // Bullet list. items: array of strings or {t, b(bold), color, indent}
  H.bullets = (s, x, y, w, h, items, opts = {}) => {
    const arr = items.map((it, i) => {
      const o = typeof it === 'string' ? { t: it } : it;
      return {
        text: o.t,
        options: {
          bullet: o.nb ? false : { code: '2022', indent: 10 },
          breakLine: true,
          bold: !!o.b,
          color: o.color || opts.color || C.SLATE,
          indentLevel: o.indent || 0,
          paraSpaceAfter: opts.gap != null ? opts.gap : 7,
        },
      };
    });
    s.addText(arr, { x, y, w, h, fontFace: F.body, fontSize: opts.size || 13, align: 'left', valign: opts.valign || 'top', margin: 0, lineSpacingMultiple: 1.04 });
  };

  // Big stat callout
  H.stat = (s, x, y, w, num, label, color) => {
    s.addText(num, { x, y, w, h: 0.85, fontFace: F.head, fontSize: 44, bold: true, color: color || C.TEAL, align: 'center', margin: 0 });
    s.addText(label, { x, y: y + 0.85, w, h: 0.85, fontFace: F.body, fontSize: 10.5, color: C.SLATE, align: 'center', valign: 'top', margin: 0, lineSpacingMultiple: 1.05 });
  };

  // Icon row: circle icon + bold header + description to its right
  H.iconRow = (s, x, y, w, name, fill, head, desc, opts = {}) => {
    const d = opts.d || 0.52;
    H.iconCircle(s, x, y + 0.05, d, name, fill);
    s.addText([
      { text: head, options: { bold: true, color: opts.headColor || C.INK, fontSize: opts.headSize || 13.5, breakLine: true, paraSpaceAfter: 2 } },
      { text: desc, options: { color: opts.descColor || C.SLATE, fontSize: opts.descSize || 11.5 } },
    ], { x: x + d + 0.22, y: y - 0.05, w: w - d - 0.22, h: opts.h || 0.95, fontFace: F.body, align: 'left', valign: 'top', margin: 0, lineSpacingMultiple: 1.05 });
  };

  // Horizontal arrow
  H.arrow = (s, x, y, len, color) => {
    s.addShape('line', { x, y, w: len, h: 0, line: { color: color || C.MUTE, width: 2.25, endArrowType: 'triangle' } });
  };

  // Course-progress marker for dark divider slides: six part pills, current highlighted
  H.partMarker = (s, current) => {
    const parts = ['1 · PRIMER', '2 · TOOLS', '3 · CRAFT', '4 · PLAYBOOK', '5 · AGENTS', '6 · ASSETS'];
    const w = 1.62, gap = 0.14, y = 0.52, h = 0.36;
    parts.forEach((label, i) => {
      const x = 0.55 + i * (w + gap);
      const active = i + 1 === current;
      s.addShape('roundRect', { x, y, w, h, rectRadius: 0.18, fill: { color: active ? C.TEAL : C.DARK_CARD }, line: active ? { type: 'none' } : { color: '3A4A55', width: 0.75 } });
      s.addText(label, { x, y: y + 0.015, w, h: h - 0.03, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 8.5, bold: active, charSpacing: 1, color: active ? 'FFFFFF' : C.ON_DARK_MUTE, margin: 0 });
    });
  };

  // "3:00" timer badge for rep slides (top right, white slides)
  H.repTimer = (s) => {
    H.iconCircle(s, 11.28, 0.4, 0.42, 'clock', C.TEAL);
    s.addText('3:00', { x: 11.78, y: 0.44, w: 0.95, h: 0.36, fontFace: F.head, fontSize: 16, bold: true, color: C.TEAL, margin: 0, valign: 'middle' });
  };

  // Guiding-prompt band, R10 format (v1.6) — the consistent chip treatment for the eight
  // course-log prompts: teal card, robot icon, solid "PROMPT n/7" chip, then numbered
  // STEP rows, each exactly TYPE THIS → (copy-paste, Consolas) + WHY → (one plain line),
  // and a workbook-tab pointer so nothing is ever retyped.
  H.promptChip = (s, x, y, w, h, n, steps, opts = {}) => {
    H.card(s, x, y, w, h, C.TEAL_TINT);
    H.iconCircle(s, x + 0.16, y + 0.13, 0.4, 'robot', C.TEAL);
    s.addShape('roundRect', { x: x + 0.66, y: y + 0.16, w: 1.3, h: 0.34, rectRadius: 0.08, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(`PROMPT ${n}/7`, { x: x + 0.66, y: y + 0.17, w: 1.3, h: 0.32, align: 'center', valign: 'middle', fontFace: F.body, fontSize: 9.5, bold: true, charSpacing: 1, color: 'FFFFFF', margin: 0 });
    if (opts.label) s.addText(opts.label, { x: x + 2.08, y: y + 0.17, w: w - 2.35, h: 0.32, fontFace: F.body, fontSize: 11, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
    const runs = [];
    steps.forEach((st, i) => {
      if (steps.length > 1) runs.push({ text: `STEP ${i + 1} · `, options: { bold: true, color: C.AMBER, fontSize: opts.size || 9.5, fontFace: F.body } });
      runs.push({ text: 'TYPE THIS → ', options: { bold: true, color: C.TEAL_DARK, fontSize: opts.size || 9.5, fontFace: F.body } });
      runs.push({ text: st.type, options: { color: C.INK, fontSize: opts.size || 9.5, fontFace: 'Consolas', breakLine: true } });
      runs.push({ text: 'WHY → ', options: { bold: true, color: C.SLATE, fontSize: (opts.size || 9.5) - 0.5, fontFace: F.body } });
      runs.push({ text: st.why, options: { color: C.SLATE, fontSize: (opts.size || 9.5) - 0.5, fontFace: F.body, italic: true, breakLine: true, paraSpaceAfter: i < steps.length - 1 ? 6 : 0 } });
    });
    const footH = opts.tab ? 0.26 : 0;
    s.addText(runs, { x: x + 0.2, y: y + 0.56, w: w - 0.4, h: h - 0.7 - footH, margin: 0, lineSpacingMultiple: 1.08, valign: 'top' });
    if (opts.tab) s.addText(`✂ copy-paste, don’t retype: tab ${opts.tab} of your Course Workbook`, { x: x + 0.2, y: y + h - 0.34, w: w - 0.4, h: 0.28, fontFace: F.body, fontSize: 9.5, italic: true, color: C.TEAL_DARK, margin: 0 });
  };

  // Brand logo chip: real favicon PNG if fetched (assets/logos/<name>.png), else a drawn
  // monogram — a failed fetch never breaks the build. Referential use, internal deck.
  H.logo = (s, x, y, d, name, fallbackLetter) => {
    const p = path.join(__dirname, 'assets', 'logos', `${name}.png`);
    s.addShape('roundRect', { x, y, w: d, h: d, rectRadius: 0.09, fill: { color: 'FFFFFF' }, line: { color: C.LINE, width: 0.75 } });
    if (require('fs').existsSync(p)) {
      const inset = d * 0.14;
      s.addImage({ path: p, x: x + inset, y: y + inset, w: d - 2 * inset, h: d - 2 * inset });
    } else {
      s.addText(fallbackLetter || (name[0] || '?').toUpperCase(), { x, y, w: d, h: d, align: 'center', valign: 'middle', fontFace: F.head, fontSize: d * 28, bold: true, color: C.TEAL_DARK, margin: 0 });
    }
  };

  // Walkthrough step banner (v1.6 family style): big numbered teal circle + title strip.
  H.stepBig = (s, x, y, w, num, title, tint) => {
    H.card(s, x, y, w, 0.52, tint || C.TEAL_TINT);
    s.addShape('ellipse', { x: x + 0.08, y: y + 0.05, w: 0.42, h: 0.42, fill: { color: C.TEAL }, line: { type: 'none' } });
    s.addText(String(num), { x: x + 0.08, y: y + 0.05, w: 0.42, h: 0.42, align: 'center', valign: 'middle', fontFace: F.head, fontSize: 18, bold: true, color: 'FFFFFF', margin: 0 });
    s.addText(title, { x: x + 0.62, y: y + 0.05, w: w - 0.75, h: 0.42, fontFace: F.body, fontSize: 12, bold: true, color: C.TEAL_DARK, margin: 0, valign: 'middle' });
  };

  // Horizontal bar row for small hand-drawn charts: label | bar (scaled) | value
  H.hbar = (s, x, y, w, label, frac, value, color, opts = {}) => {
    const labW = opts.labW || 1.7, valW = opts.valW || 1.1, barH = opts.h || 0.3;
    const barMax = w - labW - valW - 0.2;
    s.addText(label, { x, y: y - 0.02, w: labW, h: barH + 0.06, fontFace: F.body, fontSize: opts.size || 9.5, bold: !!opts.b, color: opts.labColor || C.SLATE, margin: 0, valign: 'middle' });
    s.addShape('roundRect', { x: x + labW, y, w: Math.max(0.12, barMax * frac), h: barH, rectRadius: 0.04, fill: { color }, line: { type: 'none' } });
    s.addText(value, { x: x + labW + Math.max(0.12, barMax * frac) + 0.08, y: y - 0.02, w: valW, h: barH + 0.06, fontFace: F.body, fontSize: opts.size || 9.5, bold: true, color: opts.valColor || C.INK, margin: 0, valign: 'middle' });
  };

  // Callout band (tinted, with optional icon)
  H.callout = (s, x, y, w, h, fill, textRuns, opts = {}) => {
    H.card(s, x, y, w, h, fill, opts.line);
    if (opts.iconName) H.iconCircle(s, x + 0.18, y + h / 2 - 0.21, 0.42, opts.iconName, opts.iconFill || C.TEAL);
    const tx = opts.iconName ? x + 0.78 : x + 0.25;
    s.addText(textRuns, { x: tx, y: y + 0.08, w: w - (tx - x) - 0.25, h: h - 0.16, fontFace: F.body, fontSize: opts.size || 12.5, valign: 'middle', margin: 0, lineSpacingMultiple: 1.06 });
  };

  return H;
}

module.exports = { C, F, makeHelpers };
