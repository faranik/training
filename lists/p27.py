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


def get_list_size(head_of_list: Node) -> (int, Node):
    list_size = 0

    while head_of_list is not None:
        list_size += 1
        head_of_list = head_of_list.next

    return list_size, head_of_list


def get_kth_elem(head_of_list: Node, k: int) -> Node:

    for i in range(k):
        head_of_list = head_of_list.next

    return head_of_list


def get_intersection(l1: Node, l2: Node) -> Node:
    l1_size, l1_last_node = get_list_size(l1)
    l2_size, l2_last_node = get_list_size(l2)

    if l1_last_node is not l2_last_node:
        return None

    diff = abs(l1_size - l2_size)
    if l1_size > l2_size:
        l1 = get_kth_elem(l1, diff)
    elif l1_size < l2_size:
        l2 = get_kth_elem(l2, diff)

    while l1 is not l2:
        l1 = l1.next
        l2 = l2.next

    return l1


def get_intersection_(l1: Node, l2: Node) -> Node:

    if l1 is None or l2 is None:
        return None

    stack1 = []
    while l1 is not None:
        stack1.append(l1)
        l1 = l1.next

    stack2 = []
    while l2 is not None:
        stack2.append(l2)
        l2 = l2.next

    l1 = stack1.pop()
    l2 = stack2.pop()

    if l1 is not l2:
        return None

    common = None
    while l1 is l2:
        common = l1
        if len(stack1) > 0 and len(stack2) > 0:
            l1 = stack1.pop()
            l2 = stack2.pop()
        else:
            break

    return common
