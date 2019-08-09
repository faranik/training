import unittest
from recursivity.p6 import towers_of_hanoi


class TestTowersOfHanoi(unittest.TestCase):

    def test_move(self):
        """
        Input:
            stack1: [3, 2, 1]
            stack2: []
            stack3: []
        Output:
            stack1: []
            stack2: []
            stack3: [3, 2, 1]
        :return: void
        """
        stack1 = [3, 2, 1]
        stack2 = []
        stack3 = []

        towers_of_hanoi(stack1, stack2, stack3, 3)
        self.assertEqual([3, 2, 1], stack3)

    def test_move_bigger(self):
        """
        Input:
            stack1: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            stack2: []
            stack3: []
        Output:
            stack1: []
            stack2: []
            stack3: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        :return: void
        """
        stack1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        stack2 = []
        stack3 = []

        towers_of_hanoi(stack1, stack2, stack3, 10)
        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], stack3)
