class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_island = []
        island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    
                    area = self.dfs_method(grid, i,j)
                    max_island.append(area)
        return max(max_island) if max_island else 0

    def dfs_method(self, grid, row, col):
        
        if (row < 0 or col < 0 or row >= len(grid)
            or col >= len(grid[0]) or grid[row][col] != 1):
            return 0

        grid[row][col] = 2

        left_area = self.dfs_method(grid, row - 1, col)
        right_area = self.dfs_method(grid, row + 1, col)
        up_area = self.dfs_method(grid, row, col - 1)
        down_area = self.dfs_method(grid, row, col + 1)

        return 1+left_area+right_area+up_area+down_area

        
        