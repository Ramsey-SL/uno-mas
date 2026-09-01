#!/bin/bash
# render the local preview to PDF and report the page count
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="${2:-/tmp/promo.pdf}"
rm -f "$OUT"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer --no-sandbox \
  --print-to-pdf="$OUT" --virtual-time-budget=9000 "$1" >/dev/null 2>&1
python3 - "$OUT" <<'PY'
import re,sys,os
p=sys.argv[1]
if not os.path.exists(p): print("  RENDER FAILED"); sys.exit(1)
d=open(p,'rb').read()
n=len(re.findall(rb'/Type\s*/Page[^s]', d))
if n==0:
    m=re.search(rb'/Count\s+(\d+)', d); n=int(m.group(1)) if m else 0
print(f"  {os.path.getsize(p)/1024:.0f} KB   pages: {n}")
PY
