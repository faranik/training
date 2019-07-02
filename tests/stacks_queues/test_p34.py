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

    def test_push_None(self):
        """
        queue << None
        The queue should raise ValueError exception as None is not a valid input.
        :return: void
        """
        try:
            self.queue.push(None)
            self.fail()
        except ValueError:
            pass

    def test_push_str(self):
        """
        queue << "hopa"
        The queue should raise ValueError exception as a string is not a valid input.
        :return: void
        """
        try:
            self.queue.push("hopa")
            self.fail()
        except ValueError:
            pass

    def test_push_big_number(self):
        self.queue.push(2347182734618236419873624187236418237641872364)
        print(self.queue.pop())

    def test_pop_empty_queue(self):
        """
        queue is []
        The call to pop() should raise a RuntimeError.
        :return: void
        """
        try:
            self.queue.pop()
            self.fail()
        except RuntimeError:
            pass

    def test_pop(self):
        """
        queue << 6 << 8
        queue >> 6
        queue << 7 << 5
        queue >> 8 >> 7 >> 5
        The queue should respect the FIFO order.
        :return: void
        """
        self.queue.push(6)
        self.queue.push(8)

        self.assertEqual(self.queue.pop(), 6)

        self.queue.push(7)
        self.queue.push(5)

        self.assertEqual(self.queue.pop(), 8)
        self.assertEqual(self.queue.pop(), 7)
        self.assertEqual(self.queue.pop(), 5)