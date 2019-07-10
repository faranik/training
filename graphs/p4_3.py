"""
List of Depths: Given a binary tree, design an algorithm which creates a linked
list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll
have D linked lists).

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def get_lists(root: Node) -> list:
    if not isinstance(root, Node):
        raise ValueError("Argument should be instance of Node")

    levels = []
    level = [root]

    while level:
        level_ints = []
        level_nodes = []

        for node in level:
            level_ints.append(node.data)
            if node.left is not None:
                level_nodes.append(node.left)
            if node.right is not None:
                level_nodes.append(node.right)

        levels.append(level_ints)
        level = level_nodes

    return levels
