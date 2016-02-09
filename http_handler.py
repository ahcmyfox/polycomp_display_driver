from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
from display import Display

class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print("Just received a GET request")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        query_components = parse_qs(urlparse(self.path).query)
        
        if 'message' in query_components:
            message = "".join([str(i) for i in query_components["message"]])
            self.wfile.write("OK - " + message)
            dis = Display()
            dis.simple_sliding_message(message)
        else:
            self.wfile.write("ERROR - missing GET parameter \'message\'")
        return

    def log_request(self, code=None, size=None):
        print('Request')

    def log_message(self, format, *args):
        print('Message')

if __name__ == "__main__":
    try:
        server = HTTPServer(('192.168.31.47', 8000), HTTPHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        server.socket.close()