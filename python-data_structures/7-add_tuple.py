#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)

    if (lena == 0):
        a_1, a_2 = 0, 0
    if lenb == 0:
        b_1, b_2 = 0, 0
    if lena == 1:
        a_1, a_2 = tuple_a[0], 0
    if lenb == 1:
        b_1, b_2 = tuple_b[0], 0
    if lena >= 2:
        a_1, a_2 = tuple_a[0], tuple_a[1]
    if lenb >= 2:
        b_1, b_2 = tuple_b[0], tuple_b[1]

    return (a_1 + b_1, a_2 + b_2)
