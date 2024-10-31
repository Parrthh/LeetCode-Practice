from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # STEP - 1: Initialize a 2D DP table with dimensions (len(text1) + 1) x (len(text2) + 1)
        # Each cell dp[i][j] will represent the LCS length for text1[i:] and text2[j:]
        # The "+1" in dimensions allows an extra row and column for the base cases (empty substrings).
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # STEP - 2: Fill the DP table from bottom-right to top-left
        # This way, we build up solutions to subproblems
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If characters match, increment LCS length from the next diagonal cell
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If characters do not match, take the maximum LCS length from the right or below cell
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        # The answer is the LCS of the entire text1 and text2, which we stored in dp[0][0]
        return dp[0][0]

# TIME COMPLEXITY:
# - We have two nested loops, each iterating over the lengths of text1 and text2.
# - If len(text1) is m and len(text2) is n, then the time complexity is O(m * n).

# SPACE COMPLEXITY:
# - We use a 2D DP table (list of lists) with dimensions (m + 1) x (n + 1).
# - Thus, the space complexity is O(m * n), where m and n are the lengths of text1 and text2.
