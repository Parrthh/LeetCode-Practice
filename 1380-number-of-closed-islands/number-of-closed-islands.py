from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Define a DFS method to mark the entire island as visited
        def dfs_method(grid, row, col):
            # Use a stack to simulate DFS iteratively (to avoid recursion depth issues)
            stack = [(row, col)]
            while stack:
                # Pop a cell (r, c) from the stack to process it
                r, c = stack.pop()
                # Check if the cell is within grid bounds and is land (0)
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                    # Mark the cell as visited by setting it to 2
                    grid[r][c] = 2
                    # Add all four neighboring cells to the stack to continue the DFS
                    stack.append((r - 1, c))  # Up
                    stack.append((r + 1, c))  # Down
                    stack.append((r, c - 1))  # Left
                    stack.append((r, c + 1))  # Right

        # Step 1: Mark all boundary-connected islands
        # Iterate over the grid boundary to find and mark all land cells (0) connected to the boundary
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Check if the current cell is on the boundary and is part of an island (0)
                if (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1) and grid[i][j] == 0:
                    # Use DFS to mark the entire boundary-connected island as visited
                    dfs_method(grid, i, j)

        # Step 2: Count all closed islands
        # Initialize a counter to keep track of the number of closed islands
        closed_island = 0
        # Iterate over the interior of the grid (excluding the boundary)
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                # If an unvisited land cell (0) is found, it is a closed island
                if grid[i][j] == 0:
                    # Increment the closed island counter
                    closed_island += 1
                    # Use DFS to mark all cells in this closed island as visited
                    dfs_method(grid, i, j)

        # Return the count of closed islands
        return closed_island


"""
TIME COMPLEXITY: O(M * N):
1. Each cell is visited only once. The DFS marking process makes sure that we do no revisit cells
2. STEP - 1: We visit and mark boundary connected cells
3. STEP - 2: We count closed island in the interior grid
Since each cell is visited only once, we get a time complexity of O(m * n)
where, m = no. of rows, n = no. of columns

SPACE COMPLEXITY: O(M * N)
1. The worst space complexity for a stack in a iterative DFS is O(M * N), if all cells are land(0s)
and part of larger island
2. Therefore, the space complexity is O(M*N)

"""
