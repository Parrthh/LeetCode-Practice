class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # Opposite Color:
        opposite_color = "W" if color == "B" else "B"

        directions = [
            (-1,0),     # Up
            (1,0),      # Down
            (0,-1),     # Left
            (0,1),      # Right
            (-1,-1),    # Top - left diagonal
            (-1,1),     # Top - right diagonal
            (1,-1),     # Botton - left diagonal
            (1,1)       # Bottom - right diagonal
        ]

        for dr, dc in directions:
            row, col = rMove + dr, cMove + dc
            # Count of opposite pieces
            count = 0

            # Traversing in the current direction
            while 0 <= row < 8 and 0 <= col < 8 and board[row][col] == opposite_color:
                count += 1
                row += dr
                col += dc
            
            # Check if the line ends with the same color
            if count >= 1 and 0 <= row < 8 and 0 <= col < 8 and board[row][col] == color:
                return True
        return False

"""
TIME COMPLEXITY: O(8 * n):
1. Each direction can involve traversing up to n cells (n = 8 for this grid size)
2. Simplies to O(n) for this problem

SPACE COMPLEXITY: O(1)
1. Constant space usage for variables and directions
"""

             