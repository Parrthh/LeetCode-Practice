class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_rob(i, nums):
            # Base Case: If we are beyond the last house, no money can be robbed
            if i >= len(nums):
                return 0
            
            # Memoization Check: If we have already computed the max amount for this house, return it
            if i in memo:
                return memo[i]
            
            # Calculate the maximum amount by:
            # 1. Skipping the current house (move to the next house, i+1)
            # 2. Robbing the current house, adding its value, and moving two steps ahead (i+2)
            rob_skip = max_rob(i + 1, nums)  # Skip the current house
            rob_current = nums[i] + max_rob(i + 2, nums)  # Rob the current house
            a = max(rob_skip, rob_current)  # Choose the maximum of skipping or robbing

            # Store the computed value in the memo dictionary for future reference
            memo[i] = a
            return a

        # Initialize a dictionary to store intermediate results for memoization
        memo = {}
        
        # Start calculating from the first house (index 0)
        return max_rob(0, nums)

# TIME COMPLEXITY: O(n)
# - Each house (index) is visited only once due to memoization, so the recursive calls run in O(n) time,
#   where n is the length of nums.

# SPACE COMPLEXITY: O(n)
# - We use a dictionary `memo` to store results for each house (up to n entries).
# - The recursion stack depth can reach up to n, leading to O(n) space complexity.
