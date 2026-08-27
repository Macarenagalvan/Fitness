/* ===== SEQ TIMER — motor genérico de secuencias (Fase 3) =====
   Gym rest (startRest/addRest/stopRest) y Yoga V31 siguen con su timer actual.
   No se cablearon acá a propósito: cambiarlos ahora rompe UI/estabilidad.
   Running futuro: seqStart([{id,label,sec,kind},...], {onStep,onTick,onDone,onCancel}).
   Recalcula con Date.now()/seqNow() (targetEnd), no con remaining--.
   snapshot() es el shape persistible; todavía no se guarda en DB.session. */
let _seqClock=null;
function seqNow(){ return _seqClock==null?Date.now():_seqClock; }
function seqSetClock(ms){ _seqClock=ms; }
function seqClearClock(){ _seqClock=null; }
const seqTimer={
 active:false,paused:false,stepIndex:0,steps:[],
 remainingMs:0,elapsedMs:0,startedAt:0,targetEnd:0,pausedAt:0,
 _int:null,_cbs:{},_done:false,_elapsedBefore:0
};
function seqClearInt(){ if(seqTimer._int){clearInterval(seqTimer._int);seqTimer._int=null;} }
function seqReset(){
 seqClearInt();
 seqTimer.active=false;seqTimer.paused=false;seqTimer.stepIndex=0;seqTimer.steps=[];
 seqTimer.remainingMs=0;seqTimer.elapsedMs=0;seqTimer.startedAt=0;seqTimer.targetEnd=0;seqTimer.pausedAt=0;
 seqTimer._cbs={};seqTimer._done=false;seqTimer._elapsedBefore=0;
}
function seqCurrent(){ return seqTimer.steps[seqTimer.stepIndex]||null; }
function seqNext(){ return seqTimer.steps[seqTimer.stepIndex+1]||null; }
function seqRemainingSec(){ return Math.max(0,Math.ceil(seqTimer.remainingMs/1000)); }
function seqElapsedSec(){ return Math.max(0,Math.round(seqTimer.elapsedMs/1000)); }
function seqSnapshot(){
 return {active:seqTimer.active,paused:seqTimer.paused,stepIndex:seqTimer.stepIndex,remainingMs:seqTimer.remainingMs,elapsedMs:seqTimer.elapsedMs,startedAt:seqTimer.startedAt,targetEnd:seqTimer.targetEnd,steps:seqTimer.steps.slice()};
}
function seqArm(idx,overrunMs){
 while(idx<seqTimer.steps.length){
  const st=seqTimer.steps[idx], dur=Math.max(0,(+st.sec||0)*1000), left=dur-Math.max(0,overrunMs||0);
  if(left>0){
   seqTimer.stepIndex=idx; seqTimer.paused=false;
   seqTimer.startedAt=seqNow(); seqTimer.targetEnd=seqTimer.startedAt+left; seqTimer.remainingMs=left;
   if(seqTimer._cbs.onStep) seqTimer._cbs.onStep(st,idx,seqNext());
   return true;
  }
  seqTimer._elapsedBefore+=dur; overrunMs=-(left); idx++;
 }
 seqTimer.stepIndex=Math.max(0,seqTimer.steps.length-1); seqTimer.remainingMs=0; seqTimer.elapsedMs=seqTimer._elapsedBefore; seqFinish(); return false;
}
function seqFinish(){
 if(seqTimer._done)return;
 seqTimer._done=true; seqTimer.active=false; seqTimer.paused=false; seqClearInt();
 if(seqTimer._cbs.onDone) seqTimer._cbs.onDone(seqSnapshot());
}
function seqSync(){
 if(!seqTimer.active||seqTimer.paused||seqTimer._done) return;
 const now=seqNow(), left=seqTimer.targetEnd-now, st=seqCurrent(), dur=st?((+st.sec||0)*1000):0;
 seqTimer.elapsedMs=seqTimer._elapsedBefore+Math.min(dur,Math.max(0,dur-Math.max(0,left)));
 if(left>0){ seqTimer.remainingMs=left; if(seqTimer._cbs.onTick) seqTimer._cbs.onTick(seqTimer); return; }
 seqTimer._elapsedBefore+=dur;
 if(seqTimer.stepIndex>=seqTimer.steps.length-1){ seqTimer.remainingMs=0; seqTimer.elapsedMs=seqTimer._elapsedBefore; seqFinish(); return; }
 seqArm(seqTimer.stepIndex+1,-left);
}
function seqPulse(){
 seqClearInt();
 if(_seqClock!=null)return;
 seqTimer._int=setInterval(seqSync,250);
}
function seqStart(steps,cbs){
 seqReset();
 seqTimer.steps=(steps||[]).map((s,i)=>({id:s.id||('s'+i),label:s.label||'',sec:+s.sec||0,kind:s.kind||''}));
 seqTimer._cbs=cbs||{};
 if(!seqTimer.steps.length)return false;
 seqTimer.active=true;
 if(!seqArm(0,0))return true;
 seqPulse(); seqSync(); return true;
}
function seqPause(){
 if(!seqTimer.active||seqTimer.paused||seqTimer._done)return;
 seqSync();
 if(!seqTimer.active||seqTimer._done)return;
 seqTimer.paused=true; seqTimer.pausedAt=seqNow();
 seqTimer.remainingMs=Math.max(0,seqTimer.targetEnd-seqTimer.pausedAt);
 seqClearInt();
}
function seqResume(){
 if(!seqTimer.active||!seqTimer.paused||seqTimer._done)return;
 seqTimer.paused=false; seqTimer.startedAt=seqNow(); seqTimer.targetEnd=seqTimer.startedAt+seqTimer.remainingMs;
 seqPulse(); seqSync();
}
function seqSkip(){
 if(!seqTimer.active||seqTimer._done)return;
 const st=seqCurrent(), dur=st?((+st.sec||0)*1000):0;
 seqTimer._elapsedBefore+=dur;
 if(seqTimer.stepIndex>=seqTimer.steps.length-1){ seqTimer.remainingMs=0; seqTimer.elapsedMs=seqTimer._elapsedBefore; seqFinish(); return; }
 seqArm(seqTimer.stepIndex+1,0);
 if(!seqTimer.paused) seqPulse();
 seqSync();
}
function seqCancel(){
 if(!seqTimer.active&&!seqTimer.paused){ seqReset(); return; }
 const cb=seqTimer._cbs.onCancel; seqReset(); if(cb)cb();
}
document.addEventListener('visibilitychange',function(){ if(document.visibilityState==='visible') seqSync(); });
document.addEventListener('pageshow',function(){ seqSync(); });
