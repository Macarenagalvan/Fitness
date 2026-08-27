#!/usr/bin/env python3
from pathlib import Path
p = Path("index.html")
t = p.read_text()
block = Path("mobility-block.js").read_text()
es = Path("i18n-es.txt").read_text().rstrip()
de = Path("i18n-de.txt").read_text().rstrip()

def rep(old, new, label):
    global t
    n = t.count(old)
    if n != 1:
        raise SystemExit(f"FAIL {label}: count={n}")
    t = t.replace(old, new)
    print("ok", label)

CSS = """
.mobwrap{max-width:100%;overflow-x:hidden}
.mobcard{overflow-wrap:anywhere}
.mobgoal{color:var(--muted);font-size:15px;line-height:1.4;margin-top:6px}
.moblive{text-align:center;padding:8px 0 18px}
.mobpose{font-family:Impact,sans-serif;font-size:28px;letter-spacing:1px;line-height:1.15;margin-top:12px}
.mobmeta{color:var(--volt);font-weight:800;margin-top:8px;font-size:16px}
.mobcue{color:var(--muted);font-size:15px;line-height:1.45;margin:12px 8px 0}
.mobclock{font-family:Impact,'Arial Narrow',sans-serif;font-size:56px;letter-spacing:1px;color:var(--volt);line-height:1;margin:14px 0 8px}
.mobnav{margin-top:18px;max-width:100%}
.mobnav .btn{min-height:44px}
#trainMob{max-width:100%;overflow-x:hidden}
@media(max-width:360px){.mobpose{font-size:22px}.mobclock{font-size:44px}.mobcue{font-size:14px}}
"""

rep(
"@media(max-width:360px){.ygpose{font-size:22px}.ygcue{font-size:14px}}",
"@media(max-width:360px){.ygpose{font-size:22px}.ygcue{font-size:14px}}\n"+CSS,
"css",
)
