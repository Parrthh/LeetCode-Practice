# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initial stage:
        # At the start of the program, the prev node is set to None
        # At that point the current node is at the head, which in our case is 1

        prev, temp = None, None
        curr = head

        # While loop is used to iterate over the list
        # This node runs as long as there is a current node to process, until it reaches to None

        while curr != None:
            # Here we are storing the next node, which will be 2 in our case
            temp = curr.next
            # Here, we are chaning our pointer of curr node which is at 2, to the prev node which is None
            # That is how we will be reversing the linked list througout
            curr.next = prev
            # Now, we bring our prev pointer to the curr pointer
            prev = curr
            # Here, we are moving our curr node to the temp node
            curr = temp
        return prev

      
