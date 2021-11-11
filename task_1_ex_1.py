"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse


parser = argparse.ArgumentParser(description='Parser for simple arithmetic operations')
parser.add_argument('var1', type=float)
parser.add_argument('operation', type=str)
parser.add_argument('var2', type=float)


def calculate(args):
    var1 = args.var1
    operation = args.operation
    var2 = args.var2
    if operation == '+':
        return var1 + var2
    elif operation == '-':
        return var1 - var2
    elif operation == '*':
        return var1 * var2
    elif operation == '/':
        return var1 / var2
    else:
        raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
