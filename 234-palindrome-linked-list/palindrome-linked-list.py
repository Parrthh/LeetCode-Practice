# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Test Case: For empty list or single element
        if not head or not head.next:
            return True
        
        # We need to find the middle of the linked list, so that we can split
        slow = head
        fast = head

        # So in the while loop here
        # Basically what we are doing is
        # If we have a even linked list, we look for fast and for odd we look for fast.next to check None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        second_half = self.reverse(slow)
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
        
    # To reverse the linked list
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node        
        return prev

        

        