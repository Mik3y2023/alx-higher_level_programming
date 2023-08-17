#!/usr/bin/python3
"""function that replaces all occurence of an element"""


def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    new_list = [el if el != search else replace for el in my_list]
    return new_list
