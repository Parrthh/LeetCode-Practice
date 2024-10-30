"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def __init__(self):
        self.visited_hash = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Base Case: To check if head is null
            if head == None:
                return 
            
            if head in self.visited_hash:
                return self.visited_hash[head]
            
            node = Node(head.val, None, None)
            self.visited_hash[head] = node

            node.next = self.copyRandomList(head.next)
            node.random =self.copyRandomList(head.random)

            return node

"""
# TIME COMPLEXITY:
The time complexity of this solution is O(n), where n is the number of nodes in the original linked list.

Each node is visited exactly once, so the recursive calls will run in O(n).
Additionally, each node is looked up and inserted into visited_hash in O(1) time, 
so the overall operations involving the dictionary also take O(n).
Since all operations are linear, the total time complexity remains O(n).

# SPACE COMPLEXITY:

The space complexity of this solution is also O(n).
The visited_hash dictionary stores a copy of each node from the original list, which requires O(n) space.
There is also an implicit recursive stack space usage for n recursive calls, which adds O(n) 
to the space complexity.
Thus, the overall space complexity is O(n), combining the dictionary storage and recursive stack usage.
"""