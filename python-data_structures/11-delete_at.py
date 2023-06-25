#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    return [x[1] for x in enumerate(my_list) if x[0] != idx]
