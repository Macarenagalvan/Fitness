#!/usr/bin/env python3
import runpy
from pathlib import Path
if 'id="v-mas"' in Path("index.html").read_text(encoding="utf-8") and "function navGo" in Path("index.html").read_text(encoding="utf-8"):
    print("already applied")
    raise SystemExit(0)
for part in ("phase4-a.py","phase4-b.py","phase4-c.py"):
    runpy.run_path(part, run_name="__main__")
print("all parts applied")
