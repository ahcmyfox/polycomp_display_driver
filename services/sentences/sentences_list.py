import json
import os.path
import string
from sentences_exceptions import *

class SentencesList:

    JSON_PATH = os.path.join(os.path.dirname(__file__), 'sentences_save.json')

    def __init__(self, services):
        self.services = services
        if os.path.isfile(self.JSON_PATH):
            with open(self.JSON_PATH, 'r') as sentences_file:
                self.sentences = json.loads(sentences_file.read())
        else:
            self.sentences = []

    def sort_sentences(self):
        vote_max_idx = 0
        sorted_sentences = []
        for i in range(len(self.sentences)):
            vote_max = 0
            for j in range(len(self.sentences)):
                if self.sentences[j]['vote'] > vote_max:
                    vote_max_idx = j
                    vote_max = self.sentences[j]['vote']
            sorted_sentences.append(self.sentences[vote_max_idx])
            self.sentences.pop(vote_max_idx)
        self.sentences = sorted_sentences

    def on_update(self):
        with open(self.JSON_PATH, 'w') as sentences_file:
            sentences_file.write(json.dumps(self.sentences))
        self.services.get('server').on_update()

    def clean_string(self, to_clean):
        printable = set(string.printable)
        for c in to_clean:
            if c not in printable:
                to_clean = to_clean.replace(c, '?')
        return to_clean

    def add(self, path, args):
        print args
        if ('sentence' in args) and ('person' in args) and ('date' in args):
            args['sentence'] = self.clean_string(args['sentence'])
            args['person'] = self.clean_string(args['person'])
            args['date'] = self.clean_string(args['date'])
            self.sentences.append({'sentence' : args['sentence'], 'person' : args['person'], 'date' : args['date'], 'vote' : 0})
            self.on_update()
        return json.dumps(self.sentences)

    def update(self, path, args, id):

        id = int(id)

        if id >= 0 and id < len(self.sentences):

            if 'sentence' in args:
                args['sentence'] = self.clean_string(args['sentence'])
                self.sentences[id]['sentence'] = args['sentence']

            if 'person' in args:
                args['person'] = self.clean_string(args['person'])
                self.sentences[id]['person'] = args['person']

            if 'date' in args:
                args['date'] = self.clean_string(args['date'])
                self.sentences[id]['date'] = args['date']

            self.on_update()

            return json.dumps(self.sentences[id])
        
        else:
            raise RestfulServerNotFound()

    def delete(self, path, args, id):
        id = int(id)
        if id >= 0 and id < len(self.sentences):
            self.sentences.pop(id)
            self.on_update()
            return json.dumps(self.sentences)
        else:
            raise RestfulServerNotFound()

    def vote(self, path, args, id):
        id = int(id)
        if id >= 0 and id < len(self.sentences):
            self.sentences[id]['vote'] += 1
            self.sort_sentences()
            self.on_update()
            return json.dumps(self.sentences[id])
        else:
            raise RestfulServerNotFound()

    def get_all(self, path, args):
        return json.dumps(self.sentences)

    def get(self, path, args, id):
        id = int(id)
        if id >= 0 and id < len(self.sentences):
            return json.dumps(self.sentences[id])
        else:
            raise RestfulServerNotFound()

    def serialize(self):
        serialize = []
        for sentence in self.sentences:
            serialized = '\"{}\", {}, {}'.format(sentence['sentence'], sentence['person'], sentence['date'])
            for i in range(int(sentence['vote'])):
                serialize.append(serialized)
        return serialize
