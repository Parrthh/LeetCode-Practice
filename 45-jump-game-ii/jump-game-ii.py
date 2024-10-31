class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the number of jumps, the current range end, and the farthest point reachable
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Traverse through each index except the last one (no need to jump from the last index)
        for i in range(0, len(nums) - 1):
            # Update the farthest point reachable from this index
            # The farthest point is either the previous farthest or i + nums[i] (current index + max jump from here)
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current range
            if i == current_end:
                # Make a jump to extend our range
                jumps += 1
                # Update the current range end to the farthest point we can reach
                current_end = farthest
                
                # Early exit: if we can already reach or exceed the last index, no more jumps are needed
                if current_end >= len(nums) - 1:
                    break
        
        # Return the total number of jumps required to reach the last index
        return jumps

# TIME COMPLEXITY: O(n)
# - We make a single pass through the list `nums`, where `n` is the number of elements in `nums`.
# - For each element, we calculate the farthest we can reach, and we only increment jumps when we reach the end of the current range.
# - The time complexity is thus O(n).

# SPACE COMPLEXITY: O(1)
# - This solution only uses a constant amount of extra space for the `jumps`, `current_end`, and `farthest` variables.
# - The space complexity is therefore O(1).
