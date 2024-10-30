# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node (root) is None, there is nothing to invert.
        if not root:
            return None
        
        # Recursive call: invert the right subtree.
        right = self.invertTree(root.right)
        
        # Recursive call: invert the left subtree.
        left = self.invertTree(root.left)
        
        # Swap the inverted left and right subtrees.
        root.left = right
        root.right = left
        
        # Return the root node after inversion.
        return root

        # Time Complexity: O(n)
        # Explanation: The function visits each node in the binary tree once.
        # In each visit, it performs constant-time operations, so the total time
        # complexity is O(n), where n is the number of nodes in the tree.

        # Space Complexity: O(h) in recursive stack space
        # Explanation: The recursive calls will use additional space on the call
        # stack, up to the height of the tree (h). In the worst case, for a skewed tree,
        # this height can be n (O(n)), while for a balanced tree, it will be O(log n).

        
        