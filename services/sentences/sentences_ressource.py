import sys

class SentencesRessource():

    def __init__(self, services):
        self.services = services

    def add(self, path, args):
        return False

    def update(self, path, args):
        return False

    def delete(self, path, args):
        return False

    def get(self, path, args):
        with open('.' + path, 'r') as content_file:
            return content_file.read()

