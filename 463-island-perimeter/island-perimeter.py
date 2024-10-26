class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Counts the island that we have visited, so we don't visit twice
        visited = set()
        # nested helper function that performs dfs on each cell
        # Goal is to calculate the permimeter contributed by a specific cell 
        # As well as its surrounding cells
        def dfs_method(i,j):
            # Condition checks if cell (i,j) is out of bounds of the grid
            # i.e. i or j are out of the row or column limits
            # If either condition is met, it means the part of the cell boundary contributes to the perimeter
            # Thus function return 1 to add to the perimeter count
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            # To check if the cell (i,j) is already in the visited set if yes return 0
            if (i,j) in visited:
                return 0
            # Adds the current cell (i,j) to the visits set to mark it as processed
            visited.add((i,j))
            # Recursive Perimeter calculation
            perimeter = dfs_method(i, j+1) # Right side
            perimeter += dfs_method(i+1, j) # Down 
            perimeter += dfs_method(i, j-1) # Left
            perimeter += dfs_method(i-1,j) # Up
            # Returns the total
            return perimeter
        # The nested loop here iterates through each cell in the grid to find the starting point of island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs_method(i,j)