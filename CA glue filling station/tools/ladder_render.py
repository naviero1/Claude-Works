"""Ladder-diagram renderer for the CA glue filling station PDF guide.

Draws IEC 61131-3 style ladder networks (contacts, coils, function-block
boxes, parallel branches) as vector graphics on a reportlab canvas, wrapped
as a Platypus flowable so they paginate with the document text.

Network element grammar (Python tuples/lists):
    ("no",  "Label")                      normally-open contact
    ("nc",  "Label")                      normally-closed contact
    ("coil","Label")                      output coil
    ("set", "Label") / ("rst","Label")    set / reset coil
    ("fb",  "TON", "tName", ["IN","PT:=cfgX"], ["Q","ET"])  function block
    ("box", "EQ", ["FaultCode", "0"])     compare box in the rail
    ("mov", "1", "FaultCode")             MOVE box
    ("or",  [branch, branch, ...])        parallel branches; each branch is
                                          a list of series elements

A network is: {"n": 12, "title": "...",
               "rung": [series elements],
               "outs": [[series elements], ...]}   output rows stacked in
               parallel at the right rail.
"""

from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Flowable

INK = HexColor("#1a2332")        # near-black blue ink
ACCENT = HexColor("#0b5fa5")     # label blue
BOXBG = HexColor("#eef3f8")      # FB box fill
FRAME = HexColor("#b9c4d0")      # network frame
TITLEBG = HexColor("#e4ebf2")    # network header fill

F_MONO = "Courier"
F_MONO_B = "Courier-Bold"
F_LABEL = "Helvetica"
F_TITLE = "Helvetica-Bold"

LABEL_SIZE = 6.4
PIN_SIZE = 6.0

CONTACT_W = 16.0
COIL_W = 18.0
EL_GAP = 5.0
ROW_H = 24.0
LEAD = 8.0


def _lw(text, font=F_LABEL, size=LABEL_SIZE):
    return stringWidth(text, font, size)


class _M:
    """Measured element: width, extent above the wire, extent below."""
    def __init__(self, w, up=11.0, dn=5.0):
        self.w, self.up, self.dn = w, up, dn


def measure(el):
    kind = el[0]
    if kind in ("no", "nc"):
        return _M(max(CONTACT_W, _lw(el[1]) + 3))
    if kind in ("coil", "set", "rst"):
        return _M(max(COIL_W, _lw(el[1]) + 3))
    if kind == "fb":
        _, ftype, name, ins, outs = el
        rows = max(len(ins), len(outs))
        w = max(64.0, _lw(f"{ftype}  {name}", F_MONO_B, 6.6) + 14)
        for i in range(rows):
            iw = _lw(ins[i], F_MONO, PIN_SIZE) if i < len(ins) else 0
            ow = _lw(outs[i], F_MONO, PIN_SIZE) if i < len(outs) else 0
            w = max(w, iw + ow + 26)
        h = 15 + rows * 10.0
        return _M(w, up=9.0, dn=h - 9.0)
    if kind == "box":
        _, op, args = el
        w = max(48.0, max(_lw(a, F_MONO, PIN_SIZE) for a in args) + 16)
        h = 13 + len(args) * 9.0
        return _M(w, up=8.0, dn=h - 8.0)
    if kind == "mov":
        _, src, dst = el
        w = max(56.0, _lw(f"{src} -> {dst}", F_MONO, PIN_SIZE) + 14)
        return _M(w, up=8.0, dn=13.0)
    if kind == "or":
        branches = el[1]
        widths, tops, bots = [], [], []
        for br in branches:
            bw, bu, bd = series_metrics(br)
            widths.append(bw)
            tops.append(bu)
            bots.append(bd)
        # rows are pitched so neighbours never collide
        pitch = []
        for i in range(len(branches) - 1):
            pitch.append(max(ROW_H, bots[i] + tops[i + 1] + 4))
        return _M(max(widths) + 14, up=tops[0], dn=sum(pitch) + bots[-1])
    raise ValueError(f"unknown element kind: {kind}")


def series_metrics(els):
    ms = [measure(e) for e in els]
    w = sum(m.w for m in ms) + EL_GAP * max(0, len(ms) - 1)
    up = max((m.up for m in ms), default=11.0)
    dn = max((m.dn for m in ms), default=5.0)
    return w, up, dn


def _row_offsets(rows):
    """Vertical offsets (>=0, growing downward) for stacked series rows."""
    ms = [series_metrics(r) for r in rows]
    offs = [0.0]
    for i in range(len(rows) - 1):
        offs.append(offs[-1] + max(ROW_H, ms[i][2] + ms[i + 1][1] + 4))
    return offs, ms


class LadderNetwork(Flowable):
    """One ladder network in a framed, titled box."""

    def __init__(self, net, width):
        super().__init__()
        self.net = net
        self.width = width
        self.header_h = 13.0
        self._calc()

    def _calc(self):
        rung = self.net.get("rung", [])
        outs = [list(r) for r in self.net.get("outs", [])]
        self.outs = outs
        _, up_r, dn_r = series_metrics(rung) if rung else (0, 11.0, 5.0)
        if outs:
            offs, ms = _row_offsets(outs)
            up_o = ms[0][1]
            dn_o = offs[-1] + ms[-1][2]
        else:
            up_o, dn_o = 0.0, 0.0
        self.up = max(up_r, up_o) + 4
        self.dn = max(dn_r, dn_o) + 5
        self.height = self.header_h + self.up + self.dn + 6

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)

    # ---- primitives ----------------------------------------------------
    def _wire(self, x0, x1, y):
        c = self.canv
        c.setLineWidth(1.0)
        c.setStrokeColor(INK)
        if x1 > x0:
            c.line(x0, y, x1, y)

    def _contact(self, x, y, el):
        c = self.canv
        kind, label = el[0], el[1]
        m = measure(el)
        cx = x + m.w / 2.0
        gap = 4.5
        self._wire(x, cx - gap, y)
        self._wire(cx + gap, x + m.w, y)
        c.setLineWidth(1.2)
        c.setStrokeColor(INK)
        c.line(cx - gap, y - 5, cx - gap, y + 5)
        c.line(cx + gap, y - 5, cx + gap, y + 5)
        if kind == "nc":
            c.line(cx - gap - 1.0, y - 5.5, cx + gap + 1.0, y + 5.5)
        c.setFont(F_LABEL, LABEL_SIZE)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, y + 7.0, label)
        c.setFillColor(INK)
        return m.w

    def _coil(self, x, y, el):
        c = self.canv
        kind, label = el[0], el[1]
        m = measure(el)
        cx = x + m.w / 2.0
        r = 5.2
        self._wire(x, cx - r, y)
        self._wire(cx + r, x + m.w, y)
        c.setLineWidth(1.2)
        c.setStrokeColor(INK)
        # "( )" pair: left/right halves of a circle with gaps top and bottom
        c.arc(cx - r, y - r, cx + r, y + r, startAng=100, extent=160)
        c.arc(cx - r, y - r, cx + r, y + r, startAng=-80, extent=160)
        if kind in ("set", "rst"):
            c.setFont(F_TITLE, 6.2)
            c.drawCentredString(cx, y - 2.2, "S" if kind == "set" else "R")
        c.setFont(F_LABEL, LABEL_SIZE)
        c.setFillColor(ACCENT)
        c.drawCentredString(cx, y + 7.0, label)
        c.setFillColor(INK)
        return m.w

    def _fb(self, x, y, el):
        c = self.canv
        _, ftype, name, ins, outs = el
        m = measure(el)
        rows = max(len(ins), len(outs))
        h = 15 + rows * 10.0
        top = y + 9.0
        c.setFillColor(BOXBG)
        c.setStrokeColor(INK)
        c.setLineWidth(1.0)
        c.rect(x + 4, top - h, m.w - 8, h, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont(F_MONO_B, 6.6)
        c.drawCentredString(x + m.w / 2.0, top - 10, (f"{ftype}  {name}" if name else ftype))
        c.setFont(F_MONO, PIN_SIZE)
        for i, pin in enumerate(ins):
            c.drawString(x + 7, top - 21 - i * 10.0, pin)
        for i, pin in enumerate(outs):
            c.drawRightString(x + m.w - 7, top - 21 - i * 10.0, pin)
        self._wire(x, x + 4, y)
        self._wire(x + m.w - 4, x + m.w, y)
        return m.w

    def _box(self, x, y, el):
        c = self.canv
        _, op, args = el
        m = measure(el)
        h = 13 + len(args) * 9.0
        top = y + 8.0
        c.setFillColor(BOXBG)
        c.setStrokeColor(INK)
        c.setLineWidth(1.0)
        c.rect(x + 4, top - h, m.w - 8, h, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont(F_MONO_B, 6.4)
        c.drawCentredString(x + m.w / 2.0, top - 9.5, op)
        c.setFont(F_MONO, PIN_SIZE)
        for i, a in enumerate(args):
            c.drawCentredString(x + m.w / 2.0, top - 18.5 - i * 9.0, a)
        self._wire(x, x + 4, y)
        self._wire(x + m.w - 4, x + m.w, y)
        return m.w

    def _mov(self, x, y, el):
        c = self.canv
        _, src, dst = el
        m = measure(el)
        h = 21.0
        top = y + 8.0
        c.setFillColor(BOXBG)
        c.setStrokeColor(INK)
        c.setLineWidth(1.0)
        c.rect(x + 4, top - h, m.w - 8, h, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont(F_MONO_B, 6.4)
        c.drawCentredString(x + m.w / 2.0, top - 9.5, "MOVE")
        c.setFont(F_MONO, PIN_SIZE)
        c.drawCentredString(x + m.w / 2.0, top - 18, f"{src} -> {dst}")
        self._wire(x, x + 4, y)
        self._wire(x + m.w - 4, x + m.w, y)
        return m.w

    def _or(self, x, y, el):
        c = self.canv
        branches = el[1]
        m = measure(el)
        inner_w = m.w - 14
        x0 = x + 7
        self._wire(x, x0, y)
        self._wire(x0 + inner_w, x + m.w, y)
        _, ms = _row_offsets(branches)
        offs, ms = _row_offsets(branches)
        for off, br in zip(offs, branches):
            self._series(x0, y - off, br, total_w=inner_w)
        c.setLineWidth(1.0)
        c.setStrokeColor(INK)
        c.line(x0, y - offs[-1], x0, y)
        c.line(x0 + inner_w, y - offs[-1], x0 + inner_w, y)
        return m.w

    def _element(self, x, y, el):
        k = el[0]
        if k in ("no", "nc"):
            return self._contact(x, y, el)
        if k in ("coil", "set", "rst"):
            return self._coil(x, y, el)
        if k == "fb":
            return self._fb(x, y, el)
        if k == "box":
            return self._box(x, y, el)
        if k == "mov":
            return self._mov(x, y, el)
        if k == "or":
            return self._or(x, y, el)
        raise ValueError(k)

    def _series(self, x, y, els, total_w=None):
        cur = x
        for i, el in enumerate(els):
            cur += self._element(cur, y, el)
            if i < len(els) - 1:
                self._wire(cur, cur + EL_GAP, y)
                cur += EL_GAP
        if total_w is not None and cur < x + total_w:
            self._wire(cur, x + total_w, y)
            cur = x + total_w
        return cur - x

    # ---- main draw ------------------------------------------------------
    def draw(self):
        c = self.canv
        net = self.net
        W, H = self.width, self.height
        c.setStrokeColor(FRAME)
        c.setLineWidth(0.8)
        c.setFillColor(TITLEBG)
        c.rect(0, H - self.header_h, W, self.header_h, stroke=1, fill=1)
        c.rect(0, 0, W, H, stroke=1, fill=0)
        c.setFillColor(INK)
        c.setFont(F_TITLE, 7.0)
        c.drawString(6, H - self.header_h + 3.8, f"NETWORK {net['n']:02d}")
        c.setFont(F_LABEL, 7.0)
        c.drawString(66, H - self.header_h + 3.8, net.get("title", ""))

        y = H - self.header_h - self.up
        left, right = 8.0, W - 8.0
        c.setStrokeColor(INK)
        c.setLineWidth(1.6)
        c.line(left, 5, left, H - self.header_h - 3)
        c.line(right, 5, right, H - self.header_h - 3)

        rung = net.get("rung", [])
        outs = self.outs
        if outs:
            offs, ms = _row_offsets(outs)
            out_w = max(m[0] for m in ms)
        else:
            offs, ms, out_w = [], [], 0.0

        x = left
        self._wire(x, x + LEAD, y)
        x += LEAD

        rung_avail = (right - x) - (out_w + 2 * LEAD if outs else LEAD)
        if rung:
            rung_w, _, _ = series_metrics(rung)
            drawn = self._series(x, y, rung, total_w=max(rung_w, rung_avail))
            x += drawn
        else:
            self._wire(x, x + rung_avail, y)
            x += rung_avail

        if outs:
            self._wire(x, x + LEAD, y)
            x += LEAD
            for off, row in zip(offs, outs):
                self._series(x, y - off, row, total_w=out_w)
                self._wire(x + out_w, right, y - off)
            if len(outs) > 1:
                c.setLineWidth(1.0)
                c.setStrokeColor(INK)
                c.line(x, y - offs[-1], x, y)
        else:
            self._wire(x, right, y)
