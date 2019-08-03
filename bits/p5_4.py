"""
Next Number: Given a positive integer, print the next smallest and the next
largest number that have the same number of 1 bits in their binary representation.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def move_bit(n: int, src_idx: int, dst_idx: int):
    d = (n >> src_idx) != 0

    n = n & ~(1 << dst_idx)
    if d == 1:
        n = n | (1 << dst_idx)

    n = n & ~(1 << src_idx)

    return n


def get_bounds_of_first_ones_series(n: int):
    idx, r = 0, 0
    m = n

    while (m & 1) == 0:
        idx += 1
        m >>= 1

    r = idx

    while (m & 1) != 0:
        idx += 1
        m >>= 1

    return idx - 1, r


def get_largest(n: int) -> int:
    if n == ~0:
        raise ValueError("Too big value.")

    if n == 0:
        return 0

    l, r = get_bounds_of_first_ones_series(n)

    if r != 0 and r != l:
        for i in range(r, l):
            n = move_bit(n, i, i - r)

    n = move_bit(n, l, l + 1)

    return n
