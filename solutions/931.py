class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        l = len(A)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for jdx in range(l):
            dp[0][jdx] = A[0][jdx]
        for idx in range(1, l):
            for jdx in range(l):
                candidate = list()
                if jdx-1 >= 0:
                    candidate.append(dp[idx-1][jdx-1] + A[idx][jdx])
                candidate.append(dp[idx-1][jdx] + A[idx][jdx])
                if jdx+1 < l:
                    candidate.append(dp[idx-1][jdx+1] + A[idx][jdx])
                dp[idx][jdx] = min(candidate)
        return min(dp[-1])
