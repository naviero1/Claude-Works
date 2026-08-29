#!/usr/bin/env python3
"""Build the sequential ramps for the score cells and verify text contrast on every step.

The document already assigns meaning to three hues - green for the health criteria,
amber for flavor, slate for cost - so those substitute into the sequential slot
rather than the skill's default blue. Each is its own one-hue ramp.
"""
import colorsys

def hex2rgb(h): return tuple(int(h[i:i+2], 16)/255 for i in (1, 3, 5))
def rgb2hex(r, g, b): return '#%02X%02X%02X' % tuple(round(max(0, min(1, v))*255) for v in (r, g, b))
def lum(rgb):
    f = lambda v: v/12.92 if v <= 0.03928 else ((v+0.055)/1.055)**2.4
    r, g, b = (f(v) for v in rgb)
    return 0.2126*r + 0.7152*g + 0.0722*b
def contrast(a, b):
    la, lb = lum(hex2rgb(a)), lum(hex2rgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi+0.05)/(lo+0.05)

def _mk(h, L, S):
    return rgb2hex(*colorsys.hls_to_rgb(h, L, S))

def ramp(anchor, ink, ink_inv, steps=7, l_lo=0.94, l_hi=0.30,
         sat_lo=0.22, sat_hi=1.0, floor=4.5):
    """Interpolate one hue from near-surface to deep, then snap any step that lands
    in the contrast dead band - the mid-ramp lightness where neither ink clears the
    floor - to the nearest lightness on the same side that does."""
    hls = colorsys.rgb_to_hls(*hex2rgb(anchor))
    h, s = hls[0], hls[2]
    out = []
    for i in range(steps):
        t = i/(steps-1)
        L = l_lo + (l_hi - l_lo)*t
        S = s*(sat_lo + (sat_hi - sat_lo)*t)
        best = max(contrast(_mk(h, L, S), ink), contrast(_mk(h, L, S), ink_inv))
        if best < floor:
            # walk toward whichever end is closer, keeping the ramp monotonic
            up = L < 0.5 if l_lo > l_hi else L > 0.5
            for d in [x/400 for x in range(1, 200)]:
                for cand in ([L+d, L-d] if up else [L-d, L+d]):
                    c = max(contrast(_mk(h, cand, S), ink), contrast(_mk(h, cand, S), ink_inv))
                    if c >= floor:
                        L = cand; best = c; break
                else:
                    continue
                break
        out.append(_mk(h, L, S))
    return out

THEMES = {
  'light': dict(surface='#FAFAF6', ink='#171A14', ink_inv='#FAFAF6',
                anchors={'health': '#2E6B49', 'flavor': '#946113', 'cost': '#57687A'},
                l_lo=0.945, l_hi=0.26),
  'dark':  dict(surface='#111309', ink='#EAECE1', ink_inv='#0C0E07',
                anchors={'health': '#79C495', 'flavor': '#DCA750', 'cost': '#93A7BC'},
                l_lo=0.155, l_hi=0.74),
}

RESULT, failures = {}, []
for tname, T in THEMES.items():
    RESULT[tname] = {}
    for group, anchor in T['anchors'].items():
        steps = ramp(anchor, T['ink'], T['ink_inv'], l_lo=T['l_lo'], l_hi=T['l_hi'])
        picked = []
        for s in steps:
            c_ink, c_inv = contrast(s, T['ink']), contrast(s, T['ink_inv'])
            ink = T['ink'] if c_ink >= c_inv else T['ink_inv']
            best = max(c_ink, c_inv)
            picked.append((s, ink, best))
            if best < 4.5: failures.append((tname, group, s, round(best, 2)))
        RESULT[tname][group] = picked

for tname in THEMES:
    print(f"\n{tname.upper()}  surface {THEMES[tname]['surface']}")
    for group, steps in RESULT[tname].items():
        print(f"  {group:7s} " + '  '.join(f"{s}/{c:.1f}" for s, _, c in steps))

print("\ncontrast failures (<4.5:1):", failures or "none - every step carries legible text")

# in-scope checks for a sequential ramp: lightness monotonicity and a stable hue.
# near-neutral steps are excluded from the hue check - at that saturation hue is
# numerically undefined and reports nonsense.
seq_fail = []
for tname, groups in RESULT.items():
    for group, steps in groups.items():
        Ls = [lum(hex2rgb(s)) for s, _, _ in steps]
        mono = all(a > b for a, b in zip(Ls, Ls[1:])) or all(a < b for a, b in zip(Ls, Ls[1:]))
        hs = [colorsys.rgb_to_hls(*hex2rgb(s))[0]*360 for s, _, _ in steps
              if colorsys.rgb_to_hls(*hex2rgb(s))[2] >= 0.06]
        drift = max(hs) - min(hs) if len(hs) > 1 else 0
        if not mono or drift > 8:
            seq_fail.append((tname, group, mono, round(drift, 1)))
print("sequential checks (monotonic lightness, stable hue):",
      seq_fail or "all six ramps pass")
print("\nIdentity never rests on hue: each group sits under its own labelled column")
print("header, the groups are separated by a gap, and every cell prints its number -")
print("the secondary encoding the palette guidance requires.")

import json
json.dump({t: {g: [[s, i] for s, i, _ in v] for g, v in gs.items()} for t, gs in RESULT.items()},
          open('ramps.json', 'w'), indent=1)
