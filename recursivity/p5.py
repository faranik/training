"""
Recursive Multiply: Write a recursive function to multiply two positive integers
without using the * operator (or / operator). You can use addition, subtraction,
and bit shifting, but you should minimize the number of those operations.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def multiply(n, m):
    b = n if n > m else m
    s = n if n < m else m

    if s == 0:
        return 0
    elif s == 1:
        return b

    return multiply(b, s & 1) + (multiply(b, s >> 1) << 1)
