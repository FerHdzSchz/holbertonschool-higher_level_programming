#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nw_list = []
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end = "")
            nw_list.append(my_list[i])
        except:
            exit
    print()
    return len(nw_list)
