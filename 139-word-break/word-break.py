class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Converting the dict to set
        word_set = set(wordDict)
        # initializing the dp array with False
        # Base Case: the 0-index would be true because 0 can be segmented as 0
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # For every i in the string s (len(s) + 1 because we need to check until out of bound)
        for i in range(1, len(s) + 1):
            # Loop till i
            for j in range(i):
                # Ex : if i = 4, j goes from (0,4) and checks the value
                # So if true, dp[4] = True and cached in dp array
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

        