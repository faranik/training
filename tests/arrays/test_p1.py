import unittest
from arrays.p1 import get_longest_series_of_zeros


class TestGetLongestSeriesOfZeros(unittest.TestCase):

    def test_get_longest_series(self):
        """
        Input: 00111
               01111
               00001
               00011
        Output: 2
        :return: void
        """
        arr = [[0, 0, 1, 1, 1],
               [0, 1, 1, 1, 1],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 1, 1]]

        self.assertEqual(2, get_longest_series_of_zeros(arr))

    def test_get_longest_series_None(self):
        """
        Input: None
        Output:
        It should raise a ValueError exception as the input is not valid.
        :return: void
        """
        try:
            get_longest_series_of_zeros(None)
            self.fail()
        except ValueError:
            pass

    def test_get_longest_series_empty_array(self):
        """
        Input: Empty array []
        Output:
        It should raise a ValueError exception as the input is not valid.
        :return: void
        """
        try:
            get_longest_series_of_zeros([])
            self.fail()
        except ValueError:
            pass

    def test_get_longest_series_no_zeros(self):
        """
        Input: 11111
               11111
               11111
        Output: -1
        :return: void
        """
        arr = [[1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1]]

        self.assertEqual(-1, get_longest_series_of_zeros(arr))
