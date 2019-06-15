"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class Stack:
    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, elem: int):
        if not isinstance(elem, int):
            raise ValueError("Invalid value. Data type should be integer.")

        self.arr.append(elem)
        if not self.min:
            self.min.append(elem)
        else:
            if elem <= self.min[-1]:
                self.min.append(elem)

    def pop(self) -> int:
        if self.arr:
            elem = self.arr.pop()
            if elem == self.min[-1]:
                self.min.pop()
        else:
            raise RuntimeError("Illegal pop operation on empty stack.")

        return elem

    def get_min(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            raise RuntimeError("Illegal min operation on empty stack.")
