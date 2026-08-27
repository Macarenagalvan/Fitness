#!/usr/bin/env python3
from pathlib import Path
p = Path("index.html")
s = p.read_text(encoding="utf-8")
def rep(old, new, label):
    global s
    n = s.count(old)
    if n != 1:
        raise SystemExit("replace fail %s: count=%s" % (label, n))
    s = s.replace(old, new)

rep("padding-bottom:84px", "padding-bottom:calc(92px + env(safe-area-inset-bottom))", "body")

rep(
    "  nav.tabs{position:fixed;bottom:0;left:0;right:0;background:rgba(11,12,15,.93);backdrop-filter:blur(12px);border-top:1px solid var(--line);display:flex;z-index:50;padding-bottom:env(safe-area-inset-bottom)}\n  nav.tabs button{flex:1;background:none;border:none;color:var(--muted);padding:10px 0 11px;display:flex;flex-direction:column;align-items:center;gap:3px;font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.3px}\n  nav.tabs button.on{color:var(--volt)}\n  nav.tabs svg{width:22px;height:22px}",
    "  nav.tabs{position:fixed;bottom:0;left:0;right:0;background:rgba(11,12,15,.94);backdrop-filter:blur(14px);border-top:1px solid var(--line);display:flex;z-index:50;padding:4px 2px calc(6px + env(safe-area-inset-bottom))}\n  nav.tabs button{flex:1;min-width:0;min-height:48px;background:none;border:none;color:var(--muted);padding:6px 1px 4px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:0;line-height:1.15}\n  nav.tabs button.on{color:var(--volt)}\n  nav.tabs svg{width:22px;height:22px;flex:none}\n  nav.tabs button span{max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}",
    "navcss",
)
