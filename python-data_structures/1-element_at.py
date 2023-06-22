#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0):
        elem = None
    elif idx >= len(my_list):
        elem = None
    else:
        elem = my_list[idx]
    return(elem)
