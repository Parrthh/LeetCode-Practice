class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a dp array with all for len(nums)
        dp = [1] * len(nums)
        # Start comparing from index 1 to len(nums)
        for i in range(1, len(nums)):
            # Looping for all elements upto current i and comparing
            for j in range(i):
                # Compare i with every j if greater update in dp
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        