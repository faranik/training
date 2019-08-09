import unittest
from recursivity.p7 import get_permutations


class TestGetPermutations(unittest.TestCase):

    def test_get_permutations(self):
        """
        Input: ab
        Output: [ba, ab]
        :return: void
        """
        self.assertEqual(['ba', 'ab'], get_permutations('ab'))

    def test_get_permutations_abc(self):
        """
        Input: abc
        Output: ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
        :return: void
        """
        self.assertEqual(['cba', 'bca', 'bac', 'cab', 'acb', 'abc'], get_permutations('abc'))

    def test_get_permutations_empty(self):
        """
        Input: ''
        Output: []
        :return: void
        """
        self.assertEqual([], get_permutations(''))
