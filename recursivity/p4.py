"""
Power Set: Write a method to return all subsets of a set.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def get_subsets(data, subsets, data_set):
    if len(data) > 1:
        for i, elem in enumerate(data):
            get_subsets(data[:i] + data[i + 1:], subsets, data_set)

    if len(data) == 1:
        if data[0] not in data_set:
            data_set.add(data[0])
            subsets.append(data)
    else:
        subsets.append(data)


def find_subsets(data):
    subsets = []
    data_set = set()
    get_subsets(data, subsets, data_set)
    return subsets[:-1]
