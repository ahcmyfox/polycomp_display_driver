from ci_alert import CIAlert
from router import Router
from sentences_list import SentencesList
from sentences_ressource import SentencesRessource
from sentences_view import SentencesView


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ServicesProvider(object):
    __metaclass__ = Singleton

    services = {}

    def __init__(self, server):
        self.services['server'] = server
        self.services['sentences_list'] = SentencesList(self)
        self.services['sentences_view'] = SentencesView(self)
        self.services['sentences_ressource'] = SentencesRessource(self)
        self.services['router'] = Router(self)
        self.services['ci_alert'] = CIAlert(self)

    def has(self, service):
        if (service in self.services):
            return True
        else:
            return False

    def get(self, service):
        if (self.has(service)):
            return self.services[service]
        else:
            return False


if __name__ == "__main__":
    sp = ServicesProvider()
    print (sp)
    print sp.has('router')
    print sp.has('sentences_view')
    print sp.has('bibi')
    sp2 = ServicesProvider()
    print (sp2)
