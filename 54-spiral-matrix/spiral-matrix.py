class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # left to right
            # get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in the left col:
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

"""
TIME COMPLEXITY: O(m * n)
1. Each element of the matrix is visited exactly once
2. If the matrix has m rows and n columns, the total number of elements in m x n
3. Therefore, the overall time complexity is O(m x n)

SPACE COMPLEXITY: O(m * n)
Due to the output list storing all elements of the matrix

"""