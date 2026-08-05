#!/usr/bin/env python3
"""Builds the CA glue filling station learning & troubleshooting guide PDF.

Usage:  python3 build_pdf.py [output.pdf]
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

from ladder_render import LadderNetwork
from networks import NETWORKS, SECTIONS
from notes import NET_NOTES, SECTION_INTROS

# ----------------------------------------------------------------------------
# palette / styles
# ----------------------------------------------------------------------------
INK = HexColor("#1a2332")
ACCENT = HexColor("#0b5fa5")
MUTED = HexColor("#5a6b7d")
WARNBG = HexColor("#fdf0e7")
WARNBAR = HexColor("#c2601d")
NOTEBG = HexColor("#eef3f8")
NOTEBAR = HexColor("#0b5fa5")
ROWALT = HexColor("#f2f6fa")
HEADBG = HexColor("#1a2332")

PAGE_W, PAGE_H = A4
MARGIN = 16 * mm
CONTENT_W = PAGE_W - 2 * MARGIN

S = {}
S["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=27,
                            leading=32, textColor=INK, alignment=TA_LEFT)
S["subtitle"] = ParagraphStyle("subtitle", fontName="Helvetica", fontSize=13,
                               leading=17, textColor=MUTED)
S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17,
                         leading=21, textColor=INK, spaceBefore=14, spaceAfter=6)
S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5,
                         leading=16, textColor=ACCENT, spaceBefore=11, spaceAfter=4)
S["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5,
                         leading=14, textColor=INK, spaceBefore=8, spaceAfter=3)
S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.3,
                           leading=13.2, textColor=INK, spaceAfter=5)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=12,
                             bulletIndent=3, spaceAfter=2.5)
S["note"] = ParagraphStyle("note", parent=S["body"], fontSize=8.8,
                           leading=12.2, spaceAfter=0)
S["caption"] = ParagraphStyle("caption", fontName="Helvetica-Oblique",
                              fontSize=8.4, leading=11.5, textColor=MUTED,
                              spaceBefore=2, spaceAfter=8)
S["code"] = ParagraphStyle("code", fontName="Courier", fontSize=8.2,
                           leading=10.6, textColor=INK, backColor=NOTEBG,
                           borderPadding=5, spaceAfter=6)
S["cell"] = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.3,
                           leading=10.8, textColor=INK)
S["cellb"] = ParagraphStyle("cellb", parent=S["cell"], fontName="Helvetica-Bold")
S["cellc"] = ParagraphStyle("cellc", parent=S["cell"], fontName="Courier", fontSize=8.0)
S["cellh"] = ParagraphStyle("cellh", fontName="Helvetica-Bold", fontSize=8.4,
                            leading=11, textColor=colors.white)
S["toc1"] = ParagraphStyle("toc1", parent=S["body"], fontSize=10.3, leading=17)


def s(name, txt):
    return Paragraph(txt, S[name])


# ----------------------------------------------------------------------------
# small flowables
# ----------------------------------------------------------------------------
def callout(text, kind="note", title=None):
    """Colored callout box with a left bar."""
    bar = WARNBAR if kind == "warn" else NOTEBAR
    bg = WARNBG if kind == "warn" else NOTEBG
    body = []
    if title:
        body.append(Paragraph(f"<b>{title}</b>", S["note"]))
    body.append(Paragraph(text, S["note"]))
    t = Table([[body]], colWidths=[CONTENT_W - 6])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, bar),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def make_table(header, rows, widths, align_code_cols=()):
    data = [[Paragraph(h, S["cellh"]) for h in header]]
    for r_i, row in enumerate(rows):
        line = []
        for c_i, cell in enumerate(row):
            style = "cellc" if c_i in align_code_cols else "cell"
            line.append(Paragraph(cell, S[style]))
        data.append(line)
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HEADBG),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#c3ccd6")),
    ]
    for i in range(1, len(rows) + 1):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), ROWALT))
    t.setStyle(TableStyle(style))
    return t


class StateDiagram(Flowable):
    """The Idle/Locking/Filling/Complete + Fault state machine drawing."""

    def __init__(self, width):
        super().__init__()
        self.width = width
        self.height = 208

    def wrap(self, aw, ah):
        return self.width, self.height

    def _box(self, c, x, y, w, h, label, sub, fill):
        c.setFillColor(fill)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.roundRect(x, y, w, h, 5, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawCentredString(x + w / 2, y + h - 15, label)
        c.setFont("Helvetica", 7.0)
        for i, line in enumerate(sub):
            c.drawCentredString(x + w / 2, y + h - 26 - i * 9, line)

    def _arrow(self, c, x0, y0, x1, y1, label="", above=True, color=INK):
        c.setStrokeColor(color)
        c.setLineWidth(1.0)
        c.line(x0, y0, x1, y1)
        import math
        ang = math.atan2(y1 - y0, x1 - x0)
        for da in (2.6, -2.6):
            c.line(x1, y1,
                   x1 - 7 * math.cos(ang + da * 0.24), y1 - 7 * math.sin(ang + da * 0.24))
        if label:
            c.setFont("Helvetica", 6.8)
            c.setFillColor(ACCENT)
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            c.drawCentredString(mx, my + (5 if above else -11), label)
            c.setFillColor(INK)

    def draw(self):
        c = self.canv
        W = self.width
        bw, bh = 96, 46
        y = 128
        xs = [8, 8 + (W - bw - 16) / 3, 8 + 2 * (W - bw - 16) / 3, W - bw - 8]
        fills = [HexColor("#e8f0e8"), HexColor("#fdf6e3"), HexColor("#e7eefb"), HexColor("#e8f0e8")]
        self._box(c, xs[0], y, bw, bh, "IDLE", ["StIdle (derived)", "door free"], fills[0])
        self._box(c, xs[1], y, bw, bh, "LOCKING", ["StLocking", "Q_DoorLock ON"], fills[1])
        self._box(c, xs[2], y, bw, bh, "FILLING", ["StFilling", "valve ON, watchdog"], fills[2])
        self._box(c, xs[3], y, bw, bh, "COMPLETE", ["StComplete", "done lamp, door free"], fills[3])
        mid = y + bh / 2
        self._arrow(c, xs[0] + bw, mid, xs[1], mid, "two-hand start", True)
        c.setFont("Helvetica", 6.8)
        c.setFillColor(ACCENT)
        c.drawCentredString((xs[0] + bw + xs[1]) / 2, mid - 11, "& PermStart")
        c.setFillColor(INK)
        self._arrow(c, xs[1] + bw, mid, xs[2], mid, "I_DoorLocked", True)
        self._arrow(c, xs[2] + bw, mid, xs[3], mid, "high level (raw)", True)
        # return arc COMPLETE -> IDLE
        c.setStrokeColor(INK)
        c.setLineWidth(1.0)
        top = y + bh + 26
        c.line(xs[3] + bw / 2, y + bh, xs[3] + bw / 2, top)
        c.line(xs[3] + bw / 2, top, xs[0] + bw / 2, top)
        self._arrow(c, xs[0] + bw / 2, top, xs[0] + bw / 2, y + bh,
                    "", True)
        c.setFont("Helvetica", 6.8)
        c.setFillColor(ACCENT)
        c.drawCentredString((xs[0] + xs[3] + bw) / 2, top + 4,
                            "package removed AND both buttons released")
        c.setFillColor(INK)
        # fault box
        fw, fh = 190, 40
        fx = (W - fw) / 2
        fy = 18
        c.setFillColor(WARNBG)
        c.setStrokeColor(WARNBAR)
        c.setLineWidth(1.3)
        c.roundRect(fx, fy, fw, fh, 5, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawCentredString(fx + fw / 2, fy + fh - 14, "FAULT  (FaultLatched)")
        c.setFont("Helvetica", 7.0)
        c.drawCentredString(fx + fw / 2, fy + fh - 25, "valves OFF, door free, attention lamp flashes,")
        c.drawCentredString(fx + fw / 2, fy + fh - 34, "FaultCode holds the FIRST cause")
        # arrows to fault
        for x in (xs[1] + bw / 2, xs[2] + bw / 2):
            self._arrow(c, x, y, fx + fw / 2 - 30 + (0 if x < W / 2 else 60), fy + fh,
                        "", True, color=WARNBAR)
        c.setFont("Helvetica", 6.8)
        c.setFillColor(WARNBAR)
        c.drawCentredString(W / 2, y - 24, "E-stop / door / spill / timeout / sensor error / package lost")
        # reset arrow fault -> idle
        self._arrow(c, fx, fy + fh / 2, xs[0] + bw / 2, y, "hold both buttons 3 s (cause cleared)", False)


# ----------------------------------------------------------------------------
# page furniture
# ----------------------------------------------------------------------------
DOC_TITLE = "CA Glue Filling Station — Ladder Logic & Troubleshooting Guide"


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(HexColor("#c3ccd6"))
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, PAGE_H - 11 * mm, PAGE_W - MARGIN, PAGE_H - 11 * mm)
    canvas.setFont("Helvetica", 7.3)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, PAGE_H - 9.4 * mm, DOC_TITLE)
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 9.4 * mm, "CODESYS / IEC 61131-3")
    canvas.line(MARGIN, 12 * mm, PAGE_W - MARGIN, 12 * mm)
    canvas.drawRightString(PAGE_W - MARGIN, 8.6 * mm, f"Page {doc.page}")
    canvas.drawString(MARGIN, 8.6 * mm, "Rev A — 2026-08-05")
    canvas.restoreState()


def on_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(HEADBG)
    canvas.rect(0, PAGE_H - 42 * mm, PAGE_W, 42 * mm, stroke=0, fill=1)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, PAGE_H - 44.2 * mm, PAGE_W, 2.2 * mm, stroke=0, fill=1)
    canvas.restoreState()


# ----------------------------------------------------------------------------
# content helpers
# ----------------------------------------------------------------------------
def net_by_n(n):
    for net in NETWORKS:
        if net["n"] == n:
            return net
    raise KeyError(n)


def network_block(n):
    """Rendered network + its teaching note, kept together."""
    items = [LadderNetwork(net_by_n(n), CONTENT_W)]
    note = NET_NOTES.get(n)
    if note:
        items.append(Spacer(1, 1.5))
        items.append(Paragraph(note, S["caption"]))
    else:
        items.append(Spacer(1, 6))
    return KeepTogether(items)


def var_cross_reference():
    """Variable -> written-in / read-in networks, computed from the data."""
    reads, writes = {}, {}

    def walk(els, n, sink_read, sink_write):
        for el in els:
            k = el[0]
            if k in ("no", "nc"):
                base = el[1].split(".")[0]
                sink_read.setdefault(base, set()).add(n)
            elif k in ("coil", "set", "rst"):
                sink_write.setdefault(el[1], set()).add(n)
            elif k == "fb":
                sink_write.setdefault(el[2], set()).add(n)
            elif k == "mov":
                sink_write.setdefault(el[2], set()).add(n)
            elif k == "box":
                for a in el[2]:
                    if not a.isdigit():
                        sink_read.setdefault(a, set()).add(n)
            elif k == "or":
                for br in el[1]:
                    walk(br, n, sink_read, sink_write)

    for net in NETWORKS:
        walk(net.get("rung", []), net["n"], reads, writes)
        for row in net.get("outs", []):
            walk(row, net["n"], reads, writes)

    names = sorted(set(reads) | set(writes), key=str.lower)
    rows = []
    for name in names:
        w = ", ".join(f"{x:02d}" for x in sorted(writes.get(name, [])))
        r = ", ".join(f"{x:02d}" for x in sorted(reads.get(name, [])))
        kind = ("physical input" if name.startswith("I_")
                else "physical output" if name.startswith("Q_")
                else "config" if name.startswith("cfg")
                else "timer/FB" if name.startswith(("t", "trig", "ctr")) and not name.startswith("trigDone")
                else "internal")
        if name in ("trigDone",):
            kind = "timer/FB"
        rows.append([name, kind, w or "—", r or "—"])
    return rows


# ----------------------------------------------------------------------------
# the document
# ----------------------------------------------------------------------------
def build(outpath):
    doc = BaseDocTemplate(outpath, pagesize=A4,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=16 * mm, bottomMargin=16 * mm,
                          title="CA Glue Filling Station — Ladder Logic & Troubleshooting Guide",
                          author="Engineering")
    frame = Frame(MARGIN, 16 * mm, CONTENT_W, PAGE_H - 32 * mm, id="main")
    cover_frame = Frame(MARGIN, 16 * mm, CONTENT_W, PAGE_H - 52 * mm, id="cover")
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=on_cover),
        PageTemplate(id="main", frames=[frame], onPage=on_page),
    ])

    st = []

    # ---------------- cover ----------------
    st.append(Spacer(1, 26))
    st.append(s("title", "CA Glue Filling Station"))
    st.append(Spacer(1, 4))
    st.append(s("subtitle",
                "Ladder Logic Program &amp; Learning Guide — every principle and algorithm "
                "explained for programming, operation and troubleshooting"))
    st.append(Spacer(1, 14))
    st.append(make_table(
        ["", ""],
        [["Platform", "CODESYS 3.5 — IEC 61131-3, language LD (ladder diagram)"],
         ["Program", "PLC_PRG — 58 networks, 10 sections (A–J)"],
         ["Packaging modes", "Squeeze bottle and syringe, selected by fixture sensor"],
         ["Start principle", "Two-hand opto buttons (0.5 s synchronism), auto-stop at high level"],
         ["Companion files", "GVL_IO.txt (variables) · PLC_PRG_Ladder.txt (rung listing) · PLC_PRG.st (ST mirror)"],
         ["Revision", "A — 2026-08-05"]],
        [30 * mm, CONTENT_W - 30 * mm]))
    st.append(Spacer(1, 12))
    st.append(callout(
        "The E-stop, two-hand control and guard-door lock in this program are SEQUENCE "
        "CONTROL AND INDICATION ONLY. The protective functions themselves must be implemented "
        "in safety-rated hardware (safety relay or safety PLC, selected per an ISO 13849-1 "
        "risk assessment) that removes valve power independently of this program. "
        "Chapter 2 explains exactly where that boundary lies.",
        kind="warn", title="Read this first — safety boundary"))
    st.append(Spacer(1, 10))
    st.append(s("body",
                "<b>How to use this document.</b> Chapter 1 explains what the machine does. "
                "Chapters 3–4 give you the vocabulary (I/O map, ladder elements). Chapter 5 is "
                "the heart: every network of the program, drawn as a ladder diagram, with the "
                "principle behind it and what to check when it misbehaves. Chapters 6–7 turn "
                "that knowledge into a troubleshooting routine and a commissioning checklist."))
    st.append(NextPageTemplate("main"))
    st.append(PageBreak())

    # ---------------- contents ----------------
    st.append(s("h1", "Contents"))
    for line in [
        "1 &nbsp;·&nbsp; System overview — what the station does",
        "2 &nbsp;·&nbsp; Safety architecture — what the PLC does and does not do",
        "3 &nbsp;·&nbsp; I/O reference — every signal, its wiring and its purpose",
        "4 &nbsp;·&nbsp; Ladder-logic fundamentals — the building blocks used in this program",
        "5 &nbsp;·&nbsp; The program, network by network (sections A–J)",
        "6 &nbsp;·&nbsp; Troubleshooting guide — fault codes, symptoms, online diagnosis",
        "7 &nbsp;·&nbsp; Commissioning &amp; test checklist",
        "Appendix A &nbsp;·&nbsp; Variable cross-reference (auto-generated from the program)",
        "Appendix B &nbsp;·&nbsp; Importing the program into CODESYS",
    ]:
        st.append(s("toc1", line))

    # ================= chapter 1 =================
    st.append(PageBreak())
    st.append(s("h1", "1 · System overview"))
    st.append(s("body",
                "The station fills cyanoacrylate (CA) glue from a pressurised pot into one of two "
                "package types: a <b>squeeze bottle</b> or a <b>syringe</b>. A fixture sensor tells the "
                "program which fill setup is installed, so the operator never selects a mode manually — "
                "the machine knows. The operator loads a package behind a guard door, closes the door "
                "and presses two opto-touch buttons at the same time. The program locks the door, opens "
                "the matching fill valve, and closes it automatically when the package's high-level "
                "sensor trips. A lamp tells the operator the package is full; opening the door and "
                "removing the package arms the next cycle."))
    st.append(s("h2", "1.1 · The operating sequence as a state machine"))
    st.append(s("body",
                "The whole program hangs on four sequence states plus a fault overlay. Every rung in "
                "Section G either moves the machine forward along this diagram or refuses to. If you "
                "remember one picture from this document, make it this one:"))
    st.append(StateDiagram(CONTENT_W))
    st.append(s("caption",
                "Figure 1 — the sequence state machine. Solid arrows are normal flow; the orange region "
                "is reachable from every cycle state and always de-energises both valves."))
    st.append(s("h2", "1.2 · A normal bottle fill, step by step"))
    for txt in [
        "<b>1.</b> Operator installs the bottle fixture → I_BottleMode TRUE → bottle mode lamp ON (network 48).",
        "<b>2.</b> Operator inserts an empty (or partly full) bottle → I_BottlePresent TRUE, debounced 100 ms (network 03).",
        "<b>3.</b> Operator closes the door → I_DoorClosed TRUE. ReadyBottle and PermStart become TRUE (networks 22, 25).",
        "<b>4.</b> Operator presses both opto buttons within 0.5 s → StartPulse (networks 10–14) → state LOCKING, door lock energised (networks 26, 47).",
        "<b>5.</b> Lock feedback I_DoorLocked arrives (&lt; 2 s) → state FILLING → bottle valve opens (networks 29, 45); filling lamp ON (network 50).",
        "<b>6.</b> Glue rises past the low-level sensor (this is how the program distinguishes a first fill from a top-off) and reaches the high-level sensor → valve closes THE SAME SCAN → state COMPLETE, done lamp ON (networks 32, 51).",
        "<b>7.</b> Operator releases the buttons, opens the now-unlocked door and removes the bottle → state IDLE, ready for the next package (network 33).",
    ]:
        st.append(s("bullet", txt))
    st.append(s("body",
                "A syringe fill is identical except that the syringe fixture reports mode, the package "
                "permissives also demand the syringe be clamped (I_SyrLocked) and its fill tip present "
                "(I_TipPresent), and the fill ends on the plunger-high detector instead of a liquid level."))
    st.append(callout(
        "Anything that interrupts this happy path — E-stop, door, spill, a sensor that stops making "
        "sense, a fill that takes too long — lands in the FAULT state with both valves closed, and "
        "<b>FaultCode</b> remembers the FIRST cause (chapter 6). The operator clears it by holding both "
        "opto buttons for 3 seconds after removing the cause.",
        title="When anything goes wrong"))

    # ================= chapter 2 =================
    st.append(PageBreak())
    st.append(s("h1", "2 · Safety architecture"))
    st.append(s("body",
                "A standard PLC executing this program is <b>not a safety device</b>: a single output "
                "transistor failure, a crashed runtime or a programming mistake could hold a valve open. "
                "Machine-safety standards therefore split the work in two layers:"))
    st.append(make_table(
        ["Layer", "Implemented in", "Job"],
        [["<b>Protective layer</b>",
          "Safety relay / safety PLC + safety-rated devices (ISO 13849-1)",
          "E-stop circuit, ISO 13851 two-hand relay, guard-lock interlock. Removes power from the "
          "fill-valve solenoids and the pressure supply <b>independently of the standard PLC</b>."],
         ["<b>Sequence layer</b> (this program)",
          "CODESYS application, standard I/O",
          "Decides WHEN a fill should happen, supervises timing, catches implausible sensors, drives "
          "lamps and counters, remembers the first fault cause. Mirrors the safety signals as ordinary "
          "inputs so it can annunciate and sequence around them."]],
        [32 * mm, 52 * mm, CONTENT_W - 84 * mm]))
    st.append(s("body",
                "In practice: the E-stop chain and two-hand relay outputs are wired both into the safety "
                "contactor feeding the valve solenoids <i>and</i> into the PLC inputs I_EStopOK / "
                "I_BtnLeft / I_BtnRight used here. When you troubleshoot 'valve will not open', remember "
                "there are two layers that can be blocking it — check the safety relay's LEDs as well as "
                "the program's permissive chain."))
    st.append(s("h2", "2.1 · Fail-safe wiring conventions"))
    st.append(s("body",
                "Every safety-relevant sensor in this design is wired so that the <b>healthy condition "
                "reads TRUE</b> (normally-closed contacts, light-on opto sensors). A cut cable, dead "
                "sensor or unplugged connector then looks like a problem and stops the machine, instead "
                "of silently looking like 'all clear'. This is the single most important wiring principle "
                "on the station:"))
    st.append(make_table(
        ["Signal", "Wired", "TRUE means", "A broken wire reads as"],
        [["I_EStopOK", "NC chain", "E-stop released, circuit intact", "E-stop pressed → machine stops"],
         ["I_DoorClosed", "NC in switch", "door physically closed", "door open → no start, fill aborts"],
         ["I_DoorLocked", "NC in lock", "lock bolt engaged", "unlocked → fill aborts"],
         ["I_PotLevelOK", "NC / light-on", "glue level above minimum", "pot empty → new fills blocked"],
         ["I_SpillDetect", "NO", "liquid detected (event signal)", "no detection — this sensor is "
          "supervised by routine inspection instead; it is an annunciation aid, not a protective device"]],
        [26 * mm, 20 * mm, 52 * mm, CONTENT_W - 98 * mm]))
    st.append(s("h2", "2.2 · De-energise-to-safe outputs"))
    st.append(s("body",
                "Both fill valves must be <b>spring-return, normally-closed</b> valves: glue flows only "
                "while the solenoid is energised. Every abort path in this program works by making a coil "
                "FALSE — which only translates to 'glue stops' if the valve closes when power is removed. "
                "The door lock is the opposite kind of choice: it is energise-to-lock, so a power failure "
                "leaves the door openable (nobody is locked out during a blackout; the safety layer keeps "
                "the process safe)."))
    st.append(callout(
        "Section C implements a two-hand START GESTURE modelled on ISO 13851 concepts — synchronism "
        "window, tie-down lockout, full-release re-initiation — so the sequence also refuses "
        "discordant presses. It is NOT a two-hand protective function: the fill deliberately "
        "continues after the buttons are released, because during the fill the locked guard door "
        "protects the operator, not the buttons. Actual hand protection comes from the hardware "
        "two-hand relay in the protective layer, sized and positioned per the standard.",
        kind="warn", title="Two-hand gesture vs two-hand protection"))

    # ================= chapter 3 =================
    st.append(PageBreak())
    st.append(s("h1", "3 · I/O reference"))
    st.append(s("body",
                "Addresses are placeholders — remap them to your coupler in the CODESYS device editor. "
                "The 'watch when' column is the fastest route from a symptom to a signal worth watching "
                "in the online view."))
    st.append(s("h2", "3.1 · Inputs"))
    st.append(make_table(
        ["Variable", "Addr", "Device", "Watch when…"],
        [["I_BtnLeft / I_BtnRight", "%IX0.0 / .1", "opto-touch buttons",
          "starts refused: do both go TRUE within 0.5 s of each other?"],
         ["I_DoorClosed", "%IX0.2", "guard-door switch", "no start / fault 2: does it flicker when the door is bumped?"],
         ["I_DoorLocked", "%IX0.3", "guard-lock feedback", "fault 8: does it come TRUE within 2 s of the lock energising?"],
         ["I_PotLevelOK", "%IX0.4", "pot level sensor", "attention lamp flashes: pot genuinely low, or sensor fouled?"],
         ["I_BottleMode", "%IX0.5", "fixture ID sensor", "wrong mode lamp / fault 6: seated fixture, clean target?"],
         ["I_BottleLow", "%IX0.6", "bottle low level", "top-off behaviour odd / sensor error 19: alignment, residue"],
         ["I_BottleHigh", "%IX0.7", "bottle high level", "overfill or early stop: trips exactly at the fill line?"],
         ["I_BottlePresent", "%IX1.0", "bottle presence", "fault 7 / refuses start: detects bottle, not the nest wall?"],
         ["I_TipPresent", "%IX1.1", "syringe tip sensor", "syringe start refused: tip really seated?"],
         ["I_PlungerLow", "%IX1.2", "plunger at bottom", "sensor error 20: both plunger sensors TRUE = impossible"],
         ["I_PlungerHigh", "%IX1.3", "plunger at top", "syringe overfill / early stop"],
         ["I_SyrPresent", "%IX1.4", "syringe presence", "fault 7 / refuses start"],
         ["I_SyrLocked", "%IX1.5", "clamp feedback", "refuses start: clamp fully over-centre?"],
         ["I_EStopOK", "%IX1.6", "E-stop chain (NC)", "E-stop lamp ON: chain open somewhere — find which device"],
         ["I_SpillDetect", "%IX1.7", "drip-tray probe", "fault 3 repeats: real leak, or conductive residue on probe?"]],
        [34 * mm, 20 * mm, 34 * mm, CONTENT_W - 88 * mm], align_code_cols=(0, 1)))
    st.append(s("h2", "3.2 · Outputs"))
    st.append(make_table(
        ["Variable", "Addr", "Device", "Driven by"],
        [["Q_ValveBottle", "%QX0.1", "bottle fill valve (NC, spring return)", "network 45"],
         ["Q_ValveSyringe", "%QX0.0", "syringe fill valve (NC, spring return)", "network 46"],
         ["Q_LampBottle", "%QX0.2", "packaging lamp — bottle", "network 48"],
         ["Q_LampSyringe", "%QX0.3", "packaging lamp — syringe", "network 49"],
         ["Q_LampFilling", "%QX0.4", "fill-valve-operating lamp", "network 50"],
         ["Q_LampDone", "%QX0.5", "package-filled lamp", "network 51"],
         ["Q_LampEStop", "%QX0.6", "E-stop condition lamp (steady)", "network 52"],
         ["Q_LampAttention", "%QX0.7", "operator-interaction lamp (flashes 1 Hz)", "networks 53–54"],
         ["Q_DoorLock", "%QX1.0", "guard-lock solenoid (energise-to-lock)", "network 47"]],
        [34 * mm, 20 * mm, 74 * mm, CONTENT_W - 128 * mm], align_code_cols=(0, 1)))
    st.append(callout(
        "Q_DoorLock is not in the original output list — it was added because the input list names a "
        "door lock, and a lock needs a command signal. If your door uses a purely mechanical latch, "
        "delete network 47 and wire I_DoorLocked from the latch position switch instead.",
        title="Design note — the added output"))
    st.append(s("h2", "3.3 · Diagnostic variables (no wiring — watch via HMI or online view)"))
    st.append(make_table(
        ["Variable", "Meaning"],
        [["FaultCode", "0 = none · 1 E-stop · 2 door · 3 spill · 4 fill timeout · 5 sensor plausibility · "
          "6 mode lost · 7 package lost · 8 lock failed — always the FIRST cause since the last reset"],
         ["CntBottlesFilled / CntSyringesFilled", "completed fills per package type (cmdCounterReset clears both)"],
         ["StIdle…StComplete, CycBottle/CycSyringe", "live state of the sequence machine — the first thing to check online"],
         ["CycTopOff", "TRUE while the running/last cycle started on a package that already held glue "
          "(bottle low level made / plunger off its empty stop) — explains a legitimately short fill"]],
        [52 * mm, CONTENT_W - 52 * mm], align_code_cols=(0,)))

    # ================= chapter 4 =================
    st.append(PageBreak())
    st.append(s("h1", "4 · Ladder-logic fundamentals used in this program"))
    st.append(s("body",
                "Everything in chapter 5 is built from seven ideas. If these are familiar, skip ahead; "
                "if a rung ever confuses you, come back here."))

    st.append(s("h2", "4.1 · The scan cycle — why order matters"))
    st.append(s("body",
                "A PLC does not execute rungs 'whenever'. Every few milliseconds it (1) copies all "
                "physical inputs into memory, (2) executes network 01, then 02, … then 58 using that "
                "frozen snapshot, (3) copies the result memory to the physical outputs. Three practical "
                "consequences:"))
    for txt in [
        "<b>Inputs cannot change mid-scan.</b> If network 03 and network 45 both look at I_BottlePresent, they see the same value even if the wire changed in between.",
        "<b>Later networks see earlier results from THIS scan; earlier networks see results from the LAST scan.</b> That is why ResetPulse (network 15) is computed before every latch that consumes it (16, 18, 44) — the reset acts in the same scan. The one place this program deliberately accepts a one-scan-old value is tResetHold reading FaultLatched (network 15 reads what networks 35–42 wrote last scan) — irrelevant against a 3-second hold.",
        "<b>An output coil is just memory until the scan ends.</b> Forcing a variable in CODESYS changes memory; the physical output follows at the end of the scan.",
    ]:
        st.append(s("bullet", txt))

    st.append(s("h2", "4.2 · Contacts are questions, coils are answers"))
    st.append(s("body",
                "A normally-open contact —| |— asks 'is this variable TRUE?'; a normally-closed contact "
                "—|/|— asks 'is it FALSE?'. Contacts in series are AND; parallel branches are OR. A coil "
                "—( )— writes the result of the whole rung into a variable, every scan. "
                "<b>Do not confuse contact type with wiring type</b>: I_EStopOK is wired normally-closed "
                "electrically (chapter 2), yet most rungs ask —| |— I_EStopOK because the PLC input is "
                "TRUE when healthy. The ladder symbol chooses the question, the wiring chooses the truth."))

    st.append(s("h2", "4.3 · Latches — making the PLC remember"))
    st.append(s("body",
                "A rung's coil forgets everything each scan, so memory must be built deliberately. This "
                "program shows both classic idioms on purpose:"))
    for txt in [
        "<b>Seal-in:</b> the output variable appears as a contact in parallel with its own trigger, so once TRUE it keeps itself TRUE until a series condition breaks the seal. Used for THC_Lockout (12), EStopTrip (16), SpillTrip (18) — places where the RESET CONDITION is the interesting part of the story.",
        "<b>SET / RESET coils:</b> —(S)— makes a variable TRUE and leaves it; —(R)— makes it FALSE. The variable holds its value between scans with no seal rung. Used for the state machine and FaultLatched (26–44), where different rungs own the setting and the clearing. Rule of thumb: when one rung both sets and clears, seal-in; when responsibility is split across rungs, S/R. If an S and an R fire in the same scan, the LAST executed network wins — network 43 (abort) is deliberately placed after every transition rung for exactly this reason.",
    ]:
        st.append(s("bullet", txt))

    st.append(s("h2", "4.4 · The TON timer — one block, four jobs"))
    st.append(s("body",
                "TON (on-delay) has two pins that matter: IN and Q. While IN is TRUE, elapsed time "
                "accumulates; Q turns TRUE when the preset PT is reached; the moment IN drops, everything "
                "resets instantly. From this one behaviour the program builds four different tools:"))
    st.append(make_table(
        ["Job", "Idea", "Where"],
        [["Debounce / qualify", "signal must be steadily TRUE for PT before it is believed; "
          "dis-believed instantly when it drops (fail-safe asymmetry)", "03–09, 17, 19–20"],
         ["Discordance detector", "times how long ONE button is held alone; Q = the 0.5 s window was missed", "10–11"],
         ["Watchdog", "times how long a state is allowed to last; Q = something is stuck", "28, 30–31"],
         ["Gesture recogniser", "times how long the operator deliberately holds both buttons", "15"]],
        [30 * mm, CONTENT_W - 58 * mm, 28 * mm]))

    st.append(s("h2", "4.5 · Edge detection — R_TRIG"))
    st.append(s("body",
                "R_TRIG's Q is TRUE for exactly one scan when its CLK input goes FALSE→TRUE. It converts "
                "a condition ('both buttons are down') into an event ('both buttons JUST went down'). "
                "Every start in this machine is an event, never a level — that is what forces the "
                "operator to actuate the buttons freshly for every cycle (anti-repeat). Its falling-edge "
                "twin F_TRIG guards the other direction: network 12 uses it to catch the two-hand "
                "condition DROPPING while a button is still pressed, which is what enforces full-release "
                "re-initiation."))

    st.append(s("h2", "4.6 · The two-timer flasher"))
    st.append(s("body",
                "Networks 01–02 cross-couple two TONs: A times while B's Q is FALSE; when A finishes, B "
                "starts; when B finishes it resets A and everything repeats. Blink follows tBlinkA.Q, "
                "giving a square wave with period 2 × cfgBlinkHalfPeriod (1 Hz). ANDing any condition "
                "with Blink (network 54) turns a steady condition into a flashing lamp — one oscillator "
                "serves every flashing indication you will ever add."))

    st.append(s("h2", "4.7 · Compare and move — carrying a number through ladder"))
    st.append(s("body",
                "Ladder is not only booleans. An EQ box passes power when two numbers are equal; a MOVE "
                "box copies a number when it receives power. Networks 35–42 chain them — "
                "'if FaultCode is still 0, write MY code into it' — which is the whole first-out "
                "algorithm in two boxes (section H)."))

    # ================= chapter 5 =================
    st.append(PageBreak())
    st.append(s("h1", "5 · The program, network by network"))
    st.append(s("body",
                "Each section below starts with the principle it implements, then shows its networks "
                "exactly as you will transcribe them into CODESYS. The italic line under each network is "
                "the note to remember when troubleshooting it. Network order is part of the design — "
                "keep it."))
    for sec_key in "ABCDEFGHIJ":
        first, last, sec_title = SECTIONS[sec_key]
        intro = SECTION_INTROS[sec_key]
        head = [s("h2", f"Section {sec_key} · {sec_title} (networks {first:02d}–{last:02d})")]
        head.append(s("body", intro))
        st.append(KeepTogether(head + [Spacer(1, 2)]))
        for n in range(first, last + 1):
            st.append(network_block(n))
        st.append(Spacer(1, 4))

    # ================= chapter 6 =================
    st.append(PageBreak())
    st.append(s("h1", "6 · Troubleshooting guide"))
    st.append(s("h2", "6.1 · Fault codes — first-out causes and what to check"))
    st.append(make_table(
        ["Code", "Meaning", "Likely causes → checks, in order"],
        [["1", "E-stop", "Chain open: a pressed button somewhere, a pulled cable, a dead channel. Walk the "
          "chain with the safety relay LEDs, then reset (twist out E-stop, hold both buttons 3 s)."],
         ["2", "Door opened / unlocked mid-cycle",
          "Operator opened it; door bounced (watch I_DoorClosed online while wiggling the door); lock "
          "solenoid dropped out (wiring, PSU dip)."],
         ["3", "Spill detected", "Real leak (inspect nest & lines) or residue bridging the tray probe — "
          "CA residue is conductive enough. Clean and dry the tray; reset is refused while it still reads wet."],
         ["4", "Fill timeout", "Pot pressure low/empty (but code 4 with PotLow also flashing points at supply), "
          "clogged line/needle — CA cures in moist air, valve not actually opening (listen / watch "
          "Q_LampFilling), or a high-level sensor that cannot see the glue (misaligned, fouled). Increase "
          "cfgFillTimeout* only after ruling those out."],
         ["5", "Sensor plausibility", "Two sensors disagree with physics — see networks 19–20 for exactly which "
          "combinations. Clean lenses (CA fogs optics!), re-align, check for a package half-inserted."],
         ["6", "Mode signal lost mid-cycle", "Fixture ID sensor lost its target: fixture not seated, sensor "
          "gap drifted, cable strain. Watch I_BottleMode online while pressing on the fixture."],
         ["7", "Package lost / unclamped mid-cycle", "Bottle lifted by line pressure, syringe clamp creeping "
          "open, or a presence sensor dropping out from vibration — watch the db* bits during a fill."],
         ["8", "Door lock failed to engage", "Bolt blocked (door not fully closed), solenoid dead, feedback "
          "switch dead. You have 2 s (cfgLockTimeout) — watch I_DoorLocked respond to Q_DoorLock online."]],
        [12 * mm, 40 * mm, CONTENT_W - 52 * mm]))
    st.append(s("h2", "6.2 · Symptoms that do not set a fault code"))
    st.append(make_table(
        ["Symptom", "Where to look"],
        [["Nothing happens on two-hand press",
          "Online: is StartPulse firing? If TwoHandOK never goes TRUE → THC_Lockout stuck (release BOTH "
          "buttons fully) or one button dead (networks 10–13). If TwoHandOK fires but no start → walk the "
          "PermStart chain (network 25) contact by contact: the first open contact is your answer — "
          "SafetyOK? door? PotLow? StIdle? ReadyBottle/ReadySyringe (network 22/23)?"],
         ["Attention lamp flashing, no fault code",
          "The lamp also flashes for live conditions that are not latched faults: PotLow (refill the pot), "
          "SensorErr (networks 19–21 — which impossible combination is active right now?), THC_Lockout "
          "(release both buttons), or E-stop released but not yet reset."],
         ["Mode lamps both OFF",
          "Fixture signal is mid-change or the debounce (200 ms) is still running — if permanent, the "
          "fixture sensor is not seeing its target (network 07/08)."],
         ["Done lamp never clears",
          "Network 33 needs BOTH buttons released AND the package actually removed — a presence sensor "
          "still TRUE (residue, reflective nest) keeps StComplete latched."],
         ["Valve closes but lamp says filling",
          "Q_LampFilling mirrors the COMMAND (network 50). If the lamp is off and glue still flows, the "
          "valve is mechanically stuck open — hardware, not logic."],
         ["Counters not counting",
          "The counters consume the one-scan MDoneEvent latched by network 32 — a cycle aborted by a "
          "fault never completes and is deliberately not counted. Watch MDoneEvent with a breakpoint "
          "on network 55 if in doubt; it is already FALSE again by the end of every scan (network 57)."]],
        [44 * mm, CONTENT_W - 44 * mm]))
    st.append(s("h2", "6.3 · Diagnosing online with CODESYS"))
    for txt in [
        "<b>Login → watch the power flow.</b> Open PLC_PRG in the online view: TRUE contacts and energised rung segments are highlighted blue. Find the leftmost cold contact in the rung that should be firing — that contact IS the diagnosis in 90 % of cases.",
        "<b>Build a watch list</b> with StIdle…StComplete, CycBottle/CycSyringe, FaultCode, PermStart, ReadyBottle, ReadySyringe, TwoHandOK. One glance tells you where the sequence stopped.",
        "<b>Timers tell on themselves:</b> click a TON online and read ET. A watchdog at 1.9 s of a 2 s preset is about to trip; a debounce that never accumulates means its input is chattering.",
        "<b>Force with discipline.</b> Forcing dbBottlePresent TRUE to test the sequence is fine with the door open and the pot depressurised — but never force a valve output, and always use 'Unforce all' before leaving. The safety layer will stop the machine, but you will chase ghost faults.",
        "<b>The first-out code beats the alarm flood:</b> when several things look wrong, trust FaultCode — everything after the first cause is usually consequence, not cause.",
    ]:
        st.append(s("bullet", txt))

    # ================= chapter 7 =================
    st.append(PageBreak())
    st.append(s("h1", "7 · Commissioning & test checklist"))
    st.append(s("body",
                "Run this top to bottom with the pot DEPRESSURISED and disconnected from glue until step 6. "
                "Tick each line; every line maps to the network it proves."))
    st.append(make_table(
        ["#", "Test", "Pass criterion", "Proves"],
        [["1", "Wiggle-test every input in the I/O mapping view (door, sensors, buttons, E-stop)",
          "each toggles cleanly, correct polarity per §2.1", "wiring & addresses"],
         ["2", "Both mode fixtures in turn", "correct mode lamp within 0.2 s; both lamps off mid-swap", "07–08, 48–49"],
         ["3", "Press one button, wait, add the second", "no start; attention lamp flashes until both released", "10–14, 53"],
         ["4", "Two-hand press with door open", "no start (PermStart cold at I_DoorClosed)", "25"],
         ["5", "Valid start, dry", "lock engages &lt; 2 s, StFilling reached, valve output LED on", "26–29, 45–47"],
         ["6", "Wet fill, bottle", "valve closes the instant I_BottleHigh trips; no overshoot past the fill line", "32, 45"],
         ["7", "Open door mid-fill (dry!)", "instant abort, fault 2, valves off", "37, 43"],
         ["8", "Press E-stop mid-fill", "instant abort, E-stop lamp steady, fault 1; reset needs release + 3 s hold", "16, 35, 44"],
         ["9", "Block the high-level sensor and start (dry)", "watchdog aborts at cfgFillTimeout*, fault 4", "30–31, 39"],
         ["10", "Wet the drip tray probe", "fault 3; reset refused until dried", "17–18, 36"],
         ["11", "Cover a level sensor with no bottle present", "SensorErr after 0.5 s, start refused, attention flashes", "19–21"],
         ["12", "Remove bottle mid-fill (dry)", "instant abort, fault 7", "42–43"],
         ["13", "Full bottle in nest, try to start", "refused (ReadyBottle cold at I_BottleHigh)", "22"],
         ["14", "Empty the pot below the level sensor", "attention flashes after 2 s; running fill completes; next start refused", "09, 25"],
         ["15", "Ten consecutive good fills of each type", "counters advance by exactly ten each", "55–57"]],
        [8 * mm, 62 * mm, 62 * mm, CONTENT_W - 132 * mm]))
    st.append(callout(
        "Tuning: cfgFillTimeoutBottle/Syr should be ~1.5 × your slowest legitimate fill (measure ten). "
        "cfgDebPresence 100 ms suits mechanical bounce; raise cfgDebSensorErr if load/unload transients "
        "ever annunciate. Keep cfgSyncWindow at 500 ms — it matches the hardware two-hand relay.",
        title="Timing parameters"))

    # ================= appendix A =================
    st.append(PageBreak())
    st.append(s("h1", "Appendix A · Variable cross-reference"))
    st.append(s("body",
                "Generated automatically from the network data. 'Written in' = the network that drives "
                "the variable (coil / FB instance / MOVE target); 'read in' = every network with a "
                "contact or operand on it. When a variable misbehaves, these are the only rungs that "
                "can be responsible."))
    st.append(make_table(["Variable", "Kind", "Written in", "Read in"],
                         var_cross_reference(),
                         [40 * mm, 26 * mm, 32 * mm, CONTENT_W - 98 * mm],
                         align_code_cols=(0,)))

    # ================= appendix B =================
    st.append(PageBreak())
    st.append(s("h1", "Appendix B · Importing the program into CODESYS"))
    for txt in [
        "<b>1.</b> Create a Standard project (CODESYS 3.5, your target device), language of PLC_PRG: "
        "<b>Ladder Logic Diagram (LD)</b>.",
        "<b>2.</b> Add a Global Variable List named <b>GVL_IO</b> (right-click Application → Add Object) "
        "and paste the contents of GVL_IO.txt into it.",
        "<b>3.</b> Copy the VAR…END_VAR block from the top of PLC_PRG_Ladder.txt into PLC_PRG's "
        "declaration editor.",
        "<b>4.</b> Transcribe the 58 networks IN ORDER from PLC_PRG_Ladder.txt / chapter 5. Insert "
        "contacts and coils with the toolbar; timers, triggers and counters via 'Insert Empty Box' and "
        "typing TON / R_TRIG / CTU; EQ and MOVE via the same box mechanism. Assign S/R modifiers by "
        "right-clicking a coil.",
        "<b>5.</b> Alternatively, create PLC_PRG as an <b>ST</b> POU and paste PLC_PRG.st — it is a "
        "1:1 mirror of the ladder and behaves identically. Many people commission in ST, then transcribe "
        "to LD for the maintenance team once the logic is proven.",
        "<b>6.</b> Map the %IX/%QX addresses to your hardware in the device I/O mapping editor.",
        "<b>7.</b> Use simulation mode (Online → Simulation) plus the watch list from §6.3 to dry-run "
        "the whole sequence before touching hardware — every scenario in chapter 7 can be rehearsed by "
        "writing the input variables by hand.",
    ]:
        st.append(s("bullet", txt))
    st.append(Spacer(1, 8))
    st.append(callout(
        "Companion files in this folder: <b>GVL_IO.txt</b> (all variables + wiring notes) · "
        "<b>PLC_PRG_Ladder.txt</b> (the canonical rung listing) · <b>PLC_PRG.st</b> (Structured Text "
        "mirror for simulation) · <b>tools/</b> (the scripts that generated this document).",
        title="File manifest"))

    doc.build(st)
    return outpath


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "docs", "CA_Filling_Station_Ladder_Guide.pdf")
    print("built:", build(out))
