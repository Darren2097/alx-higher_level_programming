#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    div = 0

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            new_list.append(div)
        except (ZeroDivisionError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
            new_list.append(0)

    return new_list
