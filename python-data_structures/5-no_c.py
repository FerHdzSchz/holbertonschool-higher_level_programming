#!/usr/bin/python3
def no_c(my_string):
    new_string = [x for x in my_string if "c" not in x]
    return new_string
