# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs_method(root):
            if not root: # If the root is empty it is a balanced tree
                return [True, 0]   # The height when the root is None will be 0

            # Implementing recursive functionality on both the subtrees
            left, left_height = dfs_method(root.left)
            right, right_height = dfs_method(root.right)

            # We are checking if both the subtrees are balanced
            # As well as the difference in their heights is atmost 1
            # If the difference is greater we break the loop and return False
            balanced = (left and right and abs(left_height - right_height) <= 1)

            # The current height of the node is always the max value of its subtrees + 1
            current_height = 1 + max(left_height, right_height)

            # Here we are returning results both the approaches
            # Balanced provides a boolean output
            # Current_height provides with the height of the specific node
            return balanced, current_height
        # This line starts the recursion from the root and checks whether entire tree is balanced
        balanced, _ = dfs_method(root)

        # Returns the final boolean output
        return balanced

        