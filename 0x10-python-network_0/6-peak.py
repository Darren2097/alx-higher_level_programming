#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find_peak method"""

    length = len(list_of_integers)

    if length < 3:
        return None

    peak = list_of_integers[0]
    for i in range(1, length):
        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]

    return peak
