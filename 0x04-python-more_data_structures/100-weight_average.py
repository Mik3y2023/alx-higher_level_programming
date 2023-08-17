#!/usr/bin/python3
"""function that returns the weighted average of intergers"""


def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    avg = 0

    for num in my_list:
        number += num[0] * num[1]
        avg += num[1]

    return (number / avg)
