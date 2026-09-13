#!/usr/bin/env python3
# Field Guide Part 7 chart: how fast vs. how capable — the major models and their
# versions, one panel per company (small multiples, shared axes, single house hue).
# Data: notes/research/r27_speed_accuracy_chart.md (Artificial Analysis, 2026-09-13).
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

INK = '#232A31'; SLATE = '#46545F'; MUTE = '#7A8790'
TEAL = '#0E7C7B'; TEAL_DARK = '#0A5B5A'; LINE = '#DCE3E6'; PANEL = '#F2F5F6'

# (label, intelligence index, output speed t/s, label dx, dy, ha)
PANELS = [
    ('Anthropic — Claude', [
        ('Fable 5.1', 53, 67, 8, 0, 'left'),
        ('Opus 5', 51, 53, 2, -4.6, 'center'),
        ('Sonnet 5', 38, 76, 8, 0, 'left'),
        ('Haiku 4.5', 18, 88, 8, 0, 'left'),
    ]),
    ('OpenAI — GPT', [
        ('GPT-6 Astra', 53, 60, 8, 0, 'left'),
        ('5.6 Sol', 47, 58, 8, 0, 'left'),
        ('5.6 Terra', 42, 108, 8, 0, 'left'),
        ('5.6 Luna', 38, 120, 8, -3.2, 'left'),
        ('5.5 Instant', 27, 132, 8, 0, 'left'),
        ('o3 (2025)', 20, 140, 8, -3.2, 'left'),
    ]),
    ('Google — Gemini', [
        ('3.8 Flash', 41, 277, -8, 1.6, 'right'),
        ('3.7 Flash', 40, 311, -8, -3.4, 'right'),
        ('3.6 Flash', 34, 207, 8, 0, 'left'),
        ('3.1 Pro', 30, 115, 8, 0, 'left'),
        ('3.5 Flash-Lite', 23, 365, -8, 0, 'right'),
    ]),
    ('xAI — Grok', [
        ('Grok 4.6', 44, 58, 8, 0, 'left'),
        ('Grok 4.5', 39, 56, 8, 0, 'left'),
        ('Grok 4.3', 25, 118, 8, 0, 'left'),
    ]),
    ('Open weights — self-hostable', [
        ('GLM-5.3', 45, 66, 8, 1.2, 'left'),
        ('Kimi K3', 44, 37, 0, 4.4, 'center'),
        ('DeepSeek V4.1 Flash', 40, 210, 8, 0, 'left'),
        ('DeepSeek V4 Pro', 36, 76, 8, -1.6, 'left'),
        ('Qwen3.8 Max', 40, 40, 2, -4.4, 'center'),
    ]),
]

fig, axes = plt.subplots(2, 3, figsize=(10.4, 6.4), dpi=300, sharex=True, sharey=True)
fig.patch.set_facecolor('white')
plt.rcParams['font.family'] = 'DejaVu Sans'

for idx, ax in enumerate(axes.flat):
    if idx >= len(PANELS):
        # 6th cell: how-to-read + source note
        ax.axis('off')
        ax.text(0.02, 0.96, 'How to read it', fontsize=10.5, fontweight='bold',
                color=INK, transform=ax.transAxes, va='top')
        ax.text(0.02, 0.84,
                'Up = higher on a 10-benchmark capability\n'
                'index · right = writes faster. Same scales\n'
                'in every panel, so companies compare.\n\n'
                'Each model sits at its strongest thinking\n'
                'setting: the heaviest thinkers are high and\n'
                'LEFT — depth is paid for in speed. Flash,\n'
                'Luna and Haiku buy 2–5× the speed.',
                fontsize=8.2, color=SLATE, transform=ax.transAxes, va='top', linespacing=1.3)
        ax.text(0.02, 0.0,
                'Artificial Analysis Intelligence Index v4.3 · median API\n'
                'output speed, tokens/second · Sep 2026. Names churn\n'
                'quarterly; the apps may run an older sibling.',
                fontsize=7.2, color=MUTE, transform=ax.transAxes, va='bottom', linespacing=1.35)
        continue
    title, pts = PANELS[idx]
    ax.set_facecolor('white')
    ax.set_xlim(0, 395)
    ax.set_ylim(10, 58)
    ax.grid(True, color=LINE, linewidth=0.6)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_color(LINE)
    ax.tick_params(colors=SLATE, labelsize=8, length=0)
    ax.set_title(title, fontsize=10.5, fontweight='bold', color=TEAL_DARK, loc='left', pad=6)
    best = max(p[1] for p in pts)
    for name, iq, sp, dx, dy, ha in pts:
        frontier = (iq == best)
        ax.scatter([sp], [iq], s=46 if frontier else 34, color=TEAL, zorder=3,
                   edgecolors='white', linewidths=1.2)
        ax.annotate(name, (sp, iq), xytext=(dx, dy), textcoords='offset points',
                    fontsize=8.2 if frontier else 7.6,
                    fontweight='bold' if frontier else 'normal',
                    color=INK if frontier else SLATE, ha=ha, va='center')

fig.supxlabel('output speed — tokens per second (API median)  →  faster', fontsize=9.5, color=SLATE, y=0.015)
fig.supylabel('↑  capability — Intelligence Index (10-benchmark composite)', fontsize=9.5, color=SLATE, x=0.008)
fig.suptitle('The two speeds, measured — the major models and their versions (Sep 2026)',
             fontsize=13.5, fontweight='bold', color=INK, x=0.055, ha='left', y=0.985, fontfamily='DejaVu Serif')
fig.tight_layout(rect=[0.015, 0.03, 1, 0.955])

out = os.path.join(os.path.dirname(__file__), 'assets', 'speed_accuracy_chart.png')
fig.savefig(out, facecolor='white', bbox_inches='tight')
print('chart written:', out)
