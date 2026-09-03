#!/usr/bin/env python3
"""Top-down dish illustrations, drawn as flat inline SVG.

Photographs are not possible here - the artifact sandbox admits no external
images, and captioning stock photography as a named restaurant's dish would
misrepresent a real business. These are original drawings of dish *types*,
which claim nothing about any particular kitchen.

Every colour comes from a CSS custom property so both themes work.
"""

def _wrap(body, vb=200, label=''):
    return (f'<svg class="dish" viewBox="0 0 {vb} {vb}" role="img" aria-label="{label}">'
            f'{body}</svg>')

def _plate(r=92, cx=100, cy=100, cls='pl'):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r-9}" class="pl-in"/>')

def poke():
    b = _plate()
    b += '<path d="M100 30 A70 70 0 0 1 170 100 L100 100 Z" class="f-green"/>'
    for x, y in [(118,58),(140,72),(126,84),(150,92),(132,104)]:
        b += f'<rect x="{x}" y="{y}" width="15" height="15" rx="2" class="f-tuna"/>'
    b += ('<path d="M100 100 L100 170 A70 70 0 0 1 40 128 Z" class="f-rice"/>'
          '<path d="M62 118 q14-9 27 0 q-13 9-27 0" class="f-avo"/>'
          '<path d="M58 138 q17-11 33 0 q-16 11-33 0" class="f-avo"/>')
    b += '<circle cx="150" cy="140" r="13" class="f-edam"/><circle cx="128" cy="152" r="9" class="f-edam"/>'
    for i in range(9):
        b += f'<circle cx="{72+i*6}" cy="{78+(i%3)*5}" r="1.7" class="f-seed"/>'
    return _wrap(b, label='A poke bowl seen from above')

def kebab():
    b = _plate()
    b += '<rect x="52" y="86" width="96" height="4" rx="2" class="f-skew"/>'
    for i, x in enumerate([58, 82, 106, 130]):
        b += f'<rect x="{x}" y="{72}" width="20" height="32" rx="5" class="f-char"/>'
        b += f'<path d="M{x+4} 78 h12 M{x+4} 88 h12 M{x+4} 98 h12" class="f-grill"/>'
    b += ('<path d="M40 118 q30-14 60 0 q30 14 60 0 v34 a70 70 0 0 1-120 0 Z" class="f-salad"/>'
          '<circle cx="72" cy="140" r="8" class="f-tom"/><circle cx="118" cy="148" r="7" class="f-tom"/>'
          '<circle cx="146" cy="132" r="6" class="f-tom"/>')
    b += '<circle cx="100" cy="52" r="17" class="f-yog"/>'
    return _wrap(b, label='A grilled kebab plate with salad and yogurt')

def sashimi():
    b = '<rect x="16" y="46" width="168" height="108" rx="5" class="pl"/>'
    b += '<rect x="24" y="54" width="152" height="92" rx="3" class="pl-in"/>'
    for i, x in enumerate([38, 68, 98, 128]):
        cls = 'f-tuna' if i % 2 == 0 else 'f-salmon'
        b += (f'<path d="M{x} 72 q18-9 32 4 q-4 24-18 30 q-18-5-14-34 Z" class="{cls}"/>'
              f'<path d="M{x+5} 82 q13-5 22 3" class="f-marb"/>')
    b += '<path d="M40 130 q26-12 52 0 q26 12 52 0" class="f-green" fill="none" stroke-width="7"/>'
    return _wrap(b, label='Sliced sashimi on a board')

def lentil():
    b = _plate()
    b += '<path d="M30 100 A70 70 0 0 1 100 30 L100 100 Z" class="f-lentil"/>'
    for x, y in [(52,62),(66,52),(74,70),(58,80),(84,60),(46,74)]:
        b += f'<ellipse cx="{x}" cy="{y}" rx="5" ry="4" class="f-lentil-d"/>'
    for i, (x, y) in enumerate([(112,52),(134,62),(120,76)]):
        b += f'<rect x="{x}" y="{y}" width="30" height="12" rx="6" class="f-char"/>'
    b += '<circle cx="70" cy="140" r="20" class="f-broc"/><circle cx="112" cy="150" r="16" class="f-broc"/>'
    b += '<path d="M138 124 q16-10 26 4 q-12 16-26-4" class="f-avo"/>'
    return _wrap(b, label='A lentil bowl with grilled chicken and vegetables')

def barbecue():
    b = _plate()
    b += ('<path d="M46 92 q22-30 54-22 q34-10 54 22 q-16 26-54 24 q-38 2-54-24 Z" class="f-pork"/>')
    for x, y in [(66,86),(88,78),(110,84),(132,80),(78,96),(104,98),(126,94)]:
        b += f'<ellipse cx="{x}" cy="{y}" rx="7" ry="5" class="f-bark"/>'
    b += ('<path d="M40 126 q30 22 60 0 v40 a70 70 0 0 1-60-40 Z" class="f-collard"/>'
          '<path d="M100 126 q30 22 60 0 v6 a70 70 0 0 1-60 34 Z" class="f-bean"/>')
    return _wrap(b, label='A barbecue plate with greens and beans')

def fish():
    b = _plate()
    b += ('<path d="M42 100 q34-38 78-30 q34 6 40 30 q-6 24-40 30 q-44 8-78-30 Z" class="f-fish"/>'
          '<path d="M42 100 l-18-20 v40 Z" class="f-fish"/>'
          '<circle cx="140" cy="92" r="4.5" class="f-eye"/>'
          '<path d="M74 86 q22 14 0 28 M96 82 q24 18 0 36 M118 84 q20 16 0 32" class="f-scale"/>')
    b += '<circle cx="62" cy="146" r="15" class="f-lemon"/><path d="M62 131 v30 M47 146 h30" class="f-lemonw"/>'
    b += '<path d="M104 142 q22-12 40 2 q-20 14-40-2" class="f-herb"/>'
    return _wrap(b, label='A whole grilled fish with lemon and herbs')

def pizza():
    b = _plate(r=90)
    b += '<circle cx="100" cy="100" r="76" class="f-crust"/><circle cx="100" cy="100" r="66" class="f-sauce"/>'
    for x, y, r in [(78,80,13),(118,74,11),(92,116,12),(126,110,10),(100,94,9),(74,110,8)]:
        b += f'<circle cx="{x}" cy="{y}" r="{r}" class="f-mozz"/>'
    for x, y in [(88,70),(120,96),(84,128),(130,80),(106,122)]:
        b += f'<path d="M{x} {y} q6-7 11 0 q-5 8-11 0" class="f-basil"/>'
    b += '<path d="M100 24 v152 M24 100 h152 M46 46 l108 108 M154 46 L46 154" class="f-cut"/>'
    return _wrap(b, label='A margherita pizza seen from above')

def shrimp():
    b = _plate()
    b += '<path d="M30 100 A70 70 0 0 1 170 100 Z" class="f-steam"/>'
    for cx, cy in [(74,74),(110,66),(140,86),(90,96),(126,102)]:
        b += (f'<path d="M{cx} {cy} q16-12 22 4 q4 16-12 16 q-14-1-10-14" class="f-shrimp"/>'
              f'<circle cx="{cx+20}" cy="{cy+4}" r="2" class="f-eye"/>')
    b += ('<circle cx="66" cy="134" r="14" class="f-broc"/><circle cx="104" cy="146" r="12" class="f-broc"/>'
          '<rect x="126" y="126" width="26" height="9" rx="4" class="f-carrot"/>'
          '<rect x="132" y="142" width="22" height="8" rx="4" class="f-carrot"/>')
    return _wrap(b, label='Steamed shrimp with mixed vegetables')

DISHES = dict(poke=poke, kebab=kebab, sashimi=sashimi, lentil=lentil,
              barbecue=barbecue, fish=fish, pizza=pizza, shrimp=shrimp)
