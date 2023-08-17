#!/usr/bin/python3
"""function that computes square value of all interges of a matrix"""


def square_matrix_simple(matrix=[]):
    new_list = []
    if len(matrix) == 0:
        return new_list
    new_list = [[x*x for x in y] for y in matrix]
    return new_list
