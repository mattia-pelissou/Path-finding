#!/usr/bin/env python
"""
@author: mattia
"""

class PathFinder():
    """
    Implementation of the A* algorithm
    """

    @staticmethod
    def get_node_smallest_f(open_list):
        node_min = open_list[0]
        f_min = node_min.f

        for node in open_list:
            if node.f < f_min:
                node_min = node
                f_min = node.f

        return node_min

    @staticmethod
    def reconstruct_path(current_node,start_node,end_node):
        """
        Return list of nodes from start node to end node with all the nodes being parent of one another
        """
        path = [current_node]
        parent_node = current_node.parent

        while (path[0] != start_node):
            path.insert(0,parent_node)
            parent_node = parent_node.parent

        return path

    @staticmethod
    def not_in_obstacle(node,grid):
        """
        Check if this node is node in an obstacle
        """
        # Check if inside bounds
        x_max = grid.shape[0]
        y_max = grid.shape[1]

        if (node.x <= x_max-1 and node.x >= 0 and node.y <= y_max-1 and node.y >= 0): # In bounds

            if (grid[node.x][node.y] == False): # Not in an obstacle
                return True
        else:
            return False


    def get_path(self, grid, start_node, goal_node):
        """

        """

        # Open list is a waiting list. At each step we will take the node inside the open list with the lowest cost
        open_list = [start_node]
        # Open list a list inside which we put all the nodes that have been checked already
        closed_list = []

        while (open_list != []):

            # Get the node with the smallest total cost f
            current_node = PathFinder.get_node_smallest_f(open_list)

            # Remove it from the open_list
            open_list.remove(current_node)
            # Add it to the closed list
            closed_list.append(current_node)

            # Check if the current node is the goal
            if (current_node == goal_node):
                # Goal reached !
                path = PathFinder.reconstruct_path(current_node,start_node,goal_node)
                return path

            # Compute the child wp, that is to say all the nodes accessible from the current node
            child_nodes = current_node.children

            for node in child_nodes:

                # Check is node not in obstacle
                if (PathFinder.not_in_obstacle(node, grid) == True):

                    # Check that node is not already in the closed list
                    if node not in closed_list:

                        potential_g_cost = current_node.movement_cost(node) + current_node.g

                        if ((node not in open_list) or (node in open_list and potential_g_cost < node.g)):

                            node.parent = current_node
                            node.h = node.euclidean_dist(goal_node)
                            node.g = current_node.g + current_node.movement_cost(node)
                            node.f = node.h + node.g

                            open_list.append(node)

        return 0
