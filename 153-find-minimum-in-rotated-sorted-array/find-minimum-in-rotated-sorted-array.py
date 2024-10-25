class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        
        left = 0
        right = len(nums) - 1


        if nums[left] < nums[right]:
            return nums[left]

        while left < right :
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            
        return min(nums[left],nums[right],nums[mid])
               

