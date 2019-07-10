import unittest
from graphs.p4_6 import Node
from graphs.p4_6 import get_next


class TestGetNext(unittest.TestCase):

    def setUp(self) -> None:
        """
        BST :            5
                        /  \\
                       3     8
                     /  \\   |  \
                    1   4    7   9
                    \\       |    \\
                     2       6     10
        :return: void
        """

        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)
        self.n7 = Node(7)
        self.n8 = Node(8)
        self.n9 = Node(9)
        self.n10 = Node(10)

        self.n5.left = self.n3
        self.n5.right = self.n8

        self.n3.left = self.n1
        self.n3.right = self.n4
        self.n3.parent = self.n5

        self.n8.left = self.n7
        self.n8.right = self.n9
        self.n8.parent = self.n5

        self.n1.right = self.n2
        self.n1.parent = self.n3

        self.n4.parent = self.n3

        self.n7.left = self.n6
        self.n7.parent = self.n8

        self.n9.right = self.n10
        self.n9.parent = self.n8

        self.n2.parent = self.n1

        self.n6.parent = self.n7

        self.n10.parent = self.n9

    def test_get_next_from_n2(self):
        """
        Input: Node with value 2.
        The fn get_next should return the node with value 1.
        :return: void
        """
        self.assertTrue(get_next(self.n2) is self.n3)

    def test_get_next_from_n1(self):
        """
        Input: Node with value 1.
        The fn get_next should return the node with value 2.
        :return: void
        """
        self.assertTrue(get_next(self.n1) is self.n2)

    def test_get_next_from_n3(self):
        """
        Input: Node with value 3.
        The fn get_next should return the node with value 4.
        :return: void
        """
        self.assertTrue(get_next(self.n3) is self.n4)

    def test_get_next_from_n4(self):
        """
        Input: Node with value 4.
        The fn get_next should return the node with value 5.
        :return: void
        """
        self.assertTrue(get_next(self.n4) is self.n5)

    def test_get_next_from_n5(self):
        """
        Input: Node with value 5.
        The fn get_next should return the node with value 6.
        :return: void
        """
        self.assertTrue(get_next(self.n5) is self.n6)

    def test_get_next_from_n6(self):
        """
        Input: Node with value 6.
        The fn get_next should return the node with value 7.
        :return: void
        """
        self.assertTrue(get_next(self.n6) is self.n7)

    def test_get_next_from_n7(self):
        """
        Input: Node with value 7.
        The fn get_next should return the node with value 8.
        :return: void
        """
        self.assertTrue(get_next(self.n7) is self.n8)

    def test_get_next_from_n8(self):
        """
        Input: Node with value 8.
        The fn get_next should return the node with value 9.
        :return: void
        """
        self.assertTrue(get_next(self.n8) is self.n9)

    def test_get_next_from_n9(self):
        """
        Input: Node with value 9.
        The fn get_next should return the node with value 10.
        :return: void
        """
        self.assertTrue(get_next(self.n9) is self.n10)

    def test_get_next_from_n10(self):
        """
        Input: Node with value 10.
        The fn get_next should return None.
        :return: void
        """
        self.assertIsNone(get_next(self.n10))

    def test_get_next_None(self):
        """
        Input: None
        The fn get_next should raise ValueError exception.
        :return: void
        """
        try:
            get_next(None)
            self.fail()
        except ValueError:
            pass
