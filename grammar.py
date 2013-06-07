from rule import Rule


class Grammar(object):
    def __init__(self):
        self.data = []

    def add_rule(self, rule):
        self.data.append(rule)

    def add_new_rule(self, mother, children):
        self.add_rule(Rule(mother, children))

    def get_rules(self):
        return self.data
