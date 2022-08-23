#!/usr/bin/python3

letter = 122
for i in range(122, 110, -1):
    print("{}".format(chr(letter)), end='')
    letter = letter - 33
    print("{}".format(chr(letter)), end='')
    letter = letter + 31
print("{}".format(chr(98)), end='')
print("{}".format(chr(65)))
