import math

from .exceptions import InvalidPointError

class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise InvalidPointError("Las coordenadas deben ser números.")
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        if not isinstance(value, (int, float)):
            raise InvalidPointError("La coordenada X debe ser un número.")
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        if not isinstance(value, (int, float)):
            raise InvalidPointError("La coordenada Y debe ser un número.")
        self._y = value

    def compute_distance(self, other):
        from math import hypot
        return hypot(self._x - other.get_x(), self._y - other.get_y())
