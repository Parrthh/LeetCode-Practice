class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # STEP - 1: Initialize a row to represent the bottom row of the grid.
        # Since we can only move right, each cell in the last row has 1 path to the target.
        row = [1] * n  # This represents the number of paths from each cell in the bottom row.
        
        # STEP - 2: Loop from the second-to-last row up to the top row (m - 1 iterations)
        # We are building the number of paths from each cell in the current row based on the row below.
        for i in range(m - 1):
            # Initialize a new row that will hold the number of paths from each cell in the current row.
            # We start each row with all 1s, as the rightmost column has only one path to the target.
            new_row = [1] * n
            
            # STEP - 3: Calculate paths for each cell in the current row from right to left.
            # We start from the second-to-last column and move leftward.
            for j in range(n - 2, -1, -1):
                # The number of paths from cell (i, j) is the sum of:
                # - paths from the cell to the right (new_row[j + 1])
                # - paths from the cell below (row[j])
                new_row[j] = new_row[j + 1] + row[j]
            
            # Update the row to be the new row for the next iteration,
            # representing paths from this row.
            row = new_row
        
        # STEP - 4: Return the result from the top-left corner (starting point of the robot).
        return row[0]

# TIME COMPLEXITY:
# - Outer loop runs (m - 1) times, i.e., O(m).
# - Inner loop runs (n - 1) times in each iteration, i.e., O(n).
# - Thus, the overall time complexity is O(m * n).

# SPACE COMPLEXITY:
# - We use only two lists of length n: 'row' and 'new_row', both requiring O(n) space.
# - Therefore, the overall space complexity is O(n).
