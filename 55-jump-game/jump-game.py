from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the farthest position we can reach
        farthest = 0
        
        # Traverse each index in the array
        for i in range(len(nums)):
            # If the current index is beyond the farthest reachable point, return False
            if i > farthest:
                return False
            
            # Update the farthest position we can reach from this index
            farthest = max(farthest, i + nums[i])
            
            # If the farthest point is at or beyond the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        # If we exit the loop, return False (though theoretically we should have returned earlier)
        return False
