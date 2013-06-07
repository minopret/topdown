# import Symbol


class Constituent(object):
    def __init__(self, symbol, start, end):
        self.set_symbol(symbol)
        self.set_start(start)
        self.set_end(end)

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start

    def set_end(self, end):
        self.end = end

    def get_end(self):
        return self.end

    def __str__(self):
        return "{:s} from {:d} to {:d}".format(
            self.get_symbol(), self.get_start(), self.get_end())
