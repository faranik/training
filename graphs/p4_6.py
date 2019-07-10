"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def get_most_left(n: Node) -> Node:
    if n is None:
        return None

    while n.left is not None:
        n = n.left
    return n


def get_next(n: Node) -> Node:
    if n is None:
        raise ValueError("Invalid value. Argument cannot be None.")
    next_node = get_most_left(n.right)

    if next_node is not None:
        return next_node

    while n.parent is not None and n.parent.left is not n:
        n = n.parent

    return n.parent
