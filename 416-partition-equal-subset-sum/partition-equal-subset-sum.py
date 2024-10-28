class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Check if the total sum is odd; if so, return False
        if total_sum % 2 != 0:
            return False
        
        # We need to find a subset with sum equal to half of total_sum
        target_sum = total_sum // 2
        
        # Initialize DP array
        dp = [False] * (target_sum + 1)
        dp[0] = True
        
        # Process each number in nums
        for i in nums:
            # Update dp array from right to left to avoid recomputation
            for j in range(target_sum, i - 1, -1):
                dp[j] = dp[j] or dp[j - i]
        
        # The answer is whether we can achieve the target sum
        return dp[target_sum]


