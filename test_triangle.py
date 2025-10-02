import unittest
from triangle import classify_triangle

class fooTest(unittest.TestCase):
    def test_triangle_1(self):
        t = classify_triangle(1, 2, 3)
        self.assertEqual(t, "Not a triangle")

    def test_triangle_2(self):
        t = classify_triangle(0, 0, 0)
        self.assertEqual(t, "Not a triangle")

    def test_triangle_3(self):
        t = classify_triangle(1, 5, 8)
        self.assertEqual(t, "Not a triangle")

    def test_equilateral_triangle_1(self):
        t = classify_triangle(1, 1, 1)
        self.assertEqual(t, "Equilateral")

    def test_equilateral_triangle_2(self):
        t = classify_triangle(3, 3, 3)
        self.assertEqual(t, "Equilateral")

    def test_equilateral_triangle_3(self):
        t = classify_triangle(5, 5, 5)
        self.assertEqual(t, "Equilateral")

    def test_isosceles_triangle_1(self):
        t = classify_triangle(5, 2, 5)
        self.assertEqual(t, "Isosceles")

    def test_isosceles_triangle_2(self):
        t = classify_triangle(3, 5, 3)
        self.assertEqual(t, "Isosceles")

    def test_isosceles_triangle_3(self):
        t = classify_triangle(7, 7, 10)
        self.assertEqual(t, "Isosceles")

    def test_scalene_triangle_1(self):
        t = classify_triangle(4, 2, 3)
        self.assertEqual(t, "Scalene")

    def test_scalene_triangle_2(self):
        t = classify_triangle(5, 6, 7)
        self.assertEqual(t, "Scalene")

    def test_scalene_triangle_3(self):
        t = classify_triangle(6, 7, 10)
        self.assertEqual(t, "Scalene")

    def test_right_triangle_1(self):
        t = classify_triangle(3, 4, 5)
        self.assertEqual(t, "Right Scalene")

    def test_right_triangle_2(self):
        t = classify_triangle(3, 5, 4)
        self.assertEqual(t, "Right Scalene")

    def test_right_triangle_3(self):
        t = classify_triangle(6, 8, 10)
        self.assertEqual(t, "Right Scalene")

    def test_right_triangle_4(self):
        t = classify_triangle(1, 1, 2 ** 0.5)
        self.assertEqual(t, "Right Isosceles")


if __name__ == "__main__":
    unittest.main(verbosity=2)