#!/usr/bin/env python3
# Iteration-04 repairs, carried into pass 05.
#  1. Slide 76 ("Detailed reference: Useful roles describe behavior"): the
#     citation normalization had collapsed a five-run mixed-format paragraph
#     into its first (bold) run. The run ELEMENTS and their formatting are
#     intact — only texts were moved — so the repair restores each original
#     run's text 1:1 from the pre-cleanup deck (git blob 50c729e), changing
#     ONLY the citation run's text to the canonical form. A full-deck audit
#     confirmed this is the only flattened multi-format paragraph.
#  2. Year-less "Yang 41.1%" / "Yang +4.8%" shorthand canonicalized in the
#     60-minute deck's speaker notes (the long-format deck's sources are
#     fixed separately and that deck rebuilt).
import re
import subprocess

from pptx import Presentation

HERE = __file__.rsplit('/', 1)[0]
PPTX = HERE + '/../deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx'
SP = '/tmp/claude-0/-home-user-Claude-Works/a43332a6-06a6-532a-af4a-fdd550eb8be6/scratchpad'
CANON = 'Yang et al., 2025; revised 2026'

# pristine pre-cleanup copy for the run texts
subprocess.run(['git', '-C', HERE + '/..', 'show',
                '50c729e:./deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx'],
               stdout=open(SP + '/deck_precleanup.pptx', 'wb'), check=True)
old = Presentation(SP + '/deck_precleanup.pptx')
new = Presentation(PPTX)

# ---- 1. restore slide 76, shape 10, paragraph 1, run-for-run --------------
osl, nsl = list(old.slides)[75], list(new.slides)[75]
oshape = [sh for sh in osl.shapes if sh.has_text_frame][None or 0]
oshapes = [sh for sh in osl.shapes if sh.has_text_frame]
nshapes = [sh for sh in nsl.shapes if sh.has_text_frame]
# locate by content: the paragraph whose old joined text carries the Yang citation
target = None
for si, (osh, nsh) in enumerate(zip(oshapes, nshapes)):
    for pi, (op, np_) in enumerate(zip(osh.text_frame.paragraphs, nsh.text_frame.paragraphs)):
        ofull = ''.join(r.text for r in op.runs)
        if '(Yang et al. 2025)' in ofull and 'coin flip' in ofull:
            target = (op, np_)
assert target, 'target paragraph not found'
op, np_ = target
assert len(op.runs) == len(np_.runs), (len(op.runs), len(np_.runs))
for orun, nrun in zip(op.runs, np_.runs):
    nrun.text = orun.text.replace('(Yang et al. 2025)', f'({CANON})')
restored = [r.text[:30] for r in np_.runs]
print('76 restored runs:', restored)

# ---- 2. year-less shorthand in speaker notes ------------------------------
PATS = [
    (re.compile(r'Yang \+4\.8%'), f'{CANON} — +4.8%'),
    (re.compile(r'Yang 41\.1%'), f'{CANON} — 41.1%'),
]
hits = 0
for i, sl in enumerate(new.slides, 1):
    if not sl.has_notes_slide:
        continue
    for para in sl.notes_slide.notes_text_frame.paragraphs:
        full = ''.join(r.text for r in para.runs)
        upd = full
        for pat, rep in PATS:
            upd = pat.sub(rep, upd)
        if upd != full:
            # notes paragraphs here are uniform-format; collapse is safe
            para.runs[0].text = upd
            for r in para.runs[1:]:
                r.text = ''
            hits += 1
            print(f'  notes canonicalized on slide {i}')
assert hits >= 3, hits  # slides 21, 28, 79
new.save(PPTX)
print('repairs saved')
