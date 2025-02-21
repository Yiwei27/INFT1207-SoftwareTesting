import unittest
from Lab3_Group12.app.Lab3_Yiwei_Shibin import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    # Circle Tests
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    # Trapezium Tests
    def test_trapezium_area_valid(self):
        self.assertAlmostEqual(trapezium_area(3, 5, 4), 16.0)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-3, 5, 4)

    # Ellipse Tests
    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(3, 4), 37.69911184307752)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-3, 4)

    # Rhombus Tests
    def test_rhombus_area_valid(self):
        self.assertAlmostEqual(rhombus_area(10, 8), 40.0)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-10, 8)

if __name__ == "__main__":
    unittest.main()