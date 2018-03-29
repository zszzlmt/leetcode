import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (-1 + int(math.sqrt(1 + 8 * n))) // 2
