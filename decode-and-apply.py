#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
root = Path(".")
def gather(prefix):
    numbered = [root/f"{prefix}.{i}" for i in range(40) if (root/f"{prefix}.{i}").exists()]
    if numbered:
        return "".join(p.read_text().strip() for p in numbered)
    p = root/prefix
    if p.exists():
        return p.read_text().strip()
    raise SystemExit("missing "+prefix)
raw = base64.b64decode(gather("yoga-block.js.b64"))
if hashlib.md5(raw).hexdigest() != "d9bb9147ff9be8c90fe3fc5a490d0f29":
    raise SystemExit("yoga-block md5 mismatch "+hashlib.md5(raw).hexdigest())
Path("yoga-block.js").write_bytes(raw)
Path("i18n-yoga.txt").write_bytes(base64.b64decode(gather("i18n-yoga.txt.b64")))
Path("apply-yoga.py").write_bytes(base64.b64decode(Path("apply-yoga.py.b64").read_text().strip()))
print("decoded", Path("yoga-block.js").stat().st_size, Path("i18n-yoga.txt").stat().st_size)
