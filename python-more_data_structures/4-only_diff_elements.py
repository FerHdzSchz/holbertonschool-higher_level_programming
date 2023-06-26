#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_list = []
    same  = [x  for x in set_1 for y in set_2 if x == y]
    diff_list.append([x for x in set_1 if x not in same])
    diff_list.append([x for x in set_2 if x not in same])

    return [y for x in diff_list for y in x ]
