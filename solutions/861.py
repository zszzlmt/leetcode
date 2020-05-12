class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = len(A)
        cols = len(A[0])
        for row in range(rows):
            if A[row][0] == 0:
                for col in range(cols):
                    A[row][col] = 1 - A[row][col]
        for col in range(1, cols):
            cnt = 0
            for row in range(rows):
                if A[row][col] == 1:
                    cnt += 1
            if cnt < rows / 2:
                for row in range(rows):
                    A[row][col] = 1 - A[row][col]
        res = 0
        for row in range(rows):
            tmp = 0
            for col in range(cols):
                tmp *= 2
                tmp += A[row][col]
            res += tmp
        return res