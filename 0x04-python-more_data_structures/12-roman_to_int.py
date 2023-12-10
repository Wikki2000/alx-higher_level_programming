#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 100}
    prev_value = 0
    total = 0
    for numeral in roman_string:
        current_value = roman_dict[numeral]
        if current_value >= prev_value + 1:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
    return total
