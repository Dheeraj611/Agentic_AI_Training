from collections import deque

class Solution:
    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Count fresh oranges and store rotten oranges
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    queue.append((r, c))

                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while queue and fresh > 0:

            size = len(queue)

            for _ in range(size):

                row, col = queue.popleft()

                for dr, dc in directions:

                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == 1
                    ):

                        grid[new_row][new_col] = 2
                        fresh -= 1

                        queue.append((new_row, new_col))

            minutes += 1

        if fresh == 0:
            return minutes

        return -1