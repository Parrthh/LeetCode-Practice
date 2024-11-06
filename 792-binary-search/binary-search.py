class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1 

"""
TIME COMPLEXITY: O(log n)
1. After each iteration, the search range is halved
2. Thus, the number of iterated required to reduce the search range to a single element is logarithmic

SPACE COMPLEXITY: O(1)
1. The algorithm uses only a few extra variables, which all occupy constant time O(1)
2. No additional data structures or recursion stacks are used, so the space complexity is minimal
3. Therefore, the overall space complexity is O(1)


"""