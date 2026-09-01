#!/usr/bin/env python3
"""
No-cache static preview server.

The stdlib http.server sends Last-Modified, so browsers keep replaying a cached
copy and edits appear not to land. This sends explicit no-store headers on every
response, so a plain refresh always shows the current file.

    python3 scripts/preview-server.py 8800 [directory]
"""
import functools, http.server, os, socketserver, sys

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()
    def send_response(self, *a, **k):          # never answer 304
        super().send_response(*a, **k)
    def do_GET(self):
        self.headers.__delitem__("If-Modified-Since") if "If-Modified-Since" in self.headers else None
        self.headers.__delitem__("If-None-Match") if "If-None-Match" in self.headers else None
        super().do_GET()
    def log_message(self, *a): pass

class Reuse(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8800
    root = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
    os.chdir(root)
    with Reuse(("127.0.0.1", port), functools.partial(NoCache, directory=root)) as httpd:
        print(f"no-cache preview on http://127.0.0.1:{port}  root={root}", flush=True)
        httpd.serve_forever()
