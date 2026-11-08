class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        cols = {}
        rows = {}
        count = 0
        for i in range(len(grid)):
            rows[i] = grid[i].count(1)
        for i in range(len(grid[0])):
            for j in grid:
                if j[i] == 1:
                    cols[i] = cols.get(i, 0) + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count