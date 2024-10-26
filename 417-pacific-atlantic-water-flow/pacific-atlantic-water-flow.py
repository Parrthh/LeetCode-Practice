class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        # Grid dimensions
        rows, cols = len(heights), len(heights[0])

        # Sets to keep track of cells reachable from each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        # Directions for moving up, down, left, right
        directions_traverse = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS function to mark all cells reachable from a given ocean
        def dfs_method(r: int, c: int, reachable_set: Set[Tuple[int, int]]):
            reachable_set.add((r, c))
            for dr, dc in directions_traverse:
                new_row, new_col = r + dr, c + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and
                    (new_row, new_col) not in reachable_set and
                    heights[new_row][new_col] >= heights[r][c]):
                    dfs_method(new_row, new_col, reachable_set)

        # Run DFS from all cells adjacent to the Pacific Ocean
        for i in range(rows):
            dfs_method(i, 0, pacific_reachable)  # Left border for Pacific
            dfs_method(i, cols - 1, atlantic_reachable)  # Right border for Atlantic

        for j in range(cols):
            dfs_method(0, j, pacific_reachable)  # Top border for Pacific
            dfs_method(rows - 1, j, atlantic_reachable)  # Bottom border for Atlantic

        # Find cells that can reach both oceans
        result = list(pacific_reachable & atlantic_reachable)
        return result