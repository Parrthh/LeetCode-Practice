class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        consecutive_sequence = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] - nums[i - 1] == 1:
                    current_streak += 1
                else:
                    consecutive_sequence = max(consecutive_sequence, current_streak)
                    current_streak = 1
        return max(consecutive_sequence, current_streak)



