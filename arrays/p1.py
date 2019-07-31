"""
Given a array of arrays composed of 0s and 1s like in the example below
find the index of the array which has the longest series of zeros.

00111
01111
00011 -> return the index of this array
11111
01111

An array like 10011 is not valid and will not be present into the input data.
So consider that ones are always on rights side of the array if they exist.
"""


def get_longest_series_of_zeros(arr: list) -> int:
    if not arr:
        raise ValueError("Invalid input. Input should not be empty or None.")

    bit_idx = 0
    arr_idx = -1
    for i, elem in enumerate(arr):
        found_longer = False
        while elem[bit_idx] == 0 and bit_idx < len(elem):
            bit_idx += 1
            found_longer = True

        if found_longer:
            arr_idx = i

    return arr_idx
