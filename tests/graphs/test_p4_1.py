import unittest
from graphs.p4_1 import Node
from graphs.p4_1 import route_exists


class TestRouteExists(unittest.TestCase):

    def setUp(self) -> None:
        """
        Create graph:
        1: 2, 4
        2: 3
        3: 4
        4: 5
        5: _
        :return: void
        """
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)

        n1.children.append(n2)
        n1.children.append(n4)

        n2.children.append(n3)

        n3.children.append(n4)

        n4.children.append(n5)

        self.start = n1
        self.end = n3

    def test_route_exists(self):
        """
        The function route_exists should return True for start and end nodes.
        :return: void
        """

        self.assertTrue(route_exists(self.start, self.end))

    def test_route_exists_non_existing_route(self):
        """
        The function route_exists should return False for start and a new node.
        :return: void
        """
        self.assertFalse(route_exists(self.start, Node(6)))

    def test_route_exists_None(self):
        """
        The function route_exists should raise ValueError for None as argument.
        :return: void
        """
        try:
            route_exists(None, None)
            self.fail()
        except ValueError:
            pass

    def test_route_exists_int_str(self):
        """
        The function route_exists should raise ValueError for int and str as args.
        :return: void
        """
        try:
            route_exists(4, "hopa")
            self.fail()
        except ValueError:
            pass
