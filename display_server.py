from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
from cgi import parse_header, parse_multipart

class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print("Just received a GET request")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open('display_server.html', 'r') as content_file:
            self.wfile.write(content_file.read())

    def do_POST(self):

        print("Just received a POST request")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        with open('display_server.html', 'r') as content_file:
            self.wfile.write(content_file.read())

    def log_request(self, code=None, size=None):
        print('Request')

    def log_message(self, format, *args):
        print('Message')

if __name__ == "__main__":
    try:
        server = HTTPServer(('localhost', 8000), HTTPHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        server.socket.close()