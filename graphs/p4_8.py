"""
First Common Ancestor: Design an algorithm and write code to find the first common
ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data
structure. NOTE: This is not necessarily a binary search tree.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def get_common_ancestor(root: Node, p: Node, q: Node) -> (Node, bool, bool):

    if not isinstance(root, Node) and root is not None:
        raise ValueError("Invalid type of arg root.")

    if not isinstance(p, Node) and p is not None:
        raise ValueError("Invalid type of arg p.")

    if not isinstance(q, Node) and q is not None:
        raise ValueError("Invalid type of arg q.")

    if root is None:
        return None, False, False

    a, f_a, s_a = get_common_ancestor(root.left, p, q)
    b, f_b, s_b = get_common_ancestor(root.right, p, q)

    if a:
        return a, f_a, s_a

    if b:
        return b, f_b, s_b

    if (f_a and s_a) or (f_b and s_b) or (f_a and s_b) or (f_b and s_a):
        return root, True, True

    if root is p:
        return None, True, (s_a or s_b)

    if root is q:
        return None, (f_a or f_b), True

    return None, (f_a or f_b), (s_a or s_b)
