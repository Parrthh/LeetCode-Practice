class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Get the length of the input array nums
        n = len(nums)
        
        # Initialize the result array with 1s. 
        # Each element in `result` will eventually hold the product of all elements except nums[i]

        result = [1] * n  # Space Complexity: O(n) because we use an output array of the same length as input

        # First loop: calculate the product of all elements to the left of each index
        # Time Complexity of this loop: O(n)

        for i in range(1, n):
            # result[i - 1] already contains the product of all elements to the left of index (i - 1).
            # Multiply that by nums[i - 1] to get the product of all elements to the left of index i.

            result[i] = result[i - 1] * nums[i - 1]

        # Initialize a variable to accumulate the product of elements to the right of each index.
        right_product = 1  # This variable has constant space, O(1)

        # Second loop: calculate the product of all elements to the right of each index, 
        # and multiply it with the left product already stored in `result`.
        # Time Complexity of this loop: O(n)

        for i in range(n - 1, -1, -1):  # Traverse from right to left

            # result[i] currently contains the product of all elements to the left of index i.
            # Multiply it by right_product, which is the product of all elements to the right of index i.
            result[i] *= right_product

            # Update right_product to include nums[i], so in the next iteration,
            # right_product will be the product of all elements to the right of the new index (i-1).
            right_product *= nums[i]

        return result  # The result array now contains the product of all elements except for each index

    # Time Complexity: O(n)
    # - The function has two separate loops that each go through the array once.
    # - Thus, the overall time complexity is O(n) + O(n) = O(n).

    # Space Complexity: O(n)
    # - We use an output array `result` of the same length as the input array.
    # - The additional variable `right_product` requires O(1) space.
    # - Overall, the space complexity is O(n) for the output array `result`.



