import os, ranking_chart as rc
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = """
body{margin:0;background:#FAFAF6;color:#171A14;font:14px/1.5 -apple-system,'Segoe UI',Roboto,sans-serif}
.wrap{max-width:800px;margin:0 auto;padding:26px 20px 40px}
h1{font-size:23px;margin:0 0 4px;letter-spacing:-.01em}
.sub{color:#686C77;margin:0 0 22px;font-size:13.5px;max-width:60ch}
svg.rank87{width:100%;height:auto;display:block}
.rk-head{font:600 8.2px/1 sans-serif;fill:#686C77;letter-spacing:.09em}
.rk-tier{font:700 10.5px/1 sans-serif;fill:#171A14;letter-spacing:.055em}
.rk-tier-n{font-weight:400;fill:#686C77}
.rk-tier-note{font:italic 9.2px/1 Georgia,serif;fill:#686C77}
.rk-rule{stroke:#171A14;stroke-width:.7;opacity:.5}
.rk-stripe{fill:transparent}
.rk-row:nth-child(even) .rk-stripe{fill:#171A14;opacity:.028}
.rk-n{font:500 8.4px/1 ui-monospace,'SF Mono',Menlo,monospace;fill:#9AA0A6}
.rk-d{font:12px/1 -apple-system,sans-serif;fill:#171A14}
.rk-r{font-size:10px;fill:#686C77}
.rk-v{font:600 9.6px/1 ui-monospace,Menlo,monospace;fill:#3F4A44}
.rk-p{font:9.6px/1 ui-monospace,Menlo,monospace;fill:#525F6D}
.rk-pdot{fill:#37424D}
.rk-pstem{stroke:#37424D;stroke-width:.85;opacity:.2}
.rk-pgrid,.rk-sgrid{stroke:#171A14;opacity:.10;stroke-width:.6}
.rk-flag{font:600 8px/1 ui-monospace,Menlo,monospace;fill:#946113}
.rk-ptick{font:7.6px/1 ui-monospace,Menlo,monospace;fill:#9AA0A6}
"""
open(os.path.join(HERE, 'preview87.html'), 'w').write(
    f"<!doctype html><meta charset=utf-8><style>{CSS}</style><div class=wrap>"
    "<h1>All 87 dishes, ranked</h1>"
    "<p class=sub>Bars fall from top to bottom because the list is sorted by them. "
    "The price column beside them is on its own scale and is not sorted by anything. "
    "Read down it.</p>" + rc.chart() + "</div>")
print('ok')
