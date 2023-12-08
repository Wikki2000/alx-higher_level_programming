#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0

    if my_list == []:
        return 0
    for x, y in my_list:
        num += x * y
        den += y
        average = num / den
    return average
