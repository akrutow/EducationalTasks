class ColoredPoint:
    def __init__(self, x, y, color) -> None:
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color
    
    @property
    def _field(self):
        return self._x, self._y, self._color
    
    def __repr__(self):
        return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"
    
    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._field == other._field
        return NotImplemented
    
    def __hash__(self):
        return hash(self._field)
    