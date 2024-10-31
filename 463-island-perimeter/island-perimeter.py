class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(M * N), where M is the number of rows and N is the number of columns.
        # Each cell is visited once, and each cell's neighbors are checked in four directions.

        # Space Complexity: O(M * N) in the worst case for the recursion stack if the island covers the entire grid.
        # Additionally, O(M * N) space is used for the `visited` set to track processed cells.

        # Set to store the coordinates of cells that have already been visited.
        # This prevents recounting cells and helps manage cases with multiple connections between cells.
        visited = set()

        # Define a helper function to perform DFS and calculate the perimeter of a specific cell (i, j).
        def dfs_method(i, j):
            # Check if the cell (i, j) is out of the grid's boundaries.
            # If it's out of bounds (beyond the edges of the grid), it contributes to the perimeter.
            # Additionally, if the cell is water (grid[i][j] == 0), it also contributes to the perimeter.
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1  # Each out-of-bound edge or water cell adjacent to land contributes 1 to the perimeter.
            
            # If the cell has been visited before, it should not contribute again to the perimeter calculation.
            # Returning 0 means it does not add to the perimeter since it’s already accounted for.
            if (i, j) in visited:
                return 0
            
            # Mark the cell as visited by adding its coordinates to the `visited` set.
            # This prevents revisiting and recounting during recursion.
            visited.add((i, j))

            # Initialize a perimeter count specific to this cell.
            perimeter = 0

            # Explore each of the four directions around the current cell to calculate perimeter contributions:
            # - Right: Move horizontally to the cell on the right (i, j + 1).
            # - Down: Move vertically to the cell below (i + 1, j).
            # - Left: Move horizontally to the cell on the left (i, j - 1).
            # - Up: Move vertically to the cell above (i - 1, j).
            # Each direction call contributes to the perimeter based on its result (1 if it's a boundary/water).
            perimeter += dfs_method(i, j + 1)  # Right
            perimeter += dfs_method(i + 1, j)  # Down
            perimeter += dfs_method(i, j - 1)  # Left
            perimeter += dfs_method(i - 1, j)  # Up

            # Return the total perimeter for the current cell, including contributions from all directions.
            return perimeter

        # Traverse each cell in the grid using nested loops to find the starting point of the island.
        # Once the first land cell (1) is found, initiate DFS to calculate the perimeter of the island.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If a land cell (1) is found, it marks the start of the island.
                if grid[i][j] == 1:
                    # Start the DFS function from this land cell to calculate the total perimeter of the island.
                    # The function returns immediately because we assume the grid has only one island.
                    return dfs_method(i, j)

        # If no land cell is found, this means the grid has no islands, so we return 0 as there is no perimeter.
        return 0
