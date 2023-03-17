class Coordinates:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def get_coordinates(self):
        return [self._x, self._y]
