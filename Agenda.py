from Constituent import Constituent

is_trace_on = 1


class Agenda(object):
    def __init__(self):
        self.data = []

    def add_constituent(self, constituent):
        self.data.append(constituent)

    def add_constituent(self, symbol, start, end):
        self.data.append(Constituent(symbol, start, end))

    def add_alternatives(self, list, position):
        map(
            lambda symbol, p=position, me=self:
            me.add_constituent(symbol, p, p+1),
            list
        )

    def next_constituent(self):
        constituent = self.data.pop(0)
        if is_trace_on:
            print "Entering " + str(constituent)
        return constituent

    def size(self):
        return len(self.data)
