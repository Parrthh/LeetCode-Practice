class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to keep track of seen numbers in rows, columns, and sub-boxes

        # keeps track of the numbers seen in row i
        rows = [set() for _ in range(9)]
        # keeps track of the numbers seen in column j
        cols = [set() for _ in range(9)]
        # keeps track of the numbers seen in sub-box k, where the sub-box index k is calculated
        # based on the row and column indices (i and j)
        boxes = [set() for _ in range(9)]

        # Iterate over each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                # Get the current value in the cell
                num = board[i][j]
                
                # Skip empty cells
                if num == '.':
                    continue
                
                # Calculate the sub-box index using (i // 3) * 3 + (j // 3) for each (i,j)
                # (i // 3) -> gives the row index of the sub-box
                # (j // 3) -> gives the column index of the sub-box
                # Combining these two using "* 3 +" gives a unique index for each sub-box (0-8)
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if the number is already in the current row, column, or sub-box
                if num in rows[i]:
                    return False  # Duplicate found in the row
                if num in cols[j]:
                    return False  # Duplicate found in the column
                if num in boxes[box_index]:
                    return False  # Duplicate found in the sub-box
                
                # Add the number to the corresponding row, column, and sub-box sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        # If no duplicates are found, the Sudoku board is valid
        return True

"""
TIME COMPLEXITY: O(1)
1. Checking for membership in a set is O(1)
2. Adding an element to a set is also O(1)

SPACE COMPLEXITY: O(1)
1. We use three lists of sets, each with 9 sets
2. Each set could contain up to 9 elements (since Sudoku numbers range from 1 to 9)
3. Therefore, the space complexity is O(1)
"""