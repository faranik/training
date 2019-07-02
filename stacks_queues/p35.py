"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any
other data structure (such as an array). The stack supports the following operations:
push, pop, peek, and isEmpty.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Stack:

    def __init__(self):
        self.arr = []

    def push(self, elem):
        self.arr.append(elem)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Cannot pop, I'm empty!")
        else:
            return self.arr.pop()

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Cannot peek, I'm empty!")
        else:
            return self.arr[-1]

    def is_empty(self):
        return len(self.arr) == 0

    def sort(self):
        stack = Stack()
        not_sorted = True

        while not_sorted:
            while not self.is_empty():
                a = self.pop()

                if not self.is_empty():
                    b = self.peek()
                    if a < b:
                        stack.push(a)
                    else:
                        stack.push(b)
                        stack.push(a)
                        self.pop()
                else:
                    stack.push(a)

            is_sorted = True
            while not stack.is_empty():
                a = stack.pop()
                if not self.is_empty():
                    b = self.peek()
                    if b < a:
                        is_sorted = False

                self.push(a)

            if is_sorted:
                not_sorted = False
