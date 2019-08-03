"""
Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i and j.
Write a method to insert Minto N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would
not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3
and bit 2.

EXAMPLE

Input:

N = 10000000000
M = 10011,
i = 2,
j = 6

Output: N 10001001100

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def length(n : int) -> int:
    size = 0
    while n:
        n >>= 1
        size += 1

    return size


def insert_number(m: int, n: int, j: int, i: int):
    m_size = length(m)
    j += 1

    mask = 1 << m_size
    mask -= 1
    mask <<= (j - m_size)

    n = n & (~mask)

    m = m << (j - m_size)
    m = m & mask

    n = n | m

    return n
