import unittest
from graphs.p4_12 import Node
from graphs.p4_12 import get_nb_paths


class TestNumberOfSums(unittest.TestCase):

    def setUp(self) -> None:
        self.root = Node(10)
        self.root.left = Node(5)
        self.root.left.left = Node(3)
        self.root.left.left.left = Node(3)
        self.root.left.left.right = Node(-2)
        self.root.left.right = Node(2)
        self.root.left.right.right = Node(1)
        self.root.right = Node(-3)
        self.root.right.right = Node(11)

    def test_get_nb_paths(self):
        """
        Input: The root element with the searched sum of 8.
        Output: 2, as there are two paths that give the sum of 8.
        :return: void
        """
        res = get_nb_paths(self.root, [], 8)

        self.assertEqual(res, 2)

    def test_get_nb_paths_node(self):
        """
        Input: None as root of the tree and 8 as searched sum.
        Output: 0 as there is not tree in reality.
        :return: void
        """

        self.assertEqual(0, get_nb_paths(None, [], 8))
