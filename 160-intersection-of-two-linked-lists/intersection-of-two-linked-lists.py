# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initializing two pointers
        pA, pB = headA, headB

        while pA != pB:
            # Move pointer, or reset to the other list's head if at the end
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        # Either return, the intersection node or None
        return pA

"""
TIME COMPLEXITY: O(n + m)
1. n: Length of list A
2. m: Length of list B
3. Both pointers traverse n + m nodes in totla

SPACE COMPLEXITY: O(1)
1. No additional data structures are used
"""