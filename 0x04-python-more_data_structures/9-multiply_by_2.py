#!/usr/bin/python3
"""function that returns a new dictionary witha ll values multiplied by 2"""


def multiply_by_2(a_dictionary):
    new_directory = a_dictionary.copy()
    list_keys = list(new_directory.keys())

    for x in list_keys:
        new_directory[x] *= 2
    return (new_directory)
