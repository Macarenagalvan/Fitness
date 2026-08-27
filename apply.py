#!/usr/bin/env python3
from pathlib import Path
src = Path("index.html")
text = src.read_text()

def rep(old, new, label):
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL {label}: count={n}")
    text = text.replace(old, new)
    print("ok", label)

css = """
.runcard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:14px;margin-bottom:10px}
.runcard .nm{font-weight:800;font-size:16px}
.runlive{text-align:center;padding:8px 0 18px}
.runkind{font-family:Impact,sans-serif;font-size:28px;letter-spacing:1px;margin-top:6px}
.runclock{font-family:Impact,'Arial Narrow',sans-serif;font-size:64px;letter-spacing:1px;color:var(--volt);line-height:1;margin:10px 0}
.runmeta,.runnext{color:var(--muted);font-size:15px;margin-top:6px}
.rungrid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:16px}
.runterm{margin-top:18px;opacity:.7}
.runwu{display:block;padding:10px 0;border-bottom:1px solid var(--line);font-size:15px}
.runwu:last-child{border-bottom:none}
.runhist{padding:8px 0;border-top:1px solid var(--line)}
.runhist:first-of-type{border-top:none}
.rperow{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-top:8px}
.rpeb{min-height:44px;background:var(--surface2);color:var(--txt);border:1px solid var(--line);border-radius:12px;font-weight:800}
.rpeb.on{background:var(--volt);color:#0b0c0f;border-color:var(--volt)}
.pillrow{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
@media(max-width:360px){.runclock{font-size:52px}.runkind{font-size:24px}}
"""
rep(
".morelist .btn svg{width:22px;height:22px;flex:none}",
".morelist .btn svg{width:22px;height:22px;flex:none}\n"+css,
"css",
)
rep(
"""        <button class=\"disccard soon\" onclick=\"comingSoon()\">\n          <span class=\"ico\" id=\"icoRun\"></span>\n          <span style=\"flex:1;min-width:0\"><span class=\"ttl\" data-i18n=\"disc_run\"></span><span class=\"sub\" data-i18n=\"disc_soon\"></span></span>\n        </button>""",
"""        <button class=\"disccard\" onclick=\"openRunning()\">\n          <span class=\"ico\" id=\"icoRun\"></span>\n          <span style=\"flex:1;min-width:0\"><span class=\"ttl\" data-i18n=\"disc_run\"></span><span class=\"sub\" data-i18n=\"disc_run_sub\"></span></span>\n          <span class=\"goarr\">›</span>\n        </button>""",
"card",
)
