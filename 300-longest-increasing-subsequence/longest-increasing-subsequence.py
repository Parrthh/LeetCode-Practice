from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a dp array with all elements set to 1, where dp[i] represents
        # the length of the longest increasing subsequence that ends at index i.
        # Each element in dp starts at 1 because each individual element alone can form a subsequence of length 1.
        dp = [1] * len(nums)
        
        # Iterate through each element starting from index 1 to the end of nums
        for i in range(1, len(nums)):
            # For each element nums[i], compare it with all previous elements nums[j]
            for j in range(i):
                # If nums[i] > nums[j], it means we can extend the increasing subsequence ending at j to include i.
                # Update dp[i] to be the maximum of its current value and dp[j] + 1 (the length of the sequence ending at j plus 1).
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The result is the maximum value in dp, as it represents the length of the longest increasing subsequence
        return max(dp)

# TIME COMPLEXITY: O(n^2)
# - We have a nested loop where `i` iterates over each element from 1 to len(nums) (outer loop O(n)),
#   and for each `i`, `j` iterates over all previous elements (inner loop O(n)).
# - This gives an overall time complexity of O(n^2).

# SPACE COMPLEXITY: O(n)
# - We use a dp array of size len(nums), so the space complexity is O(n).
