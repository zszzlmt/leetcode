class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        valid = 2
        while valid < n:
            dp.append(dp[-1] + dp[-2])
            valid += 1
        return dp[n]