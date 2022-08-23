#!/usr/bin/python3

def uppercase(str):
    new = ''
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            new += chr(ord(s) - 32)
        else:
            new += s

    print("{}".format(new))
