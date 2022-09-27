#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and returns the
number of characters written"""


def write_file(filename="", text=""):
    """write_file method"""

    num_char = 0

    with open(filename, 'w', encoding='utf-8') as f:
        num_char += f.write(text)

    return num_char
