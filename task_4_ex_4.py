"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 3, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    vrfd_indexes, result = [0], []
    indexes = list(filter(lambda el: type(el) is int and len(string) > el > 0, indexes))
    print(indexes)
    for idx in range(len(indexes)-1):
        if indexes[idx] == indexes[-1]:
            break
        if indexes[idx] > indexes[idx+1]:
            print(indexes[idx])
            indexes.remove(indexes[idx+1])
    [vrfd_indexes.append(el) for el in indexes if el not in vrfd_indexes]
    print(vrfd_indexes)
    result = [string[idxfrom:idxto] for idxfrom, idxto in zip(vrfd_indexes, vrfd_indexes[1:] + [None])]
    return result
