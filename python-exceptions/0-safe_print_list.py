#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elem += 1
        except IndexError:
            exit
    print()
    return num_elem
