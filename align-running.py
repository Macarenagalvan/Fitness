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
""" {week:2,phase:\"walkrun\",goalKey:\"run_g2\",rpe:\"2–3\",sessions:[
  {id:\"s1\",type:\"intervals\",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:\"s2\",type:\"intervals\",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:\"s3\",type:\"walk\",sec:28*60,optional:1,warmup:0,cooldown:0}]},""",
""" {week:2,phase:\"walkrun\",goalKey:\"run_g2\",rpe:\"2–3\",sessions:[
  {id:\"s1\",type:\"intervals\",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:\"s2\",type:\"intervals\",sets:8,workSec:45,walkSec:120,warmup:1,cooldown:1},
  {id:\"s3\",type:\"walk\",sec:28*60,secMin:25*60,secMax:30*60,optional:1,warmup:0,cooldown:0}]},""",
"w2-opt",
)
