class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # Because we cannot revisit the cell we have already visited (the same letter cell cannot be used more than once)
        path = set()

        # Index tells us about the current charater of the target word
        def backtracking_method(r, c, index):
            # If we ever reach the end of the word, or index equals the last position
            # Or if we found the word
            if index == len(word):
                return True
            # All the below conditions are invalid
            if (r < 0 or 
                c < 0 or 
                r >= rows or 
                c >= cols or 
                word[index] != board[r][c] or 
                (r,c) in path):
                return False
            # If we are out of the previous loop, that means we found the character we need
            # Therefore, we add it to our set as we don't want to visit that cell again
            path.add((r, c))
            # We add 1 to the index, because we have found our current character, 
            # and we are looking for the next character
            res = (backtracking_method(r + 1, c, index + 1) or
                    backtracking_method(r - 1, c, index + 1) or
                    backtracking_method(r, c + 1, index + 1) or
                    backtracking_method(r, c - 1, index + 1))
            # Remove the position we just added it to the path
            # Therefore, we don't have to visit
            path.remove((r,c))
            return res
        # Go through every cell/position in the matrix and run the backtracking method
        for r in range(rows):
            for c in range(cols):
                # Here, index is 0, because we are starting at that position
                if backtracking_method(r, c, 0):
                    return True
        # And if we never return True, that means we were not able to find the solution
        return False

"""
TIME COMPLEXITY: O(n * m * 4 ^ L)
1. We iterate through each cell of the board using nested loops -> O(n * m)

2. For each cell, we may need to explore 4 possible directions (up, down, left, right)
recursively for each character in the word
In the worst case, we might explore up to 4 possible paths for every character in the word
The length of the word is L, so the worst-case scenario involves exploring up to 4^L paths

3. Overall Time complexity: O(n * m * 4 ^ L)
because we try to start the search from each of the n *m cells, and for each starting point,
we might explore up to 4 ^ L paths

SPACE COMPLEXITY: O(L)
1. We use a set called path to store the cells we have visited during the backtracking. Thus, the space
required for the path set is O(L)

2. The maximum depth of the recursion tree is equal to the length of the word (L), because
in the worst case, we make a recursive call for each character in the word

3. This means the space used by the call stack is O(L)

4. Therefore, overall time complexity is O(L)

"""