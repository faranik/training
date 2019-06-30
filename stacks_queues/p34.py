"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, elem: int):
        self.arr.append(elem)

    def pop(self) -> (int, bool):
        if len(self.arr) == 0:
            return 0, False
        else:
            return self.arr.pop(), True


class MyQueue:
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()

    def push(self, elem: int):
        self.stack_new.push(elem)

    def pop(self) -> int:
        print("Old: ", self.stack_old.arr)
        print("New: ", self.stack_new.arr)
        elem, success = self.stack_old.pop()

        if not success:
            self.__move_from_new_to_old()
            elem, success = self.stack_old.pop()

        if success:
            return elem
        else:
            raise RuntimeError("Empty queue.")

    def __move_from_new_to_old(self):
        elem, success = self.stack_new.pop()

        while success:
            self.stack_old.push(elem)
            elem, success = self.stack_new.pop()
