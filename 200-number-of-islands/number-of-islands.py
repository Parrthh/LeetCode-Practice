class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs_method(grid, i, j)
                    island+=1
        return island


    def dfs_method(self, grid, row, col):

        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])
            or grid[row][col] != "1"):
            return 

        grid[row][col] = "0"

        self.dfs_method(grid, row - 1, col)
        self.dfs_method(grid, row + 1, col)
        self.dfs_method(grid, row, col - 1)
        self.dfs_method(grid, row, col + 1)        
    