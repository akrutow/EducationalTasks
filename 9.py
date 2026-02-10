class HistoryDict:
    def __init__(self, data=None):
        if data:
            self.data = data.copy()
        else:
            self.data = {}
        self.reserve_data = {}
        for k, v in self.data.items():
            if k not in self.reserve_data:
                self.reserve_data[k] = []
                self.reserve_data[k].append(v)

    def keys(self):
        return self.data.keys()    

    def values(self):
        return self.data.values() 

    def items(self):
        return self.data.items() 

    def history(self, key):
        if key not in self.reserve_data:
            return []
        return self.reserve_data[key]

    def all_history(self):
        return self.reserve_data 

    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data.keys()

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
        if key not in self.reserve_data:
            self.reserve_data[key] = []
            self.reserve_data[key].append(value)
        else:
            self.reserve_data[key].append(value)

    def __delitem__(self, key):
        del self.data[key]
        del self.reserve_data[key]
