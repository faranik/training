"""
Flip Bit to Win: You have an integer and you can flip exactly one bit from
a 0 to a 1. Write code to find the length of the longest sequence of 1s you
could create.

EXAMPLE

Input: 1775 (or: 11011101111)

Output: 8

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def flip_bit_to_win(n: int) -> int:
    if n == 0:
        return 1
    
    tuples = []
    last = 0
    count = 0

    while n:
        d = (n & 1) != 0

        while d:
            count += 1
            n >>= 1
            d = (n & 1) != 0

        tuples.append((last, count))
        last = count
        count = 0

        n >>= 1

    options = [x[0] + x[1] for x in tuples]
    return max(options) + 1
