# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Creating a dummy node that points to the head
        dummy = ListNode(0, head)
        # Initializing two pointers, both starting at the dummy node
        first_pointer, second_pointer = dummy,dummy

        # Moving the first_pointer n+1 steps ahead
        for _ in range(n+1):
            if first_pointer is None:
                return None
            first_pointer = first_pointer.next
        
        # Move both the first and second pointers until first reaches the end
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        second_pointer.next = second_pointer.next.next
       
        # Removing the nth node by skipping it
        return dummy.next
       
        # Removing the head of the modified list (which might change)
        
"""
TIME COMPLEXITY:
1. Moving first_pointer n + 1 steps takes O(n + 1) = O(n) time
2. After creating the gap, both pointer are moved together until first_pointer reaches the end.
This takes O(L - n), L -> length of the first
3. Therefore, the overall time complexity for this is O(L), which is same as O(n), if n is close to L

SPACE COMPLEXITY:
1. The solution used few additional pointers which occupy constant space.
2. Therefore, the space complexity is O(1), as only a constant amount of extra space is used

"""