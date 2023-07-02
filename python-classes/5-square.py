#!/usr/bin/python3
""" Square class with error handling"""


class Square:
    """Base class + private attribute + type checker + size setter"""

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

    @property
    def size(self):
        """"
        Getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate area of a square
        """
        return self.__size**2

    def my_print(self):
        """
        Print with # a square of self.size
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)
