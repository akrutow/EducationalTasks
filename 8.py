class OrderedSet:
    def __init__(self, iterable=None) -> None:
        if iterable:
            self.iterable = list(iterable)
        else:
            self.iterable = []

    def add(self, item):
        self.iterable.append(item)
        return set(self.iterable)

    def discard(self, item):
        if item in self.iterable:
            self.iterable.remove(item)
        return set(self.iterable)

    def __len__(self):
        return len(set(self.iterable))

    def __iter__(self):
        result = []
        for i in self.iterable:
            if i not in result:
                result.append(i)
        yield from result

    def __contains__(self, i):
        return i in set(self.iterable)
    
    def __eq__(self, other):
        if isinstance(other, set):
            return set(self.iterable) == other
        elif isinstance(other, OrderedSet):
            return self.iterable == other.iterable
        return NotImplemented

