class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to make it easier to skip duplicates and use two-pointer technique
        nums.sort()
        res = []  # This will hold the resulting triplets

        # Step 2: Iterate through the array, treating each element as the potential first element of a triplet
        for i in range(len(nums)):
            # Skip duplicate elements for `i` to avoid duplicate triplets in `res`
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Initialize two pointers, left and right, for the current `i`
            left, right = i + 1, len(nums) - 1

            # Step 4: Use two pointers to find pairs that sum up to `-nums[i]`
            while left < right:
                # Calculate the sum of the triplet
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # If the total is zero, we've found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Step 5: Move both pointers to skip duplicates and find new pairs
                    # Skip duplicate elements for `left`
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate elements for `right`
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward to check for other potential pairs
                    left += 1
                    right -= 1

                elif total < 0:
                    # If the sum is too small, move the left pointer to the right to increase the sum
                    left += 1
                else:
                    # If the sum is too large, move the right pointer to the left to decrease the sum
                    right -= 1

        # Step 6: Return the list of unique triplets
        return res

"""
TIME COMPLEXITY:
1. combining the sorting step and the main loop, the time complexity is: O(nlogn) + O(n^2) = O(n^2)
2. Since O(n^2) dominates O(nlogn), the overall time complexity is O(n^2)

SPACE COMPLEXITY:O(N^2)
1. The space complexity is O(n^2) in the worst case due to the storage of triplets in the result list


"""