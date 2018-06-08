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


a = Circle(2)
print('Radius: ' + str(a.radius))
print('Diameter: ' + str(a.diameter))
print('Area:  ' + str(a.area))
a.diameter = 50
print('Radius: ' + str(a.radius))
print('Diameter: ' + str(a.diameter))
print('Area:  ' + str(a.area))
d = Circle.from_diameter(10)
print(d.diameter)
d.diameter = 5
print(d.radius)
print(d)
print(repr(d))
dd = eval(repr(d))
print(dd)
# b = Circle(12)
# print('Radius: ' + str(b.radius))
# print('Diameter: ' + str(b.diameter))
# print('Area:  ' + str(b.area))



