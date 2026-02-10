class Grouper:
    def __init__(self, iterable, key):
        self.result = {}
        self.key = key
        for i in iterable:
            if self.key(i) not in self.result:
                self.result[self.key(i)] = []
                self.result[self.key(i)].append(i)
            else:
                self.result[self.key(i)].append(i)
        
    def add(self, item):
        if self.key(item) not in self.result:
                self.result[self.key(item)] = []
                self.result[self.key(item)].append(item)
        else:
            self.result[self.key(item)].append(item)

    def group_for(self, item):
        return self.key(item)

    def __len__(self):
        return len(self.result)
    
    def __iter__(self):
        yield from tuple(self.result.items())

    def __contains__(self, item):
        return item in self.result

    def __getitem__(self, key):
        return self.result[key]
