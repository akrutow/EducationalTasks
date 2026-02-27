class GameObject:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Player(GameObject):
    __slots__ = ('nickname', )

    def __init__(self, x, y, nickname):
        super().__init__(x, y)
        self.nickname = nickname