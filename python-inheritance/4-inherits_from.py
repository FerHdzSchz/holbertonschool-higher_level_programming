#!/usr/bin/python3
"""
Checks for is_instance or same class
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
    """
    if (type(obj) == a_class) | (isinstance(obj, a_class)) | issubclass(obj, a_class):
        return True
    else:
        return False