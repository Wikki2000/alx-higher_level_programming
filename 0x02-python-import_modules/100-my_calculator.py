#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    operator = ['+', '-', '*', '/']

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }
    result = operations[argv[2]](a, b)
    print("{} {} {} = {}".format(a, argv[2], b, result))
