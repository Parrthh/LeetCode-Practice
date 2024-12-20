class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""          # Stores the longest palindromic substring found
        res_length = 0    # Stores the length of the longest palindromic substring

        # Iterate through each character in the string as the center
        for i in range(len(s)):
            # Check for odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If the current palindrome is longer than the previous longest
                if (right - left + 1) > res_length:
                    res = s[left: right + 1]     # Update the result
                    res_length = right - left + 1  # Update the length
                left -= 1  # Expand to the left
                right += 1 # Expand to the right

            # Check for even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If the current palindrome is longer than the previous longest
                if (right - left + 1) > res_length:
                    res = s[left: right + 1]     # Update the result
                    res_length = right - left + 1  # Update the length
                left -= 1  # Expand to the left
                right += 1 # Expand to the right

        return res

"""
TIME COMPLEXITY: O(n ^ 2)
1. For each character, we expand outwards to check both odd and even-length
palindromes which take O(n) time
2. We do this for each of n characters in the string

SPACE COMPLEXITY: O(1)
1. We use few variables and no extra data structure

"""