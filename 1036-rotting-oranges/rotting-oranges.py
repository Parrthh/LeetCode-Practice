class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rotten_queue = deque()
        time_lapse, fresh_oranges = 0, 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    rotten_queue.append([i,j])

        directions_traverse = [[0,1],[0,-1],[1,0],[-1,0]]
        while rotten_queue and fresh_oranges > 0:
            for a in range(len(rotten_queue)):
                i,j = rotten_queue.popleft()
                for dr, dc in directions_traverse:
                    rows, cols = dr + i, dc + j
                    if (rows < 0 or
                        rows >= len(grid) or
                        cols < 0 or
                        cols >= len(grid[0]) or
                        grid[rows][cols] != 1):
                        continue
                    grid[rows][cols] = 2
                    rotten_queue.append([rows, cols])
                    fresh_oranges -= 1
            time_lapse += 1
        return time_lapse if fresh_oranges == 0 else -1