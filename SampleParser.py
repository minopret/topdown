from Lexicon import Lexicon
from Grammar import Grammar
from Rule import Rule
from Symbol import Symbol
from Lexical import Lexical
from Parser import Parser
# from Registry import Registry


class SampleParser(Parser):
    def test(self):
        NP = Lexical("NP", {"AGR": "?x"})
        NP.set_variable_code("?x", -1L)

        lexicon = Lexicon()

        the = Lexical("ART", {"ROOT": "?the", "AGR": "?v"})
        the.set_variable("?the", ["the"])
        the.set_variable("?v", ["3s", "3p"])
        lexicon.add_word("the", [the])

        dog = Lexical("N", {"ROOT": "?dog1", "AGR": "?3s"})
        dog.set_variable("?3s", ["3s"])
        dog.set_variable("?dog1", ["DOG1"])
        lexicon.add_word("dog", [dog])

        grammar = Grammar()
        r1 = Rule(
            Symbol("NP", {"AGR": "?a"}), [
                Symbol("ART", {"AGR": "?a"}), Symbol("N", {"AGR": "?a"})
            ]
        )
        r1.set_variable_code("?a", -1L)
        # -1L should be default for any undefined variable
        # that is referenced while constructing
        grammar.add_rule(r1)

        sentence = ["the", "dog"]

        self.parse(NP, lexicon, grammar, sentence)


if __name__ == '__main__':
    SampleParser().test()
    print
