
import unittest
from lists.node import Node
from lists.p28 import get_loop


class TestListLoop(unittest.TestCase):

    def test_get_loop(self):
        """
        list: 1 -> 2 -> 3 -> 4 -> 2 (2 is the same Node instance as the first 2)

        get_loop should return the Node instance with value 2

        :return: void
        """
        n4 = Node(4, None)
        n3 = Node(3, n4)
        n2 = Node(2, n3)
        n1 = Node(1, n2)

        n4.next = n2

        #import pdb
        #pdb.set_trace()

        self.assertTrue(get_loop(n1) is n2)

    def test_get_loop_None(self):
        """
        list: None

        get_loop should return None

        :return: void
        """

        self.assertTrue(get_loop(None) is None)

    def test_get_loop_one_elem(self):
        """
        list: 1 -> None

        get_loop should return the head of the list.

        :return: void
        """
        n = Node(1, None)
        n.next = n

        self.assertTrue(get_loop(n) is n)

    def test_get_loop_no_loop(self):
        """
        list: 1 -> 2 -> 3 -> 4

        get_loop should return None as there is not a loop

        :return: void
        """
        n = Node(4, None)
        n = Node(3, n)
        n = Node(2, n)
        n = Node(1, n)

        self.assertTrue(get_loop(n) is None)
