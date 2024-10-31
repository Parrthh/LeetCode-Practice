class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # m is the length of word1, n is the length of word2
        m, n = len(word1), len(word2)

        # STEP - 1: Initialize the DP table with (m + 1) rows and (n + 1) columns
        # dp[i][j] will represent the minimum edit distance to convert word1[0:i] to word2[0:j]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # STEP - 2: Base cases
        # - If word2 is empty, we need i deletions to match the empty word
        # - If word1 is empty, we need j insertions to match word2
        for i in range(m + 1):
            dp[i][0] = i  # Cost of deleting characters from word1 to match an empty word2
        for j in range(n + 1):
            dp[0][j] = j  # Cost of inserting characters into word1 to match word2

        # STEP - 3: Fill the DP table using the recurrence relation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If characters are the same, no additional cost needed; take previous state
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If characters differ, we choose the minimum cost among:
                    # - Deletion (dp[i - 1][j])
                    # - Insertion (dp[i][j - 1])
                    # - Replacement (dp[i - 1][j - 1])
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion from word1
                                       dp[i][j - 1],    # Insertion into word1
                                       dp[i - 1][j - 1] # Replacement in word1
                                      )
        
        # STEP - 4: The answer is in the bottom-right cell of the DP table
        # which represents converting the entirety of word1 to word2
        return dp[m][n]

# TIME COMPLEXITY:
# - We fill an (m + 1) x (n + 1) DP table.
# - Each cell computation takes O(1) time.
# - Therefore, the overall time complexity is O(m * n).

# SPACE COMPLEXITY:
# - We use a 2D DP table with (m + 1) x (n + 1) cells.
# - Thus, the space complexity is O(m * n).
