#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = 0
    if len(my_list) == 0:
        mx = None
    else:
        mx = my_list[0]
        for x in my_list:
            if x > mx:
                mx = x
    return mx
