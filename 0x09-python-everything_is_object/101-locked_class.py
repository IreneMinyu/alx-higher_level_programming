#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """ locked class that only allows dynamically creation of
    the instance attribute "first_name"""
    __slots__ = ["first_name"]
