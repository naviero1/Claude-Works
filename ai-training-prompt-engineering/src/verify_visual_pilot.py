#!/usr/bin/env python3
"""Preservation verification for the six-slide visual pilot.

Compares pilot versions A and B against the confirmed baseline per
rocksteady-handoff.md section 8: slide count/identity/order, untouched slide
parts, notes, theme/master/layout parts, verbatim visible text on the six
modified slides, font-change conformance to the approved log, and the exact
slide-87 bar geometry. Prints a machine-readable summary; exits nonzero on
any failure.
"""
import json
import os
import sys
import zipfile
from lxml import etree

from pptx import Presentation
from pptx.util import Emu
from pptx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "deliverables", "From_Prompts_to_Agents_Facilitated_60_Minute.pptx")
A = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v01.pptx")
B = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v01_S34B.pptx")
LOG = os.path.join(ROOT, "notes", "visual-polish", "pilot", "font_change_log.json")

TARGETS = {23: 278, 28: 283, 34: 291, 37: 294, 53: 308, 87: 342}
FAILS = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAILS.append(msg)


def canon(xml_bytes):
    return etree.tostring(etree.fromstring(xml_bytes), method="c14n")


def slide_partname(prs, idx):
    return prs.slides[idx].part.partname


def notes_xml(prs, idx):
    s = prs.slides[idx]
    if not s.has_notes_slide:
        return b""
    return s.notes_slide.part.blob


def visible_texts(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                txt = "".join(r.text for r in p.runs)
                if txt.strip():
                    out.append(txt)
        if getattr(sh, "has_table", False) and sh.has_table:
            for row in sh.table.rows:
                for c in row.cells:
                    if c.text.strip():
                        out.append(c.text)
    return out


def run_sizes(slide):
    """(text, size_pt or None, bold, family) for every non-empty run."""
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.text.strip():
                        out.append((r.text, r.font.size.pt if r.font.size else None,
                                    r.font.bold, r.font.name))
    return out


def main():
    base = Presentation(BASE)
    va = Presentation(A)
    vb = Presentation(B)

    # 1. count / identity / order
    for name, prs in (("A", va), ("B", vb)):
        ids = [int(e.get("id")) for e in prs.slides._sldIdLst.findall(qn("p:sldId"))]
        base_ids = [int(e.get("id")) for e in base.slides._sldIdLst.findall(qn("p:sldId"))]
        check(len(prs.slides._sldIdLst) == 103, f"{name}: 103 slides")
        check(ids == base_ids, f"{name}: native slide id order identical to baseline")
        for pos, sid in TARGETS.items():
            check(ids[pos - 1] == sid, f"{name}: slide {pos} keeps sid-{sid}")

    # 2. untouched slide parts: canonical XML equality
    diff_a = [i + 1 for i in range(103)
              if canon(base.slides[i].part.blob) != canon(va.slides[i].part.blob)]
    check(sorted(diff_a) == sorted(TARGETS), f"A: only the six pilot slide parts differ ({diff_a})")
    diff_b = [i + 1 for i in range(103)
              if canon(va.slides[i].part.blob) != canon(vb.slides[i].part.blob)]
    check(diff_b == [34], f"B vs A: only slide 34 differs ({diff_b})")

    # 3. notes parts identical everywhere
    bad_notes = [i + 1 for i in range(103) if notes_xml(base, i) != notes_xml(va, i)]
    check(not bad_notes, f"A: all notes parts byte-identical to baseline ({bad_notes})")
    bad_notes_b = [i + 1 for i in range(103) if notes_xml(va, i) != notes_xml(vb, i)]
    check(not bad_notes_b, f"B: all notes parts identical to A ({bad_notes_b})")

    # 4. theme / master / layout / presentation-level parts
    with zipfile.ZipFile(BASE) as zb, zipfile.ZipFile(A) as za, zipfile.ZipFile(B) as zbb:
        def infra(z):
            return {n: z.read(n) for n in z.namelist()
                    if ("theme" in n or "slideMaster" in n or "slideLayout" in n)
                    and n.endswith(".xml")}
        ib, ia, ibb = infra(zb), infra(za), infra(zbb)
        check(set(ib) == set(ia) and all(ib[k] == ia[k] for k in ib),
              "A: theme/master/layout parts byte-identical to baseline")
        check(set(ia) == set(ibb) and all(ia[k] == ibb[k] for k in ia),
              "B: theme/master/layout parts byte-identical to A")

    # 5. verbatim visible text preserved on the six modified slides
    approved_new = {  # approved labels / new objects only
        23: {"Audience + source", "method", "format + tone + check"},
        28: set(),
        34: set(),
        37: {"Schematic", "Date-range selector", "metric selector", "reset control",
             "supplier and site filters", "summary values", "trend chart",
             "sortable detail table"},
        53: set(),
        87: set(),
    }
    approved_new_b = {34: {"Supplier_Data_Exercise.xlsx"}}
    for pos in TARGETS:
        bt = visible_texts(base.slides[pos - 1])
        at = visible_texts(va.slides[pos - 1])
        missing = [t for t in bt if t not in at]
        check(not missing, f"A slide {pos}: every baseline text present verbatim ({missing})")
        extra = [t for t in at if t not in bt and t not in approved_new[pos]]
        check(not extra, f"A slide {pos}: no unapproved new text ({extra})")
    # B slide 34
    bt = visible_texts(base.slides[33])
    at34b = visible_texts(vb.slides[33])
    missing = [t for t in bt if t not in at34b]
    check(not missing, f"B slide 34: every baseline text present verbatim ({missing})")
    extra = [t for t in at34b if t not in bt and t not in approved_new_b[34]]
    check(not extra, f"B slide 34: no unapproved new text ({extra})")

    # 6. font conformance: every changed size is a logged <20pt increase
    with open(LOG) as f:
        log = json.load(f)
    logged = {(e["slide"], e["text"][:40]): (e["orig_pt"], e["new_pt"]) for e in log}
    for pos in TARGETS:
        base_rs = {t: (s, b, n) for t, s, b, n in run_sizes(base.slides[pos - 1])}
        for text, size, bold, name in run_sizes(va.slides[pos - 1]):
            if text in base_rs:
                bs, bb, bn = base_rs[text]
                if bs is not None and size is not None and abs(size - bs) > 0.01:
                    key_ok = any(e["slide"] == pos and e["text"].startswith(text[:30])
                                 for e in log) or any(
                                 e["slide"] == pos and text.startswith(e["text"][:30].rstrip("."))
                                 for e in log)
                    check(bs < 20 and size > bs and key_ok,
                          f"A slide {pos}: size change {bs}->{size} for '{text[:40]}' is a logged <20pt increase")
                if bb is not None and bold is not None:
                    check(bb == bold, f"A slide {pos}: emphasis preserved for '{text[:40]}'")

    # 7. slide 87: exact bar geometry + full table intact
    s87 = va.slides[86]
    spec = {
        "pilot-bar-Alpha": (11.12, 3.1015625, 0.27111644018118836, 0.2),
        "pilot-bar-Bravo": (11.12, 3.8828125, 0.9583155990636305, 0.2),
        "pilot-bar-Cardinal": (11.12, 4.6640625, 0.3536124728763161, 0.2),
    }
    found = {}
    for sh in s87.shapes:
        if sh.name in spec:
            found[sh.name] = (Emu(sh.left).inches, Emu(sh.top).inches,
                              Emu(sh.width).inches, Emu(sh.height).inches)
    for name, exp in spec.items():
        got = found.get(name)
        ok = got is not None and all(abs(g - e) < 0.002 for g, e in zip(got, exp))
        check(ok, f"slide 87 {name}: geometry matches spec exactly ({got})")
    tbl = [sh for sh in s87.shapes if sh.has_table][0].table
    cells = [c.text for r in tbl.rows for c in r.cells]
    base_tbl = [sh for sh in base.slides[86].shapes if sh.has_table][0].table
    base_cells = [c.text for r in base_tbl.rows for c in r.cells]
    check(cells == base_cells and len(cells) == 20, "slide 87: all 20 table cells unchanged")
    check(not any("TOTAL" in n for n in found), "slide 87: no TOTAL bar")

    # 8. crop provenance file exists and matches source hash
    import hashlib
    def sha(p):
        return hashlib.sha256(open(p, "rb").read()).hexdigest()
    prov = open(os.path.join(ROOT, "notes", "visual-polish", "crop-provenance.md")).read()
    check(sha(os.path.join(ROOT, "references", "exercise-data", "Supplier_Data_Exercise.xlsx")) in prov,
          "crop provenance records the exact source workbook hash")
    check(sha(os.path.join(ROOT, "notes", "visual-polish", "pilot", "s34b_workbook_crop.png")) in prov,
          "crop provenance records the exact crop image hash")

    print()
    if FAILS:
        print(f"RESULT: {len(FAILS)} FAILURE(S)")
        sys.exit(1)
    print("RESULT: ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
