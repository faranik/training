"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value: int):
        if not isinstance(value, int):
            raise ValueError("The argument should be a valid integer.")

        if self.root is None:
            self.root = Node(value)
        else:
            curr = self.root
            while curr is not None:
                if value < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = Node(value)
                        break
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = Node(value)
                        break


def add_middle(numbers: list, tree : BinaryTree):
    if len(numbers) == 0:
        return

    if len(numbers) == 1:
        tree.add(numbers[0])
    else:
        middle_idx = int(len(numbers) / 2)
        tree.add(numbers[middle_idx])
        add_middle(numbers[:middle_idx], tree)
        add_middle(numbers[middle_idx + 1:], tree)


def create_minimal_tree(numbers: list) -> BinaryTree:
    tree = BinaryTree()
    add_middle(numbers, tree)
    return tree