#!/usr/bin/python3
"""function that replaces an element without modiying the original"""


def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
