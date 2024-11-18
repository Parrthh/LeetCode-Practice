class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # We create a dictionary "edge_count" to store the count of each edge position
        edge_count = {}
        # We iterate through each row of the wall
        for row in wall:
            # For each brick (except the last one in the row), we calculate the edge position by adding
            # The bricks width to "edge_position"
            edge_position = 0
            # Skip the last brick in each row because it represents the end of the row
            for brick in row[:-1]:
                edge_position += brick
                # Count the number of times this edge position occures
                edge_count[edge_position] = edge_count.get(edge_position, 0) + 1
        # Finding the max number of aligned edges
        max_edges = max(edge_count.values(), default = 0)
        # The minimum number of crossed bricks is total_rows - max_edges
        return len(wall) - max_edges

"""
TIME COMPLEXITY: O(n * m)
1. n -> no of rows (height of the wall)
2. m -> avg number of bricks per row
3. We iterate through each brick in each row once, so the time complexity is linear to the total no of bricks

SPACE COMPLEXITY: O(n * m)
1. The dictionary edge_count sotres at most n * m entries in the worst case


"""