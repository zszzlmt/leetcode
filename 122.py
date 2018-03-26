class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([prices[idx] - prices[idx - 1] if prices[idx] > prices[idx - 1] else 0 for idx in range(1, len(prices))])
