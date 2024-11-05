class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

"""
TIME COMPLEXITY: O(m * n)
1. Because we iterate through every element in the matrix twice, once to identify which rows and columns
needed to be zeroed, once to set these rows and cols to zero

SPACE COMPLEXITY: O(m + n)
1. This is due to two sets rows and cols, which can hold at most m row indices and n column indices

"""