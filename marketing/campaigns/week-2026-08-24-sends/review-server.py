#!/usr/bin/env python3
"""Review server for the Uno Mas promo assets.
Serves the folder AND accepts POST /save to persist feedback so Claude can read it.
Writes feedback.json (machine) + FEEDBACK.md (human/Claude readable).
Usage: python3 review-server.py [port]
"""
import http.server, socketserver, json, os, sys, datetime

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
ROOT = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(ROOT, "feedback.json")
MD_PATH   = os.path.join(ROOT, "FEEDBACK.md")

LABELS = {
 "A1":"Late Night menu — print (1080x1350)",
 "B1":"Late Night social — feed (1080x1350)",
 "B2":"Late Night social — story (1080x1920)",
 "C1":"Gift card — feed (1080x1350)",
 "C2":"Gift card — story (1080x1920)",
 "C3":"Gift card — table tent (750x1050, 5x7in)",
 "D1":"Email s1 — gift card hero (1200x630)",
 "D2":"Email s2 — Beer & Bites (1200x500)",
 "D3":"Email s3 — Late Night (1200x500)",
 "E1":"SMS — Tue Aug 25, 11am",
 "E2":"SMS — Thu Aug 27, 3-4pm",
 "E3":"SMS — Fri Aug 28, 4pm (recommended add)",
 "E4":"Email subject lines",
 "Q1":"Friday SMS — add it, or swap for Thursday's?",
 "Q2":'"Big F\'N" to every phone — conscious choice?',
 "Q3":"Pre-load split — 140 x $10 / 60 x $20?",
 "GENERAL":"Overall notes",
}
ORDER = list(LABELS.keys())

def write_md(data):
    items = data.get("items", {})
    ts = data.get("updated", "")
    ap = [k for k,v in items.items() if v.get("status")=="approved"]
    ch = [k for k,v in items.items() if v.get("status")=="changes"]
    lines = [
      "# Review Feedback — Gift Card + Late Night",
      "",
      f"**Last saved:** {ts}",
      f"**Approved:** {len(ap)}  ·  **Needs changes:** {len(ch)}  ·  **Untouched:** {len([k for k in ORDER if k not in items or not items[k].get('status')])}",
      "",
      "> Auto-written by review-server.py. Claude reads this file.",
      "",
    ]
    if ch:
        lines += ["## ⚠️ Needs changes", ""]
        for k in ORDER:
            v = items.get(k) or {}
            if v.get("status")=="changes":
                lines.append(f"### {k} — {LABELS.get(k,k)}")
                c=(v.get("comment") or "").strip()
                lines.append(f"{c}" if c else "_(no comment given)_")
                lines.append("")
    if ap:
        lines += ["## ✅ Approved", ""]
        for k in ORDER:
            v = items.get(k) or {}
            if v.get("status")=="approved":
                c=(v.get("comment") or "").strip()
                lines.append(f"- **{k}** — {LABELS.get(k,k)}" + (f"  \n  _note:_ {c}" if c else ""))
        lines.append("")
    # comments with no status
    orphan=[k for k in ORDER if (items.get(k) or {}).get("comment","").strip() and not (items.get(k) or {}).get("status")]
    if orphan:
        lines += ["## 💬 Comments (no decision yet)", ""]
        for k in orphan:
            lines.append(f"### {k} — {LABELS.get(k,k)}")
            lines.append(items[k]["comment"].strip()); lines.append("")
    untouched=[k for k in ORDER if k not in items or (not items[k].get("status") and not items[k].get("comment","").strip())]
    if untouched:
        lines += ["## ⬜ Not yet reviewed", "", ", ".join(untouched), ""]
    open(MD_PATH,"w",encoding="utf8").write("\n".join(lines))

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass
    def do_POST(self):
        if self.path.rstrip("/") != "/save":
            self.send_error(404); return
        try:
            n = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(n) or b"{}")
            data["updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            json.dump(data, open(JSON_PATH,"w",encoding="utf8"), indent=2, ensure_ascii=False)
            write_md(data)
            body = json.dumps({"ok":True,"saved":data["updated"]}).encode()
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.send_header("Content-Length",str(len(body)))
            self.end_headers(); self.wfile.write(body)
        except Exception as e:
            self.send_error(500, str(e))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), H) as httpd:
    print(f"Review server → http://127.0.0.1:{PORT}")
    print(f"Feedback saves to {MD_PATH}")
    httpd.serve_forever()
