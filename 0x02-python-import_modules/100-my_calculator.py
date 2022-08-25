#!/usr/bin/python3

if __name__ == '__main__':

    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif argv[2] not in ["+", "-", "*", "/"]:
        print("unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == "+":
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
        elif argv[2] == "-":
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
        elif argv[2] == "*":
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
        elif argv[2] == "/":
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
