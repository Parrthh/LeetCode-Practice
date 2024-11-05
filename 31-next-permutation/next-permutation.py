class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        # Start from the second-to-last element and move left
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            # Move left until we find a position where nums[i] < nums[i + 1]
            i -= 1
        
        # If we found a valid 'i' (not -1), meaning there's a way to get a larger permutation
        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to swap with
            # Start from the end of the list
            j = len(nums) - 1
            # Move left until we find the first element that is greater than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j] to create the smallest possible increment in value
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the subarray to the right of index 'i' (from i+1 to end)
        # This reverses the descending order to make it the smallest lexicographical order
        left, right = i + 1, len(nums) - 1
        while left < right:
            # Swap elements at 'left' and 'right' and move the pointers inward
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


"""
TIME COMPLEXITY : O(N)

Step - 1: takes O(n) to find the rightmost ascending element
Step - 2: takes O(n) to find the element to swap
Step - 3: takes O(n) to reverse the segment
Overall, time complexity is O(n)

SPACE COMPLEXITY: O(1)
1. The algorithm modifies the list nums in place and does not use extra space
that grows with the input size


"""