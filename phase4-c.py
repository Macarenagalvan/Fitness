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
    '  nav_home:"Start", nav_routine:"Plan", nav_train:"Training", nav_library:"Übungen", nav_journal:"Tagebuch", nav_progress:"Fortschritt",',
    '  nav_home:"Heute", nav_routine:"Plan", nav_train:"Training", nav_library:"Übungen", nav_journal:"Tagebuch", nav_progress:"Fortschritt", nav_week:"Woche", nav_more:"Mehr",\n  disc_strength:"Kraft", disc_strength_sub:"Dein aktueller Plan", disc_run:"Laufen", disc_yoga:"Yoga", disc_yoga_sub:"20 Min. zu Hause", disc_mobility:"Mobilität", disc_soon:"Demnächst", coming_soon:"Demnächst", more_title:"Mehr", train_back:"Zurück zu Disziplinen",',
    "de",
)

rep(
    '''const NAV_ITEMS=[
 ["inicio","home","nav_home"],
 ["rutina","clipboard","nav_routine"],
 ["entrenar","dumbbell","nav_train"],
 ["ejercicios","grid","nav_library"],
 ["diario","book","nav_journal"],
 ["progreso","chart","nav_progress"]
];
function buildNav(){
 document.getElementById('navBar').innerHTML=NAV_ITEMS.map(([v,i,k])=>`<button class="${v===currentView?'on':''}" data-v="${v}" onclick="go('${v}')">${ICONS[i]}<span>${t(k)}</span></button>`).join("");
}

/* ===== NAV ===== */
function go(v){ currentView=v; document.querySelectorAll(".view").forEach(s=>s.classList.remove("on")); document.getElementById("v-"+v).classList.add("on");
 document.querySelectorAll("nav.tabs button").forEach(b=>b.classList.toggle("on",b.dataset.v===v)); window.scrollTo(0,0);
 if(v==="inicio")renderHub(); if(v==="resumen")renderResumen(); if(v==="rutina")renderRutina(); if(v==="entrenar")renderTrainSelect(); if(v==="ejercicios")renderLibrary(); if(v==="diario")renderJournal(); if(v==="progreso")renderProgreso(); }''',
    '''const NAV_ITEMS=[
 ["inicio","home","nav_home"],
 ["entrenar","dumbbell","nav_train"],
 ["resumen","calendar","nav_week"],
 ["progreso","chart","nav_progress"],
 ["mas","dots","nav_more"]
];
let trainPane="hub";
function buildNav(){
 document.getElementById('navBar').innerHTML=NAV_ITEMS.map(([v,i,k])=>`<button class="${v===currentView?'on':''}" data-v="${v}" onclick="navGo('${v}')">${ICONS[i]}<span>${t(k)}</span></button>`).join("");
}
function navGo(v){ if(v==="entrenar")trainPane="hub"; go(v); }
function showTrainHub(){
 trainPane="hub";
 const h=document.getElementById("trainHub"),g=document.getElementById("trainGym");
 if(h)h.style.display="block"; if(g)g.style.display="none";
 renderTrainHub();
}
function showTrainGym(){
 trainPane="gym";
 const h=document.getElementById("trainHub"),g=document.getElementById("trainGym");
 if(h)h.style.display="none"; if(g)g.style.display="block";
 renderTrainSelect();
}
function renderTrainHub(){
 setIc("icTrainHub","dumbbell"); setIc("icoFuerza","dumbbell"); setIc("icoYoga","stretchman"); setIc("icoRun","run"); setIc("icoMob","rotate");
}
function openStrengthTrain(){ trainPane="gym"; go("entrenar"); }
function comingSoon(){ showModal(`<h3>${t("coming_soon")}</h3><button class="btn" style="margin-top:10px" onclick="closeModal()">${t("got_it")}</button>`); }
function renderMore(){
 setIc("icMore","dots");
 const box=document.getElementById("moreBody"); if(!box)return;
 box.innerHTML=`<button class="btn sec" onclick="go('diario')">${ICONS.book}<span style="margin-left:8px">${t('nav_journal')}</span></button>
<button class="btn sec" onclick="go('rutina')">${ICONS.clipboard}<span style="margin-left:8px">${t('nav_routine')}</span></button>
<button class="btn sec" onclick="go('ejercicios')">${ICONS.grid}<span style="margin-left:8px">${t('nav_library')}</span></button>
<button class="btn sec" onclick="go('progreso')">${ICONS.camera}<span style="margin-left:8px">${t('ba_title')}</span></button>
<button class="btn sec" onclick="go('progreso')">${ICONS.drop}<span style="margin-left:8px">${t('cycle_title')}</span></button>
<button class="btn sec" onclick="openSettings()">${ICONS.gear}<span style="margin-left:8px">${t('settings')}</span></button>
<button class="btn sec" onclick="exportData()">${ICONS.download}<span style="margin-left:8px">${t('backup_dl')}</span></button>
<button class="btn sec" onclick="document.getElementById('importFileMore').click()">${ICONS.upload}<span style="margin-left:8px">${t('backup_up')}</span></button>
<input type="file" id="importFileMore" accept="application/json" style="display:none" onchange="importData(event)">
<button class="btn sec" onclick="showHelp()">${ICONS.help}<span style="margin-left:8px">${t('how_to')}</span></button>
<button class="btn danger" onclick="wipe()">${t('delete_all')}</button>
<p class="xs muted" style="text-align:center;margin-top:8px">${t('data_local')}</p>`;
}

/* ===== NAV ===== */
function go(v){ currentView=v; document.querySelectorAll(".view").forEach(s=>s.classList.remove("on")); const el=document.getElementById("v-"+v); if(el)el.classList.add("on");
 const tabOn=["inicio","entrenar","resumen","progreso","mas"].includes(v)?v:"mas";
 document.querySelectorAll("nav.tabs button").forEach(b=>b.classList.toggle("on",b.dataset.v===tabOn)); window.scrollTo(0,0);
 if(v==="inicio")renderHub(); if(v==="resumen")renderResumen(); if(v==="rutina")renderRutina();
 if(v==="entrenar"){ if(trainPane==="gym")showTrainGym(); else showTrainHub(); }
 if(v==="ejercicios")renderLibrary(); if(v==="diario")renderJournal(); if(v==="progreso")renderProgreso(); if(v==="mas")renderMore(); }''',
    "navjs",
)

rep(
    "function renderHub(){ setIc('bubEnt','dumbbell');setIc('bubRut','clipboard');setIc('bubEje','grid');setIc('bubDia','book');setIc('bubPro','chart');setIc('bubRes','trophy'); renderTodayCard(); }",
    "function renderHub(){ renderTodayCard(); }",
    "hub",
)

rep(
    'function startSuggested(){ go("entrenar"); setTimeout(()=>{document.getElementById("trainDaySel").value=nextDayIdx();renderTrain();},120); }',
    'function startSuggested(){ trainPane="gym"; go("entrenar"); setTimeout(()=>{const sel=document.getElementById("trainDaySel"); if(sel){sel.value=nextDayIdx();renderTrain();}},120); }',
    "sug",
)

p.write_text(s, encoding="utf-8")
print("applied", p.stat().st_size)
