#!/usr/bin/python3
"""function that removes all characters c and C from a string"""


def no_c(my_string):
    """translate() takes a dictionary as an argument.
    the dictionary maps Unicode ordinals to coresponding translation"""
    new_string = my_string.translate({ord(x): None for x in "cC"})
    return new_string
