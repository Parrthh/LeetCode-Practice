# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the tree is empty, the depth is 0.
        if root is None:
            return 0
        
        else:
            # Recursive case:
            # Compute the maximum depth of the left subtree.
            left_depth = self.maxDepth(root.left)
            
            # Compute the maximum depth of the right subtree.
            right_depth = self.maxDepth(root.right)
            
            # The depth of the current node is the greater of the depths of
            # its left and right subtrees, plus 1 (to count the current node).
            return max(left_depth, right_depth) + 1

        # Time Complexity: O(n)
        # Explanation: Each node in the tree is visited exactly once to compute its depth,
        # resulting in a total time complexity of O(n), where n is the number of nodes.

        # Space Complexity: O(h)
        # Explanation: The recursive call stack will hold up to h recursive calls at a time,
        # where h is the height of the tree. In the worst case (skewed tree), this is O(n),
        # and for a balanced tree, it's O(log n).

