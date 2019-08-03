import unittest
from bits.p5_1 import insert_number


class TestInsertNumber(unittest.TestCase):

    def test_insert_number(self):
        n = int('10000000000', 2)
        m = int('10011', 2)

        l = insert_number(m, n, 6, 2)

        print(l)