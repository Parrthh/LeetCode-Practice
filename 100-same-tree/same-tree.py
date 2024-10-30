# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: If both nodes are None, they are identical (both empty).
        if not p and not q:
            return True
        
        # Base case 2: If one of the nodes is None and the other isn't,
        # they are not identical because one tree has an extra node.
        if not q or not p:
            return False
        
        # Base case 3: If the values of the current nodes are not equal,
        # then the trees are not identical.
        if p.val != q.val:
            return False
        
        # Recursive case:
        # Check if the left subtree of 'p' is identical to the left subtree of 'q'
        # AND if the right subtree of 'p' is identical to the right subtree of 'q'.
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
