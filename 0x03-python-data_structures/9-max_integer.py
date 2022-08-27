#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    else:
        max_num = 0
        for i, num in enumerate(my_list):
            if i == 0 or num > max_num:
                max_num = num

        return max_num
