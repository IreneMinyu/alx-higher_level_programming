#!/usr/bin/python3
"""Empty Class"""


class Rectangle:
    """Define an empty rectangle class"""
    pass


Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
