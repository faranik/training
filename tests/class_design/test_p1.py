import unittest
from class_design.p1 import CircularArray


class TestCircularArray(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = CircularArray(3)

    def test_object_initialization(self):
        """
        Input: 3
        Output: The created instance has an array of size 3
        :return: void
        """
        self.assertEqual(3, len(self.obj.arr))

    def test_write_and_read(self):
        """
        Input: 3 and 7
        Result: The numbers 3 and 7 should be writen in the circular array.
        :return: void
        """
        self.obj.write(3)
        self.obj.write(7)

        self.assertEqual(3, self.obj.read())
        self.assertEqual(7, self.obj.read())

    def test_write_more_then_sizeof_array(self):
        """
        Input: 3, 5, 7, 9
        Result: As the size of circular array is 3, 4th write (9) should not be writen
                to the circular buffer because there is no place for it.
        :return: void
        """
        self.obj.write(3)
        self.obj.write(5)
        self.obj.write(7)
        self.obj.write(9)

        self.assertEqual(3, self.obj.read())
        self.assertEqual(5, self.obj.read())
        self.assertEqual(7, self.obj.read())
        self.assertIsNone(self.obj.read())

    def test_iterator(self):
        """
        Input: 3, 4, 5
        Result: We should be able to iterate on the circular array in a for loop.
        :return: void
        """
        ground_truth = [3, 4, 5]
        self.obj.write(ground_truth[0])
        self.obj.write(ground_truth[1])
        self.obj.write(ground_truth[2])

        idx = 0
        for value in self.obj:
            self.assertEqual(ground_truth[idx], value)
            idx += 1

        for i, value in enumerate(self.obj):
            self.assertEqual(ground_truth[i], value)
