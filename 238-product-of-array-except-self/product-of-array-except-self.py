class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1,n):
            result[i] = result[i - 1] * nums[i - 1]
        right_product = 1
        for i in range(n - 1, - 1, - 1):
            result[i] *= right_product
            right_product *= nums[i]
        return result

"""
TIME COMPLEXITY: O(N)
1. Calculating the left products: O(n)
2. Calculating the right products and updating result: O(n)
3. Total Time complexity: O(n)

SPACE COMPLEXITY: O(N)
1. The result array uses O(n) space
2. Right_product uses O(1) space
3. Therefore, the total space complexity is O(n)


"""