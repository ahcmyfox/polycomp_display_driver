import cgi
import sys
import threading
import time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from urlparse import urlparse
from service_provider import ServicesProvider
from sentences_exceptions import *

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

        sp = ServicesProvider(None)
        
        try:
            contents = sp.get('router').route('GET', path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write(e.get_message())

    def do_POST(self):

        path = urlparse(self.path).path
        print("Just received a POST request")

        args = {}

        if int(self.headers['Content-Length']) > 0:
            form = cgi.FieldStorage(fp=self.rfile,
                                    headers=self.headers,
                                    environ={'REQUEST_METHOD': 'POST',
                                            'CONTENT_TYPE': self.headers['Content-Type'],
                                            })
            for i in form:
                args[i] = form.getvalue(i)

        sp = ServicesProvider(None)

        try:
            contents = sp.get('router').route('POST', path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write(e.get_message())

    def do_DELETE(self):

        path = urlparse(self.path).path
        print("Just received a DELETE request")

        sp = ServicesProvider(None)

        try:
            contents = sp.get('router').route('DELETE', path, {})
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write(e.get_message())

    def do_PATCH(self):

        path = urlparse(self.path).path
        print("Just received a PATCH request")

        args = {}

        if int(self.headers['Content-Length']) > 0:
            form = cgi.FieldStorage(fp=self.rfile,
                                    headers=self.headers,
                                    environ={'REQUEST_METHOD': 'POST',
                                            'CONTENT_TYPE': self.headers['Content-Type'],
                                            })
            for i in form:
                args[i] = form.getvalue(i)

        sp = ServicesProvider(None)

        try:
            contents = sp.get('router').route('PATCH', path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write(e.get_message())

    def do_PUT(self):

        path = urlparse(self.path).path
        print("Just received a PUT request")

        args = {}

        if int(self.headers['Content-Length']) > 0:
            form = cgi.FieldStorage(fp=self.rfile,
                                    headers=self.headers,
                                    environ={'REQUEST_METHOD': 'POST',
                                            'CONTENT_TYPE': self.headers['Content-Type'],
                                            })
            for i in form:
                args[i] = form.getvalue(i)

        sp = ServicesProvider(None)

        try:
            contents = sp.get('router').route('PUT', path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write(e.get_message())

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

if __name__ == "__main__":
    server = SentencesServer(8000, on_update)
    try:
        server.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        sys.exit(0)
