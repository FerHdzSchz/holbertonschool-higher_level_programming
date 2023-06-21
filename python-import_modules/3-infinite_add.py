#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    rolling_sum = 0
    for arg in args[1:]:
        rolling_sum += int(arg)
    print(rolling_sum)