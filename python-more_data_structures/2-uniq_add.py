#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    addition = map(sum, set(my_list))
    return addition
