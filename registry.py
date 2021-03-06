class Registry(object):
    NOT_PRESENT = "-"
    instance = None

    def __init__(self):
        self.value = []
        self.index = {}

    def encode(self, value):
        if value not in self.index:
            self.index[value] = len(self.value)
            self.value.append(value)
        return 1L << self.index[value]

    def decode(self, bits):
        return [
            self.value[i]
            for i in range(len(self.value))
            if bits & (1L << i) != 0
        ]

Registry_instance = Registry()
Registry.instance = Registry_instance
Registry.instance.encode(Registry.NOT_PRESENT)
