# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Store the value of the current node (root) to use in comparisons.
        parent_node = root.val

        # Get the values of nodes p and q.
        p_val = p.val
        q_val = q.val

        # Case 1: If both p and q are greater than the current node's value,
        # they are both in the right subtree, so we move to the right.
        if p_val > parent_node and q_val > parent_node:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Case 2: If both p and q are less than the current node's value,
        # they are both in the left subtree, so we move to the left.
        elif p_val < parent_node and q_val < parent_node:
            return self.lowestCommonAncestor(root.left, p, q)

        # Case 3: If p and q are on opposite sides of the current node or
        # if one of them is equal to the current node, then the current node
        # is the lowest common ancestor.
        else:
            return root

        # Time Complexity: O(h)
        # Explanation: In a balanced BST, each recursive call eliminates half of
        # the remaining tree, where h is the height of the tree. Thus, in a balanced BST,
        # the time complexity is O(log n). In the worst case, for a completely skewed tree,
        # the time complexity is O(n), where n is the number of nodes.

        # Space Complexity: O(h)
        # Explanation: The recursion stack will go as deep as the height of the tree,
        # which is h. For a balanced BST, this height is O(log n), but in the worst case
        # of a skewed tree, it can be O(n).
