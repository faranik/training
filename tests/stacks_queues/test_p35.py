import unittest
from stacks_queues.p35 import Stack


class TestSortedStack(unittest.TestCase):

    def test_sort(self):
        """
        stack [1, 3, 2, 4, 0]
        After stack.sort() call the stack should be [4 3 2 1 0]

        :return: void
        """
        stack = Stack()
        stack.push(1)
        stack.push(3)
        stack.push(2)
        stack.push(4)
        stack.push(0)

        stack.sort()

        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 4)

    def test_sort_empty(self):
        """
        stack []
        After stack.sort() call the stack should stay []

        :return: void
        """
        stack = Stack()

        stack.sort()

        self.assertEqual(len(stack.arr), 0)

    def test_sort_one_elem(self):
        """
        stack = [3]
        Aster the stack.sort() call the stack should be [3]

        :return: void
        """
        stack = Stack()
        stack.push(3)

        stack.sort()

        self.assertEqual(stack.pop(), 3)

