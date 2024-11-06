class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
"""
TIME COMPLEXITY: O(log n)
1. Due to the binary search, where the search range is halved in each iteration

SPACE COMPLEXITY: O(1)
1. Only a constant amount of space is used for variables, regardless of the input size
"""









        


        