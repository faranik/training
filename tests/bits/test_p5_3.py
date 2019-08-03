import unittest
from bits.p5_3 import flip_bit_to_win


class TestFlipBitToWin(unittest.TestCase):

    def test_flip_bit_to_win_1755(self):
        """
        Input: 1775 or 11011101111
        Output: 8
        :return: void
        """
        self.assertEqual(8, flip_bit_to_win(1775))

    def test_flip_bit_to_win_1772(self):
        """
        Input: 1772 or 11011101100
        Output: 6
        :return: void
        """
        self.assertEqual(6, flip_bit_to_win(1772))

    def test_flip_bit_to_win_0(self):
        """
        Input: 0
        Output: 1
        :return: void
        """
        self.assertEqual(1, flip_bit_to_win(0))
