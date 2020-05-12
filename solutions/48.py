class Solution(object):

    def exchange(self, matrix, i, j, ii, jj):
        t = matrix[i][j]
        matrix[i][j] = matrix[ii][jj]
        matrix[ii][jj] = t

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l == 0 or l == 1:
            return
        for idx in range(l):
            for jdx in range(idx, l):
                self.exchange(matrix, idx, jdx, jdx, idx)
        for idx in range(l):
            for jdx in range(l // 2):
                self.exchange(matrix, idx, jdx, idx, l - 1 - jdx)