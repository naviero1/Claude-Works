#!/usr/bin/env python3
"""Set document metadata and build a chapter outline so a 68-page reference is navigable."""
import pypdf, pypdfium2 as pdfium

SRC = 'The-Fast-Casual-Compendium.pdf'

# locate each chapter by the heading text on its page
MARKS = [
    ('87 named dishes',                   'The Fast-Casual Compendium'),
    ('What sixty menus actually tell you','Seven findings'),
    ('What money does and does not buy',  'One · Money'),
    ('Sodium is the currency',            'Two · Sodium'),
    ('What flavor actually costs',        'Three · Flavor'),
    ('Orders that beat the order',        'Four · Swaps'),
    ('What a ranking leaves out',         'The sample'),
    ('The food the first edition missed', 'New in this edition'),
    ('Nine criteria, written out',        'The model'),
    ('How much of this is measured',      'Confidence'),
    ('Where this model misfires',         'Against interest'),
    ('The ranking',                       'The ranking'),
    ('What was wrong',                    'Verification log'),
    ('What a score is',                   'Method and provenance'),
]

doc = pdfium.PdfDocument(SRC)
# headings are uppercased and letter-spaced by CSS, so normalise before matching
def norm(t): return ' '.join(t.replace('\u2060', '').split()).lower()
pages = [norm(doc[i].get_textpage().get_text_range()) for i in range(len(doc))]
# chapters appear in order, so each search starts where the last one landed;
# without that, a phrase like "the ranking" matches prose long before its chapter
found, cursor = [], 0
for needle, label in MARKS:
    for i in range(cursor, len(pages)):
        if norm(needle) in pages[i]:
            found.append((label, i)); cursor = i; break
    else:
        print(f'  ! not located: {label}')

r = pypdf.PdfReader(SRC)
w = pypdf.PdfWriter()
for p in r.pages:
    w.add_page(p)
for label, i in found:
    w.add_outline_item(label, i)
w.add_metadata({
    '/Title': 'The Fast-Casual Compendium — Second Edition',
    '/Subject': ('Eighty-seven delivery dishes across the Research Triangle, North Carolina, '
                 'scored on seven health criteria plus flavor and cost, with a full verification log.'),
    '/Keywords': 'nutrition, delivery, Research Triangle, restaurant, sodium, ranking',
    '/Creator': 'compendium build pipeline',
})
with open(SRC, 'wb') as f:
    w.write(f)

print(f'{len(r.pages)} pages, {len(found)} outline entries')
for label, i in found:
    print(f'  p{i+1:>3}  {label}')
