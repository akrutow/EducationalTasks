class ProtectedObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)
    
    def __getattribute__(self, attr):
        if attr[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        if attr[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, attr)

