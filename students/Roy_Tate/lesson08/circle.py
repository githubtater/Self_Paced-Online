#!/usr/bin/python3

## author: Roy Tate (githubtater)

import math

class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return (self._radius ** 2 * math.pi)

    @classmethod
    def from_diameter(self, val):
        return Circle(val / 2)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        new_radius = self._radius
        new_radius += other.radius
        return Circle(new_radius)

    def __mul__(self, other):
        new_radius = self._radius
        if isinstance(other, int):
            new_radius *= other
        elif isinstance(other, Circle):
            new_radius *= other.radius
        else:
            raise TypeError('Cannot multiply circle by {} because {} is not supported.'.format(other, type(other)))
        return Circle(new_radius)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def sort_key(self):
        return self._radius

a = Circle(10)
b = Circle(22)
c = Circle(15)
# circles = [a, b, c]
# circles.sort(key=Circle.sort_key)
# print(circles)


