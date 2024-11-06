class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Step 1: Calculate the total sum of all stones
        # This helps us determine the target for partitioning the stones into two subsets
        total_sum = sum(stones)
        
        # Step 2: Define target as half of the total sum (we want to get close to this)
        # By aiming for half the total sum, we can minimize the weight difference between two subsets
        target = total_sum // 2
        
        # Step 3: Initialize a dp array to store the achievable subset sums up to 'target'
        # dp[j] represents the maximum subset sum we can achieve that does not exceed 'j'
        dp = [0] * (target + 1)
        
        # Step 4: Process each stone to update the dp array
        # For each stone, update the dp array in reverse order to avoid using the same stone twice
        for stone in stones:
            # Iterate in reverse from 'target' down to 'stone' (we can only consider achievable sums)
            for j in range(target, stone - 1, -1):
                # dp[j] is updated to the maximum of its current value or dp[j - stone] + stone
                # dp[j - stone] represents the sum we can achieve if we include the current stone
                dp[j] = max(dp[j], dp[j - stone] + stone)
        
        # Step 5: The answer is the minimum possible weight of the last stone
        # dp[target] is the largest achievable subset sum close to 'target' (half of total_sum)
        # To minimize the last remaining stone weight, we calculate the result as:
        # total_sum - 2 * dp[target]
        # This gives the difference between the total sum and twice the closest achievable subset sum to target
        return total_sum - 2 * dp[target]

""" 
TIME COMPLEXITY: O(n * S)
1. where n is the number of stones and S is the sum of all stone weights
2. S is the sum of all stone weights

SPACE COMPLEXITY: O(S)
1. S is the sum of all stone weights
"""