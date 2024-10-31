class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize the DP array where dp[i] will store the number of ways to make amount i
        dp = [0] * (amount + 1)
        
        # Base case: There's one way to make amount 0, by choosing no coins
        dp[0] = 1

        # For each coin, update the dp array to count the number of ways to make each amount
        for coin in coins:
            # Start from the value of the coin to the target amount
            for i in range(coin, amount + 1):
                # Add the number of ways to make (i - coin) to dp[i]
                # This effectively counts all combinations that include this coin
                dp[i] += dp[i - coin]

        # Return the number of ways to make the full amount
        return dp[amount]

# TIME COMPLEXITY:
# - Outer loop iterates over each coin, which has time complexity O(len(coins)).
# - Inner loop iterates from the coin's value up to amount, giving O(amount) per coin.
# - Overall time complexity: O(len(coins) * amount).

# SPACE COMPLEXITY:
# - We use a single 1D DP array of size amount + 1, so space complexity is O(amount).
