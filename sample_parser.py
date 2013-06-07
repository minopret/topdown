from lexicon import Lexicon
from grammar import Grammar
from rule import Rule
from symbol import Symbol
from lexical import Lexical
from parser import Parser
from logger import Logger


class SampleParser(Parser):
    def __init__(self):
        Parser.__init__(self, logger=Logger())

    def make_lexicon(self):
        lexicon = Lexicon()

        the = Lexical("ART", {"ROOT": "?the", "AGR": "?v"})
        the.set_variable("?the", ["the"])
        the.set_variable("?v", ["3s", "3p"])
        lexicon.add_word("the", [the])

        dog = Lexical("N", {"ROOT": "?dog1", "AGR": "?3s"})
        dog.set_variable("?3s", ["3s"])
        dog.set_variable("?dog1", ["DOG1"])
        lexicon.add_word("dog", [dog])

        return lexicon

    def make_grammar(self):
        grammar = Grammar()
        r1 = Rule(
            Symbol("NP", {"AGR": "?a"}), [
                Symbol("ART", {"AGR": "?a"}), Symbol("N", {"AGR": "?a"})])
        r1.set_variable_code("?a", -1L)
        # -1L should be default for any undefined variable
        # that is referenced while constructing
        grammar.add_rule(r1)
        return grammar

    def test(self):
        NP = Lexical("NP", {"AGR": "?x"})
        NP.set_variable_code("?x", -1L)

        lexicon = self.make_lexicon()
        grammar = self.make_grammar()
        sentence = ["the", "dog"]

        self.parse(NP, lexicon, grammar, sentence)


def main():
    SampleParser().test()
    print


if __name__ == '__main__':
    main()
