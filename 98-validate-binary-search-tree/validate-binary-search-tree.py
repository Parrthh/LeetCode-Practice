# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Min value is set to negative infinity
        # Max value is set to positive infinity
        def isBST(node, min_value = float('-inf'), max_value= float('inf')):
            if not node:
                return True
            
            if node.val <= min_value or node.val >= max_value:
                return False
            
            return isBST(node.left, min_value, node.val) and isBST(node.right, node.val, max_value)
        
        return isBST(root)

"""
TIME COMPLEXITY:
1. Each node is visited exactly once in this approach, 
which means the algorithm performs a constant amount of work per node

2. For a tree with n nodes, the time complexity is therefore O(n), because each node is processed once

SPACE COMPLEXITY: O(H), h-> height of the tree
1. In worst case, the tree is skewed (either left-skewed or right-skewed)
and the recursion stack will hold n recursive calls (one for each node)
2. In the best case, (for a balanced tree), the height of the tree is log(n),
and therefore, the recursion stack will hold O(log n)

"""