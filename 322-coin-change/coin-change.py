from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Initialize the dp array with a large value (amount + 1),
        # which represents the maximum value that `dp[a]` could theoretically hold.
        # This allows us to use `min()` effectively later in the recurrence relation.
        dp = [amount + 1] * (amount + 1)
        
        # Base case: It takes 0 coins to make an amount of 0
        dp[0] = 0

        # Step 2: Fill the dp array for each amount from 1 to `amount`
        for a in range(1, amount + 1):  # For each amount `a` from 1 to `amount`
            for c in coins:  # Check each coin `c` in the list of coins
                # Check if we can use the current coin `c` to make amount `a`
                if a - c >= 0:  # If `a - c` is non-negative, it means we can use `c` to make `a`
                    # Recurrence relation:
                    # We take the minimum between the current `dp[a]` and `1 + dp[a - c]`,
                    # where `1 + dp[a - c]` represents using the coin `c` and adding it
                    # to the minimum number of coins required to make amount `a - c`
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # Step 3: Return the result
        # If `dp[amount]` is still `amount + 1`, it means the amount cannot be formed
        # with the given coins, so return -1. Otherwise, return `dp[amount]`, which
        # holds the minimum number of coins needed to form the amount.
        return dp[amount] if dp[amount] != amount + 1 else -1

# TIME COMPLEXITY: O(n * m)
# - `n` is the target `amount`, and `m` is the number of coin denominations in `coins`.
# - We iterate through each amount from `1` to `amount`, giving us `O(n)`.
# - For each amount, we loop over each coin in `coins`, resulting in `O(m)`.
# - Therefore, the overall time complexity is `O(n * m)`.

# SPACE COMPLEXITY: O(n)
# - We use a `dp` array of size `amount + 1`, so the space complexity is `O(n)`.
