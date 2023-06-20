#!/usr/bin/env python3
add = __import__('add_0').add

if __name__ == '__main__':
    a = 1
    b = 2
    n = add(a, b)
    print(f"{a:d} + {b:d} = {n:d}")
