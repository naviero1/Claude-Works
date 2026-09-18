#!/usr/bin/env python3
"""Integration v06 — owner-directed (in session, 2026-09-18).

Oscar: the restored slides belong in the FINAL DECK's main flow, not the
appendix. This pass moves them into their natural teaching positions,
replaces the two summarized twins with their rich versions, renumbers every
page-number shape, and remaps every textual "slide N" cross-reference (in
visible text AND speaker notes) via the old->new position map.

New order (by v05 position):
  1..3, [109 four eras replaces 4], 5, [110 hardware replaces 6], 7..15,
  106 fluency, 107 hall of shame, 108 flattery, 16..17, 111 assistants,
  18..47, 104 vehicle, 48..54, 105 context failures, 55..103.
  Old live 4 and 6 are dropped (superseded by their rich versions; both
  remain recoverable in git history). Result: 109 slides.

Inserted slides keep their internal design (owner: "as they are"); their
footers switch from "Restored classic" phrasing to the live-deck footer and
their page numbers update. Speaker notes elsewhere are byte-preserved except
for remapped slide-number references, which are disclosed.

Input: pilot v05.  Output: From_Prompts_to_Agents_Visual_Pilot_v06.pptx
"""
import os
import re

from pptx import Presentation
from pptx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v05.pptx")
OUT = os.path.join(ROOT, "notes", "visual-polish", "pilot", "From_Prompts_to_Agents_Visual_Pilot_v06.pptx")

# new order expressed in v05 positions (1-based); live 4 and 6 dropped.
# Owner 2026-09-18: ALL restored slides must sit within the first slides
# (the first training session only reaches the early deck), so the vehicle
# and context-failure slides join the early cluster after the assistant
# comparison instead of parts 5-6.
NEW_ORDER = (
    [1, 2, 3, 109, 5, 110]
    + list(range(7, 16))            # 7..15
    + [106, 107, 108, 16, 17, 111, 104, 105]
    + list(range(18, 104))          # 18..103
)
DROPPED = {4, 6}
MOVED = {104, 105, 106, 107, 108, 109, 110, 111}


def main():
    prs = Presentation(SRC)
    sldIdLst = prs.slides._sldIdLst
    ids = sldIdLst.findall(qn("p:sldId"))
    assert len(ids) == 111
    assert len(NEW_ORDER) == 109, len(NEW_ORDER)
    assert set(NEW_ORDER) | DROPPED == set(range(1, 112))

    # map: v05 position -> new position (dropped slides map to their
    # replacement's new position so stale references still land right)
    new_pos = {old: i + 1 for i, old in enumerate(NEW_ORDER)}
    new_pos[4] = new_pos[109]
    new_pos[6] = new_pos[110]

    # ---- reorder the sldIdLst ----
    elements = {i + 1: el for i, el in enumerate(ids)}
    # drop 4 and 6 entirely (rId parts become orphaned but harmless; the
    # package keeps them out of the presentation)
    for el in ids:
        sldIdLst.remove(el)
    for old in NEW_ORDER:
        sldIdLst.append(elements[old])
    # properly drop the two replaced slides' parts
    for old in DROPPED:
        el = elements[old]
        rId = el.get(qn("r:id"))
        prs.part.drop_rel(rId)

    # ---- fix page numbers + moved-slide footers ----
    for i, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if sh.name == "page-number" and sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        if r.text.strip().isdigit():
                            r.text = str(i)
            if sh.name == "detail-link" and sh.has_text_frame:
                t = sh.text_frame.text
                # integrated slides in the live section get the live footer
                live_end = new_pos[70]
                if ("Restored classic" in t) or ("Related live slide" in t and i <= live_end):
                    for p in sh.text_frame.paragraphs:
                        for j, r in enumerate(p.runs):
                            r.text = "From Prompts to Agents" if j == 0 else ""

    # ---- remap textual slide references (visible text + notes) ----
    ref_pat = re.compile(r"\b(slides?)\s+([0-9]{1,3}(?:\s*[–—-]\s*[0-9]{1,3})?"
                         r"(?:\s*,\s*[0-9]{1,3}(?:\s*[–—-]\s*[0-9]{1,3})?)*)\b",
                         re.IGNORECASE)
    num_pat = re.compile(r"[0-9]{1,3}")

    def remap_numbers(numstr):
        def sub(m):
            n = int(m.group(0))
            return str(new_pos.get(n, n)) if 1 <= n <= 111 else m.group(0)
        return num_pat.sub(sub, numstr)

    def remap_text(t):
        return ref_pat.sub(lambda m: m.group(1) + " " + remap_numbers(m.group(2)), t)

    changed_refs = []

    def process_tf(tf, where):
        for p in tf.paragraphs:
            for r in p.runs:
                if "v1.10 CONSOLIDATION" in r.text:
                    continue  # historical owner quote stays frozen
                if r.text and ("slide" in r.text.lower()):
                    new = remap_text(r.text)
                    if new != r.text:
                        changed_refs.append((where, r.text.strip()[:70], new.strip()[:70]))
                        r.text = new

    for i, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if sh.has_text_frame:
                process_tf(sh.text_frame, f"s{i}:{sh.name}")
        if slide.has_notes_slide:
            process_tf(slide.notes_slide.notes_text_frame, f"s{i}:notes")

    print(f"remapped {len(changed_refs)} slide-number references:")
    for where, old, new in changed_refs:
        print(f"  {where}: '{old}' -> '{new}'")

    assert len(prs.slides._sldIdLst) == 109
    prs.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
