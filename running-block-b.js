let runLive=null, runFb={rpe:3,breath:"controlled",legs:"fresh",could:1,km:""}, runWuOn={};

function runPaneShow(){
 const h=document.getElementById("trainHub"),g=document.getElementById("trainGym"),r=document.getElementById("trainRun");
 if(h)h.style.display="none"; if(g)g.style.display="none"; if(r)r.style.display="block";
}
function showTrainRun(){ trainPane="run"; runPaneShow(); renderRunning(); }
function openRunning(){
 ensureRunningDB(DB);
 if(!runProg().startedAt){ runProg().startedAt=today(); save(); }
 trainPane="run";
 if(DB.runningSession&&DB.runningSession.active) runResumeSession();
 go("entrenar");
}
function runBackHub(){
 if(runLive&&(runLive.view==="active"||runLive.view==="cooldown")&&(seqTimer.active||seqTimer.paused)) runPersist();
 trainPane="hub"; showTrainHub();
}
function runPersist(){
 if(!runLive){ DB.runningSession=null; save(); return; }
 DB.runningSession={
  active:true,week:runLive.week,sessionId:runLive.sessionId,view:runLive.view,
  skippedSteps:runLive.skippedSteps||0,startedAt:runLive.startedAt,
  completedMain:!!runLive.completedMain,
  snap:(seqTimer.active||seqTimer.paused)?seqSnapshot():null
 };
 save();
}
function runClearLive(){ runLive=null; DB.runningSession=null; save(); }
function runCbs(){
 return {
  onStep:function(){ runPaintLive(); runPersist(); },
  onTick:function(){ runPaintLive(); },
  onDone:function(){ runOnSeqDone(); },
  onCancel:function(){}
 };
}
function runResumeSession(){
 const rs=DB.runningSession; if(!rs||!rs.active) return;
 runLive={week:rs.week,sessionId:rs.sessionId,view:rs.view||"active",skippedSteps:rs.skippedSteps||0,startedAt:rs.startedAt||seqNow(),completedMain:!!rs.completedMain};
 if((rs.view==="active"||rs.view==="cooldown")&&rs.snap&&rs.snap.steps&&rs.snap.steps.length){
  if(!(seqTimer.active||seqTimer.paused)) seqRestore(rs.snap,runCbs());
 }
}
function runGapDays(){ const last=runProg().lastRunAt; if(!last) return 0; return daysBetween(last,today()); }
function runGapHint(){
 const d=runGapDays(); if(d<=0) return "";
 if(d>=15) return t("run_gap_long",{n:d});
 if(d>=8) return t("run_gap_mid",{n:d});
 if(d>=1) return t("run_gap_short",{n:d});
 return "";
}
function renderRunning(){
 ensureRunningDB(DB);
 const box=document.getElementById("runBody"); if(!box) return;
 if(runLive){
  if(runLive.view==="warmup"){ box.innerHTML=runHtmlWarmup(); return; }
  if(runLive.view==="active"||runLive.view==="cooldown"){ box.innerHTML=runHtmlLive(); runPaintLive(); return; }
  if(runLive.view==="feedback"){ box.innerHTML=runHtmlFeedback(); return; }
 }
 box.innerHTML=runHtmlHome();
}
function runPhaseLabel(ph){
 return t(ph==="walkrun"?"run_ph_walkrun":ph==="transition"?"run_ph_trans":ph==="k5"?"run_ph_5k":"run_ph_build");
}
