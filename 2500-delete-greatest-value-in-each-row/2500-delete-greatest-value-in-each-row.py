class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sum = 0
        for j in range(len(grid[0])):
            mx = 0
            for i in range(len(grid)):
                a = max(grid[i])
                grid[i].remove(a)
                mx = max(mx, a)
            sum += mx
        return sum
