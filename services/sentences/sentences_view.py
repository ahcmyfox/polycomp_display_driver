import os.path


class SentencesView:
    VIEW_PATH = os.path.join(os.path.dirname(__file__), 'index.html')

    def __init__(self, services):
        self.services = services

    @staticmethod
    def add(path, args):
        return False

    @staticmethod
    def update(path, args):
        return False

    @staticmethod
    def delete(path, args):
        return False

    @staticmethod
    def vote(path, args):
        return False

    def get(self, path, args):
        with open(self.VIEW_PATH, 'r') as content_file:
            return content_file.read()
