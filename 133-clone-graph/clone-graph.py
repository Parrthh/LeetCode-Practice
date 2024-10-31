# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Time Complexity: O(V + E), where V is the number of nodes (vertices) 
        # and E is the number of edges in the graph.
        # This is because we visit each node and traverse each edge once during cloning.

        # Space Complexity: O(V), due to the space required to store cloned nodes 
        # in the `cloned_node` dictionary and the recursive stack for DFS.

        # Base Case: If the input node is None, return None since there is no graph to clone.
        if not node:
            return None
        
        # Dictionary to store the cloned nodes, mapping each original node to its clone.
        cloned_node = {}

        # DFS function to perform a depth-first traversal and clone each node and its neighbors.
        def dfs_method(original_node):
            # If the current node has already been cloned, return the clone.
            # This prevents revisiting nodes and resolves cycles in the graph.
            if original_node in cloned_node:
                return cloned_node[original_node]
            
            # Create a new clone of the current node with the same value.
            # Initially, this clone has no neighbors.
            clone = Node(original_node.val)
            # Store this clone in the cloned_node dictionary to track it.
            cloned_node[original_node] = clone
            
            # Recursively visit all the neighbors of the original node.
            # For each neighbor, call dfs_method to clone the neighbor and get the cloned neighbor node.
            for neighbor in original_node.neighbors:
                # Append each cloned neighbor to the current clone's neighbors list.
                clone.neighbors.append(dfs_method(neighbor))
            
            # After cloning all neighbors, return the fully constructed clone node.
            return clone

        # Begin DFS from the input node to clone the entire graph.
        return dfs_method(node)
