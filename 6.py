class Row:
    def __init__(self, **kwargs) -> None:
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)
    
    def __setattr__(self, attr, value):
        if attr not in self.__dict__:
            raise AttributeError('Установка нового атрибута невозможна')
        raise AttributeError('Изменение значения атрибута невозможно')
    
    def __delattr__(self, attr):
        raise AttributeError('Удаление атрибута невозможно')
    
    def __repr__(self):
        return f"Row({", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])})"
    
    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))
