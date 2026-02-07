class SparseArray:
    def __init__(self, default) -> None:
        self.default = default
        self.temp = [self.default]
        self.array = []

    def __setitem__(self, key, value):
        self.array.extend(self.temp * (key - len(self.array) + 1))
        self.array[key] = value

    def __getitem__(self, key):
        if key >= len(self.array):
            return self.default
        return self.array[key]

