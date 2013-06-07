from Registry import *
# from Scope import Scope


class Symbol(object):
    START_SYMBOL_NAME = "S"

    def __init__(self, category, dictionary, scope=None):
        """
        The dictionary maps feature names to variable names.
        Each variable must be defined in the associated scope before use.
        """
        self.category = category
        self.features = 0L
        self.feature = {}
        self.registry = Registry.instance
        self.scope = scope
        for feature in dictionary.keys():
            self.set_feature_variable(feature, dictionary[feature])

    def get_category(self):
        return self.category

    def deepcopy(self):
        copy = Symbol(self.category, {}, self.scope)
        copy.features = self.features
        copy.feature = self.feature.copy()
        copy.registry = self.registry
        return copy

    def set_feature_variable(self, feature, variable):
        self.features = self.features | self.registry.encode(feature)
        self.feature[feature] = variable

    def get_feature_variable(self, feature):
        return self.feature[feature]

    def get_feature_values(self, feature):
        return self.scope.get_variable_values(
            self.get_feature_variable(feature))

    def get_feature_code(self, feature):
        return self.scope.get_variable_code(self.get_feature_variable(feature))

    def reset_feature_code(self, feature, code):
        variable = self.get_feature_variable(feature)
        if variable is None:
            raise ValueError
        return self.scope.set_variable_code(variable, code)

    def get_scope(self):
        return self.scope

    def set_scope(self, scope):
        self.scope = scope

    def resolve(self, symbol):
        """
        Constituents of rules don't act the same for feature matching
        as constituents in the agenda do. This method acts appropriately
        for the case that the "self" constituent is in an arc, while the
        "symbol" constituent is from the agenda.

        It is only necessary to examine features that are present
        in this, the arc constituent.  When the other constituent
        does not mention one of those features, the other constituent
        is assigned a value of "-" (not present) for that feature.
        If, for any feature, the other constituent has a value that
        is not allowed by this constituent's value, then the two
        constituents have no intersection and cannot be resolved.

        Here is another important asymmetry: When our two variables
        intersect, we'll update the value of the variable in my
        scope.
        """

        if self.category != symbol.category:
            raise ValueError('Symbols do not have the same category')

        our_features = self.features & symbol.features
        my_features = self.features & ~symbol.features

        for feature in self.registry.decode(our_features):
            yours = symbol.get_feature_code(feature)
            self.resolve_feature_values(feature, yours)
        for feature in self.registry.decode(my_features):
            yours = self.registry.encode(Registry.NOT_PRESENT)
            self.resolve_feature_values(feature, yours)

    def resolve_feature_values(self, feature, yours):
        mine = self.get_feature_code(feature)
        ours = mine & yours
        if ours == 0L:
            raise ValueError('Symbols do not have the same feature values')
        elif ours == mine:
            pass
        else:
            self.reset_feature_code(feature, ours)

    def __str__(self):
        def feature_value_str(symbol, feature):
            code = symbol.get_feature_code(feature)
            if code == -1L:
                return "%s: %s" % (
                    feature, symbol.get_feature_variable(feature))
            else:
                return "%s: %s" % (feature, symbol.get_feature_values(feature))

        return "%s%s" % (self.category, map(
            lambda x, s=self, f=feature_value_str: f(s, x), self.feature.keys()
        ))
