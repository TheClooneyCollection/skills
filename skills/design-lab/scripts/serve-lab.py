# Serve a design lab folder on 127.0.0.1 with caching off, so the browser never shows a stale page.
# Usage: python3 serve-lab.py <lab dir> [port]   (default port 8091)
import functools, http.server, sys

class NoStore(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

root = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8091
http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(NoStore, directory=root)).serve_forever()
