import cgi
import sys
import threading
import time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from urlparse import urlparse
from service_provider import ServicesProvider

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class SentencesHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        path = urlparse(self.path).path
        print("GET " + path)

        query = urlparse(self.path).query
        args = dict()

        if len(query) > 0:
            for qc in query.split("&"):
                args[qc.split("=")[0]] = qc.split("=")[1]

        sp = ServicesProvider()
        contents = sp.get('router').do_GET(path, args)

        if contents:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):

        print("Just received a POST request")

        form = cgi.FieldStorage(fp=self.rfile,
                                headers=self.headers,
                                environ={'REQUEST_METHOD': 'POST',
                                         'CONTENT_TYPE': self.headers['Content-Type'],
                                         })
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        sp = ServicesProvider()
        contents = sp.get('router').do_POST(self.path, args)

        if contents:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):

        print("Just received a DELETE request")

        form = cgi.FieldStorage(fp=self.rfile,
                                headers=self.headers,
                                environ={'REQUEST_METHOD': 'POST',
                                         'CONTENT_TYPE': self.headers['Content-Type'],
                                         })
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        sp = ServicesProvider()
        contents = sp.get('router').do_DELETE(self.path, args)

        if contents:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.end_headers()

    def do_PATCH(self):

        print("Just received a PATCH request")

        form = cgi.FieldStorage(fp=self.rfile,
                                headers=self.headers,
                                environ={'REQUEST_METHOD': 'PATCH',
                                         'CONTENT_TYPE': self.headers['Content-Type'],
                                         })
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        sp = ServicesProvider()
        contents = sp.get('router').do_PATCH(self.path, args)

        if contents:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):

        print("Just received a PUT request")

        form = cgi.FieldStorage(fp=self.rfile,
                                headers=self.headers,
                                environ={'REQUEST_METHOD': 'PUT',
                                         'CONTENT_TYPE': self.headers['Content-Type'],
                                         })
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        sp = ServicesProvider()
        contents = sp.get('router').do_PUT(self.path, args)

        if contents:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.end_headers()

class SentencesServer(ThreadedHTTPServer, object):

    def __init__(self, port, update_callback=None):
        super(SentencesServer, self).__init__(('0.0.0.0', port), SentencesHTTPHandler)
        self.sp = ServicesProvider(self)
        self.update_callback = update_callback

    def start(self):
        thread = threading.Thread(target=self.serve_forever)
        thread.daemon = True
        thread.start()

    def stop(self):
        self.shutdown()

    def on_update(self):
        if callable(self.update_callback):
            self.update_callback(self.sp.get('sentences_list').serialize())

    def get_sentences(self):
        return self.sp.get('sentences_list').serialize()

    def get_ci_alert(self):
        return self.sp.get('ci_alert').get_message()


def on_update(content):
    print "SENTENCES UPDATE"
    print content


if __name__ == "__main__":
    server = SentencesServer(8000, on_update)
    try:
        server.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        sys.exit(0)
