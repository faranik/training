import unittest
from graphs.p4_8 import Node
from graphs.p4_8 import get_common_ancestor


class TestGetCommonAncestor(unittest.TestCase):
    def setUp(self) -> None:
        """
        Binary Tree
                          5
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

        self.n8.left = self.n7
        self.n8.right = self.n9

        self.n1.right = self.n2

        self.n7.left = self.n6

        self.n9.right = self.n10

    def test_get_common_ancestor_n2_n4(self):
        """
        Input: Nodes with values 2 and 4
        Output: Should return the node with value 3
        :return: void
        """
        root = self.n5
        n, _, _ = get_common_ancestor(root, self.n2, self.n4)

        self.assertTrue(n is self.n3)

    def test_get_common_ancestor_n3_n8(self):
        """
        Input: nodes with values 3 and 8.
        Output: Should return the root node with value 5.
        :return: void
        """
        root = self.n5
        n, _, _ = get_common_ancestor(root, self.n3, self.n8)

        self.assertTrue(n is root)

    def test_get_common_ancestor_no_ancestor(self):
        """
        Input: One node from the binary tree and one unknown.
        Output: Should return None as no common ancestor exists.
        :return: void
        """
        root = self.n5
        n, _, _ = get_common_ancestor(root, self.n3, Node(11))

        self.assertTrue(n is None)

    def test_get_common_ancestor_root_is_None(self):
        """
        Input: The root node is None.
        Output: Should return None.
        :return: void
        """
        n, _, _ = get_common_ancestor(None, self.n3, self.n8)

        self.assertTrue(n is None)

    def test_common_ancestor_parent_and_child(self):
        """
        Input: The nodes with value 7 and 6. The node 7 is parent of node 6.
        Output: Should return the parent of 7 which is the node with value 8
        :return: void
        """
        root = self.n5
        n, _, _ = get_common_ancestor(root, self.n7, self.n6)

        self.assertTrue(n is self.n8)

    def test_common_ancestor_args_type_verification(self):
        """
        Input: A string and two integers.
        Output: Should raise ValueError as the type of arguments is not valid.
        :return: void
        """
        try:
            get_common_ancestor("hopa", 6, 18)
            self.fail()
        except ValueError:
            pass