class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
"""
TIME COMPLEXITY: O(N)
1. where n is the length of list. We only iterate through the list once

SPACE COMPLEXITY: O(1)
1. Since no additional data structures are used
"""