#!/usr/bin/python3
"""function that adds all unique integers in a list"""


def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    number = 0

    for x in uniq_list:
        number += x
    return (number)
