"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C - > D -> E -> C [the same C as earlier)
Output: C

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""

from lists.node import Node


def get_loop(head_of_list: Node) -> Node:
    """
    Time complexity: O(2N)
    Space complexity: O(1)

    :param head_of_list: First element of the list.
    :return: Instance of the first node of the loop. None if there is not a loop.
    """
    if head_of_list is None or head_of_list.next is None or head_of_list.next.next is None:
        return None

    slow_runner = head_of_list.next
    fast_runner = head_of_list.next.next

    while slow_runner is not fast_runner:

        slow_runner = slow_runner.next
        if fast_runner.next is not None:
            fast_runner = fast_runner.next.next
        else:
            return None

        if slow_runner is None or fast_runner is None:
            return None

    curr = head_of_list
    while curr is not slow_runner:
        curr = curr.next
        slow_runner = slow_runner.next

    return curr


def get_loop_(head_of_list: Node) -> Node:
    """
    Time complexity: O(N)
    Space complexity: O(N)

    :param head_of_list: The head of the list.
    :return: Instance of the first node of the loop. None if there is not a loop.
    """
    uniques = {}

    head_of_loop = None
    while head_of_list is not None:
        if head_of_list not in uniques:
            uniques[head_of_list] = True
        else:
            head_of_loop = head_of_list
            break

        head_of_list = head_of_list.next
    return head_of_loop
