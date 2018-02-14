import copy
class Solution(object):

    traval = None
    row = None
    col = None
    s = None

    def __area__(self, g, x, y):
        self.s += 1
        self.traval[x][y] = -1
        if self.__check__(x + 1, y) and g[x + 1][y] == 1 and self.traval[x + 1][y] != -1:
            self.__area__(g, x + 1, y)
        if self.__check__(x, y + 1) and g[x][y + 1] == 1 and self.traval[x][y + 1] != -1:
            self.__area__(g, x, y + 1)
        if self.__check__(x - 1, y) and g[x - 1][y] == 1 and self.traval[x - 1][y] != -1:
            self.__area__(g, x - 1, y)
        if self.__check__(x, y - 1) and g[x][y - 1] == 1 and self.traval[x][y - 1] != -1:
            self.__area__(g, x, y - 1)


    def __check__(self, x, y):
        if 0 <= x < self.row and 0 <= y < self.col:
            return True
        return False

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.traval = copy.deepcopy(grid)
        self.row = len(grid)
        self.col = len(grid[0])
        res = 0
        for idx_r in range(self.row):
            for idx_c in range(self.col):
                if grid[idx_r][idx_c] == 1 and self.traval[idx_r][idx_c] != -1:
                    self.s = 0
                    self.__area__(grid, idx_r, idx_c)
                    if self.s > res:
                        res = self.s
        return res
