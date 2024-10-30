class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx = idx + 1
        return idx