from pathlib import Path
def cat(prefix, dest):
    parts=sorted(Path('.').glob(prefix+'*.txt'))
    if not parts:
        raise SystemExit('missing '+prefix)
    Path(dest).write_text(''.join(p.read_text() for p in parts))
    print('wrote', dest, [p.name for p in parts], Path(dest).stat().st_size)
cat('p8a','apply-hoy.py')
cat('p8h','hoy-block.js')
