#!/usr/bin/python3

import sys


def safe_function(fct, *args):

    try:
        return fct(*args)
    except Exception as ex:
        ex = "Exception: " + str(ex) + "\n"
        sys.stderr.write(ex)
        return None
