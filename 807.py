class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dim = len(grid)
        col_max = list()
        row_max = list()
        total_sum = 0
        for i in range(dim):
            i_col = [grid[idx][i] for idx in range(dim)]
            col_max.append(max(i_col))
            i_row = grid[i]
            row_max.append(max(i_row))
        for i in range(dim):
            for j in range(dim):
                target = min(row_max[i], col_max[j])
                total_sum += target - grid[i][j]
        return total_sum
