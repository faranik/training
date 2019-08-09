"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows
and c columns. The robot can only move in two directions, right and down, but certain
cells are "off limits" such that the robot cannot step on them. Design an algorithm
to find a path for the robot from the top left to the bottom right.

Source: Cracking the Coding Interview: 189 Programming Questions and Solutions
by Gayle Laakmann McDowell
"""

class PathPlanner:
    def __init__(self, nb_rows: int, nb_cols: int, obstacles: list):
        self.r = nb_rows
        self.c = nb_cols
        self.obs = obstacles
        self.path = []

    def can_step(self, i: int, j: int) -> bool:
        if i < 0 or i >= self.r:
            return False
        if j < 0 or j >= self.c:
            return False
        if (i, j) in self.obs:
            return False
        return True

    def get_path(self) -> list:
        self.path = []
        self.__compute_path(0, 0)
        self.path.reverse()
        return self.path

    def __compute_path(self, row: int, col: int) -> bool:
        if row == self.r - 1 and col == self.c - 1:
            self.path.append((row, col))
            return True

        if not self.can_step(row, col):
            return False

        if self.__compute_path(row + 1, col) or self.__compute_path(row, col + 1):
            self.path.append((row, col))
            return True
        return False
