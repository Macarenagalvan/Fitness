function runHtmlHome(){
 const p=runProg(), w=runWeekDef(p.week), done=runDoneRequired(p.week), gap=runGapHint();
 const sess=(w.sessions||[]).map(s=>{
  const ok=runIsRequiredDone(p.week,s.id);
  const lab=s.optional?t("run_optional"):(s.role==="short"?t("run_short"):s.role==="long"?t("run_long"):t("run_session",{n:s.id==="s1"?1:s.id==="s2"?2:3}));
  return `<div class="runcard"><div class="row between"><div><div class="nm">${esc(lab)}</div><div class="ht">${esc(runSessionTitle(s))}</div></div><span class="badge ${ok?"up":"hold"}">${ok?t("run_done_mark"):t("run_pending")}</span></div><button class="btn" style="margin-top:10px" onclick="runBegin('${s.id}')">${ok?t("run_repeat"):t("run_start")}</button></div>`;
 }).join("");
 const hist=(p.history||[]).slice().reverse().slice(0,12).map(h=>`<div class="runhist"><div><b>${esc(h.date)}</b> · ${t("run_week_n",{n:h.week})} · ${esc(h.title||h.sessionId)}</div><div class="xs muted">${h.durMin||0} min${h.km?(" · "+h.km+" km"):""} · RPE ${h.rpe==null?"—":h.rpe} · ${h.completed?t("run_completed"):t("run_cut")}</div></div>`).join("")||`<div class="empty">${t("run_no_hist")}</div>`;
 const hits=(DB.runningAchievements||[]).slice().reverse().map(a=>`<div class="xs" style="margin-top:6px">🏅 ${esc(t("run_ach_"+a.id))}</div>`).join("")||`<div class="xs muted">${t("run_no_ach")}</div>`;
 return `<button class="btn ghost" style="margin-bottom:10px" onclick="runBackHub()">${t("train_back")}</button>
  <h2 class="sec"><span class="ic">${ICONS.run}</span>${t("disc_run")}</h2>
  <div class="card"><div class="display" style="font-size:26px">${t("run_week_of",{n:p.week})}</div>
   <div class="small muted">${esc(runPhaseLabel(w.phase))} · RPE ${esc(w.rpe)}</div>
   <div style="margin-top:8px">${esc(t(w.goalKey))}</div>
   <div class="xs muted" style="margin-top:8px">${t("run_req_prog",{a:done.size,b:runRequired(p.week).length})}</div></div>
  ${gap?`<div class="note">${esc(gap)}</div>`:""}
  <div class="note">${t("run_pace_tip")}</div>
  ${sess}
  <div class="card"><div class="xs muted" style="text-transform:uppercase;letter-spacing:.5px">${t("run_history")}</div>${hist}</div>
  <div class="card"><div class="xs muted" style="text-transform:uppercase;letter-spacing:.5px">${t("run_milestones")}</div>${hits}</div>
  <div class="card"><div class="xs muted" style="margin-bottom:8px">${t("run_manual")}</div>
   <button class="btn sec" onclick="runRepeatWeek()">${t("run_btn_repeat")}</button>
   <button class="btn sec" style="margin-top:8px" onclick="runShiftWeek(-1)">${t("run_btn_back")}</button>
   <button class="btn ghost" style="margin-top:8px" onclick="runConfirmAdvance()">${t("run_btn_fwd")}</button></div>`;
}
function runBegin(id){
 const p=runProg(), s=runSessDef(p.week,id); if(!s) return;
 runWuOn={};
 runLive={week:p.week,sessionId:id,view:s.warmup?"warmup":"active",skippedSteps:0,startedAt:seqNow(),completedMain:false};
 if(runLive.view==="active") runStartMain();
 else renderRunning();
 runPersist();
}
function runHtmlWarmup(){
 const items=["run_wu_walk","run_wu_ankles","run_wu_knees","run_wu_hips","run_wu_swing","run_wu_squat","run_wu_calf"];
 const rows=items.map(k=>`<label class="runwu"><input type="checkbox" ${runWuOn[k]?"checked":""} onchange="runWuOn['${k}']=this.checked"> ${t(k)}</label>`).join("");
 return `<button class="btn ghost" style="margin-bottom:10px" onclick="runAbortConfirm()">${t("cancel")}</button>
  <h2 class="sec">${t("run_warmup")}</h2><div class="note">${t("run_wu_hint")}</div>
  <div class="card">${rows}</div>
  <button class="btn" onclick="runStartMain()">${t("run_start_ints")}</button>`;
}
function runStartMain(){
 if(!runLive) return;
 const s=runSessDef(runLive.week,runLive.sessionId); if(!s) return;
 runLive.view="active"; runLive.completedMain=false;
 seqStart(runBuildSteps(s),runCbs());
 renderRunning(); runPersist();
}
function runHtmlLive(){
 return `<div class="runlive"><div class="runkind" id="runKind">—</div><div class="runclock" id="runClock">0:00</div>
  <div class="runmeta" id="runMeta"></div><div class="runnext" id="runNext"></div>
  <div class="rungrid"><button class="btn" id="runPauseBtn" onclick="runTogglePause()">${t("run_pause")}</button>
  <button class="btn sec" onclick="runDoSkip()">${t("run_skip")}</button></div>
  <button class="btn ghost runterm" onclick="runAbortConfirm()">${t("run_end")}</button></div>`;
}
function runPaintLive(){
 const kind=document.getElementById("runKind"), clock=document.getElementById("runClock");
 if(!kind||!clock) return;
 const st=seqCurrent(), nxt=seqNext(), isCd=runLive&&runLive.view==="cooldown";
 kind.textContent=st?((st.kind==="run"?t("run_jog"):t("run_walk")).toUpperCase()):(isCd?t("run_cooldown").toUpperCase():"—");
 kind.style.color=st&&st.kind==="run"?"var(--volt)":"var(--blue)";
 clock.textContent=runFmt(seqRemainingSec());
 const s=runLive?runSessDef(runLive.week,runLive.sessionId):null;
 const meta=document.getElementById("runMeta"), nx=document.getElementById("runNext");
 if(s&&s.type==="intervals"&&st&&st.kind==="run"){
  const n=parseInt((st.id||"w0").slice(1),10)+1;
  if(meta) meta.textContent=t("run_rep_of",{a:n,b:s.sets});
 }else if(meta){ meta.textContent=isCd?t("run_cool_hint"):(s?runSessionTitle(s):""); }
 if(nx) nx.textContent=nxt?t("run_next",{lab:nxt.label,t:runFmt(nxt.sec)}):t("run_next_end");
 const pb=document.getElementById("runPauseBtn");
 if(pb) pb.textContent=seqTimer.paused?t("run_resume"):t("run_pause");
}
function runTogglePause(){
 if(!seqTimer.active&&!seqTimer.paused) return;
 if(seqTimer.paused) seqResume(); else seqPause();
 runPaintLive(); runPersist();
}
function runDoSkip(){
 if(!(seqTimer.active||seqTimer.paused)) return;
 if(runLive) runLive.skippedSteps=(runLive.skippedSteps||0)+1;
 seqSkip(); runPaintLive(); runPersist();
}
function runOnSeqDone(){
 if(!runLive) return;
 const s=runSessDef(runLive.week,runLive.sessionId);
 if(runLive.view==="active"&&s&&s.cooldown){
  runLive.view="cooldown"; runLive.completedMain=true;
  seqStart([{id:"cd",label:t("run_walk"),sec:5*60,kind:"walk"}],runCbs());
  renderRunning(); runPersist(); return;
 }
 runLive.completedMain=true; runLive.view="feedback"; seqReset(); renderRunning(); runPersist();
}
function runAbortConfirm(){
 showModal(`<h3>${t("run_end_q")}</h3><p class="small muted">${t("run_end_h")}</p>
  <button class="btn" style="margin-top:10px" onclick="closeModal()">${t("run_keep")}</button>
  <button class="btn danger" style="margin-top:8px" onclick="runAbortNow()">${t("run_end_yes")}</button>`);
}
function runAbortNow(){
 closeModal();
 if(seqTimer.active||seqTimer.paused) seqCancel();
 if(!runLive){ showTrainRun(); return; }
 runLive.view="feedback"; runLive.cutEarly=true; renderRunning(); runPersist();
}
function runHtmlFeedback(){
 const s=runLive?runSessDef(runLive.week,runLive.sessionId):null;
 const askKm=s&&s.askKm;
 const rpeBtns=Array.from({length:10},(_,i)=>i+1).map(n=>`<button class="rpeb ${runFb.rpe===n?"on":""}" onclick="runFb.rpe=${n};renderRunning()">${n}</button>`).join("");
 const breath=[["easy","run_br_easy"],["controlled","run_br_ctrl"],["taxed","run_br_tax"],["gasping","run_br_gasp"]].map(([k,l])=>`<button class="pill ${runFb.breath===k?"on":""}" onclick="runFb.breath='${k}';renderRunning()">${t(l)}</button>`).join("");
 const legs=[["fresh","run_lg_fresh"],["tired","run_lg_tired"],["heavy","run_lg_heavy"],["pain","run_lg_pain"]].map(([k,l])=>`<button class="pill ${k==="pain"?"red":""} ${runFb.legs===k?"on":""}" onclick="runFb.legs='${k}';renderRunning()">${t(l)}</button>`).join("");
 return `<h2 class="sec">${t("run_how")}</h2>
  <div class="card"><div class="xs muted">${t("rpe_label")}</div><div class="rperow">${rpeBtns}</div></div>
  <div class="card"><div class="xs muted">${t("run_breath")}</div><div class="pillrow">${breath}</div></div>
  <div class="card"><div class="xs muted">${t("run_legs")}</div><div class="pillrow">${legs}</div></div>
  <div class="card"><div class="xs muted">${t("run_more_q")}</div><div class="pillrow">
    <button class="pill ${runFb.could===1?"on":""}" onclick="runFb.could=1;renderRunning()">${t("run_yes")}</button>
    <button class="pill ${runFb.could===0?"on":""}" onclick="runFb.could=0;renderRunning()">${t("run_no")}</button></div></div>
  ${askKm?`<div class="card"><label class="fld">${t("run_km_label")}</label><input id="runKm" inputmode="decimal" value="${esc(runFb.km||"")}" placeholder="5.0"></div>`:""}
  <button class="btn" onclick="runSaveFeedback()">${t("finish_save")}</button>
  <button class="btn ghost" style="margin-top:8px" onclick="runDiscard()">${t("cancel")}</button>`;
}
function runDiscard(){ if(seqTimer.active||seqTimer.paused) seqCancel(); runClearLive(); renderRunning(); }
function runDecision(entries){
 const bad=entries.filter(e=>e.rpe>=5||e.breath==="gasping"||e.legs==="heavy"||e.legs==="pain"||e.couldDoAnother===false||!e.completed);
 if(entries.some(e=>e.legs==="pain")) return "pain";
 if(bad.length) return "repeat";
 const good=entries.every(e=>e.completed&&e.rpe<=4&&(e.breath==="easy"||e.breath==="controlled")&&e.legs!=="pain"&&e.couldDoAnother===true);
 return good?"advance":"repeat";
}
function runRequiredLogs(week){
 const ids=runRequired(week).map(s=>s.id), out={};
 (runProg().history||[]).forEach(h=>{ if(h.week===week&&ids.indexOf(h.sessionId)>=0&&!h.repeat) out[h.sessionId]=h; });
 return ids.map(id=>out[id]).filter(Boolean);
}
function runUnlockAchievements(entry){
 const have=new Set((DB.runningAchievements||[]).map(a=>a.id));
 const add=id=>{ if(!have.has(id)){ DB.runningAchievements.push({id,date:today()}); have.add(id); } };
 const hist=runProg().history||[];
 if(hist.length===1) add("first");
 if(runRequired(entry.week).every(s=>hist.some(h=>h.week===entry.week&&h.sessionId===s.id&&h.completed&&!h.repeat))) add("week_pair");
 const jog=runProg().jogSec||0;
 if(jog>=300) add("jog5"); if(jog>=600) add("jog10");
 if(entry.week>=9&&entry.completed) add("block5");
 if(entry.week>=12&&entry.completed&&entry.sessionId==="s1") add("cont20");
 if(entry.week>=14&&entry.completed) add("cont30");
 const km=+entry.km||0;
 if(km>=3) add("km3"); if(km>=5) add("km5"); if(km>=7) add("km7"); if(km>=10) add("km10"); if(km>=11) add("km12");
}
function runSaveFeedback(){
 if(!runLive) return;
 const s=runSessDef(runLive.week,runLive.sessionId); if(!s) return;
 const kmEl=document.getElementById("runKm"); if(kmEl){ const v=(kmEl.value||"").trim(); if(v) runFb.km=v; }
 const planned=runBuildSteps(s).reduce((a,x)=>a+(+x.sec||0),0);
 const extra=(s.cooldown?300:0);
 const elapsed=runLive.cutEarly?Math.max(1,Math.round((seqNow()-runLive.startedAt)/60000)):Math.max(1,Math.round((planned+extra)/60));
 const completed=!runLive.cutEarly && !!runLive.completedMain && (runLive.skippedSteps||0)<Math.max(2,(s.sets||1));
 const already=runIsRequiredDone(runLive.week,runLive.sessionId);
 const entry={
  type:"running",date:today(),week:runLive.week,sessionId:runLive.sessionId,
  durMin:elapsed,completed,rpe:+runFb.rpe,breath:runFb.breath,legs:runFb.legs,
  couldDoAnother:!!runFb.could,skippedSteps:runLive.skippedSteps||0,
  km:runFb.km?String(runFb.km).replace(",","."):null,
  optional:!!s.optional,repeat:already&&!s.optional,exercises:[],
  title:runSessionTitle(s)
 };
 DB.logs.push(entry);
 const p=runProg();
 p.history.push(entry); p.lastRunAt=today();
 p.completedSessions.push({week:entry.week,sessionId:entry.sessionId,date:entry.date,repeat:!!entry.repeat,optional:!!s.optional});
 if(completed) p.jogSec=(p.jogSec||0)+runWorkSec(s);
 runUnlockAchievements(entry);
 let msg="";
 if(!s.optional){
  const reqLogs=runRequiredLogs(entry.week);
  if(reqLogs.length>=runRequired(entry.week).length){
   const decision=runDecision(reqLogs);
   p.lastDecision=decision;
   if(decision==="advance"&&p.week<24){ p.week=p.week+1; msg=t("run_adv_ok",{n:p.week}); }
   else if(decision==="pain") msg=t("run_pain_msg");
   else msg=t("run_rep_msg");
  }
 }
 save();
 if(seqTimer.active||seqTimer.paused) seqCancel();
 runClearLive();
 showModal(`<h3>${t("run_saved")}</h3><p class="small">${msg||t("run_saved_ok")}</p><button class="btn" style="margin-top:10px" onclick="closeModal();renderRunning()">${t("done")}</button>`);
 renderRunning();
}
function runRepeatWeek(){ runProg().lastDecision="repeat"; save(); showModal(`<h3>${t("run_rep_msg")}</h3><button class="btn" style="margin-top:10px" onclick="closeModal();renderRunning()">${t("got_it")}</button>`); }
function runShiftWeek(delta){
 const p=runProg(), nw=Math.max(1,Math.min(24,(p.week||1)+delta));
 if(nw===p.week) return;
 p.week=nw; p.lastDecision=delta<0?"back":"manual"; save(); renderRunning();
}
function runConfirmAdvance(){
 showModal(`<h3>${t("run_fwd_q")}</h3><p class="small muted">${t("run_fwd_h")}</p>
  <button class="btn" style="margin-top:10px" onclick="closeModal();runShiftWeek(1);">${t("run_btn_fwd")}</button>
  <button class="btn ghost" style="margin-top:8px" onclick="closeModal()">${t("cancel")}</button>`);
}
function seqRestore(snap,cbs){
 seqReset();
 if(!snap||!snap.steps||!snap.steps.length) return false;
 seqTimer.steps=snap.steps.slice();
 seqTimer._cbs=cbs||{};
 seqTimer.stepIndex=Math.max(0,Math.min(snap.stepIndex||0,seqTimer.steps.length-1));
 seqTimer._elapsedBefore=0;
 for(let i=0;i<seqTimer.stepIndex;i++) seqTimer._elapsedBefore+=(+(seqTimer.steps[i].sec)||0)*1000;
 seqTimer.active=true; seqTimer._done=false;
 const rem=Math.max(0,+snap.remainingMs||0);
 const st=seqCurrent(), dur=st?((+st.sec||0)*1000):0;
 seqTimer.elapsedMs=seqTimer._elapsedBefore+Math.max(0,dur-rem);
 if(snap.paused){
  seqTimer.paused=true; seqTimer.remainingMs=rem; seqTimer.startedAt=0; seqTimer.targetEnd=0;
  if(seqTimer._cbs.onStep) seqTimer._cbs.onStep(st,seqTimer.stepIndex,seqNext());
  return true;
 }
 seqTimer.paused=false; seqTimer.startedAt=seqNow(); seqTimer.targetEnd=seqTimer.startedAt+rem; seqTimer.remainingMs=rem;
 if(seqTimer._cbs.onStep) seqTimer._cbs.onStep(st,seqTimer.stepIndex,seqNext());
 seqPulse(); seqSync(); return true;
}
