#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 5 == 0:
            if i == 100:
                print("{}".format(i), end="")
            else:
                print("{}".format("Buzz", end=" "))
        elif i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz", end=" "))
        else:
            print("{}".format(i), end=" ")
