#!/usr/bin/python3

if __name__ == '__main__':

    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))

    my_tuple = (1, len(argv))

    for i in range(my_tuple[0], my_tuple[1]):
        print("{:d}: {}".format(i, argv[i]))
