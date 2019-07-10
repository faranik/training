import unittest
from graphs.p4_3 import Node
from graphs.p4_3 import get_lists


class TestGetLists(unittest.TestCase):

    def test_get_lists(self):

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        lists = get_lists(root)

        self.assertEqual(len(lists), 3)
        self.assertEqual(lists[0], [1])
        self.assertEqual(lists[1], [2, 3])
        self.assertEqual(lists[2], [4, 5, 6, 7])
