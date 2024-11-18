class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # # Initializing set to store unqiue palindrome subsequences of length 3
        # unique_set = set()

        # # We iterate over each character in the string,
        # # Considering each as a potential middle character of a palindrome
        # for i in range(1, len(s) - 1):
        #     # Creating a set of characters that appear before i
        #     left_set = set(s[:i])
        #     # Creating a set of characters that appear after i
        #     right_set = set(s[i+1:])

        #     # If a character exists in both "left_set" and "right_set", it can form a palindrome
        #     # With s[i]
        #     for char in left_set:
        #         if char in right_set:
        #             # If a palindrome is found, add it to the unqiue_set
        #             unique_set.add(char + s[i] + char)
        # return len(unique_set)

        # Initialize arrays to track seen characters
        prefix_seen = [set() for _ in range(len(s))]
        suffix_seen = [set() for _ in range(len(s))]

        # Fill prefix_seen with characters seen before each index
        seen = set()
        for i in range(len(s)):
            prefix_seen[i] = seen.copy()
            seen.add(s[i])

        # Fill suffix_seen with characters seen after each index
        seen = set()
        for i in range(len(s) - 1, -1, -1):
            suffix_seen[i] = seen.copy()
            seen.add(s[i])
        
        # Count unique palindromic sequence
        unique_set = set()
        for i in range(1, len(s) - 1):
            for char in prefix_seen[i]:
                if char in suffix_seen[i]:
                    unique_set.add(char + s[i] + char)
        return len(unique_set)

"""
TIME COMPLEXITY: O(n)
1. Prefix and suffix tracking each take O(n) time
2. Counting palindromic subsequence takes O(n) time

SPACE COMPLEXITY: O(n)
1. We use two arrays "prefix_seen" and "suffix_seen", each of size O(n)
"""