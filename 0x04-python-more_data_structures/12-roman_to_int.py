#!/usr/bin/python3
"""function that converts a roman numeral to an interger"""


def to_subtract(list_number):
    to_sub = 0
    max_list = max(list_number)

    for x in list_number:
        if max_list > x:
            to_sub += x
        return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_num.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for ch in roman_string:
        for r_number in list_keys:
            if r_number == ch:
                if roman_num.get(ch) <= last_roman:
                    number += to_subtract(list_number)
                    list_number = [roman_num.get(ch)]
                else:
                    list_number.append(roman_num.get(ch))
                last_roman = roman_num.get(ch)

        number += to_subtract(list_number)

        return (number)
