#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        ex = "Exception: " + str(ex) + "\n"
        sys.stderr.write(ex)
        return False
