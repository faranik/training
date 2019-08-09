"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the child can run up
the stairs.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def count_ways_rec(n: int, memo: list) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways_rec(n - 1, memo) + count_ways_rec(n - 2, memo) + count_ways_rec(n - 3, memo)
        return memo[n]


def count_ways(n: int) -> int:
    memo = [-1] * (n + 1)
    return count_ways_rec(n, memo)


"""
Count ways iterative approach.
"""


def factorial(n: int, factorials) -> int:
    if n == 0:
        return 1
    if factorials[n] == 0:
        factor = 1
        for i in range(1, n+1):
            factor *= i
        factorials[n] = factor
    return factorials[n]


def count_ways_iter(n: int, facts)-> int:
    assert n > 0

    count = 0
    for c in range(int(n/3) + 1):
        for b in range(int((n - (3 * c)) / 2) + 1):
            a = n - (3 * c) - (2 * b)
            count += int(factorial(a + b + c, facts) / factorial(a, facts) / factorial(b, facts) / factorial(c, facts))

    return count


factorials = [0] * 101
print(count_ways_iter(100, factorials))
