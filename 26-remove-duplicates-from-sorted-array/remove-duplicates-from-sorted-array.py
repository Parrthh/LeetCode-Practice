from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize an index 'idx' to track the position for the next unique element
        idx = 1  # Starts from 1 since the first element is always unique in a sorted array
        
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous element
            if nums[i - 1] != nums[i]:
                # If it's unique, place it at the 'idx' position and increment 'idx'
                nums[idx] = nums[i]
                idx += 1  # Move to the next position for a new unique element
                
        # Return the length of the array with unique elements
        return idx

        # Time Complexity Analysis:
        # - The loop iterates through the array once, so the time complexity is O(n),
        #   where n is the length of the array.
        
        # Space Complexity Analysis:
        # - The algorithm operates in-place without using extra space for another array,
        #   so the space complexity is O(1) (ignoring input space).
