import unittest
from graphs.p4_2 import Node
from graphs.p4_2 import BinaryTree
from graphs.p4_2 import create_minimal_tree


class TestCreateMinimalTree(unittest.TestCase):

    def test_create_minimal_tree(self):
        """
        Input: [1, 2, 3, 4, 5, ,6 ,7]
        Output:         4
                      /   \
                    2       6
                  /  \\    /   \\
                1     3   5     7
        :return: void
        """
        tree = create_minimal_tree([1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(tree.root.data, 4)
        self.assertEqual(tree.root.left.data, 2)
        self.assertEqual(tree.root.right.data, 6)
        self.assertEqual(tree.root.left.left.data, 1)
        self.assertEqual(tree.root.left.right.data, 3)
        self.assertEqual(tree.root.right.left.data, 5)
        self.assertEqual(tree.root.right.right.data, 7)
