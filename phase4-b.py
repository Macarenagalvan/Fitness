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

rep(
    '''  <section class="view" id="v-entrenar">
    <div class="card tight"><label class="fld" data-i18n="which_day"></label><select id="trainDaySel" onchange="renderTrain()"></select></div>
    <div id="trainBody"></div>
    <button class="btn" id="saveTrainBtn" style="margin-top:6px;display:none" onclick="saveWorkout()"><span class="ic" id="icCheck"></span><span data-i18n="save_workout"></span></button>
  </section>''',
    '''  <section class="view" id="v-entrenar">
    <div id="trainHub">
      <h2 class="sec"><span class="ic" id="icTrainHub"></span><span data-i18n="nav_train"></span></h2>
      <div class="disclist">
        <button class="disccard" onclick="openStrengthTrain()">
          <span class="ico" id="icoFuerza"></span>
          <span style="flex:1;min-width:0"><span class="ttl" data-i18n="disc_strength"></span><span class="sub" data-i18n="disc_strength_sub"></span></span>
          <span class="goarr">›</span>
        </button>
        <button class="disccard" onclick="openYoga()">
          <span class="ico" id="icoYoga"></span>
          <span style="flex:1;min-width:0"><span class="ttl" data-i18n="disc_yoga"></span><span class="sub" data-i18n="disc_yoga_sub"></span></span>
          <span class="goarr">›</span>
        </button>
        <button class="disccard soon" onclick="comingSoon()">
          <span class="ico" id="icoRun"></span>
          <span style="flex:1;min-width:0"><span class="ttl" data-i18n="disc_run"></span><span class="sub" data-i18n="disc_soon"></span></span>
        </button>
        <button class="disccard soon" onclick="comingSoon()">
          <span class="ico" id="icoMob"></span>
          <span style="flex:1;min-width:0"><span class="ttl" data-i18n="disc_mobility"></span><span class="sub" data-i18n="disc_soon"></span></span>
        </button>
      </div>
    </div>
    <div id="trainGym" style="display:none">
      <button class="btn ghost" style="margin-bottom:10px" onclick="showTrainHub()"><span data-i18n="train_back"></span></button>
      <div class="card tight"><label class="fld" data-i18n="which_day"></label><select id="trainDaySel" onchange="renderTrain()"></select></div>
      <div id="trainBody"></div>
      <button class="btn" id="saveTrainBtn" style="margin-top:6px;display:none" onclick="saveWorkout()"><span class="ic" id="icCheck"></span><span data-i18n="save_workout"></span></button>
    </div>
  </section>''',
    "entrenar",
)

rep(
    '''    <div id="photoGallery" style="margin-top:12px"></div>
  </section>
</div>''',
    '''    <div id="photoGallery" style="margin-top:12px"></div>
  </section>

  <section class="view" id="v-mas">
    <h2 class="sec"><span class="ic" id="icMore"></span><span data-i18n="more_title"></span></h2>
    <div class="morelist" id="moreBody"></div>
  </section>
</div>''',
    "mas",
)

rep(
    """ rocket:'<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 3c3.5 2 5.5 5.5 5.5 9.5L15 18H9l-2.5-5.5C6.5 8.5 8.5 5 12 3z\"/><circle cx=\"12\" cy=\"10\" r=\"1.8\"/><path d=\"M9 18l-2 3M15 18l2 3\"/></svg>'\n};""",
    """ rocket:'<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 3c3.5 2 5.5 5.5 5.5 9.5L15 18H9l-2.5-5.5C6.5 8.5 8.5 5 12 3z\"/><circle cx=\"12\" cy=\"10\" r=\"1.8\"/><path d=\"M9 18l-2 3M15 18l2 3\"/></svg>',\n run:'<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"14\" cy=\"4.5\" r=\"1.7\"/><path d=\"M4 19l4.2-3.2 2.3-3.1 3.2 1.4 3.8 5.1M10.5 12.7L8 16M13.5 10.2l2.2-2.6 3.3.6\"/></svg>',\n dots:'<svg viewBox=\"0 0 24 24\" fill=\"currentColor\"><circle cx=\"6\" cy=\"12\" r=\"1.7\"/><circle cx=\"12\" cy=\"12\" r=\"1.7\"/><circle cx=\"18\" cy=\"12\" r=\"1.7\"/></svg>'\n};""",
    "icons",
)

rep(
    '  nav_home:"Inicio", nav_routine:"Rutina", nav_train:"Entrenar", nav_library:"Ejercicios", nav_journal:"Diario", nav_progress:"Progreso",',
    '  nav_home:"Hoy", nav_routine:"Rutina", nav_train:"Entrenar", nav_library:"Ejercicios", nav_journal:"Diario", nav_progress:"Progreso", nav_week:"Semana", nav_more:"Más",\n  disc_strength:"Fuerza", disc_strength_sub:"Tu rutina actual", disc_run:"Running", disc_yoga:"Yoga", disc_yoga_sub:"20 min en casa", disc_mobility:"Movilidad", disc_soon:"Próximamente", coming_soon:"Próximamente", more_title:"Más", train_back:"Volver a disciplinas",',
    "es",
)

p.write_text(s, encoding="utf-8")
print("applied", p.stat().st_size)
