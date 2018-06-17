class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for idx in range(len(A) - 2):
            if A[idx + 1] > A[idx] and A[idx + 1] > A[idx + 2]:
                return idx + 1
