from Arc import Arc
# import Agenda, Grammar, Symbol, Constituent

is_trace_on = 1


class Chart(object):
    def __init__(self, grammar, agenda):
        self.data = []
        self.grammar = grammar
        self.agenda = agenda

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
                except ValueError as v:
                    print(v)

    def introduce(self, arc):
        if is_trace_on:
            print("    An arc can be extended " + str(arc))
        self.data.append(arc)
        self.introduce_symbol(arc.next_symbol(), arc.get_end())

    def introduce_symbol(self, symbol, position):
        if symbol is None:
            return
        if is_trace_on:
            print("Introducing symbol " + str(symbol))
        is_first = 1
        for rule in self.grammar.get_rules():
            if rule.get_mother().get_category() == symbol.get_category():
                if is_trace_on and is_first:
                    print "    Using the top-down rule,",
                    print(" new active arcs are added for " + str(symbol))
                    is_first = 0
                self.introduce(Arc(rule, 0, position, position))
