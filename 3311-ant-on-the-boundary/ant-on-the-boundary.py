class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        total, c = 0, 0
        
        for i in range(len(nums)):
            
            total += nums[i]

            if total == 0:
                c+=1
        return c

        