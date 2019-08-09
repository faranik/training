"""
Magic Index: A magic index in an array A [1. .. n -1] is defined to be an index
such that A[ i] i. Given a sorted array of distinct integers, write a method to
find a magic index, if one exists, in array A.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def bin_search_magic(first: int, last: int, arr: list) -> int:
    if arr[first] > first:
        return -1
    if arr[first] == first:
        return first
    if arr[last] == last:
        return last
    if first == last or last < first or first + 1 == last:
        return -1

    magic = -1
    middle = first + int((last - first) / 2)

    if arr[middle] < middle:
        magic = bin_search_magic(middle, last, arr)
    else:
        magic = bin_search_magic(first, middle, arr)

    return magic


def find_magic(arr: list) -> int:
    return bin_search_magic(0, len(arr) - 1, arr)
