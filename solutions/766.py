class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        row_table = [-1] * (row - 1)
        col_table = [-1] * (col - 1)
        diag = -1

        for i in range(row):
            for j in range(col):
                if i == j:
                    if diag == -1:
                        diag = matrix[i][j]
                    elif matrix[i][j] != diag:
                        return False
                elif i > j:
                    idx = i - j - 1
                    if row_table[idx] == -1:
                        row_table[idx] = matrix[i][j]
                    elif matrix[i][j] != row_table[idx]:
                        return False
                elif i < j:
                    idx = j - i - 1
                    if col_table[idx] == -1:
                        col_table[idx] = matrix[i][j]
                    elif matrix[i][j] != col_table[idx]:
                        return False
        return True
