class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = list()
        dp.append(0)
        dp.append(0)
        for idx in range(2, len(cost) + 1):
            dp.append(min(dp[idx - 1] + cost[idx - 1], dp[idx - 2] + cost[idx - 2]))
        return dp[-1]
