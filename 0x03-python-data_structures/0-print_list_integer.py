#!/usr/bin/python3

"""function that prints all intergers of a list"""

def print_list_integer(my_list=[]):
    for list_element in range(len(my_list)):
        print("{:d}".format(my_list[list_element]))
