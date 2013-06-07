# import Rule, Symbol


class Arc(object):
    def __init__(self, rule, progress, start, end):
        self.set_rule(rule.deepcopy())
        self.set_progress(progress)
        self.set_start(start)
        self.set_end(end)

    def set_rule(self, rule):
        self.rule = rule

    def get_rule(self):
        return self.rule

    def set_progress(self, progress):
        self.progress = progress

    def get_progress(self):
        return self.progress

    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start

    def set_end(self, end):
        self.end = end

    def get_end(self):
        return self.end

    def get_children(self):
        return self.get_rule().get_children()

    def get_child(self, i):
        return self.get_rule().get_child(i)

    def get_mother(self):
        return self.get_rule().get_mother()

    def next_symbol(self):
        if self.get_progress() >= self.size():
            return None
        return self.get_child(self.get_progress())

    def size(self):
        return self.get_rule().size()

    def __str__(self):
        children1 = reduce(
            lambda x, y: x + " " + str(y),
            self.get_children()[0:self.get_progress()], "")
        children2 = reduce(
            lambda x, y: x + " " + str(y),
            self.get_children()[self.get_progress():], "")
        return "{:s} ->{:s} o{:s} from {:d} to {:d}".format(
            self.get_mother(), children1, children2,
            self.get_start(), self.get_end())
