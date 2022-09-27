#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8) and
returns the number of characters added"""


def append_write(filename="", text=""):
    """append_write method"""

    num_chars = 0

    with open(filename, 'a', encoding='utf-8') as f:
        num_chars += f.write(text)

    return num_chars
