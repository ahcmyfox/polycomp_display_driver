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

    def on_update(self):
        with open(self.JSON_PATH, 'w') as sentences_file:
            sentences_file.write(json.dumps(self.sentences))
        self.services.get('server').on_update()

    def add(self, path, args):
        print args
        if ('sentence' in args) and ('person' in args) and ('date' in args):
            self.sentences.append({'sentence' : args['sentence'], 'person' : args['person'], 'date' : args['date']})
            self.on_update()
        return json.dumps(self.sentences)

    def update(self, path, args):
        if ('id' in args):
            if ('sentence' in args):
                self.sentences['id']['sentence'] = args['sentence']
            if ('person' in args):
                self.sentences['id']['person'] = args['person']
            if ('date' in args):
                self.sentences['id']['date'] = args['date']
            self.on_update()
        return json.dumps(self.sentences)

    def delete(self, path, args):
        if ('id' in args):
            self.sentences.pop(int(args['id']))
            self.on_update()
        return json.dumps(self.sentences)

    def get(self, path, args):
        if ('id' in args):
            return json.dumps(self.sentences[args['id']])
        else:
            return json.dumps(self.sentences)

    def serialize(self):
        serialize = []
        for sentence in self.sentences:
            serialized = '\"{}\", {}, {}'.format(sentence['sentence'], sentence['person'], sentence['date']);
            serialize.append(serialized)
        return serialize

