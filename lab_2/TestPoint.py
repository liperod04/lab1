import unittest
from Point import Point # Import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(5, 9)
        self.p4 = Point(5, 9)
        self.p5 = Point(3, 3)
        self.p6 = Point(8, 9)
        self.p7 = Point(3, 4) 
        self.p8 = Point(-3, -4)
        self.p9 = Point(1, 2)
        self.p10 = Point(4, 6)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)

    def test_eq(self):
        """Tests if Points are equal to each other"""
        self.assertEqual(self.p3, self.p4)
        self.assertNotEqual(self.p5, self.p6)
        

    def test_equidistant(self):
        """Tests if points are the same distance from the origin"""
        self.assertEqual(Point.equidistant(self.p7, self.p8), True)
        self.assertNotEqual(Point.equidistant(self.p5, self.p6), True)

    def test_within(self):
        """Tests if points are within determined distance from each other"""
        self.assertEqual(Point.within(self.p9, 5, self.p10), True)
        

unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects