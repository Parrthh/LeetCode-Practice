class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


"""
TIME COMPLEXITY: O(n)
1. The loop runs n times, and each iteration involves constant-time operations

SPACE COMPLEXITY: O(n)
1. The result list requires additional space proportional to the size of the input array
"""