#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        if len(matrix) == 0:
            print("\n")
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                print("{}".format(matrix[i][j]))
            else:
                print("{}".format(matrix[i][j]), end= " ")