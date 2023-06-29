#!/usr/bin/python3
def safe_print_integer(value):
    output = False
    try:
        print("{:d}".format(value))
        output = True
    except (TypeError, NameError, ValueError) as e:
        pass

    return output
