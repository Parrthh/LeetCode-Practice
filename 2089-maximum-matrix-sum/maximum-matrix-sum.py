class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # This will store the sum of absolute values of all elements in the matrix
        total_sum = 0
        # This will keep track of the smallest absolute value
        min_abs_value = float('inf')
        # Count of negative numbers
        negative_nums = 0

        for row in matrix:
            for value in row:
                total_sum += abs(value)
                if value < 0:
                    negative_nums += 1
                min_abs_value = min(min_abs_value, abs(value))
        # If there are an odd number of negative values, subtract twice the smallest absolute value
        if negative_nums % 2 != 0:
            total_sum -= 2*min_abs_value
        return total_sum
                