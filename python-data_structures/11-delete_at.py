#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0) or (idx > len(my_list)):
        return my_list

    for x, y in enumerate(my_list):
        if x == idx:
            del my_list[idx]
    return my_list