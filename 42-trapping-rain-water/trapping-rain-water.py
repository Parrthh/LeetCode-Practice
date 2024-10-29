class Solution:
    def trap(self, height: List[int]) -> int:
        # If the height list is empty, return 0 since no water can be trapped.
        if not height:
            return 0

        # Initialize pointers and variables to track maximums and water trapped
        left, right = 0, len(height) - 1        # Two pointers, starting from both ends
        left_max, right_max = height[left], height[right]   # Track the max heights from left and right
        trapped = 0 # Accumulator for total trapped water

        # While the left pointer is to the left of the right pointer
        while left < right: 
            # Determine which side is limiting the water level
            if height[left] < height[right]:
                # If left side is smaller, focus on the left pointer
                if height[left] >= left_max:
                    # Update left_max to the current height if it's the highest seen so far from the left
                    left_max = height[left]
                else:
                    # Calculate water trapped at the left position
                    # It is limited by left_max, so we use left_max - height[left]
                    trapped += left_max - height[left]
                # Move the left pointer inward
                left += 1
            else:
                # If right side is smaller or equal, focus on the right pointer
                if height[right] >= right_max:
                    # Update right_max to the current height if it's the highest seen so far from the right
                    right_max = height[right]
                else:
                    # Calculate water trapped at the right position
                    # It is limited by right_max, so we use right_max - height[right]
                    trapped += right_max - height[right]     
                # Move the right pointer inward
                right -= 1
        # Return the total trapped water calculated
        return trapped            

        # TIME COMPLEXITY: O(n) -> because we traverse the array only once
        # SPACE COMPLEXITY: O(1)-> because we only use a fixed amount of extra space for pointers and counters, independent of the size of input
            