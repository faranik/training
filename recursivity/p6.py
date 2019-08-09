"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N
disks of different sizes which can slide onto any tower. The puzzle starts with disks
sorted in ascending order of size from top to bottom (Le., each disk sits on top of an
even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""


def towers_of_hanoi(stack1: list, stack2: list, stack3: list, n: int):
    if n == 1:
        stack3.append(stack1.pop())
    else:
        towers_of_hanoi(stack1, stack3, stack2, n - 1)
        towers_of_hanoi(stack1, stack2, stack3, 1)
        towers_of_hanoi(stack2, stack1, stack3, n - 1)
