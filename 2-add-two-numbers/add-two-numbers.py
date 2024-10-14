# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        head = ListNode()
        new_curr = head

        curr1 = l1
        curr2 = l2

        carry = 0

        while(1):

            su_m = curr1.val + curr2.val + carry
            carry = su_m // 10
            su_m = su_m % 10
            print(carry)
            new_curr.val = su_m

            
            curr1 = curr1.next
            curr2 = curr2.next

            if curr1 and curr2:
                new_curr.next = ListNode()
                new_curr = new_curr.next
            else:
                break


        if curr1 == None and curr2 == None:
            if carry != 0:
                new_curr.next = ListNode()
                new_curr = new_curr.next
                new_curr.val = carry
                new_curr.next = None

            new_curr.nxt = None

        else:

            left_curr = curr1 if curr2 == None else curr2

            left_curr.val += carry
            new_curr.next = left_curr
            new_curr = new_curr.next

            while new_curr and new_curr.val >= 10:
                carry = new_curr.val//10
                new_curr.val = new_curr.val%10

                if new_curr.next == None and carry > 0:
                    new_curr.next = ListNode()
                    new_curr = new_curr.next
                    new_curr.val = carry
                    new_curr.next = None
                    break

                new_curr = new_curr.next
                new_curr.val += carry


        return head











        

        