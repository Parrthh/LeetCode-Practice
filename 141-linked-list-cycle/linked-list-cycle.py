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
        