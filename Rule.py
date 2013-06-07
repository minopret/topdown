from Scope import Scope


class Rule(Scope):
    def __init__(self, mother, children):
        Scope.__init__(self)
        self.set_mother(mother)
        self.set_children(children)

    def set_mother(self, mother):
        mother.set_scope(self)
        self.mother = mother

    def get_mother(self):
        return self.mother

    def set_children(self, children):
        for child in children:
            child.set_scope(self)
        self.children = children

    def get_children(self):
        return self.children

    def get_child(self, i):
        return self.get_children()[i]

    def size(self):
        return len(self.get_children())

    def deepcopy(self):
        mother = self.get_mother().deepcopy()
        children = [x.deepcopy() for x in self.get_children()]

        copy = Rule(mother, children)

        Scope.deepcopy(self, copy)

        # I haven't thought through whether the next lines are necessary.
        # They don't hurt.
        copy.get_mother().set_scope(copy)
        for child in copy.get_children():
            child.set_scope(copy)

        return copy

    def __str__(self):
        return str(self.get_mother()) + " ->" + reduce(
            lambda x, y: x + " " + str(y), self.get_children())
