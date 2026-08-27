#!/usr/bin/env python3
from pathlib import Path
import base64
root = Path(".")
parts = []
for n in ["yoga-block.js.b64.a", "yoga-block.js.b64.b", "yoga-block.js.b64"]:
    p = root / n
    if p.exists():
        parts.append(p.read_text().strip())
        if n.endswith(".b64"):
            break
if not parts:
    raise SystemExit("missing yoga b64")
Path("yoga-block.js").write_bytes(base64.b64decode("".join(parts)))
Path("i18n-yoga.txt").write_bytes(base64.b64decode(Path("i18n-yoga.txt.b64").read_text().strip()))
Path("apply-yoga.py").write_bytes(base64.b64decode(Path("apply-yoga.py.b64").read_text().strip()))
print("decoded", Path("yoga-block.js").stat().st_size)
