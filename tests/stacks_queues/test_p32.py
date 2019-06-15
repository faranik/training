import unittest
from stacks_queues.p32 import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self):
        """
        stack << 1 << 4

        stack.arr should contain two elements, 1 and 4
        :return: void
        """
        self.stack.push(1)
        self.stack.push(4)

        self.assertTrue(len(self.stack.arr) == 2)
        self.assertEqual(self.stack.arr[0], 1)
        self.assertEqual(self.stack.arr[1], 4)

    def test_push_None(self):
        """
        stack << None

        stack should raise invalid value exception
        :return: void
        """
        try:
            self.stack.push(None)
            self.fail("The stack's push function should not accept other values than integers")
        except ValueError:
            pass

    def test_push_str(self):
        """
        stack << "hopa"

        stack should raise invalid value exception
        :return: void
        """
        try:
            self.stack.push("jora")
            self.fail("The stack's push function should not accept other valuers that integers")
        except ValueError:
            pass

    def test_pop(self):
        """
        stack << 1 << 4
        stack >> 1 >> 4

        If 1 then 4 were pushed to stack then first pop should return 4 and second 1
        :return: void
        """
        self.stack.push(1)
        self.stack.push(4)

        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty(self):
        """
        If the stack is empty the stack should raise a runtime exception.
        :return: void
        """
        try:
            self.stack.pop()
            self.fail("Pop on empty stack should raise runtime error.")
        except RuntimeError:
            pass

    def test_min(self):
        """
        stack.arr << 3 << 4 << 2 << 5 << 6 << 9 << 0 << 5 << 6
        stack.min << 3 << 2 << 0

        This test is a sequence of push/pop operation on stack and min interrogation.
        :return: void
        """
        self.stack.push(3)
        self.assertEqual(self.stack.get_min(), 3)

        self.stack.push(4)
        self.assertEqual(self.stack.get_min(), 3)

        self.stack.push(2)
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.push(5)
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.push(6)
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.push(9)
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.push(0)
        self.assertEqual(self.stack.get_min(), 0)

        self.stack.push(5)
        self.assertEqual(self.stack.get_min(), 0)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 0)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 3)

        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 3)