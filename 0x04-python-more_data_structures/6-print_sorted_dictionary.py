#!/usr/bin/python3
"""function that prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    list_order = list(a_dictionary.keys())
    list_order.sort()

    for x in list_order:
        print("{}: {}".format(x, a_dictionary.get(x)))
