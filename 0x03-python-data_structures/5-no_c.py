#!/usr/bin/python3

def no_c(my_string):

    str_list = list(my_string)
    new_string = ""

    for c in str_list:
        if c != "c" and c != "C":
            new_string += c

    return new_string
