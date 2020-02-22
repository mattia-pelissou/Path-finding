#!/usr/bin/env python
"""
@author: mattia
Multiple tests are run in this script
"""

import sys
import unittest
import numpy as np
from path_node import Node
from path_BFS import PathFinder_BFS
from path_plotter import PathPlotter
from path_validator import PathValidator


class Challenge1TestCase(unittest.TestCase):

    def setUp(self):
        self.pathfinder = PathFinder_BFS()

    def tearDown(self):
        self.pathfinder = None

    def _run_test(self, grid, queries):
        for query in queries:
            path = self.pathfinder.get_path(grid, query[0], query[1])
            PathPlotter.path_visualizer(grid, path)

            self.assertTrue(PathValidator.is_valid_path(grid, query, path),
                            "Invalid path %s for query %s." % (path, query))

    def test_1_straight_no_obstacle(self):
        grid = np.zeros((grid_width, grid_height)).astype(np.bool)
        queries = [
            [Node(5, 5, 0), Node(5, 8, 0)],
            [Node(16, 5, 1), Node(8, 5, 1)],
            [Node(5, 15, 3), Node(16, 15, 3)],
        ]
        self._run_test(grid, queries)

    def test_2_turn_no_obstacle(self):
        grid = np.zeros((grid_width, grid_height)).astype(np.bool)
        queries = [
            [Node(5, 7, 0), Node(15, 8, 3)],
            [Node(16, 5, 2), Node(8, 5, 1)],
            [Node(15, 15, 1), Node(16, 15, 3)],
        ]
        self._run_test(grid, queries)

    def test_3_obstacle(self):
        grid = np.zeros((grid_width, grid_height)).astype(np.bool)
        # Obstacle
        grid[0:12, 12:14] = True
        queries = [
                [Node(2, 2, 0), Node(2, 16, 0)],
                [Node(14, 8, 0), Node(6, 17, 0)],
                [Node(18, 8, 2), Node(4, 17, 1)],
                [Node(15, 15, 1), Node(16, 15, 3)]
        ]
        self._run_test(grid, queries)

    def test_4_with_multiple_obstacles(self):
        grid = np.zeros((grid_width, grid_height)).astype(np.bool)
        # Obstacles
        grid[3:4, 0:15] = True
        grid[13:14, 5:20] = True
        queries = [
            [Node(0, 0, 0), Node(16, 15, 0)]
        ]
        self._run_test(grid, queries)


if __name__ == '__main__':
    # Just to avoir creating .pyc files
    sys.dont_write_bytecode = True

    # Grid size
    grid_width  = 20
    grid_height = 20

    unittest.main()
