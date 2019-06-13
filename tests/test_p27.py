import os
import unittest
from lists.p27 import Node
from lists.p27 import get_intersection


class TestListIntersection(unittest.TestCase):

    def test_get_intersection(self):
        """
        l1: 1 -> 2 -> 3 \
                        7 -> 9
        l2:     4 -> 0 /
        get_intersection should return Node instance with value 7.

        :return: void
        """
        common = Node(9, None)
        common = Node(7, common)

        l1 = Node(3, common)
        l1 = Node(2, l1)
        l1 = Node(1, l1)

        l2 = Node(0, common)
        l2 = Node(4, l2)

        self.assertTrue(get_intersection(l1, l2) is common)

    def test_get_intersection_non_existent_intersection(self):
        """
        l1: 1 -> 2 -> 3 -> 7 -> 9
        l2:     4 -> 0 -> 7 -> 9
        get_intersection should return None because the list are not intersected by reference.

        :return: void
        """
        l1 = Node(9, None)
        l1 = Node(7, l1)
        l1 = Node(3, l1)
        l1 = Node(2, l1)
        l1 = Node(1, l1)

        l2 = Node(9, None)
        l2 = Node(7, l2)
        l2 = Node(0, l2)
        l2 = Node(4, l2)

        self.assertTrue(get_intersection(l1, l2) is None)

    def test_get_intersection_l1_None(self):
        """
        l1: None
        l2: 4 -> 0 -> 7 -> 9
        get_intersection should return None.

        :return: void
        """
        l2 = Node(9, None)
        l2 = Node(7, l2)
        l2 = Node(0, l2)
        l2 = Node(4, l2)

        self.assertTrue(get_intersection(None, l2) is None)

    def test_get_intersection_l2_None(self):
        """
        l1: 1 -> 2 -> 3 -> 7 -> 9
        l2: None
        get_intersection should return None.

        :return: void
        """
        l1 = Node(9, None)
        l1 = Node(7, l1)
        l1 = Node(3, l1)
        l1 = Node(2, l1)
        l1 = Node(1, l1)

        self.assertTrue(get_intersection(l1, None) is None)

    def test_get_intersection_l1_None_l2_None(self):
        """
        l1: None
        l2: None
        get_intersection should return None.

        :return: void
        """

        self.assertTrue(get_intersection(None, None) is None)

    def test_get_intersection_l1_concatenated_with_l2(self):
        """
        l1: 1 -> 2 -> 3
                      \
        l2:           7 -> 9
        get_intersection should return 7

        :return: void
        """
        l2 = Node(9, None)
        l2 = Node(7, l2)

        l1 = Node(3, l2)
        l1 = Node(2, l1)
        l1 = Node(1, l1)

        self.assertTrue(get_intersection(l1, l2) is l2)

    def test_get_intersection_l2_concatenated_with_l1(self):
        """
        l1:             7 -> 9
                       /
        l2: 1 -> 2 -> 3
        get_intersection should return 7

        :return: void
        """
        l1 = Node(9, None)
        l1 = Node(7, l1)

        l2 = Node(3, l1)
        l2 = Node(2, l2)
        l2 = Node(1, l2)

        self.assertTrue(get_intersection(l1, l2) is l1)

    def test_get_intersection_l1_is_l2(self):
        """
        l1: \
             1 -> 2 -> 3
            /
        l2:
        get_intersection should return 1

        :return: void
        """
        l1 = Node(3, None)
        l1 = Node(2, l1)
        l1 = Node(1, l1)

        self.assertTrue(get_intersection(l1, l1) is l1)
