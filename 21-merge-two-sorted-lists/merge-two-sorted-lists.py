# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Placeholder node for the result list
        dummy = ListNode()
        # Tail node to perform the merge process
        tail = dummy

        # While loop to iterate over both the lists
        # It also checks if anyone of the list is not null
        # If it is then we directly go the outside if case to add values
        # Directly in the result list
        while list1 and list2:    
            # Comparing the curr nodes of both the list
            if list1.val < list2.val:
                # if curr of l1 is small compared to curr of l2
                tail.next = list1
                list1 = list1.next
            else:
                # if curr of l2 is small compared to l1
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # There can be a case wherein anyone of the list might be longer than the other
        # So we directly store it into the result list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Returning our final list
        return dummy.next
        
