/* ===== FASE 5 · RUNNING ===== */
function ensureRunningDB(d){
 if(!d.programs||typeof d.programs!=="object") d.programs={};
 const r=d.programs.running;
 if(!r||typeof r!=="object"){
  d.programs.running={week:1,completedSessions:[],history:[],startedAt:null,lastDecision:null,lastRunAt:null,jogSec:0};
 }else{
  if(!(r.week>=1&&r.week<=24)) r.week=1;
  if(!Array.isArray(r.completedSessions)) r.completedSessions=[];
  if(!Array.isArray(r.history)) r.history=[];
  if(r.jogSec==null) r.jogSec=0;
 }
 if(d.runningSession===undefined) d.runningSession=null;
 if(!Array.isArray(d.runningAchievements)) d.runningAchievements=[];
 return d;
}
function runProg(){ ensureRunningDB(DB); return DB.programs.running; }
function runWeekDef(w){ return RUNNING_PROGRAM.find(x=>x.week===(w||runProg().week))||RUNNING_PROGRAM[0]; }
function runSessDef(week,id){ return (runWeekDef(week).sessions||[]).find(s=>s.id===id)||null; }
function runRequired(week){ return (runWeekDef(week).sessions||[]).filter(s=>!s.optional); }
function runFmt(sec){ sec=Math.max(0,Math.round(+sec||0)); const m=Math.floor(sec/60),s=sec%60; return m+":"+String(s).padStart(2,"0"); }
function runFmtPretty(sec){ sec=Math.max(0,Math.round(+sec||0)); if(sec<60) return sec+" s"; if(sec%60===0) return (sec/60)+" min"; return runFmt(sec); }
function runSessionTitle(s){
 if(!s) return "";
 if(s.type==="intervals") return s.sets+" × "+runFmtPretty(s.workSec)+" / "+runFmtPretty(s.walkSec);
 if(s.type==="walk") return t("run_walk_min",{n:Math.round(s.sec/60)});
 if(s.distKm) return t("run_dist_or_time",{km:s.distKm,n:Math.round(s.sec/60)});
 return t("run_cont_min",{n:Math.round((s.secMin||s.sec)/60)});
}
function runBuildSteps(s){
 const steps=[];
 if(!s) return steps;
 if(s.type==="intervals"){
  for(let i=0;i<s.sets;i++){
   steps.push({id:"w"+i,label:t("run_jog"),sec:s.workSec,kind:"run"});
   steps.push({id:"r"+i,label:t("run_walk"),sec:s.walkSec,kind:"walk"});
  }
 }else{
  steps.push({id:"main",label:s.type==="walk"?t("run_walk"):t("run_run"),sec:s.sec,kind:s.type==="walk"?"walk":"run"});
 }
 return steps;
}
function runWorkSec(s){
 if(!s) return 0;
 if(s.type==="intervals") return s.sets*s.workSec;
 if(s.type==="walk") return 0;
 return s.sec||0;
}
function runDoneRequired(week){
 const ids=new Set(runRequired(week).map(s=>s.id));
 const got=new Set();
 (runProg().completedSessions||[]).forEach(c=>{
  if(c.week===week&&ids.has(c.sessionId)&&!c.repeat) got.add(c.sessionId);
 });
 return got;
}
function runIsRequiredDone(week,id){ return runDoneRequired(week).has(id); }

const RUNNING_PROGRAM=[
 {week:1,phase:"walkrun",goalKey:"run_g1",rpe:"2–3",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:30,walkSec:120,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:30,walkSec:120,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:25*60,optional:1,warmup:0,cooldown:0}]},
 {week:2,phase:"walkrun",goalKey:"run_g2",rpe:"2–3",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:28*60,optional:1,warmup:0,cooldown:0}]},
 {week:3,phase:"walkrun",goalKey:"run_g3",rpe:"3",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:60,walkSec:90,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:60,walkSec:90,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:30*60,optional:1,warmup:0,cooldown:0}]},
 {week:4,phase:"walkrun",goalKey:"run_g4",rpe:"3",sessions:[
  {id:"s1",type:"intervals",sets:10,workSec:60,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:10,workSec:60,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:30*60,optional:1,warmup:0,cooldown:0}]},
 {week:5,phase:"walkrun",goalKey:"run_g5",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:90,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:90,walkSec:60,warmup:1,cooldown:1}]},
 {week:6,phase:"walkrun",goalKey:"run_g6",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:120,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:120,walkSec:60,warmup:1,cooldown:1}]},
 {week:7,phase:"walkrun",goalKey:"run_g7",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:6,workSec:180,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:6,workSec:180,walkSec:60,warmup:1,cooldown:1}]},
 {week:8,phase:"walkrun",goalKey:"run_g8",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:5,workSec:240,walkSec:90,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:5,workSec:240,walkSec:90,warmup:1,cooldown:1}]},
 {week:9,phase:"walkrun",goalKey:"run_g9",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:5,workSec:300,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:5,workSec:300,walkSec:60,warmup:1,cooldown:1}]},
 {week:10,phase:"transition",goalKey:"run_g10",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:3,workSec:480,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:2,workSec:600,walkSec:120,warmup:1,cooldown:1}]},
 {week:11,phase:"transition",goalKey:"run_g11",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:2,workSec:720,walkSec:120,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:17*60,warmup:1,cooldown:1}]},
 {week:12,phase:"transition",goalKey:"run_g12",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:21*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:24*60,warmup:1,cooldown:1}]},
 {week:13,phase:"k5",goalKey:"run_g13",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:27*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:28*60,warmup:1,cooldown:1}]},
 {week:14,phase:"k5",goalKey:"run_g14",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:30*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:25*60,warmup:1,cooldown:1}]},
 {week:15,phase:"k5",goalKey:"run_g15",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:34*60,distKm:"5",askKm:1,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:28*60,warmup:1,cooldown:1}]},
 {week:16,phase:"build",goalKey:"run_g16",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:30*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:39*60,role:"long",warmup:1,cooldown:1}]},
 {week:17,phase:"build",goalKey:"run_g17",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:30*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:44*60,role:"long",warmup:1,cooldown:1}]},
 {week:18,phase:"build",goalKey:"run_g18",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:31*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:49*60,role:"long",warmup:1,cooldown:1}]},
 {week:19,phase:"build",goalKey:"run_g19",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:30*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:48*60,role:"long",distKm:"7-8",askKm:1,warmup:1,cooldown:1}]},
 {week:20,phase:"build",goalKey:"run_g20",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:32*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:55*60,role:"long",warmup:1,cooldown:1}]},
 {week:21,phase:"build",goalKey:"run_g21",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:32*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:60*60,role:"long",warmup:1,cooldown:1}]},
 {week:22,phase:"build",goalKey:"run_g22",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:32*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:68*60,role:"long",warmup:1,cooldown:1}]},
 {week:23,phase:"build",goalKey:"run_g23",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:32*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:60*60,role:"long",distKm:"10",askKm:1,warmup:1,cooldown:1}]},
 {week:24,phase:"build",goalKey:"run_g24",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:32*60,role:"short",warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:75*60,role:"long",distKm:"10-12",askKm:1,warmup:1,cooldown:1}]}
];
