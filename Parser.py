from Agenda import Agenda
from Chart import Chart


class Parser(object):
    def parse(self, start_symbol, lexicon, grammar, sentence):
        agenda = Agenda()
        chart = Chart(grammar, agenda)
        chart.introduce_symbol(start_symbol, 0)
        position = 0
        while position < len(sentence) or agenda.size() > 0:
            if agenda.size() == 0:
                agenda.add_alternatives(
                    lexicon.get_interpretations(sentence[position]), position)
                position = position + 1
            chart.extend_arcs(agenda.next_constituent())
