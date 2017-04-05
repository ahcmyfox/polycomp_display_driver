import sys
import os.path

class SentencesView():

    VIEW_PATH = os.path.join(os.path.dirname(__file__), 'index.html')

    def __init__(self, services):
        self.services = services

    def add(self, path, args):
        return False

    def update(self, path, args):
        return False

    def delete(self, path, args):
        return False

    def vote(self, path, args):
        return False

    def get(self, path, args):
        with open(self.VIEW_PATH, 'r') as content_file:
            return content_file.read()

