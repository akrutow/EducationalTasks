class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = iterable.copy()

    def append(self, obj):
        return self.iterable.append(obj)

    def pop(self, i=None):
        if i is None:
            return self.iterable.pop(-1)
        else:
            return self.iterable.pop(i)

    def __len__(self):
        return len(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key % len(self.iterable)]
