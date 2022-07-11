#!/usr/bin/python3
"""
Unittest for base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """
    Contains multiple testing methods
    """

    def setUp(self):
        """
        To reset __nb_objects
        """
        Base._Base__nb_objects = 0

    def test_setValidid(self):
        """
        Creating Base object with valid int id
        """
        object1 = Base(45)
        self.assertEqual(object1.id, 45)

    def test_setValidid2(self):
        """
        Creating Base object with a string id
        """
        object2 = Base("string")
        self.assertEqual(object2.id, "string")

    def test_setNoneid(self):
        """
        Creating Base object with None as id
        """
        object3 = Base(None)
        self.assertEqual(object3.id, 1)

    def test_setNoneid2(self):
        """
        Creating Base object with None as id mulitple times
        """
        object4 = Base(None)
        self.assertEqual(object4.id, 1)
        object4.id = "bleh"
        self.assertEqual(object4.id, "bleh")
        object4 = Base(None)
        self.assertEqual(object4.id, 2)

    def test_toJSONstr(self):
        """
        Testing instance to_json_string within Base: EMPTY LIST
        """
        self.assertEqual(Base().to_json_string([]), "[]")

    def test_toJSONstr2(self):
        """
        Testing instance to_json_string within Base: NONE
        """
        self.assertEqual(Base().to_json_string(None), "[]")

    def test_toJSONstr3(self):
        """
        Testing instance to_json_string within Base: ACTUAL LIST
        """
        self.assertEqual(Base().to_json_string([4, 6]), "[4, 6]")

    def test_fromJSONstr(self):
        """
        Testing instance from_json_string within Base: EMPTY LIST
        """
        self.assertEqual(Base().from_json_string("[]"), [])

    def test_fromJSONstr2(self):
        """
        Testing instance from_json_string within Base: NONE
        """
        self.assertEqual(Base().from_json_string(None), [])

    def test_fromJSONstr3(self):
        """
        Testing instance from_json_string within Base: ACTUAL LIST
        """
        self.assertEqual(Base().from_json_string("[4, 6]"), [4, 6])

    def test_create(self):
        """
        Testing instance create within Base: NORMAL RECTANGLE
        """
        rect1 = Rectangle(8, 2)
        rect1_dic = rect1.to_dictionary()
        rectA = rect1.create(**rect1_dic)
        self.assertEqual(str(rectA), "[Rectangle] (1) 0/0 - 8/2")

    def test_create2(self):
        """
        Testing instance create within Base: NORMAL SQUARE
        """
        sq1 = Square(4)
        sq1_dic = sq1.to_dictionary()
        sqA = sq1.create(**sq1_dic)
        self.assertEqual(str(sqA), "[Square] (1) 0/0 - 4")


if __name__ == '__main__':
    unittest.main()
