#!/usr/bin/python3
"""
Inherits from list
"""


class MyList(list):
    """
    Class that inherits from list
    """

    def print_sorted(self):
        """
        return sorted list
        """
        return sorted(self)
