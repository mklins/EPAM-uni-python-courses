"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse


def from_roman_numerals(args):
    result = 0
    values_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    numeral = args.N
    for num in numeral:
        if num not in values_numerals:
            raise ValueError
    if len(numeral) < 2:
        result = values_numerals[numeral]
    else:
        for n in range(len(numeral)-1):
            for vn in values_numerals:
                if numeral[n] == vn:
                    if values_numerals[numeral[n]] < values_numerals[numeral[n+1]]:
                        result -= values_numerals[vn]
                        break
                    else:
                        result += values_numerals[vn]
                        break
        result += values_numerals[numeral[-1]]
    return result


def main():
    parser = argparse.ArgumentParser(description='Roman numeral to Arabic numeral converter')
    parser.add_argument('N', type=str, help='Roman numeral to convert', metavar='numeral')
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
