#!/usr/bin/python3

if __name__ == '__main__':

    from sys import argv

    result = 0

    if len(argv) == 1:
        print("0")
    else:
        my_tuple = (1, len(argv))

        for i in range(my_tuple[0], my_tuple[1]):
            result += int(argv[i])

        print("{:d}".format(result))
