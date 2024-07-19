import unittest
from shapes import Circle, Triangle, calculate_area

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

    def test_triangle_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

        non_right_triangle = Triangle(2, 2, 3)
        self.assertFalse(non_right_triangle.is_right_angle())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # Это не треугольник

if __name__ == '__main__':
    unittest.main()
