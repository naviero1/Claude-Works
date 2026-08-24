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
