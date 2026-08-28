from pathlib import Path
def cat(prefix, dest):
    parts=sorted(Path('.').glob(prefix+'*.txt'))
    if not parts:
        raise SystemExit('missing '+prefix)
    Path(dest).write_text(''.join(p.read_text() for p in parts))
    print('wrote', dest, 'parts', [p.name for p in parts], 'bytes', Path(dest).stat().st_size)
cat('p7a','apply-mobility.py')
cat('p7m','mobility-block.js')
