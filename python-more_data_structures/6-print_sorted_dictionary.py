#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {k: a_dictionary[k] for k in sorted(list(a_dictionary.keys()))}
    for i in new_dict.items():
        print("{}: {}".format(i[0], i[1]))
