#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    for num in set(my_list):
        addition += num
    return addition
