"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    if '"' or "'" in string:
        stringlist = list(string)
        for idx in range(len(stringlist)):
            if stringlist[idx] == '"':
                stringlist[idx] = "'"
            elif stringlist[idx] == "'":
                stringlist[idx] = '"'
        string = ''.join(stringlist)
    return string
