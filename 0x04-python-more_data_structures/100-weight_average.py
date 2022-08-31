#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        score = 0
        weight = 0

        for my_tuple in my_list:
            score += my_tuple[0] * my_tuple[1]
            weight += my_tuple[1]

        return (score / weight)
    return 0
