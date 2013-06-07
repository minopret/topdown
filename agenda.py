from constituent import Constituent


class Agenda(object):
    def __init__(self, logger=None):
        self.data = []
        self.logger = logger

    def debug(self, s):
        if self.logger is not None:
            self.logger.debug(s)

    def add_constituent(self, symbol, start=None, end=None):
        if start is None and end is None:
            constituent = symbol
            self.data.append(constituent)
        else:
            self.data.append(Constituent(symbol, start, end))

    def add_alternatives(self, list, position):
        for symbol in list:
            self.add_constituent(symbol, position, position + 1)

    def next_constituent(self):
        constituent = self.data.pop(0)
        self.debug("Entering " + str(constituent))
        return constituent

    def size(self):
        return len(self.data)
