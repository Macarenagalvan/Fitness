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

rep(
    ".shortbadge{display:inline-flex;align-items:center;gap:5px;background:rgba(255,176,32,.14);color:var(--amber);border:1px solid rgba(255,176,32,.35);padding:5px 9px;border-radius:999px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.4px}\n</style>",
    ".shortbadge{display:inline-flex;align-items:center;gap:5px;background:rgba(255,176,32,.14);color:var(--amber);border:1px solid rgba(255,176,32,.35);padding:5px 9px;border-radius:999px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.4px}\n.disclist{display:flex;flex-direction:column;gap:10px;margin-top:4px}\n.disccard{display:flex;align-items:center;gap:12px;width:100%;text-align:left;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:16px 14px;min-height:72px;color:var(--txt);text-transform:none;letter-spacing:0;font-weight:600}\n.disccard .ico{width:44px;height:44px;border-radius:13px;display:grid;place-items:center;flex:none;background:rgba(202,255,0,.12);color:var(--volt)}\n.disccard .ico svg{width:22px;height:22px}\n.disccard .ttl,.disccard .sub{display:block}\n.disccard .ttl{font-family:Impact,sans-serif;font-size:20px;letter-spacing:1px;line-height:1.05}\n.disccard .sub{font-size:13px;color:var(--muted);margin-top:3px}\n.disccard .goarr{margin-left:auto;color:var(--muted);font-size:22px;line-height:1}\n.disccard.soon{opacity:.78}\n.disccard.soon .ico{background:var(--surface2);color:var(--muted)}\n.morelist{display:flex;flex-direction:column;gap:8px}\n.morelist .btn{justify-content:flex-start;text-transform:none;letter-spacing:.2px;min-height:48px}\n.morelist .btn svg{width:22px;height:22px;flex:none}\n@media(max-width:360px){nav.tabs button{font-size:8.5px} .disccard .ttl{font-size:18px}}\n</style>",
    "v31css",
)

rep(
    '''  <section class="view on" id="v-inicio">
    <div id="todayCard"></div>
    <div class="hub">
      <div class="bub small" style="left:36.5%;top:1.2%" onclick="go('rutina')"><div><div class="bi" id="bubRut"></div><div class="bl" data-i18n="nav_routine"></div></div></div>
      <div class="bub small" style="left:70%;top:25.6%" onclick="go('ejercicios')"><div><div class="bi" id="bubEje"></div><div class="bl" data-i18n="nav_library"></div></div></div>
      <div class="bub small" style="left:57.1%;top:65%" onclick="go('progreso')"><div><div class="bi" id="bubPro"></div><div class="bl" data-i18n="nav_progress"></div></div></div>
      <div class="bub small" style="left:15.6%;top:65%" onclick="go('diario')"><div><div class="bi" id="bubDia"></div><div class="bl" data-i18n="nav_journal"></div></div></div>
      <div class="bub small" style="left:3%;top:25.6%" onclick="go('resumen')"><div><div class="bi" id="bubRes"></div><div class="bl" data-i18n="nav_resumen"></div></div></div>
      <div class="bub center" onclick="go('entrenar')"><div><div class="bi" id="bubEnt"></div><div class="bl" data-i18n="nav_train"></div></div></div>
    </div>
    <div class="hubhint" data-i18n="hub_hint"></div>
  </section>''',
    '''  <section class="view on" id="v-inicio">
    <div id="todayCard"></div>
  </section>''',
    "inicio",
)

p.write_text(s, encoding="utf-8")
print("applied", p.stat().st_size)
