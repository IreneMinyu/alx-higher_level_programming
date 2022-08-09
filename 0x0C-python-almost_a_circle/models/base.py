#!/usr/bin/python3
"""
base.py
class Base
importing json
importing os.path
importing turtle
"""
import json
import os.path
import turtle


class Base:
    """
    Main purpose: manage the id attribute and handle json
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Either set id or increment __nb__objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation
        -- before had:
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
        -- now:
        """
        ld = list_dictionaries
        return ("[]" if ld is None or not ld else json.dumps(ld))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string representation to a file
        """
        filename = str(cls.__name__) + ".json"
        if list_objs is None:
            list_objs = []
        finlist = []
        for item in list_objs:
            finlist.append(item.to_dictionary())
        with open(filename, "w+", encoding="utf-8") as fil:
            fil.write(Base.to_json_string(finlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        -- before:
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
        -- now:
        """
        js = json_string
        return ([] if js is None or not js else json.loads(js))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ is "Square":
            instance = cls(1)
        else:
            return None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        jsonlist = []
        if not os.path.isfile(filename):
            return []
        with open(filename) as fil:
            jsonlist = cls.from_json_string(fil.read())
        return [cls.create(**item) for item in jsonlist]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws the shapes
        """
        shape = turtle.Turtle()
        page = turtle.Screen()
        page.title("These are shapes")
        for item in list_rectangles + list_squares:
            shape.up()
            shape.setpos(item.x, item.y)
            shape.down()
            for i in range(0, 4):
                shape.forward(item.width)
                shape.right(90)
                shape.forward(item.height)
        page.exitonclick()
