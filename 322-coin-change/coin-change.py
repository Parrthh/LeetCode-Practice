class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Initialize the dp array with a large value (amount + 1)
        dp = [amount + 1] * (amount + 1)
        # Base case: it takes 0 coins to make an amount of 0
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                # We are trying to compute the amount a, c is the current coin we are looking at
                # Check if we can use the current coin (c) to make amount a
                if a - c >= 0:
                    # Recurrence relation
                    # Update dp[a] with the minimum number of coins needed to make amount a
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

