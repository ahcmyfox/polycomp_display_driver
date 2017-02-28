import sys
import os.path
import json

class SentencesList():

    def __init__(self, services):
        self.services = services
        if (os.path.isfile('sentences_save.json')):
            with open('sentences_save.json', 'r') as sentences_file:
                self.sentences = json_loads(sentences_file.read())
        else:
            self.sentences = []

    def add(self, path, args):
        print args
        if ('sentence' in args) and ('person' in args) and ('date' in args):
            self.sentences.append({'sentence' : args['sentence'], 'person' : args['person'], 'date' : args['date']})
        return json.dumps(self.sentences)

    def update(self, path, args):
        if ('id' in args):
            if ('sentence' in args):
                self.sentences['id']['sentence'] = args['sentence']
            if ('person' in args):
                self.sentences['id']['person'] = args['person']
            if ('date' in args):
                self.sentences['id']['date'] = args['date']
        return json.dumps(self.sentences)

    def delete(self, path, args):
        if ('id' in args):
            self.sentences.pop(int(args['id']))
        return json.dumps(self.sentences)

    def get(self, path, args):
        if ('id' in args):
            return json.dumps(self.sentences[args['id']])
        else:
            return json.dumps(self.sentences)

    def serialize(self):
        serialize = []
        for sentence in self.sentences:
            serialize.append(sentence['person'] + " a dit  : \"" + sentence['sentence'] + "\" le " + sentence['date'])
        return serialize

