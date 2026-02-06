class LoopTracker:
    def __init__(self, iterable):
        self.iterable = tuple(iterable)
        self.index = -1
        self.stop_counter = 0
        self.last_elem = None
        self.generic_counter = 0

    @property
    def accesses(self):
        return self.generic_counter

    @property
    def empty_accesses(self):
        return self.stop_counter  

    @property
    def first(self):
        if list(self.iterable):
            return list(self.iterable)[0]
        else:
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self.last_elem:
            return self.last_elem
        else:
            raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        if self.index >= len(self.iterable)-1:
            return True
        return False

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.iterable):
            self.stop_counter += 1
            raise StopIteration
        self.generic_counter += 1
        self.last_elem = self.iterable[self.index]
        return self.last_elem
