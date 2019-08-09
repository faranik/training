import unittest
from recursivity.p5 import multiply


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        """
        Input: 2 * 2
        Output: 4
        :return: void
        """
        self.assertEqual(4, multiply(2, 2))

    def test_multiply_zero(self):
        """
        Input: 0 * 2
        Output: 0
        :return: void
        """
        self.assertEqual(0, multiply(0, 2))

    def test_multiply_bigger(self):
        """
        Input: 1 000 000 * 1 000 000
        Output: 1 000 000 000 000
        :return: void
        """
        self.assertEqual(1000000000000, multiply(1000000, 1000000))
