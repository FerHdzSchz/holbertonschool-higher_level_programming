#!/usr/bin/python3
for i in range(0,10):
    for j in range(0,10):
        print(f"{i}{j}", end ="")
        if i == 9 and j == 9:
            continue
        else:
            print(", ", end="")