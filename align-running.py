#!/usr/bin/env python3
from pathlib import Path
p = Path("index.html")
t = p.read_text()

def rep(old, new, label):
    global t
    n = t.count(old)
    if n != 1:
        raise SystemExit(f"FAIL {label}: count={n}")
    t = t.replace(old, new)
    print("ok", label)

rep(
''' {week:2,phase:"walkrun",goalKey:"run_g2",rpe:"2–3",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:28*60,optional:1,warmup:0,cooldown:0}]},''',
''' {week:2,phase:"walkrun",goalKey:"run_g2",rpe:"2–3",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:28*60,secMin:25*60,secMax:30*60,optional:1,warmup:0,cooldown:0}]},''',
"w2-opt",
)

rep(
''' {week:4,phase:"walkrun",goalKey:"run_g4",rpe:"3",sessions:[
  {id:"s1",type:"intervals",sets:10,workSec:60,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:10,workSec:60,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:30*60,optional:1,warmup:0,cooldown:0}]},''',
''' {week:4,phase:"walkrun",goalKey:"run_g4",rpe:"3",sessions:[
  {id:"s1",type:"intervals",sets:10,workSec:60,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:10,workSec:60,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:30*60,optional:1,labelKey:"run_opt_w4",warmup:0,cooldown:0}]},''',
"w4-opt",
)

rep(
''' {week:5,phase:"walkrun",goalKey:"run_g5",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:90,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:90,walkSec:60,warmup:1,cooldown:1}]},''',
''' {week:5,phase:"walkrun",goalKey:"run_g5",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:90,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:90,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:30*60,optional:1,labelKey:"run_opt_w5",warmup:0,cooldown:0}]},''',
"w5-opt",
)

rep(
''' {week:6,phase:"walkrun",goalKey:"run_g6",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:120,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:120,walkSec:60,warmup:1,cooldown:1}]},''',
''' {week:6,phase:"walkrun",goalKey:"run_g6",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:8,workSec:120,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:8,workSec:120,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:25*60,optional:1,labelKey:"run_opt_w6",warmup:0,cooldown:0}]},''',
"w6-opt",
)

rep(
''' {week:7,phase:"walkrun",goalKey:"run_g7",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:6,workSec:180,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:6,workSec:180,walkSec:60,warmup:1,cooldown:1}]},''',
''' {week:7,phase:"walkrun",goalKey:"run_g7",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:6,workSec:180,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:6,workSec:180,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:25*60,optional:1,labelKey:"run_opt_easy",warmup:0,cooldown:0}]},''',
"w7-opt",
)

rep(
''' {week:8,phase:"walkrun",goalKey:"run_g8",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:5,workSec:240,walkSec:90,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:5,workSec:240,walkSec:90,warmup:1,cooldown:1}]},''',
''' {week:8,phase:"walkrun",goalKey:"run_g8",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:5,workSec:240,walkSec:90,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:5,workSec:240,walkSec:90,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:25*60,optional:1,labelKey:"run_opt_easy",warmup:0,cooldown:0}]},''',
"w8-opt",
)

rep(
''' {week:9,phase:"walkrun",goalKey:"run_g9",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:5,workSec:300,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:5,workSec:300,walkSec:60,warmup:1,cooldown:1}]},''',
''' {week:9,phase:"walkrun",goalKey:"run_g9",rpe:"3–4",sessions:[
  {id:"s1",type:"intervals",sets:5,workSec:300,walkSec:60,warmup:1,cooldown:1},
  {id:"s2",type:"intervals",sets:5,workSec:300,walkSec:60,warmup:1,cooldown:1},
  {id:"s3",type:"walk",sec:25*60,optional:1,labelKey:"run_opt_easy",warmup:0,cooldown:0}]},''',
"w9-opt",
)

rep(
'  {id:"s2",type:"continuous",sec:17*60,warmup:1,cooldown:1}]},',
'  {id:"s2",type:"continuous",sec:17*60,secMin:16*60,secMax:18*60,warmup:1,cooldown:1}]},',
"w11-s2",
)

rep(
''' {week:12,phase:"transition",goalKey:"run_g12",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:21*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:24*60,warmup:1,cooldown:1}]},''',
''' {week:12,phase:"transition",goalKey:"run_g12",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:21*60,secMin:20*60,secMax:22*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:24*60,secMin:22*60,secMax:25*60,warmup:1,cooldown:1}]},''',
"w12",
)

rep(
''' {week:13,phase:"k5",goalKey:"run_g13",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:27*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:28*60,warmup:1,cooldown:1}]},''',
''' {week:13,phase:"k5",goalKey:"run_g13",rpe:"3–4",sessions:[
  {id:"s1",type:"continuous",sec:27*60,secMin:25*60,secMax:28*60,warmup:1,cooldown:1},
  {id:"s2",type:"continuous",sec:28*60,secMin:25*60,secMax:28*60,warmup:1,cooldown:1}]},''',
"w13",
)

rep(
'  {id:"s1",type:"continuous",sec:34*60,distKm:"5",askKm:1,warmup:1,cooldown:1},',
'  {id:"s1",type:"continuous",sec:34*60,secMin:32*60,secMax:35*60,distKm:"5",askKm:1,warmup:1,cooldown:1},',
"w15",
)

rep(
'  {id:"s2",type:"continuous",sec:39*60,role:"long",warmup:1,cooldown:1}]},',
'  {id:"s2",type:"continuous",sec:39*60,secMin:38*60,secMax:40*60,role:"long",warmup:1,cooldown:1}]},',
"w16",
)

rep(
'  {id:"s2",type:"continuous",sec:44*60,role:"long",warmup:1,cooldown:1}]},',
'  {id:"s2",type:"continuous",sec:44*60,secMin:42*60,secMax:45*60,role:"long",warmup:1,cooldown:1}]},',
"w17",
)

rep(
'  {id:"s2",type:"continuous",sec:49*60,role:"long",warmup:1,cooldown:1}]},',
'  {id:"s2",type:"continuous",sec:49*60,secMin:48*60,secMax:50*60,role:"long",warmup:1,cooldown:1}]},',
"w18",
)

rep(
'  {id:"s2",type:"continuous",sec:68*60,role:"long",warmup:1,cooldown:1}]},',
'  {id:"s2",type:"continuous",sec:68*60,secMin:65*60,secMax:70*60,role:"long",warmup:1,cooldown:1}]},',
"w22",
)

rep(
'  {id:"s2",type:"continuous",sec:75*60,role:"long",distKm:"10-12",askKm:1,warmup:1,cooldown:1}]}',
'  {id:"s2",type:"continuous",sec:75*60,secMin:70*60,secMax:80*60,role:"long",distKm:"10-12",askKm:1,warmup:1,cooldown:1}]}',
"w24",
)

rep(
'''function runSessionTitle(s){
 if(!s) return "";
 if(s.type==="intervals") return s.sets+" × "+runFmtPretty(s.workSec)+" / "+runFmtPretty(s.walkSec);
 if(s.type==="walk") return t("run_walk_min",{n:Math.round(s.sec/60)});
 if(s.distKm) return t("run_dist_or_time",{km:s.distKm,n:Math.round(s.sec/60)});
 return t("run_cont_min",{n:Math.round((s.secMin||s.sec)/60)});
}''',
'''function runSessionTitle(s){
 if(!s) return "";
 if(s.type==="intervals") return s.sets+" × "+runFmtPretty(s.workSec)+" / "+runFmtPretty(s.walkSec);
 if(s.distKm&&s.secMin&&s.secMax) return t("run_dist_or_range",{km:s.distKm,a:Math.round(s.secMin/60),b:Math.round(s.secMax/60)});
 if(s.distKm) return t("run_dist_or_time",{km:s.distKm,n:Math.round(s.sec/60)});
 if(s.secMin&&s.secMax) return t("run_range_min",{a:Math.round(s.secMin/60),b:Math.round(s.secMax/60)});
 if(s.type==="walk") return t("run_walk_min",{n:Math.round(s.sec/60)});
 return t("run_cont_min",{n:Math.round((s.secMin||s.sec)/60)});
}''',
"title",
)

rep(
'  const ok=runIsRequiredDone(p.week,s.id);\n  const lab=s.optional?t("run_optional"):(s.role==="short"?t("run_short"):s.role==="long"?t("run_long"):t("run_session",{n:s.id==="s1"?1:s.id==="s2"?2:3}));',
'  const ok=s.optional?(runProg().history||[]).some(h=>h.week===p.week&&h.sessionId===s.id):runIsRequiredDone(p.week,s.id);\n  const lab=s.optional?t(s.labelKey||"run_optional"):(s.role==="short"?t("run_short"):s.role==="long"?t("run_long"):t("run_session",{n:s.id==="s1"?1:s.id==="s2"?2:3}));',
"home-label",
)

rep(
'  run_dist_or_time:"{km} km o {n} min",',
'  run_dist_or_time:"{km} km o {n} min",\n  run_dist_or_range:"{km} km o {a}–{b} min",\n  run_range_min:"{a}–{b} min",\n  run_opt_easy:"Opcional fácil",\n  run_opt_w4:"Caminata o repetir semana 3",\n  run_opt_w5:"Caminata o fácil de semana 4",\n  run_opt_w6:"Opcional fácil, solo si recuperaste bien",',
"i18n-es",
)

rep(
'  run_dist_or_time:"{km} km oder {n} Min.",',
'  run_dist_or_time:"{km} km oder {n} Min.",\n  run_dist_or_range:"{km} km oder {a}–{b} Min.",\n  run_range_min:"{a}–{b} Min.",\n  run_opt_easy:"Optionale leichte Einheit",\n  run_opt_w4:"Spaziergang oder Woche 3 wiederholen",\n  run_opt_w5:"Spaziergang oder leichte Einheit aus Woche 4",\n  run_opt_w6:"Leicht, nur wenn du gut erholt bist",',
"i18n-de",
)

p.write_text(t)
print("WROTE", p.stat().st_size)
for k in ["run_opt_w6","secMin:20*60","labelKey","run_dist_or_range","run_range_min"]:
    if k not in t:
        raise SystemExit("missing "+k)
print("sanity ok")
