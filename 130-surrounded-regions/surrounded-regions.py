from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modify the board in-place to capture surrounded regions.
        """
        # Edge Case: If the board is empty, return immediately
        if not board:
            return 
        
        # Get the number of rows and columns in the board
        rows, cols = len(board), len(board[0])

        # Directions for moving up, down, left, right
        directions_traverse = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS function to mark border-connected 'O's as temporary 'T'
        def dfs_method(r, c):
            # Base Case for DFS:
            # If the cell is out of bounds or not an 'O', stop recursion
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"):
                return
            # Mark the cell as 'T' to indicate it is connected to the border
            board[r][c] = "T"

            # Explore in all four directions
            for dr, dc in directions_traverse:
                dfs_method(r + dr, c + dc)

        # STEP - 1: Use DFS from all border 'O's and mark them as 'T'
        # Traverse the left and right borders
        for i in range(rows):
            dfs_method(i, 0)        # Left border
            dfs_method(i, cols - 1) # Right border
        
        # Traverse the top and bottom borders
        for j in range(cols):
            dfs_method(0, j)        # Top border
            dfs_method(rows - 1, j) # Bottom border
        
        # STEP - 2: Replace all remaining 'O's with 'X's (they are surrounded)
        # and replace 'T's back with 'O's (they are not surrounded)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    # These 'O's are fully surrounded, so change them to 'X'
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    # These 'T's are connected to the border, so change them back to 'O'
                    board[i][j] = "O"

# TIME COMPLEXITY:
# - Let n be the number of rows and m be the number of columns.
# - The DFS will visit each cell at most once, resulting in O(n * m) time complexity.
# - Traversing all border cells is O(n + m) but is subsumed by O(n * m) from DFS traversal.
# - Overall time complexity: O(n * m).

# SPACE COMPLEXITY:
# - Space complexity is mainly due to recursion depth in DFS, which can go up to O(n * m) in the worst case.
# - No additional data structures are used, so the overall space complexity is O(n * m) due to recursion.
