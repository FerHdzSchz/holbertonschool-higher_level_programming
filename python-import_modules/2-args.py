#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    num_args = len(args) - 1

    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args > 1:
        print("{} arguments:".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))

    k = 1
    if num_args > 0:
        for arg in args[1:]:
            print("{}: {}".format(k, arg))
            k += 1
