#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j in i:
            if j + 1 == len(matrix[i]):
                print("{}".format(j))
            else:
                print("{}".format(j), end= " ")
