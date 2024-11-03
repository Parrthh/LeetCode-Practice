class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        max_profit = 0
        min_profit = prices[0]

        for i in range(len(prices)):
            min_profit = min(min_profit,prices[i])
            max_profit = max(max_profit, prices[i] - min_profit)

        return max_profit

