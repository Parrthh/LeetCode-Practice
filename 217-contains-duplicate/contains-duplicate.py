class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for i in nums:
            if dict_nums.get(i, None) == None:
                dict_nums[i] = 1
            else:
                return True
        return False
            
