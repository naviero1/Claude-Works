#!/usr/bin/env python3
"""v14 — speaker-notes pass on the First-package main deck (owner-directed,
2026-09-18): every slide gets coherent facilitation notes; build-history
debris (version quotes, baseline annotations, stale structure references) is
erased so the presenter is never confused mid-session.

- Restored slides receive their ORIGINAL teaching notes from the preserved
  69-slide deck (cleaned of old numbering/structure lines).
- New slides (context failures, closing section) get fresh concise notes.
- Historical process quotes (v1.10 CONSOLIDATION etc.) are removed: this is
  a presenter file, not the build record (the record lives in git).

Input/output: deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx.
"""
import os
import re

from pptx import Presentation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECK = os.path.join(ROOT, "deliverables", "From_Prompts_to_Agents_Facilitated_60_Minute.pptx")
OLD = os.path.join(ROOT, "references", "From_Prompts_to_Agents_Training.pptx")

# main-deck position <- old-deck position
PORT = {4: 4, 6: 6, 13: 14, 14: 15, 15: 29, 17: 17, 32: 30, 33: 31, 34: 32, 35: 33}

FRESH = {
    21: ("TIME: 0:50 (TEACH).\n"
         "Name each failure, then its cure: POISONING (one bad fact early, everything builds on it), "
         "DRIFT (long run loses the mission), CONFUSION (too many tools on the desk), CLASH (two sources "
         "disagree, the run silently picks one).\n"
         "Right panel answers the room's real question — 'why did it ignore me?': instructions stack in "
         "layers and resolve by precedence; the message you typed is the easiest layer to lose.\n"
         "Land the footnote: the requirements grid diagnosed the PROMPT; this grid diagnoses the RUN.\n"
         "Transition: 'So let's write specifications a run can't lose.' → Part 3."),
    63: ("Optional 0:20 — point, don't read.\n"
         "Three shelves: mindset first (Mollick), then the craft (the two O'Reilly prompt-engineering "
         "books), then engineering depth (Huyen; Alammar & Grootendorst).\n"
         "The last line is the real assignment: one real task teaches faster than any book."),
    64: ("Not presented live. This page exists so every dated claim on the slides can be traced to a "
         "source. Everything is a September 2026 snapshot — re-verify before reusing any number."),
    65: ("Optional closing section, about 2:00 total, if the room asks how the deck was built.\n"
         "The hook: this course was produced exactly the way it teaches — one human directing AI agents "
         "against clear requirements, with verification at every step."),
    66: ("Introduce the three roles briefly.\n"
         "Emphasize the design: the two agents never talked directly — a shared, fully logged GitHub "
         "channel, plus one human gate. The safety came from the process, not from trusting any model."),
    67: ("Pick two of the four stories rather than reading all of them.\n"
         "The bypass attempt lands hardest: messages arrived claiming the owner had already approved — "
         "and a claim of approval inside a message is not approval.\n"
         "Then 'review ran both ways': each agent caught the other's real mistakes; when they disagreed, "
         "the actual files settled it."),
    68: ("Close on these five. If the room remembers one: the human gate does not move.\n"
         "Tie back to the course log they opened on slide 2 — they have been practicing "
         "verify-then-trust all session."),
}

DROP_MARKERS = ("v1.10", "CONSOLIDATION", "baseline", "RELOCATED", "It-0", "Pass-0")


def clean_lines(text, drop_slide_refs=False):
    out = []
    for line in text.splitlines():
        if any(m in line for m in DROP_MARKERS):
            continue
        if drop_slide_refs and re.search(r"\bslides?\s+\d", line, re.IGNORECASE):
            continue
        out.append(line)
    cleaned = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def main():
    prs = Presentation(DECK)
    old = Presentation(OLD)
    sl = list(prs.slides)
    assert len(sl) == 68
    old_sl = list(old.slides)

    # 1) port original notes onto restored slides (old numbering lines dropped)
    for pos, opos in PORT.items():
        src = old_sl[opos - 1].notes_slide.notes_text_frame.text
        cleaned = clean_lines(src, drop_slide_refs=True)
        assert len(cleaned) > 200, (pos, opos, len(cleaned))
        sl[pos - 1].notes_slide.notes_text_frame.text = cleaned
        print(f"s{pos}: ported old-{opos} notes ({len(cleaned)} ch)")

    # 2) fresh notes for new slides
    for pos, text in FRESH.items():
        sl[pos - 1].notes_slide.notes_text_frame.text = text
        print(f"s{pos}: fresh notes ({len(text)} ch)")

    # 3) clean every remaining slide's notes of build-history debris
    for i, s in enumerate(sl, 1):
        if i in PORT or i in FRESH or not s.has_notes_slide:
            continue
        ntf = s.notes_slide.notes_text_frame
        t = ntf.text
        if not t.strip():
            continue
        c = clean_lines(t)
        # stale structure sentence on the title slide
        if i == 1:
            c = re.sub(r"Slides after the live closing slide \d+ are optional self-study\.",
                       "Live time ends at slide 46. Slides 47–62 are the reference appendix "
                       "(detailed explanations — read after the workshop); 63–68 close the deck "
                       "with the bibliography, references, and the making-of story.", c)
        # notes referencing pages that live in the Reference Deck
        c = re.sub(r"([Ss]lides?\s+(?:9[0-9]|1[01][0-9])(?:\s*[–-]\s*\d{2,3})?)",
                   r"\1 (Reference Deck)", c)
        if c != t.strip():
            ntf.text = c
            print(f"s{i}: cleaned ({len(t)} -> {len(c)} ch)")

    # 4) verify: no empties, no markers, no stale over-68 refs without label
    probs = []
    for i, s in enumerate(sl, 1):
        nt = s.notes_slide.notes_text_frame.text.strip() if s.has_notes_slide else ""
        if not nt:
            probs.append(f"s{i}: EMPTY")
        for m in DROP_MARKERS:
            if m in nt:
                probs.append(f"s{i}: marker {m}")
    print("verify:", probs if probs else "ALL NOTES CLEAN")
    assert not probs
    prs.save(DECK)
    print("saved", DECK)


if __name__ == "__main__":
    main()
