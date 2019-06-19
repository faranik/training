import unittest
from stacks_queues.p33 import SetOfStacks


class TestSetOfStacks(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = SetOfStacks(3)

    def test_instance_correct_corrected(self):
        """
        The set of stacks should contain only one sub-stacks.
        :return: void
        """
        self.assertEqual(len(self.stack.arr), 1)

    def test_push(self):
        """
        stack << 6
        The stack should contain one value and it should be 6.
        :return: void
        """
        self.stack.push(6)

        self.assertEqual(self.stack.arr[0].arr[0], 6)

    def test_push_None(self):
        """
        stack << None
        The stack should raise invalid value exception.
        :return: void
        """
        try:
            self.stack.push(None)
            self.fail()
        except ValueError:
            pass

    def test_push_str(self):
        """
        stack << "hopa"
        The stack should raise invalid value exception.
        :return: void
        """
        try:
            self.stack.push("hopa")
            self.fail()
        except ValueError:
            pass

    def test_push_creates_new_sub_stack(self):
        """
        stack << 1 << 2 << 3 << 4
        The stack should have the form:
            first sub-stack [1, 2, 3]
            second sub-stack [4]
        :return: void
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(len(self.stack.arr), 2)
        self.assertEqual(self.stack.arr[1].arr[0], 4)
        self.assertEqual(len(self.stack.arr[0].arr), 3)
        self.assertEqual(len(self.stack.arr[1].arr), 1)

    def test_pop(self):
        """
        stack << 1 << 2 << 3 << 4
        stack << 1 >> 2 >> 3 >> 4
        The stack should respect the LIFO sequence.
        :return: void
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty_stack(self):
        """
        stack >>
        The stack should raise RuntimeError as it is empty.
        :return: void
        """
        try:
            self.stack.pop()
            self.fail()
        except RuntimeError:
            pass

    def test_pop_after_pop_at(self):
        """
        stack << 1 << 2 << 3 << 4 << 5 << 6 << 7
        stack >> 3 >> 6 >> 7 by using pop_at
        pop should return 5
        :return: void
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(7)

        self.stack.pop_at(0)
        self.stack.pop_at(1)
        self.stack.pop_at(2)

        self.assertEqual(self.stack.pop(), 5)

    def test_pop_at(self):
        """
        stack << 1 << 2 << 3 << 4 << 5 << 6 << 7
        The stack should have this internal structure:
            sub-stack1: [1, 2, 3]
            sub-stack2: [4, 5, 6]
            sub-stack3: [7]
        pop_at(0) should return 3
        pop_at(1) should return 6
        pop_at(2) should return 7
        :return: void
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(7)

        self.assertEqual(self.stack.pop_at(0), 3)
        self.assertEqual(self.stack.pop_at(1), 6)
        self.assertEqual(self.stack.pop_at(2), 7)

    def test_pop_at_invalid_index(self):
        """
        stack << 1 << 2 << 3 << 4 << 5 << 6 << 7
        The stack should have this internal structure:
            sub-stack1: [1, 2, 3]
            sub-stack2: [4, 5, 6]
            sub-stack3: [7]
        pop_at(1000) should raise ValueError exception
        :return: void
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(7)

        try:
            self.stack.pop_at(1000)
            self.fail()
        except ValueError:
            pass
