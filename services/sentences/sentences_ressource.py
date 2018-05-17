import os.path


class SentencesRessource:

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

    @staticmethod
    def get(path, args):
        with open(os.path.dirname(__file__) + path, 'r') as content_file:
            return content_file.read()
