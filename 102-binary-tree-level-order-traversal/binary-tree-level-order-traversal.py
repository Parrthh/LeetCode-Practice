# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# If the tree is empty, then there is no need to traverse
       if root is None:
           return [ ]
      
       # This list will store the final level-order travesal.
       # Each element in this list will represent one level of the tree
       result = []
       # deque is a double ended queue, which is optimal for adding and removing from both ends
       # We initialize the queue with the root node of the tree
       # This ensures that we begin our traversal from the root
       queue = deque([root])
      
       # This loop continues as long as there are nodes in the queue.
       # As we process nodes at each level, their children (the next level) will be added to queue
       while queue:
           # This captures the number of nodes at each level (i.e. how many nodes at each level)
           # We need this because the number of nodes at each level can vary
           # We want to process all the nodes at every level one at a time
           level_length = len(queue)
           # This will store the values of the nodes at the current level
           level = []
          
           # This loop iterates exactly "level_size" times
           # The "level_size" variables corresponds to the number of nodes present at the current                  level
           # For each iteration we process one node from the current level, append its value to the level list, and add its children to the queue (for processing in the next level)
          
           for _ in range(level_length):
               # We remove the node from the front of the queue, the nodes are processed in FIFO
               node = queue.popleft()
               # We visit the node by appending its value to the level list, which will store the values of all nodes at this level
               level.append(node.val)
              
               if node.left:
                   queue.append(node.left)
               if node.right:
                   queue.append(node.right)
           result.append(level)
       return result

"""
TIME COMPLEXITY: O(n)
1. Each node in the tree is visited once, and once, meaning the total work done
by the algorithm is directly proportional to the number of nodes
2. Adding nodes to and removing nodes from the deque takes O(1) time, and since we do this operation
once per node, the overall time complexity is O(n)

SPACE COMPLEXITY: O(n)
1. The queue that stores nodes at each level. In the worst case (for a full binary tree),
the queue may hold up to half of the total nodes at the last level, which is O(n)
2. The result list, which stores all nodes in a nested list of format
"""