#!/usr/bin/python3
"""
    Class to define a square with private attribute
"""


class Square:

    """Base class + private attribute"""
    def __init__(self, size) -> None:
        """
        Attr:
            size: len of side
        """
        self.__size = size
