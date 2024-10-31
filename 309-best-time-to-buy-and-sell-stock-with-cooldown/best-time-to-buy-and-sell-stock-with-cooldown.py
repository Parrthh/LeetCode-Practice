class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # Initialize DP arrays
        hold = [0] * n
        sell = [0] * n
        cooldown = [0] * n

        # Base cases for day 0
        hold[0] = -prices[0]   # Buying the stock on the first day
        sell[0] = 0            # Cannot sell on the first day
        cooldown[0] = 0        # No action taken

        # Fill DP arrays for each day
        for i in range(1, n):
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            cooldown[i] = max(cooldown[i-1], sell[i-1])

        # The result is the max profit on the last day when we are not holding a stock
        return max(sell[n-1], cooldown[n-1])

# TIME COMPLEXITY: O(n), where n is the number of days.
# - We iterate over the prices array once to fill the DP arrays.

# SPACE COMPLEXITY: O(n) for the DP arrays hold, sell, and cooldown.
