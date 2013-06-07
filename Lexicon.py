class Lexicon(object):
    def __init__(self):
        self.data = {}

    # interpretations are instances of Lexical

    def add_word(self, word, interpretations):
        self.data[word] = interpretations

    def get_interpretations(self, word):
        return self.data[word]
