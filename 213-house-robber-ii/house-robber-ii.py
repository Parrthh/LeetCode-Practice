class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge Cases: If there are no houses, return 0
        if len(nums) == 0 or nums is None:
            return 0
        # Edge Case: If there is only one house, return its value
        if len(nums) == 1:
            return nums[0]
        
        # Since houses are in a circle, we consider two cases:
        # 1. Exclude the first house: rob from the second house to the last
        # 2. Exclude the last house: rob from the first house to the second-to-last
        return max(self.max_rob(nums[1:]), self.max_rob(nums[:-1]))

    def max_rob(self, nums: List[int]) -> int:
        # This helper function solves the House Robber I problem on a linear list of houses
        # Initialize variables to store the maximum robbed amount for two previous houses
        t1, t2 = 0, 0
        
        # Iterate through each house in the list
        for current in nums:
            # `t1` represents the maximum amount we can rob up to the current house
            # `t2` represents the maximum amount we could rob up to the previous house
            # Temporarily store the previous value of t1
            temp = t1
            # Update t1 to be the max of:
            # - Robbing the current house (current + t2)
            # - Skipping the current house and keeping the previous max (t1)
            t1 = max(current + t2, t1)
            # Update t2 to the previous value of t1 (temp)
            t2 = temp

        # `t1` now holds the maximum amount that can be robbed from this linear arrangement
        return t1

# TIME COMPLEXITY: O(N)

# SPACE COMPLEXITY: O(1)