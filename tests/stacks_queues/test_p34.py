import unittest
from stacks_queues.p34 import MyQueue


class TestMyQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = MyQueue()

    def test_push(self):
        """
        queue << 6 << 8
        queue >> 8 >> 6
        The queue should return 6 then 8 if we pushed 6 then 8.
        :return: void
        """
        self.queue.push(6)
        self.queue.push(8)

        self.assertEqual(self.queue.pop(), 6)
        self.assertEqual(self.queue.pop(), 8)
