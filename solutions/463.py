class Solution(object):

    rows = None
    cols = None
    grid = None

    def __check__(self, i, j):
        pos = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        cnt = 0
        for x, y in pos:
            if x < 0 or y < 0 or x >= self.rows or y >= self.cols or self.grid[x][y] == 0:
                cnt += 1
        return cnt

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j]:
                    res += self.__check__(i, j)
        return res
