from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import cgi
import re
import os.path
import json

sentence_list = [{"sentence" : "I love chocolat", "person" : "Arnaud", "date":"22/02/2017"}]

def controller_ressource(path, args):
    fname = '.' + path
    if os.path.isfile(fname):
        with open(fname, 'r') as content_file:
            return content_file.read()
    else:
        raise Exception(404)

def controller_root(path, args):
    return controller_ressource('/display_server.html', args)

def controller_list(path, args):
    return json.dumps(sentence_list);

def controller_add(path, args):
    if ((len(args['sentence']) > 0) and (len(args['person']) > 0) and (len(args['sentence']) > 0)):
        sentence_list.append({"sentence" : args['sentence'], "person" : args['person'], "date":args['sentence']})
        return json.dumps({'status':'ok', 'list':sentence_list})
    else:
        return json.dumps({'status':'ko', 'message':'Bad value'})

def controller_delete(path, args):
    return "delete"

class MyHTTPHandler(BaseHTTPRequestHandler):

    handlers = [{'method' : 'get',  'route' : '^\/.+\.[png|jpg|css|js]' , 'callback' : controller_ressource},
                {'method' : 'get',  'route' : '^\/list$'                , 'callback' : controller_list},
                {'method' : 'get',  'route' : '^\/$'                    , 'callback' : controller_root},
                {'method' : 'post', 'route' : '^\/delete$'              , 'callback' : controller_delete},
                {'method' : 'post', 'route' : '^\/add$'                 , 'callback' : controller_add}];

    
    def route(self, method, path, args):

        for handler in self.handlers:
            if ((handler['method'] == method) and (re.match(handler['route'], path))):
                try:
                    contents = handler['callback'](path, args)
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(contents)
                    return
                except Exception as e:
                    self.send_response(e.args[0])
                    self.send_header("Content-type", "plain")
                    self.end_headers()
                    return

        self.send_response(404)
        self.send_header("Content-type", "plain")
        self.end_headers()
        self.wfile.write("404 not found")

    def do_GET(self):

        path  = urlparse(self.path).path
        print("GET " + path)

        query = urlparse(self.path).query
        query_components = dict()

        if len(query) > 0:
            for qc in query.split("&"):
                query_components[qc.split("=")[0]] = qc.split("=")[1]

        self.route('get', path, query_components)


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

        self.route('post', self.path, args)


if __name__ == "__main__":
    try:
        server = HTTPServer(('localhost', 8000), MyHTTPHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        server.socket.close()