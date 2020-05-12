class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [[1 - A[row][len(A[0]) - 1 - col] for col in range(len(A[0]))] for row in range(len(A))]
        return B