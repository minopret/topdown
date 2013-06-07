from arc import Arc
from symbol import Error


class Chart(object):
    def __init__(self, grammar, agenda, logger=None):
        self.data = []
        self.grammar = grammar
        self.agenda = agenda
        self.logger = logger

    def debug(self, s):
        if self.logger is not None:
            self.logger.debug(s)

    def extend_arcs(self, constituent):
        for arc in self.data:
            if (
                arc.get_end() == constituent.get_start()
                and arc.next_symbol().get_category()
                == constituent.get_symbol().get_category()
            ):
                new_arc = Arc(
                    arc.get_rule(), arc.get_progress(), arc.get_start(),
                    constituent.get_end())
                try:
                    new_arc.next_symbol().resolve(constituent.get_symbol())
                    new_arc.set_progress(new_arc.get_progress() + 1)
                    self.introduce(new_arc)
                    if new_arc.get_progress() == new_arc.size():
                        self.agenda.add_constituent(
                            new_arc.get_mother(), new_arc.get_start(),
                            new_arc.get_end())
                except Error as e:
                    self.debug(e)

    def introduce(self, arc):
        self.debug("    An arc can be extended " + str(arc))
        self.data.append(arc)
        self.introduce_symbol(arc.next_symbol(), arc.get_end())

    def introduce_symbol(self, symbol, position):
        if symbol is None:
            return
        self.debug("Introducing symbol " + str(symbol))
        is_first = 1
        for rule in self.grammar.get_rules():
            if rule.get_mother().get_category() == symbol.get_category():
                if is_first:
                    self.debug(
                        "    Using the top-down rule,"
                        " new active arcs are added for " + str(symbol))
                is_first = 0
                self.introduce(Arc(rule, 0, position, position))
