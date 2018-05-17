class CIAlert:

    def __init__(self, services):
        self.services = services
        self.message = ""

    def add(self, path, args):
        if ('sentence' in args) and ('person' in args) and ('date' in args):
            self.message = self.serialize(args)
        return self.message

    def update(self, path, args):
        return self.add(path, args)

    def delete(self, path, args):
        self.message = ""
        return self.message

    def get(self, path, args):
        return self.message

    @staticmethod
    def serialize(args):
        return '{} {} {}'.format(args['person'], args['date'], args['sentence'])

    def get_message(self):
        return self.message
