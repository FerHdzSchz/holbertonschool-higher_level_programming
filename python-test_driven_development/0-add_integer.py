#!/usr/bin/python3
"""
This is an addition function
>>> add_integer(1, 2)
3
"""

def add_integer(a, b=98):
    """
    Returns the sum of a and b integers

    Params:
    -------
    a - integer
    b - integer

    Returns:
    --------
    Sum of parameters

    """

    if isinstance(a, float) or isinstance(a, int):
        sum1 = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, float) or isinstance(b, int):
        sum2 = int(b)
    else:
        raise TypeError("b must be an integer")

    total = sum1 + sum2

    return total