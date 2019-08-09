import unittest
from recursivity.p4 import find_subsets

class TestFindSubsets(unittest.TestCase):

    def test_find_subsets(self):
        """
        Input: [1, 2, 3 , ]
        Outpur: [[3],
                 [2],
                 [2, 3],
                 [1],
                 [1, 3],
                 [1, 2]]
        :return: void
        """
        self.assertEqual([[3], [2], [2, 3], [1], [1, 3], [1, 2]], find_subsets([1, 2, 3]))

