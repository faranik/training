import unittest
from recursivity.p3 import find_magic

class TestFindMagic(unittest.TestCase):

    def test_find_magic(self):
        """
        Input: [-10, -5, 0, 3, 7]
        Output: 3
        :return: void
        """
        arr = [-10, -5, 0, 3, 7]
        self.assertEqual(3, find_magic(arr))

    def test_find_magic_no_magic(self):
        """
        Input: [-10, -5, 3, 4, 7, 9]
        Output: -1
        :return: void
        """
        self.assertEqual(-1, find_magic([-10, -5, 3, 4, 7, 9]))
