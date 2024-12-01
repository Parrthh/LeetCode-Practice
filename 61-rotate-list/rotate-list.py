# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Reducing k using Modular Arithmetic:
        # Purpose: Optimize the number of rotations
            # Rotating a list n times ( where n = length of list) results in the same list. Therefore,
            # k = k % length
        k %= length
        if k == 0:
            return head
        
        # Finding the new tail:
        # Find the node that will become the new tail after the rotation
        # The new tail is at the position length - k (1-based index)
        new_tail_position = length - k
        new_tail = head
        for _ in range(new_tail_position - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        current.next = head
        return new_head
        
"""
TIME COMPLEXITY: O(n)
1. One traversal to find the length and another to find the new tail

SPACE COMPLEXITY: O(n)
1. Only uses a few pointers for manipulation
"""