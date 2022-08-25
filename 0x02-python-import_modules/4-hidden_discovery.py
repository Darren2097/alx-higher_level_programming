#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    list_name = dir(hidden_4)
    for line in list_name:
        if not line.startswith("__"):
            print("{}".format(line))
