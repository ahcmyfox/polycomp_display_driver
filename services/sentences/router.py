import re
from sentences_exceptions import *

class Router:
    routes = [  {
                    'path': '^\/.+\.[png|jpg|css|js]', 
                    'service': 'sentences_ressource',
                    'endpoints': {
                                    'GET' : 'get'
                                 }
                },
                {
                    'path': '^\/sentences$', 
                    'service': 'sentences_list',
                    'endpoints': {
                                    'GET'    : 'get_all',
                                    'POST'   : 'add'
                                 }
                },
                {
                    'path': '\/sentences\/(?P<id>[0-9]+)$', 
                    'service': 'sentences_list',
                    'endpoints': {
                                    'GET'    : 'get',
                                    'DELETE' : 'delete',
                                    'PATCH'  : 'update',
                                    'PUT'    : 'update'
                                 }
                },
                {
                    'path': '\/sentences\/(?P<id>[0-9]+)\/vote$', 
                    'service': 'sentences_list',
                    'endpoints': {
                                    'POST' : 'vote'
                                 }
                },
                {
                    'path': '^\/ci_alert$', 
                    'service': 'ci_alert',
                    'endpoints': {
                                    'GET'    : 'get',
                                    'POST'   : 'add',
                                    'DELETE' : 'delete'
                                 }
                },
                {
                    'path': '^\/$', 
                    'service': 'sentences_view',
                    'endpoints': {
                                    'GET' : 'get'
                                 }
                }
            ]

    def __init__(self, services):
        self.services = services

    def route(self, method, path, args):
        for route in self.routes:
            url_args = re.match(route['path'], path)
            if url_args:
                if method in route['endpoints']:
                    try:
                        return getattr(self.services.get(route['service']), route['endpoints'][method])(path, args, **url_args.groupdict())
                    except AttributeError:
                        raise RestfulServerBadRequest()
                    except RestfulServerException as e:
                        raise e
                    except Exception:
                        raise RestfulServerInternalServerError()
                else:
                    raise RestfulServerMethodNotAllowed()
        raise RestfulServerNotFound()