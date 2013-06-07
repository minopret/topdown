from symbol import Symbol
from scope import Scope


class Lexical(Symbol, Scope):
    def __init__(self, category, dictionary):
        Symbol.__init__(self, category, dictionary, self)
        Scope.__init__(self)
