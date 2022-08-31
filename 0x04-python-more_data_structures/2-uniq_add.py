#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_numbers = list(set(my_list))
    sum_num = 0

    for i in range(len(unique_numbers)):
        sum_num += int(unique_numbers[i])

    return sum_num
