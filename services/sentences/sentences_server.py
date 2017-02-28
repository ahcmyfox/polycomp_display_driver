import  sys
from    BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from    urlparse import urlparse, parse_qs
import  cgi
from    service_provider import ServicesProvider
import  time

class SentencesHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        path  = urlparse(self.path).path
        print("GET " + path)

        query = urlparse(self.path).query
        args = dict()

        if len(query) > 0:
            for qc in query.split("&"):
                args[qc.split("=")[0]] = qc.split("=")[1]

        sp = ServicesProvider()
        contents = sp.get('router').do_GET(path, args)

        if (contents != False):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.send_header("Content-type", "plain")
            self.end_headers()


    def do_POST(self):

        print("Just received a POST request")

        form = cgi.FieldStorage(fp      = self.rfile,
                                headers = self.headers,
                                environ = {'REQUEST_METHOD' : 'POST',
                                           'CONTENT_TYPE' : self.headers['Content-Type'],
                                           })
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        sp = ServicesProvider()
        contents = sp.get('router').do_POST(self.path, args)

        if (contents != False):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.send_header("Content-type", "plain")
            self.end_headers()


    def do_DELETE(self):

        print("Just received a DELETE request")

        form = cgi.FieldStorage(fp      = self.rfile,
                                headers = self.headers,
                                environ = {'REQUEST_METHOD' : 'POST',
                                           'CONTENT_TYPE' : self.headers['Content-Type'],
                                           })
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        sp = ServicesProvider()
        contents = sp.get('router').do_DELETE(self.path, args)

        if (contents != False):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.send_header("Content-type", "plain")
            self.end_headers()


class SentencesServer(HTTPServer, object):

    def __init__(self, port):
        super(SentencesServer, self).__init__(('0.0.0.0', port), SentencesHTTPHandler)
        self.sp = ServicesProvider()

    def get_list(self):
        return self.sp.get('sentences_list').serialize()

if __name__ == "__main__":
    try:
        server = SentencesServer(8000)
        t = 0
        while True:
            t = t + 1
            server.handle_request()
            if (t == 100):
                t = 0
                print server.get_list()
            time.sleep(0.01)
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        server.shutdown()
        server.socket.close()