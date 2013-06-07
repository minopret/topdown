from Registry import Registry


class Scope(object):
    # map each variable from name to range bits
    def __init__(self):
        self.variable = {}
        self.registry = Registry.instance

    def deepcopy(self, scope=None):
        if scope is None:
            scope = Scope()
        scope.variable = self.variable.copy()
        scope.registry = self.registry
        return scope

    def add_variable_value(self, name, value):
        varname = self.variable.get(name, 0L)
        self.variable[name] = varname | self.registry.encode(value)

    def set_variable(self, name, range):
        self.variable[name] = reduce(
            lambda x, y, s=self: x | s.registry.encode(y),
            range,
            0)

    def set_variable_code(self, name, code):
        self.variable[name] = code

    def get_variable(self, name):
        return self.variable[name]

    def get_variable_code(self, name):
        return self.variable.get(name, 0L)

    def get_variable_values(self, name):
        r = Registry.instance
        return r.decode(self.variable.get(name, 0L))
