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
rep(".morelist .btn svg{width:22px;height:22px;flex:none}", ".morelist .btn svg{width:22px;height:22px;flex:none}\n"+css, "css")
rep('''        <button class="disccard soon" onclick="comingSoon()">
          <span class="ico" id="icoRun"></span>
          <span style="flex:1;min-width:0"><span class="ttl" data-i18n="disc_run"></span><span class="sub" data-i18n="disc_soon"></span></span>
        </button>''', '''        <button class="disccard" onclick="openRunning()">
          <span class="ico" id="icoRun"></span>
          <span style="flex:1;min-width:0"><span class="ttl" data-i18n="disc_run"></span><span class="sub" data-i18n="disc_run_sub"></span></span>
          <span class="goarr">›</span>
        </button>''', "card")
rep('''      <button class="btn" id="saveTrainBtn" style="margin-top:6px;display:none" onclick="saveWorkout()"><span class="ic" id="icCheck"></span><span data-i18n="save_workout"></span></button>
    </div>
  </section>''', '''      <button class="btn" id="saveTrainBtn" style="margin-top:6px;display:none" onclick="saveWorkout()"><span class="ic" id="icCheck"></span><span data-i18n="save_workout"></span></button>
    </div>
    <div id="trainRun" style="display:none">
      <div id="runBody"></div>
    </div>
  </section>''', "pane")
es = Path("i18n-es.txt").read_text().rstrip()+"\n"
de = Path("i18n-de.txt").read_text().rstrip()+"\n"
rep('  onb_name:"Tu nombre (opcional)", onb_goal:"Entrenos por semana"\n },', '  onb_name:"Tu nombre (opcional)", onb_goal:"Entrenos por semana",\n'+es+' },', "i18n-es")
rep('  onb_name:"Dein Name (optional)", onb_goal:"Trainings pro Woche"\n }', '  onb_name:"Dein Name (optional)", onb_goal:"Trainings pro Woche",\n'+de+' }', "i18n-de")
rep('  if(!Array.isArray(d.yogaLogs))d.yogaLogs=[];\n  return d;}}catch(e){} return seed(); }', '  if(!Array.isArray(d.yogaLogs))d.yogaLogs=[];\n  ensureRunningDB(d);\n  return d;}}catch(e){} return seed(); }', "load")
rep('function seed(){ return {lang:"es",name:"",startDate:today(),activeDay:0,routine:defaultRoutine(),logs:[],yogaLogs:[],journal:[],weights:[],photos:[],measures:[],cycle:[],settings:{weeklyGoal:3,cycleLen:28},machineSettings:{},programStartDate:today(),gems:0,frozenWeeks:[],prCount:0,medalsSeen:[],routineMig:true,onboarded:false,session:null}; }', 'function seed(){ return ensureRunningDB({lang:"es",name:"",startDate:today(),activeDay:0,routine:defaultRoutine(),logs:[],yogaLogs:[],journal:[],weights:[],photos:[],measures:[],cycle:[],settings:{weeklyGoal:3,cycleLen:28},machineSettings:{},programStartDate:today(),gems:0,frozenWeeks:[],prCount:0,medalsSeen:[],routineMig:true,onboarded:false,session:null}); }', "seed")
rep("if(!Array.isArray(DB.yogaLogs))DB.yogaLogs=[]; save(); applyStatic(); closeModal(); go(\"inicio\"); alert(t('imported'));", "if(!Array.isArray(DB.yogaLogs))DB.yogaLogs=[]; ensureRunningDB(DB); save(); applyStatic(); closeModal(); go(\"inicio\"); alert(t('imported'));", "import")
rep('''function navGo(v){ if(v==="entrenar")trainPane="hub"; go(v); }
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
}''', '''function navGo(v){ if(v==="entrenar"){ trainPane=(DB.runningSession&&DB.runningSession.active)?"run":"hub"; } go(v); }
function showTrainHub(){
 trainPane="hub";
 const h=document.getElementById("trainHub"),g=document.getElementById("trainGym"),r=document.getElementById("trainRun");
 if(h)h.style.display="block"; if(g)g.style.display="none"; if(r)r.style.display="none";
 renderTrainHub();
}
function showTrainGym(){
 trainPane="gym";
 const h=document.getElementById("trainHub"),g=document.getElementById("trainGym"),r=document.getElementById("trainRun");
 if(h)h.style.display="none"; if(g)g.style.display="block"; if(r)r.style.display="none";
 renderTrainSelect();
}''', "nav")
rep(' if(v==="entrenar"){ if(trainPane==="gym")showTrainGym(); else showTrainHub(); }', ' if(v==="entrenar"){ if(trainPane==="gym")showTrainGym(); else if(trainPane==="run")showTrainRun(); else showTrainHub(); }', "go")
block = Path("running-block-a.js").read_text()+Path("running-block-b.js").read_text()+Path("running-block-c.js").read_text()
rep("/* ===== INIT ===== */", block + "\n/* ===== INIT ===== */", "js")
Path("index.html").write_text(text)
print("WROTE", Path("index.html").stat().st_size)
for k in ["openRunning","RUNNING_PROGRAM","seqRestore","ensureRunningDB","disc_run_sub","trainRun","run_g24"]:
    if k not in text:
        raise SystemExit("missing "+k)
print("sanity ok")
