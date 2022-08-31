#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dict = dict(a_dictionary)

    for i, j in new_dict.items():
        new_dict[i] = j * 2

    return new_dict
