class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrom(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check_palindrom(left + 1, right) or check_palindrom(left, right - 1)
            left += 1
            right -= 1
        return True
"""
TIME COMPLEXITY : O(n)
1. The main comparison loop runs in O(n), where n is the length of the string
2. The worst case involves checking two substring of length "n-1" for palindrome status, each taking O(n) time
3. Therefore, the overall time complexity is O(n)

SPACE COMPLEXITY: O(1)
1. As no additional space or extra data structures are used besides pointers.
"""
