#!/usr/bin/env python3
"""Assemble the report from parts.

Emits two files from one source of truth (src/body.html + src/style.css + src/app.js):

  index.html     standalone document — open it in any browser, no network needed
                 beyond the Google Fonts link
  artifact.html  body fragment for the Artifact publisher, which supplies its own
                 <!doctype>/<head>/<body> wrapper
"""
import pathlib, re, sys

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent

TITLE = "The Inventory Doctrine"
DESC = ("How supply chain and manufacturing theory treated inventory before 2019, "
        "what COVID broke, and why the KPIs and risk models changed.")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Archivo:wght@400;500;600;700;800&'
         'family=IBM+Plex+Mono:wght@400;500;600&'
         'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&'
         'display=swap">')

body = (SRC / "body.html").read_text()
body = re.sub(r"<!--#include ([\w.-]+)-->",
              lambda m: (SRC / "partials" / m.group(1)).read_text().rstrip(), body)
css = (SRC / "style.css").read_text()
js = "\n".join((SRC / f).read_text() for f in ("app.js", "data-series.js", "data-longarc.js"))

head_bits = f'<title>{TITLE}</title>\n{FONTS}\n<style>\n{css}\n</style>'
tail = f'<script>\n{js}\n</script>'

# --- artifact fragment: no html/head/body tags -------------------------------
(OUT / "artifact.html").write_text(f"{head_bits}\n{body}\n{tail}\n")

# --- standalone document -----------------------------------------------------
(OUT / "index.html").write_text(
    '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    f'<meta name="description" content="{DESC}">\n'
    f'{head_bits}\n'
    '</head>\n<body>\n'
    f'{body}\n{tail}\n'
    '</body>\n</html>\n'
)

for f in ("index.html", "artifact.html"):
    n = len((OUT / f).read_text())
    print(f"{f:16s} {n:>9,d} bytes")
