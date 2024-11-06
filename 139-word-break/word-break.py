class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to a set for faster lookup
        word_set = set(wordDict)

        # Initialize a dp array where dp[i] indicates if the substring s[0:i] can be segmented
        # Base Case: dp[0] is True because an empty substring is considered "segmented"
        dp = [False] * (len(s) + 1)
        dp[0] = True  # This base case helps handle substrings starting from index 0

        # Iterate over each possible end index `i` from 1 to len(s)
        for i in range(1, len(s) + 1):
            # For each `i`, iterate from `j = 0` to `i`, checking each possible starting point of the substring
            for j in range(i):
                # dp[j] indicates if s[0:j] can be segmented
                # s[j:i] is the current substring we're checking to see if it exists in word_set
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    # Break early since we've confirmed that s[0:i] can be segmented
                    break
        
        # dp[len(s)] holds the result, indicating if the entire string s can be segmented
        return dp[len(s)]

# TIME COMPLEXITY: O(n^2)
# - We iterate over each index `i` from 1 to len(s), giving an outer loop of `O(n)`.
# - For each `i`, we have an inner loop that goes from `0` to `i`, giving an inner complexity of O(n) as well.
# - The overall complexity is O(n^2) due to the nested loops.

# SPACE COMPLEXITY: O(n)
# - We use a dp array of size len(s) + 1, so the space complexity is O(n).
