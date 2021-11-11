"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse, math, operator


parser = argparse.ArgumentParser(description='Parser for standard math functions')
parser.add_argument('operation', type=str)
parser.add_argument('var1', type=float)
parser.add_argument('var2', type=float, nargs='?')


def calculate(args):
    operation = args.operation
    var1 = args.var1
    var2 = args.var2
    if operation in dir(math):
        if args.var2 is None:
            return getattr(math, operation)(var1)
        else:
            return getattr(math, operation)(var1,var2)
    elif operation in dir(operator):
        if var2 is None:
            return getattr(operator, operation)(var1)
        else:
            return getattr(operator, operation)(var1,var2)
    else:
        raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
