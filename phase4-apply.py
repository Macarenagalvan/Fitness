#!/usr/bin/env python3
from pathlib import Path
p = Path("index.html")
s = p.read_text(encoding="utf-8")
if 'id="v-mas"' in s and "function navGo" in s:
    print("already applied")
    raise SystemExit(0)

def rep(old, new, label):
    global s
    n = s.count(old)
    if n != 1:
        raise SystemExit("replace fail %s: count=%s" % (label, n))
    s = s.replace(old, new)

rep("padding-bottom:84px", "padding-bottom:calc(92px + env(safe-area-inset-bottom))", "body")
