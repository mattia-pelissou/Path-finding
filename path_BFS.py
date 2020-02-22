#!/usr/bin/env python
"""
@author: mattia
"""

class PathFinder_BFS():
    """
    Implementation of the BFS (Breadth-first search) algorithm
    """

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

        # We use a queue, which is a list inside which we put the nodes that need to be considered on a First In First Out way
        queue = [start_node]

        visited_nodes = [start_node]

        while (queue != []):

            # Get the first node in the queue
            current_node = queue[0]

            # Compute the child wp, that is to say all the nodes accessible from the current node
            child_nodes = current_node.children

            for node in child_nodes:
                node.parent = current_node

                # Check is node not in obstacle
                if (PathFinder_BFS.not_in_obstacle(node, grid) == True):

                    # Check that node is not already in the closed list
                    if node not in visited_nodes:
                        visited_nodes.append(node)

                        if node == goal_node:
                            # Goal found
                            path = PathFinder_BFS.reconstruct_path(node,start_node,goal_node)                            
                            return path

                        else:
                            queue.append(node)

            # Remove first element of the queue
            queue.pop(0)

        return 0
