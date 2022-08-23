#!/usr/bin/python3

def uppercase(str):
    new = ''
    for s in str:
        if ord(s) >= 65 and ord(s) <= 90:
            new += chr(ord(s) - 32)
        else:
            new += s

    print("{}".format(new))
