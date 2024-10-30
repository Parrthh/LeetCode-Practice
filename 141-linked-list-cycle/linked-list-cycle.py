# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = set()
        curr = head
        while curr:
            if curr in nodes_seen:
                return True
            nodes_seen.add(curr)
            curr = curr.next
        return False
    
"""
Time complexity : O(N)
As we visit each of the n elements in the list at most once. 
Adding a node to the hash table costs only O(1) time

Space Complexity: O(n)
The space depends on the number of elements added to the hash table,
which contains at most n elements


"""