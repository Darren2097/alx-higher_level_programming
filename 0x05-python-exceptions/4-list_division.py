#!/usr/bin/python3

def check_division(a, b):

    div = 0

    try:
        div = a / b
    except (ZeroDivisionError):
        print("division by 0")
    except (TypeError):
        print("wrong type")
    finally:
        return div

def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(list_length):
        try:
            div = check_division(my_list_1[i], my_list_2[i])
            new_list.append(div)
        except (IndexError):
            print("out of range")
            new_list.append(0)

    return new_list
