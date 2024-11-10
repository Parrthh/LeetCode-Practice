class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs_method(r,c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return 
            image[r][c] = color

            dfs_method(r -1 , c)
            dfs_method(r + 1, c)
            dfs_method(r, c - 1)
            dfs_method(r, c + 1)
        dfs_method(sr,sc)
        return image

"""
TIME COMPLEXITY: O(n * m)


SPACE COMPLEXITY: O(n * m)
"""