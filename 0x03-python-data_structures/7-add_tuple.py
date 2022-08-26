#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    else:
        tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    else:
        tuple_b = (tuple_b[0], tuple_b[1])

    sum1 = 0
    sum2 = 0

    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]

    return (sum1, sum2)

if __name__ == '__main__':
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
