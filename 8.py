class ReversedSequence:
    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return ReversedSequence(self.sequence[key])
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key < 0 or key >= len(self.sequence):
            raise IndexError('Неверный индекс')
        return self.sequence[::-1][key]
    
    def __iter__(self):
        yield from self.sequence[::-1]
