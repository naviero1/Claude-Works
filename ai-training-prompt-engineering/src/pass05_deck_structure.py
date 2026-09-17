#!/usr/bin/env python3
# Iteration-05 deck pass, stage 1 of 2: STRUCTURE.
# Live application block becomes the nine-step sequence. By original file name:
#   new live order 33-44 = [34, 36, 37, 35, 39, 40, 41, 42, 43, NEW1, NEW2, 44]
#   (NEW1/NEW2 duplicate the slide-36 body layout for the two quotation steps)
#   old 33 (course-log study aid) and old 38 (quotation extension) move to the
#   end of the reference appendix (positions 102, 103). Total 103 slides,
#   live count unchanged at 70. Content is rewritten in stage 2.
import re
import shutil
import zipfile

PPTX = __file__.rsplit('/', 1)[0] + '/../deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx'
RNS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

with zipfile.ZipFile(PPTX) as z:
    names = z.namelist()
    data = {n: z.read(n) for n in names}

pres = data['ppt/presentation.xml'].decode('utf-8')
prels = data['ppt/_rels/presentation.xml.rels'].decode('utf-8')
ctypes = data['[Content_Types].xml'].decode('utf-8')

# guard: skip if already restructured
entries = re.findall(r'<p:sldId\b[^>]*/>', pres)
if len(entries) != 101:
    raise SystemExit(f'expected 101 sldId entries, found {len(entries)} — already restructured?')

# ---- 1. duplicate slide36 (and its notes) twice as slide102/slide103 parts
for new_n in (102, 103):
    data[f'ppt/slides/slide{new_n}.xml'] = data['ppt/slides/slide36.xml']
    data[f'ppt/slides/_rels/slide{new_n}.xml.rels'] = data['ppt/slides/_rels/slide36.xml.rels']
    data[f'ppt/notesSlides/notesSlide{new_n}.xml'] = data['ppt/notesSlides/notesSlide36.xml']
    data[f'ppt/notesSlides/_rels/notesSlide{new_n}.xml.rels'] = data['ppt/notesSlides/_rels/notesSlide36.xml.rels']
    # the slide's rels point at its notesSlide by relative target — retarget the copy
    srels = data[f'ppt/slides/_rels/slide{new_n}.xml.rels'].decode('utf-8')
    srels = srels.replace('notesSlide36.xml', f'notesSlide{new_n}.xml')
    data[f'ppt/slides/_rels/slide{new_n}.xml.rels'] = srels.encode('utf-8')
    nrels = data[f'ppt/notesSlides/_rels/notesSlide{new_n}.xml.rels'].decode('utf-8')
    nrels = nrels.replace('slide36.xml', f'slide{new_n}.xml')
    data[f'ppt/notesSlides/_rels/notesSlide{new_n}.xml.rels'] = nrels.encode('utf-8')
    # content types
    for part in (f'/ppt/slides/slide{new_n}.xml', f'/ppt/notesSlides/notesSlide{new_n}.xml'):
        kind = 'slide' if '/slides/' in part else 'notesSlide'
        override = (f'<Override PartName="{part}" ContentType="application/vnd.openxmlformats-'
                    f'officedocument.presentationml.{kind}+xml"/>')
        ctypes = ctypes.replace('</Types>', override + '</Types>')
    # presentation relationship
    rid = f'RnewSlide{new_n}'
    prels = prels.replace('</Relationships>',
                          f'<Relationship Id="{rid}" Type="{RNS}/slide" Target="slides/slide{new_n}.xml"/></Relationships>')

# ---- 2. rebuild sldIdLst in the new order --------------------------------
# map current entries to their slide file via presentation rels
rid2file = {}
for m in re.finditer(r'<Relationship\b[^>]*>', prels):
    tag = m.group(0)
    rid = re.search(r'Id="([^"]+)"', tag)
    tgt = re.search(r'Target="slides/(slide\d+\.xml)"', tag)
    if rid and tgt:
        rid2file[rid.group(1)] = tgt.group(1)
entry_by_file = {}
max_id = 0
for e in entries:
    rid = re.search(r'r:id="([^"]+)"', e).group(1)
    sid = int(re.search(r'\bid="(\d+)"', e).group(1))
    max_id = max(max_id, sid)
    entry_by_file[rid2file[rid]] = e

def new_entry(n, sid):
    return (f'<p:sldId xmlns:r="{RNS}" id="{sid}" r:id="RnewSlide{n}"/>')

order_files = ([f'slide{i}.xml' for i in range(1, 33)]
               + ['slide34.xml', 'slide36.xml', 'slide37.xml', 'slide35.xml', 'slide39.xml',
                  'slide40.xml', 'slide41.xml', 'slide42.xml', 'slide43.xml']
               + ['slide102.xml', 'slide103.xml', 'slide44.xml']
               + [f'slide{i}.xml' for i in range(45, 102)]
               + ['slide33.xml', 'slide38.xml'])
assert len(order_files) == 103, len(order_files)
new_list = []
for f in order_files:
    if f in entry_by_file:
        new_list.append(entry_by_file[f])
    else:
        max_id += 1
        new_list.append(new_entry(int(re.search(r'\d+', f).group(0)), max_id))
head, sep, tail = pres.partition('<p:sldIdLst>')
_, sep2, rest = tail.partition('</p:sldIdLst>')
pres = head + sep + ''.join(new_list) + sep2 + rest

data['ppt/presentation.xml'] = pres.encode('utf-8')
data['ppt/_rels/presentation.xml.rels'] = prels.encode('utf-8')
data['[Content_Types].xml'] = ctypes.encode('utf-8')

tmp = PPTX + '.tmp'
with zipfile.ZipFile(PPTX) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    written = set()
    for item in zin.infolist():
        zout.writestr(item, data[item.filename])
        written.add(item.filename)
    for n, blob in data.items():
        if n not in written:
            zout.writestr(n, blob)
shutil.move(tmp, PPTX)
print('structure stage done: 103 slides, block reordered, two donors inserted, two pages appended to the appendix')
