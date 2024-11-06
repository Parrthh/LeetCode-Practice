class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Step 1: Get the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Step 2: Create a DP array with the same dimensions as the grid and initialize it to 0
        # This DP array will store the number of ways to reach each cell
        dp = [[0] * n for _ in range(m)]
        
        # Step 3: Initialize the starting point
        # If the starting cell has an obstacle, there are 0 ways to reach it
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # Step 4: Fill the first row
        # For each cell in the first row, if there's no obstacle, it inherits the number of ways
        # from the previous cell (to its left), because it can only be reached from the left in the first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:  # No obstacle
                dp[0][j] = dp[0][j - 1]  # Inherit from the left cell
            # If there's an obstacle, dp[0][j] stays 0 because there's no way to reach it
        
        # Step 5: Fill the first column
        # Similarly, for each cell in the first column, if there's no obstacle, it inherits the number of ways
        # from the cell directly above it, as it can only be reached from above in the first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:  # No obstacle
                dp[i][0] = dp[i - 1][0]  # Inherit from the cell above
            # If there's an obstacle, dp[i][0] stays 0
        
        # Step 6: Fill the rest of the grid
        # For each cell (i, j) starting from (1, 1), if there's no obstacle, the number of ways to reach it
        # is the sum of the ways to reach the cell above it and the cell to its left
        # This is because it can be reached either from above or from the left
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # No obstacle
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # If there's an obstacle, dp[i][j] stays 0 as there’s no way to reach it
        
        # Step 7: The answer is in the bottom-right cell of the DP array
        # This cell contains the number of unique paths to reach the bottom-right corner
        return dp[m - 1][n - 1]

"""
TIME COMPLEXITY: O(m * n)
1. m -> no of rows, n -> no of cols. We iterate over each cell once

SPACE COMPLEXITY: O(m * n)
1. Because of the dp array


"""