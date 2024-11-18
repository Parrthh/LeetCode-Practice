class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0

        for char in s:
            if char == "[":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)
        return (max_imbalance + 1) // 2

"""
TIME COMPLEXITY: O(n)
1. We only traverse the string once, so the time complexity is linear

SPACE COMPLEXITY: O(1)
1. We only use a few variables (balance and max_imbalance), so the space complexity is constant

"""