"""
Route Between Nodes: Given a directed graph, design an algorithm to find
out whether there is a route between two nodes.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""

from queue import Queue


class Node:
    def __init__(self, data: int):
        self.data = data
        self.children = []
        self.visited = False


def route_exists(start: Node, end: Node) -> bool:
    if start is None or end is None:
        raise ValueError("Invalid arguments. They should not be None.")

    if not isinstance(start, Node) or not isinstance(end, Node):
        raise ValueError("Invalid arguments. The should be of type Node.")

    to_visit = Queue(0)
    to_visit.put(start)

    while not to_visit.empty():
        n = to_visit.get()
        if n is end:
            return True
        n.visited = True

        for child in n.children:
            if not child.visited:
                to_visit.put(child)

    return False
