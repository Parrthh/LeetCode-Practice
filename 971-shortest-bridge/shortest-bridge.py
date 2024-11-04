from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Define the 4 possible directions for exploration (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 1: Find and mark the first island using DFS
        # Time Complexity of this DFS marking step: O(n^2) in the worst case, since we may visit each cell once.
        # Space Complexity of DFS recursion stack: O(n^2) in the worst case due to recursive calls.
        def dfs(row, col):
            # Mark this cell as part of the first island (using the number 2)
            grid[row][col] = 2
            # Add this cell to the queue for BFS expansion
            queue.append((row, col))
            
            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Check if the neighbor is within bounds and part of the island (1)
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col)  # Recursively mark all connected land cells as part of the first island
        
        # Step 2: Use DFS to locate the first island and mark all its cells
        queue = deque()  # Initialize queue for BFS
        found_first_island = False  # Flag to stop after finding the first island
        
        # Iterate over the grid to find the first cell that is part of an island (1)
        # Time Complexity of this iteration: O(n^2) as we may have to check each cell once to find the first island.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Start DFS to mark all cells of the first island
                    dfs(i, j)
                    found_first_island = True
                    break  # Break the inner loop after finding the first island
            if found_first_island:
                break  # Break the outer loop after finding the first island

        # Step 3: Use BFS to expand from the first island and find the shortest path to the second island
        steps = 0  # Track the number of steps needed to reach the second island
        
        # Time Complexity of BFS expansion: O(n^2) in the worst case, as BFS may visit each cell once.
        # Space Complexity of BFS queue: O(n^2) in the worst case, where all cells are added to the queue.
        while queue:
            # Process all nodes in the current BFS layer
            for _ in range(len(queue)):
                row, col = queue.popleft()
                # Explore all 4 directions
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Check if the neighbor is within bounds
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == 1:
                            # If we reach the second island, return the number of steps taken
                            return steps
                        if grid[new_row][new_col] == 0:
                            # Mark water cells as visited by converting them to 2
                            grid[new_row][new_col] = 2
                            # Add the cell to the queue to continue BFS from here
                            queue.append((new_row, new_col))
            # Increment the number of steps after completing one layer of BFS
            steps += 1
        
        # Return -1 if no path is found, although the problem guarantees two islands
        return -1

# Time Complexity Analysis:
# 1. DFS (to mark the first island): O(n^2) in the worst case, as each cell may be visited once.
# 2. BFS (to find the shortest bridge): O(n^2) in the worst case, as each cell may be visited once.
# 3. Initial grid iteration to locate the first island: O(n^2).

# Total Time Complexity: O(n^2) + O(n^2) + O(n^2) = O(n^2), which is dominated by the DFS and BFS.

# Space Complexity Analysis:
# 1. DFS recursion stack: O(n^2) in the worst case, if the entire grid is land.
# 2. BFS queue: O(n^2) in the worst case, if we need to add each cell to the queue.
# 3. The grid itself uses O(n^2) space, but this is given as input and does not contribute to auxiliary space complexity.

# Total Space Complexity: O(n^2) due to the recursion stack (DFS) and queue (BFS).
