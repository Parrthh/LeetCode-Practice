class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)

        reverse(0, k - 1)

        reverse(k, n - 1)

"""
TIME COMPLEXITY: O(N)
1. Each reversal operation is O(n), and there are three such operations. So the total time complexity is O(n)

SPACE COMPLEXITY: O(1)
1. The algorithm modifies the array-in place, using only a few extra variables

"""