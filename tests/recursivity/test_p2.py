import unittest
from recursivity.p2 import PathPlanner


class TestPathPlanner(unittest.TestCase):

    def test_get_path(self):
        planner = PathPlanner(5, 4, [(1, 0), (1, 2), (3, 1), (3, 3)])

        path = planner.get_path()

        self.assertEqual(path, [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3)])
