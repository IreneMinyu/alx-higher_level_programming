#!/usr/bin/python3
"""
Unittest for square.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Contains multiple testing methods
    """

    def setUp(self):
        """
        To reset __nb_objects
        """
        Base._Base__nb_objects = 0

    def test_checkInheritance(self):
        """
        Checking Square instance inherits Rectangle
        """
        self.assertIsInstance(Square(5), Rectangle)

    def test_createRegular(self):
        """
        Creating Square instance with all regular values
        """
        sq1 = Square(20, 8, 9, 999)
        self.assertEqual(str(sq1), "[Square] (999) 8/9 - 20")

    def test_createRegular2(self):
        """
        Creating Square instance with just size
        """
        sq2 = Square(55)
        self.assertEqual(str(sq2), "[Square] (1) 0/0 - 55")

    def test_sizeError(self):
        """
        Creating Square instance with size as a string
        """
        with self.assertRaises(TypeError):
            Square("sizee")

    def test_sizeError2(self):
        """
        Creating Square instance with size as a negative
        """
        with self.assertRaises(ValueError):
            Square(-96)

    def test_xError(self):
        """
        Creating Square instance with x as a string
        """
        with self.assertRaises(TypeError):
            Square(3, "Ex", 6)

    def test_xError2(self):
        """
        Creating Square instance with x as a negative
        """
        with self.assertRaises(ValueError):
            Square(3, -6, 6)

    def test_yError(self):
        """
        Creating Square instance with y as a string
        """
        with self.assertRaises(TypeError):
            Square(3, 2, "trees")

    def test_yError2(self):
        """
        Creating Square instance with y as a negative
        """
        with self.assertRaises(ValueError):
            Square(3, 2, -3)

    def test_area(self):
        """
        Returning the area of a Square
        """
        sq3 = Square(4)
        self.assertEqual(sq3.area(), 16)


if __name__ == '__main__':
    unittest.main()
