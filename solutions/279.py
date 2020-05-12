class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        i = 1
        while i <= n:
            dp_i = i
            for j in range(1, int(i**(0.5))+1):
                dp_i = min(dp_i, dp[i - j * j] + 1)
            dp.append(dp_i)
            i += 1
        return dp[-1]