#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for i in len(my_list):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = search

    return (new_list)
