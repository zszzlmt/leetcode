class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = [0]
        min_price = prices[0]
        for price in prices[1:]:
            profit.append(price - min_price)
            if price < min_price:
                min_price = price
        return max(profit)
