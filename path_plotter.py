#!/usr/bin/env python
"""
@author: mattia
"""

import numpy as np
import matplotlib.pyplot as plt


class PathPlotter():
    """
    Used for plotting the path
    """

    @staticmethod
    def path_visualizer(grid, path):
        """
        grid: Array with True and False
        path: List of Nodes
        """

        newgrid = np.zeros((grid.shape[0],grid.shape[1]))
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] == True:
                    newgrid[i][j] = 0
                else:
                    newgrid[i][j] = 1


        for node in path:
            newgrid[node.x][node.y] = 0.5


        newgrid[path[0].x, path[0].y] = 0.4
        newgrid[path[-1].x, path[-1].y] = 0.7


        plt.figure()
        # im = plt.imshow(newgrid.T, interpolation='none', vmin=0, vmax=1, aspect='equal', origin='lower');
        im = plt.imshow(newgrid.T, interpolation='none', cmap = 'gist_ncar',vmin=0, vmax=1, origin='lower');

        ax = plt.gca();

        # Major ticks
        ax.set_xticks(np.arange(0, grid.shape[0], 1));
        ax.set_yticks(np.arange(0, grid.shape[1], 1));

        # Labels for major ticks
#        ax.set_xticklabels(np.arange(1, grid.shape[0], 1));
#        ax.set_yticklabels(np.arange(1, grid.shape[1], 1));

        # Minor ticks
        ax.set_xticks(np.arange(-.5, grid.shape[0], 1), minor=True);
        ax.set_yticks(np.arange(-.5, grid.shape[1], 1), minor=True);

        # Gridlines based on minor ticks
        ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

        plt.xlabel('X')
        plt.ylabel('Y')


        # Arrows

        for node in path:
            arrow_length = 0.8
            if node.orientation == 0:
                dx = 0
                dy = arrow_length
                x = node.x
                y = node.y - 0.5

            elif node.orientation == 1:
                dx = arrow_length
                dy = 0
                x = node.x - 0.5
                y = node.y

            elif node.orientation == 2:
                dx = 0
                dy = - arrow_length
                x = node.x
                y = node.y + 0.5

            elif node.orientation == 3:
                dx = - arrow_length
                dy = 0
                x = node.x + 0.5
                y = node.y

            plt.arrow(x,y,dx,dy,head_width=0.2, head_length=0.3, length_includes_head=True,width=0.05, color = 'black')


        plt.ion()
        plt.show()
        raw_input("Press Enter to close plot...")
        plt.close()
