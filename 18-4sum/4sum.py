class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicate numbers for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate numbers for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1 

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result

"""
TIME COMPLEXITY : O(N ^ 3)
1. Sorting the array: O(nlogn)
2. Iterating through the array: O(n ^ 3)
3. Therefore the overall time complexity is O(n ^ 3)

SPACE COMPLEXITY: O(1)
1. The space complexity is O(1) for sorting and pointers (excluding the output)
"""