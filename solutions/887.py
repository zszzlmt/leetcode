class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for row in range(len(grid)):
            res += max(grid[row])
        for col in range(len(grid[0])):
            cols = list()
            for row in range(len(grid)):
                if grid[row][col]:
                    res += 1
                cols.append(grid[row][col])
            res += max(cols)
        return res