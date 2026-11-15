import functools
import http.client
import http.server
from pathlib import Path
import runpy
import tempfile
import threading
import unittest


NoStore = runpy.run_path(str(Path(__file__).resolve().parents[1] /
                            'skills/design-lab/scripts/serve-lab.py'))['NoStore']


class QuietHandler(NoStore):
    def log_message(self, *args):
        pass


class ServeLab(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ('index.html', 'round/index.html', 'round/image.svg', '.env',
                     'x/.git/config', '.temp/index.html', 'unindexed/image.svg',
                     'htm-only/index.htm'):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(name)
        self.server = http.server.ThreadingHTTPServer(
            ('127.0.0.1', 0), functools.partial(QuietHandler, directory=self.root))
        self.addCleanup(self.server.server_close)
        self.thread = threading.Thread(
            target=lambda: self.server.serve_forever(poll_interval=0.01), daemon=True)
        self.thread.start()
        self.addCleanup(self.stop_server)

    def stop_server(self):
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.assertFalse(self.thread.is_alive())

    def request(self, path, expected, method='GET'):
        connection = http.client.HTTPConnection(*self.server.server_address, timeout=5)
        try:
            connection.request(method, path)
            response = connection.getresponse()
            self.assertEqual(response.status, expected, path)
            self.assertEqual(response.getheader('Cache-Control'), 'no-store, max-age=0')
            return response.read()
        finally:
            connection.close()

    def test_visual_files_and_indexes_load_and_refresh(self):
        for path in ('/', '/round/', '/round/image.svg', '/?note=.env'):
            self.request(path, 200)
        (self.root / 'index.html').write_text('revised')
        self.assertEqual(self.request('/', 200), b'revised')
        self.request('/round/image.svg', 200, 'HEAD')

    def test_hidden_segments_are_not_served_even_when_encoded(self):
        for path in ('/.env', '/x/.git/config', '/.temp/', '/%2eenv',
                     '/x/%2egit/config', '/x%2f.git/config', '/round/../index.html'):
            for method in ('GET', 'HEAD'):
                with self.subTest(path=path, method=method):
                    self.request(path, 404, method)

    def test_directories_without_html_index_never_list_files(self):
        for path in ('/unindexed', '/unindexed/', '/htm-only/', '/missing'):
            self.request(path, 404)
        (self.root / 'index.html').unlink()
        self.request('/', 404)


if __name__ == '__main__':
    unittest.main()
