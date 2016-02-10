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
        
        print(query_components)

        if 'anim' in query_components:
            effect = query_components["anim"][0]
        else:
            effect = "static"

        dis = Display()

        if effect == 'time':
            dis.time_message()
            self.wfile.write("OK")
            return

        if 'message' in query_components:
            messages = [] 
            for message in query_components["message"]:
                messages.append(message)
            self.wfile.write("OK")
            if (effect == 'static'):
                dis.multiple_static_message(messages)
            elif (effect == 'sliding'):
                print ('sliding')
                dis.multiple_sliding_message(messages)
            elif (effect == 'alert'):
                dis.alert_message(messages[0])
            else:
                self.wfile.write("ERROR - unknown anim \'" + effect + "\'")
        else:
            self.wfile.write("ERROR - missing GET parameter \'message\'")
        return

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