# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k-=1
            if k == 0:
                return current.val
            current = current.right

"""
TIME COMPLEXITY: O(N)
1. Since we traverse nodes in an in-order fashion, we visit each node at most once
2. Thus, in the worst case, this would take O(n) time if k is very large
3. We stop as soon as we reach the kth smallest element,
which can sometimes be faster than visiting all nodes

SPACE COMPLEXITY: O(h), h -> height of the tree
1. In the worst case, the stack will hold all the nodes on a single path from root to leaf,
which is the height of the tree
2. For a balanced tree, the height is O(logn), but in the worst case (for a skewed tree), 
it can be O(n)
"""
        
          
            

                
        