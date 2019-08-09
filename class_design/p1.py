"""
Circular Array: Implement a CircularArray class that supports an array-like
data structure which can be efficiently rotated. If possible, the class
should use a generic type (also called a template), and should support
iteration via the standard for (Obj 0 : circularArray) notation.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


class CircularArray:

    def __init__(self, size):
        self.size = size
        self.arr = [None] * size

        self.writer = 0
        self.reader = 0

    def write(self, obj):
        if obj is None:
            raise ValueError("Invalid argument.")

        if self.arr[(self.writer + 1) % self.size] is None:
            self.writer += 1
            self.arr[self.writer % self.size] = obj

        if self.writer > self.size:
            self.writer = self.writer % self.size

    def read(self):
        value = None
        if self.arr[(self.reader + 1) % self.size] is not None:
            self.reader += 1
            value = self.arr[self.reader % self.size]
            self.arr[self.reader % self.size] = None

        if self.reader > self.size:
            self.reader = self.reader % self.size

        return value

    def __iter__(self):
        return self

    def __next__(self):
        value = self.read()

        if value is None:
            raise StopIteration()

        return value
