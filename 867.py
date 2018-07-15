class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[row][col] for row in range(len(A))] for col in range (len(A[0]))]
