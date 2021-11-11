def split_by_index(string, indexes):
    vrfd_indexes, result, temp = [0], [], []
    indexes= filter(lambda el: type(el) is int and len(string) > el > 0, indexes)
    indexes = list(indexes)
    print(indexes)
    maxi = 0
    for idx in range(len(indexes)-1):
        if indexes[idx] == indexes[-1]:
            break
        #if maxi >
        if indexes[idx] > indexes[idx+1]:
            maxi = indexes[idx]
            print(indexes[idx])
            indexes.remove(indexes[idx+1])
    [vrfd_indexes.append(el) for el in indexes if el not in vrfd_indexes]
    print(vrfd_indexes)
    for idxs in range(1, len(vrfd_indexes)):
        print(idxs)
        result.append(string[vrfd_indexes[idxs-1]:vrfd_indexes[idxs]])
    result.append(string[vrfd_indexes[-1]:len(string)])
    #result = [string[i:j] for i, j in zip(vrfd_indexes, vrfd_indexes[1:] + [None])]
    return result


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 3, 8, -4, 0, "u", 12, 8, 13, 40]))


def split_by_index(string, indexes):
    vrfd_indexes, result = [0], []
    for idx in range(1, len(indexes) - 1):
        if type(indexes[idx]) is int and len(string) > indexes[idx] > 0:
            if type(indexes[idx + 1]) is int and indexes[idx-1] <= indexes[idx] <= indexes[idx + 1]:
                vrfd_indexes.append(indexes[idx])
    if type(indexes[-1]) is int and len(string) > indexes[-1] > 0:
        vrfd_indexes.append(indexes[len(indexes) - 1])
    print(vrfd_indexes)
    for idxs in range(len(vrfd_indexes)-1):
        print(idxs)
        result.append(string[vrfd_indexes[idxs]:vrfd_indexes[idxs+1]])
        print(result)
    result.append(string[vrfd_indexes[-1]:len(string)])
    return result