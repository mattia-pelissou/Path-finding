#!/usr/bin/env python
"""
@author: mattia
"""

import numpy as np

class Node():
    """
    Class Node. A note is a waypoint with associated orientation, parent and costs h, g and f
    Note about orientation. Orientation is an integer between 0 and 3 inclusive.
        0 maps to the unit vector (0, 1)
        1 maps to the unit vector (1, 0)
        2 maps to the unit vector (0, -1)
        3 maps to the unit vector (-1, 0)
    An easy way to think about the orientation is that 0 is North, 1 is East, 2 is South, and 3 is West.
    """

    def __init__(self, x, y, orientation, parent = None, g = 0, h = 0):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def movement_cost(self, other):
        if self.orientation == other.orientation:
            return 1
        else:
            return 2

    @property
    def tuple(self):
        return tuple((self.x, self.y, self.orientation))

    def __str__(self):
        return 'Waypoint({}, {}, {})'.format(self.x, self.y, self.orientation)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.orientation == other.orientation

    def __ne__(self, other):
        return not self.__eq__(other)

    def euclidean_dist(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


    @property
    def children(self):
        """
        Returns all the child nodes of the input node
        A child node is a node that can be reached from the current node with all the allowed movements
        """
        x = self.x
        y = self.y
        orientation = self.orientation

        if (orientation == 0):
            child_nodes = [
            Node(x, y+1, 0),
            Node(x, y-1, 0),
            Node(x+1, y+1, 1),
            Node(x-1, y+1, 3),
            Node(x-1, y-1, 1),
            Node(x+1, y-1, 3)
            ]
        elif (orientation == 1):
            child_nodes = [
            Node(x+1,y,1),
            Node(x+1,y+1,0),
            Node(x+1,y-1,2),
            Node(x-1,y,1),
            Node(x-1,y+1,2),
            Node(x-1,y-1,0),
            ]
        elif (orientation == 3):
            child_nodes = [
            Node(x-1,y,3),
            Node(x-1,y+1,0),
            Node(x-1,y-1,2),
            Node(x+1,y,3),
            Node(x+1,y+1,2),
            Node(x+1,y-1,0)
            ]
        elif (orientation == 2):
            child_nodes = [
            Node(x,y+1,2),
            Node(x+1,y+1,3),
            Node(x-1,y+1,1),
            Node(x,y-1,2),
            Node(x-1,y-1,3),
            Node(x+1,y-1,1)
            ]

        return child_nodes
