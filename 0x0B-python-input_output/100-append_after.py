#!/usr/bin/python3
"""function that inserts a line of text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """append_after method"""

    new_line = []

    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            new_line.append(line)
            if search_string in line:
                new_line.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        for line in new_line:
            f.write(line)
