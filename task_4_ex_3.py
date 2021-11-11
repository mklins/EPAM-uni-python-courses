"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str = ' ') -> list:
    result = []
    if type(str_to_split) is not str:
        raise ValueError
    idxfrom = 0
    for idxto in range(len(str_to_split)):
        if str_to_split[idxto] == delimiter:
            result.append(str_to_split[idxfrom:idxto])
            idxfrom = idxto+1
    result.append(str_to_split[idxfrom:])
    return result
