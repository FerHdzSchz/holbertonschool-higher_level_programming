#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for atribs in dir(hidden_4):
        if atribs[0:2] != '__':
            print(atribs)
