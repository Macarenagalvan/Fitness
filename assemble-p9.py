from pathlib import Path
def ensure(dest, prefix):
    p=Path(dest)
    if p.exists() and p.stat().st_size>2000:
        print('keep', dest, p.stat().st_size); return
    parts=sorted(Path('.').glob(prefix+'*.txt'))
    if not parts:
        raise SystemExit('missing '+dest)
    p.write_text(''.join(x.read_text() for x in parts))
    print('wrote', dest, p.stat().st_size)
ensure('apply-week.py','p9a')
ensure('week-block.js','p9w')
