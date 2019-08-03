import unittest
from bits.p5_4 import get_largest


class TestGetLargest(unittest.TestCase):

    def test_get_largest_1(self):
        """
        Input: 1  (binary: 001)
        Output: 2 (binary: 010)
        :return: void
        """
        self.assertEqual(2, get_largest(1))

    def test_get_largest_9(self):
        """
        Input: 6 (binary: 0110)
        Output: 9 (binary: 1001)
        :return: void
        """
        self.assertEqual(9, get_largest(6))

    def test_get_largest_0(self):
        """
        Input: 0
        Output: 0
        :return: void
        """
        self.assertEqual(0, get_largest(0))
