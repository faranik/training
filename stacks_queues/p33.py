"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific substack.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Stack:
    def __init__(self, size):
        self.arr = []
        self.limit_size = size

    def push(self, elem: int) -> bool:
        if len(self.arr) == self.limit_size:
            return False
        self.arr.append(elem)
        return True

    def pop(self) -> int:
        if len(self.arr) == 0:
            raise RuntimeError("I'm empty!")
        return self.arr.pop()


class SetOfStacks:
    def __init__(self, stack_size):
        self.arr = [Stack(stack_size)]
        self.stack_size = stack_size

    def push(self, elem: int):
        if not isinstance(elem, int):
            raise ValueError("Invalid value. Data type should be integer.")

        if not self.arr[-1].push(elem):
            self.arr.append(Stack(self.stack_size))
            self.arr[-1].push(elem)

    def pop(self) -> int:
        try:
            return self.arr[-1].pop()
        except RuntimeError:
            if len(self.arr) == 1:
                raise RuntimeError("The stack is empty.")
            else:
                self.arr.pop()
                return self.arr[-1].pop()

    def pop_at(self, idx):
        if idx < 0 or idx >= len(self.arr):
            raise ValueError("Outbound index in input.")
        return self.arr[idx].pop()
