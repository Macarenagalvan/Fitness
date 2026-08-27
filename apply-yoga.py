#!/usr/bin/env python3
from pathlib import Path
p = Path("index.html")
t = p.read_text()
block = Path("yoga-block.js").read_text()

def rep(old, new, label):
    global t
    n = t.count(old)
    if n != 1:
        raise SystemExit(f"FAIL {label}: count={n}")
    t = t.replace(old, new)
    print("ok", label)

CSS = """
.ygwrap{max-width:100%;overflow-x:hidden}
.ygcard{overflow-wrap:anywhere}
.yglive{text-align:center;padding:8px 0 18px}
.ygpose{font-family:Impact,sans-serif;font-size:28px;letter-spacing:1px;line-height:1.1;margin-top:10px}
.ygmeta{color:var(--volt);font-weight:800;margin-top:8px;font-size:16px}
.ygcue{color:var(--muted);font-size:15px;line-height:1.45;margin:10px 8px 0}
#trainYoga{max-width:100%;overflow-x:hidden}
@media(max-width:360px){.ygpose{font-size:22px}.ygcue{font-size:14px}}
"""

rep(
"@media(max-width:360px){.runclock{font-size:52px}.runkind{font-size:24px}}",
"@media(max-width:360px){.runclock{font-size:52px}.runkind{font-size:24px}\n"+CSS,
"css",
)

C="<"+"/div>"
rep(
'<div id="trainRun" style="display:none">',
'<div id="trainYoga" style="display:none"><div id="yogaBody">'+C+C+'<div id="trainRun" style="display:none">',
"pane",
)

rep(
'function navGo(v){ if(v==="entrenar"){ trainPane=(DB.runningSession&&DB.runningSession.active)?"run":"hub"; } go(v); }',
'function navGo(v){ if(v==="entrenar"){ trainPane=(DB.runningSession&&DB.runningSession.active)?"run":(DB.yogaSession&&DB.yogaSession.active)?"yoga":"hub"; } go(v); }',
"navGo",
)

rep(
"function showTrainHub(){\n trainPane=\"hub\";\n const h=document.getElementById(\"trainHub\"),g=document.getElementById(\"trainGym\"),r=document.getElementById(\"trainRun\");\n if(h)h.style.display=\"block\"; if(g)g.style.display=\"none\"; if(r)r.style.display=\"none\";\n renderTrainHub();\n}".replace('\\"', '"') if False else "function showTrainHub(){\n trainPane=\"hub\";\n const h=document.getElementById(\"trainHub\"),g=document.getElementById(\"trainGym\"),r=document.getElementById(\"trainRun\");\n if(h)h.style.display=\"block\"; if(g)g.style.display=\"none\"; if(r)r.style.display=\"none\";\n renderTrainHub();\n}",
"x",
"skip",
)
