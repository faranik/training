"""
BST Sequences: A binary search tree was created by traversing through an
array from left to right and inserting each element. Given a binary search
tree with distinct elements, print all possible arrays that could have
led to this tree.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def merge(f: list, s: list) -> list:
    merges = [f + s, s + f]

    for i in range(1, len(f)):
        for j in range(1, len(s) + 1):
            merges.append(f[:i] + s[:j] + f[i:] + s[j:])

    for i in range(1, len(s)):
        for j in range(1, len(s) + 1):
            merges.append(s[:i] + f[:j] + s[i:] + f[j:])

    return merges


def get_weaved(l: list, r: list) -> list:
    weaves = []

    for i in l:
        for j in r:
            for k in merge(i, j):
                weaves.append(k)

    return weaves


def get_bst_sequences(root: Node) -> list:
    l = get_bst_sequences(root.left) if root.left else []
    r = get_bst_sequences(root.right) if root.right else []

    weaves = get_weaved(l, r)
    result = []

    for elem in weaves:
        result.append([root.data] + elem)

    if not result:
        result = [[root.data]]

    return result




