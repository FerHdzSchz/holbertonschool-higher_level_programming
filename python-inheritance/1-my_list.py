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
        sorted_l = sorted(self)
        return sorted_l
