#!/usr/bin/env python3
from pathlib import Path
import base64
root = Path(".")
def gather(prefix):
    numbered = [root/f"{prefix}.{i}" for i in range(16) if (root/f"{prefix}.{i}").exists()]
    if numbered:
        return "".join(p.read_text().strip() for p in numbered)
    p = root/prefix
    if p.exists():
        return p.read_text().strip()
    raise SystemExit("missing "+prefix)
Path("yoga-block.js").write_bytes(base64.b64decode(gather("yoga-block.js.b64")))
Path("i18n-yoga.txt").write_bytes(base64.b64decode(gather("i18n-yoga.txt.b64")))
Path("apply-yoga.py").write_bytes(base64.b64decode(Path("apply-yoga.py.b64").read_text().strip()))
print("decoded", Path("yoga-block.js").stat().st_size, Path("i18n-yoga.txt").stat().st_size)
