class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize row with 1 for n time (n is our column)
        row = [1] * n
        # Looping through m-1 rows
        for i in range(m-1):
            # Initializing new row with one, but it will be used to calculate paths
            new_row = [1] * n
            # Looping through n-2 rows
            for j in range(n-2, -1, -1):
                # Calculating path for m -1 row or n - 2 column
                new_row[j] = new_row[j+1] + row[j]
            # row would then be used for another iteration with updated values
            row = new_row
        # Starting point of our robot
        return row[0]

        # TIME COMPLEXITY:
        # 1. Outer loop: m - 1 i.e m
        # 2. Inner loop: n - 2 i.e: n
        # Therefore, O(m x n)

        # SPACE COMPLEXITY:
        # 1. Initializing rows and new_rows of n elements: O(n), as well as i variable 
        # Therefore, Space Complexity is O(n)
