#!/usr/bin/env python3
# Cleanup pass (Beebop iteration 03, owner-approved) — citation normalization
# in the 60-minute deck. The 41.1% study (arXiv:2505.13360) is cited as
# "Yang et al., 2025; revised 2026" everywhere (submitted 2025, revised v3
# 2026 per notes/research/r15). Text-run edits on slides 24/30/32/76 only.
import re
from pptx import Presentation

PPTX = __file__.rsplit('/', 1)[0] + '/../deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx'
CANON = 'Yang et al., 2025; revised 2026'
PATS = [
    (re.compile(r'Yang et al\., arXiv 2505\.13360'), CANON + ' — arXiv:2505.13360'),
    (re.compile(r'Yang et al\.,? 2025(?!; revised)'), CANON),
    (re.compile(r'Yang 2026 \(41\.1%\)'), CANON + ' (41.1%)'),
    (re.compile(r'Yang 2026'), CANON),
]

p = Presentation(PPTX)
total = 0
for i, sl in enumerate(p.slides, 1):
    frames = [sh.text_frame for sh in sl.shapes if sh.has_text_frame]
    if sl.has_notes_slide:
        frames.append(sl.notes_slide.notes_text_frame)
    for tf in frames:
        for para in tf.paragraphs:
            full = ''.join(r.text for r in para.runs)
            new = full
            for pat, rep in PATS:
                new = pat.sub(rep, new)
            if new != full:
                para.runs[0].text = new
                for r in para.runs[1:]:
                    r.text = ''
                total += 1
                print(f'  slide {i}: normalized')
assert total >= 6, total  # 24 notes x2, 30, 32, 76 body+notes x3
p.save(PPTX)
print(f'citation normalization: {total} paragraphs updated')
