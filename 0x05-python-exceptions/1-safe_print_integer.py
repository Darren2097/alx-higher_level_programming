#!/usr/bin/python3

def safe_print_integer(value):

    try:
        print("{:d}".format())
        return True
    except (TypeError, ValueError):
        return False
