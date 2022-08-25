#!/usr/bin/python3

if __name__ == '__main__':

    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in ["+", "-", "*", "/"]:
        print("unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] == "+":
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
        elif sys.argv[2] == "-":
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
        elif sys.argv[2] == "*":
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
        elif sys.argv[2] == "/":
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
