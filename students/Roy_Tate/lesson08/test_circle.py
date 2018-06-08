

import unittest
import circle
import math
from io import StringIO


class CircleTest(unittest.TestCase):

    def setUp(self):
        self.radius = 5

    def test_radius_returns_correct_value(self):
        c = circle.Circle(self.radius)
        assert c.radius == self.radius

    def test_diameter_calculates_properly(self):
        c = circle.Circle(self.radius)
        self.assertEqual(c.diameter, self.radius * 2)

    def test_diameter_can_be_modified_and_radius_is_updated_correctly(self):
        # Create an initial circle with radius 10
        c = circle.Circle(10)
        self.assertEqual(c.radius, c.diameter / 2)
        c.diameter = 50
        self.assertEqual(c.radius, c.diameter / 2)

    def test_area_of_circle_calculated_properly(self):
        c = circle.Circle(self.radius)
        self.assertEqual(c.area, self.radius ** 2 * math.pi)

    def test_circle_created_by_invoking_diameter(self):
        c = circle.Circle.from_diameter(10)
        self.assertEqual(c.diameter, 10)

    def test_string_output(self):
        pass

    def test_repr_output(self):
        pass



if __name__ == "__main__":
    unittest.main()