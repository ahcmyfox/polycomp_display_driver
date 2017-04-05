import sys
import os.path
import json

class SentencesList():

    JSON_PATH = os.path.join(os.path.dirname(__file__), 'sentences_save.json')

    def __init__(self, services):
        self.services = services
        if (os.path.isfile(self.JSON_PATH)):
            with open(self.JSON_PATH, 'r') as sentences_file:
                self.sentences = json.loads(sentences_file.read())
        else:
            self.sentences = []

    def get_sorted_sentences(self):
        sorted_sentences = []
        for i in range(len(self.sentences)):
            vote_max = 0
            for j in range(len(self.sentences)):
                if (self.sentences[j]['vote'] >= vote_max):
                    vote_max_idx = j
                    vote_max = self.sentences[j]['vote']
            sorted_sentences.append(self.sentences[vote_max_idx])
            self.sentences.pop(vote_max_idx)
        self.sentences = sorted_sentences
        return json.dumps(sorted_sentences)

    def on_update(self):
        with open(self.JSON_PATH, 'w') as sentences_file:
            sentences_file.write(json.dumps(self.sentences))
        self.services.get('server').on_update()

    def add(self, path, args):
        print args
        if ('sentence' in args) and ('person' in args) and ('date' in args):
            self.sentences.append({'sentence' : args['sentence'], 'person' : args['person'], 'date' : args['date'], 'vote' : 0})
            self.on_update()
        return self.get_sorted_sentences()

    def update(self, path, args):
        if ('id' in args):
            if ('sentence' in args):
                self.sentences['id']['sentence'] = args['sentence']
            if ('person' in args):
                self.sentences['id']['person'] = args['person']
            if ('date' in args):
                self.sentences['id']['date'] = args['date']
            self.on_update()
        return self.get_sorted_sentences()

    def delete(self, path, args):
        if ('id' in args):
            self.sentences.pop(int(args['id']))
            self.on_update()
        return self.get_sorted_sentences()

    def vote(self, path, args):
        if ('id' in args):
            self.sentences[int(args['id'])]['vote'] += 1 ;
            self.on_update()
        return self.get_sorted_sentences()

    def get(self, path, args):
        if ('id' in args):
            return json.dumps(self.sentences[args['id']])
        else:
            return self.get_sorted_sentences()

    def serialize(self):
        serialize = []
        for sentence in self.sentences:
            serialized = '\"{}\", {}, {}'.format(sentence['sentence'], sentence['person'], sentence['date']);
            serialize.append(serialized)
        return serialize

