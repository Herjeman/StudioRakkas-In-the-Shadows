import math
import numpy


class Vector2:
    """Class for holding a location, direction or scale."""

    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_magnitude(self) -> float:
        """Returns a float representing the length of the vector.
        Calculated by sqrt(x^2 + y^2)"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self):
        """Returns a vector with the same direction but with length 1.
        This is useful for getting the pure direction"""

        norm = self.get_magnitude()
        x = self.x / norm
        y = self.y / norm

        return Vector2(x, y)

    def get_rotated(self, degrees):
        """Returns a vector that is rotated by degrees"""

        cos = math.cos(degrees)
        sin = math.sin(degrees)

        x = self.x * cos * -sin
        y = self.y * sin * cos

        return Vector2(x, y)

    def get_rotated_towards(self, target):
        """Returns a vector of same length that is rotated towards target"""

        direction = self - target
        direction = direction.get_normalized()

        degrees = compare_angle(self, direction)

        cos = math.cos(degrees)
        sin = math.sin(degrees)

        x = self.x * cos * -sin
        y = self.y * sin * cos

        return Vector2(x, y)


    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return Vector2(self.x * other, self.y * other)


def multiply_dot(a: Vector2, b: Vector2):
    """Returns a float calculated: a.x * b.x + a.y * b.y"""

    return a.x * b.x + a.y * b.y


def compare_angle(a: Vector2, b: Vector2):
    """Returns the angle between a and b"""

    return numpy.arccos(multiply_dot(a, b) / a.get_magnitude() * b.get_magnitude())
