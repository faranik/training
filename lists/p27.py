"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""
class Node:
    def __init__(self, data: int, next):
        self.data = data
        self.next = next


def get_intersection(l1: Node, l2: Node) -> Node:
    n = None

    if l1.next is not None and l2.next is not None:
        n = get_intersection(l1.next, l2.next)
    elif l1.next is not None and l2.next is None:
        n = get_intersection(l1.next, l2)
    elif l1.next is None and l2.next is not None:
        n = get_intersection(l1, l2.next)
    else:
        if l1 is l2:
            return l1
        else:
            return None

    if n is None:
        return None
    else:
        if l1 is l2:
            return l1
        else:
            return n
