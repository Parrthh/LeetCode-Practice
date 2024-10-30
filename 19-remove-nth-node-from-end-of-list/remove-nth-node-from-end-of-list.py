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
            first_pointer = first_pointer. next
        
        # Move both the first and second pointers until first reaches the end
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        second_pointer.next = second_pointer.next.next
       
        # Removing the nth node by skipping it
        return dummy.next
       
        # Removing the head of the modified list (which might change)
        