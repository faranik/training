"""
Paths with Sum: You are given a binary tree in which each node contains an
integer value (which might be positive or negative). Design an algorithm to
count the number of paths that sum to a given value. The path does not
need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def has_sum(numbers: list, s: int) -> bool:

    for i in range(len(numbers)):
        s = s - numbers[(-1 * i) - 1]
        if s == 0:
            return True

        if s < 0:
            break
    return False


def get_nb_paths(n: Node, stack: list, s: int) -> int:
    if n is None:
        return 0

    stack.append(n.data)
    l = get_nb_paths(n.left, stack, s)
    r = get_nb_paths(n.right, stack, s)

    nb = l + r
    if has_sum(stack, s):
        nb = nb + 1

    stack.pop()
    return nb
