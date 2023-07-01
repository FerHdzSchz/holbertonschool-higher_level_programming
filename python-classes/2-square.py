#!/usr/bin/python3
""" Square class with error handling"""
class Square:
    """Base class + private attribute + type checker"""

    def __init__(self, size=0):
        """
        Attr:
            size: len of side
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size