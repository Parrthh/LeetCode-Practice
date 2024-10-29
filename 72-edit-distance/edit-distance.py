class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize DP table with (m+1) x (n+1) size
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        
        # Base cases: filling the first row and first column
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters from word1 to match an empty word2
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters from word2 to match an empty word1
        
        # Fill the DP table with the minimum operations for each substring
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # If characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If characters differ, choose the minimum cost of insert, delete, or replace
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Delete (from word1)
                                       dp[i][j - 1],    # Insert (to word1)
                                       dp[i - 1][j - 1] # Replace (in word1)
                                      )
        
        # Result: minimum edit distance between word1 and word2
        return dp[m][n]


