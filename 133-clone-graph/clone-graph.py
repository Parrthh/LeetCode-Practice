"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base Case: Check if node is none, and return none as there is no graph to clone
        if not node:
            return None
        # Create a dict to store the cloned nodes
        cloned_node = {}
        # Implementing dfs functionality
        def dfs_method(original_node):
            # If the original_node exists and is already cloned
            # Return the clone to avoid infinite recursion
            if original_node in cloned_node:
                return cloned_node[original_node]
            # Create a new node with the same value of original node
            # Store the value in cloned_node
            clone = Node(original_node.val)
            cloned_node[original_node] = clone
            # For each neighbor in original_node
            # Recursively call dfs_method function to clone neighbors
            # Append the clones to clone.neighbors
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs_method(neighbor))
            # Return the clone of the starting node
            return clone
        # Recursively implement dfs function on all node
        return dfs_method(node)
