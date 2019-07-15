import unittest
from graphs.p4_9 import Node
from graphs.p4_9 import merge
from graphs.p4_9 import get_bst_sequences


class TestBSTSequences(unittest.TestCase):

    def test_merge(self):
        """
        Input: Two list of one element, [1] and [2].
        Output: A list [[1, 2], [2, 1]]
        :return: void
        """
        res = merge([1], [2])

        self.assertEqual(res, [[1, 2], [2, 1]])

    def test_merge_lists_of_size_2(self):
        """
        Input: Two lists of two elements each.
        Output: Should return a list of 6 lists.
        :return: void
        """
        res = merge([1, 2], [3, 4])

        self.assertEqual(len(res), 6)

    def test_merge_lists_of_size_3(self):
        """
        Input: Two lists of three elements each.
        Output: Should return a list of 14 lists.
        :return: void
        """
        res = merge([1, 2, 3], [4, 5, 6])

        self.assertEqual(len(res), 14)

    def test_get_bst_sequences_two_levels(self):
        """
        Input:     2
                  /  \
                 1    3
        Output: [[2, 1, 3], [2, 3, 1]]
        :return: void
        """
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        n2.left = n1
        n2.right = n3

        r = get_bst_sequences(n2)

        self.assertEqual(r, [[2, 1, 3], [2, 3, 1]])

    def test_get_bst_sequences_three_levels(self):
        """
        Input:             5
                    2               7
                1       3       6        8
        Output: A list of 56 lists, every one starting with 5.
        :return: void
        """
        root = Node(5)
        root.left = Node(2)
        root.right = Node(7)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(8)

        r = get_bst_sequences(root)

        self.assertEqual(56, len(r))
        for elem in r:
            self.assertEqual(elem[0], 5)


