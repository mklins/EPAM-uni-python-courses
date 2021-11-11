"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum
from typing import List


class SortOrder(Enum):
    ascending = 'ascending order'
    descending = 'descending order'


def check_types(num_list, sort_oder):
    print(type(num_list))
    if not isinstance(num_list, list) or not isinstance(sort_oder, SortOrder):
        raise TypeError


def is_sorted(num_list: List[int], sort_order: SortOrder) -> bool:
    check_types(num_list, sort_order)
    if sort_order.value == SortOrder.ascending.value:
        for idx in range(len(num_list)-1):
            if num_list[idx] > num_list[idx+1]:
                return False
        return True
    elif sort_order.value == SortOrder.descending.value:
        for idx in range(len(num_list)-1):
            if num_list[idx] < num_list[idx+1]:
                return False
        return True


def transform(num_list: List[int], sort_order: SortOrder) -> List[int]:
    check_types(num_list, sort_order)
    if is_sorted(num_list, sort_order):
        for idx in range(len(num_list)):
            num_list[idx] += idx
    return num_list
