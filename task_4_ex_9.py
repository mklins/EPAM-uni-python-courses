"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    result = 0
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise TypeError
    for num in str(n):
        if int(num) % 2 != 0:
            result += int(num)
    return result
