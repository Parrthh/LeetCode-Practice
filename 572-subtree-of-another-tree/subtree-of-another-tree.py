# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_method(node):
            # If the node here is empty, no tree is rooted at this node
            # Thus "tree rooted at node" cannot be same as "tree rooted at subroot"
            if node is None:
                return False
            
            # Here, we call the identical_check function to compare the subtree rooted at the node
            # is identical to the subroot
            elif identical_check(node, subRoot):
                return True
            
            # If the current node is not the root of the tree that matches with the subRoot
            # We then recursively check the left and right children of the current node
            return dfs_method(node.left) or dfs_method(node.right)

        
        # Here, we check the subtrees rooted at node1 and node2 are same
        def identical_check(node1, node2):
            # If both nodes are empty the tree is identical
            if node1 is None or node2 is None:
                return node1 is None and node2 is None
            
            return (node1.val == node2.val and identical_check(node1.left, node2.left) and 
            identical_check(node1.right, node2.right))

        return dfs_method(root)
            
        

        