# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree is empty
        if not root:
            return None

        # Initialize a queue for level-order traversal
        queue = deque([root])
        level = 0  # Start from level 0 (even)

        while queue:
            # Get the current level's nodes
            level_size = len(queue)
            current_level_nodes = []

            # Collect all nodes at the current level
            for i in range(level_size):
                node = queue.popleft()
                
                # Append node values if on an odd level
                if level % 2 == 1:
                    current_level_nodes.append(node)
                
                # Enqueue child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the values of nodes at the current odd level
            if level % 2 == 1:
                # Reverse the values in the collected nodes
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    current_level_nodes[left].val, current_level_nodes[right].val = (
                        current_level_nodes[right].val,
                        current_level_nodes[left].val,
                    )
                    left += 1
                    right -= 1
            
            # Move to the next level
            level += 1

        return root

        # Time Complexity: O(n)
        # Explanation: We visit each node once during level-order traversal,
        # and at most, we perform a reverse operation on half the nodes in odd levels.
        # Therefore, the time complexity is O(n), where n is the number of nodes.

        # Space Complexity: O(n)
        # Explanation: We use a queue for level-order traversal, which, in the worst case,
        # may hold all nodes at a particular level. Therefore, the space complexity is O(n).
