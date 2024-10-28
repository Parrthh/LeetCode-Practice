class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # Because we start multiplying with the first element
        max_prod = min_prod =  res = nums[0]

        for i in nums[1:]:
            if i < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(i, i * max_prod)
            min_prod = min(i, i * min_prod)

            res = max(res, max_prod)
        return res

