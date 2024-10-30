# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a dummy node to act as the head of the merged list
        # Because when we are creating an object here
        # The value of the object is 0
        # That is why when we are returning dummy, we next to use dummy.next to avoid 0
        dummy = ListNode()
        
        # Pointer temp keep tracks of the last node in the merged list
        temp = dummy

        # While loop the compare the current nodes of list1 and list2
        # Anyone which is smaller will be stored in dummy
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        # There can be a test case, where one list can have more elements compared to another
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        # As we have our dummy node, we would want to skip that
        # Therefore, we use dummy.next
        return dummy.next



