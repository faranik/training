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
    uniques = {}

    while head_of_list is not None:
        if head_of_list not in uniques:
            uniques[head_of_list] = True
        else:
            return head_of_list

        head_of_list = head_of_list.next
