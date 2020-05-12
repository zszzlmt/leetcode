import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        table = set([idx ** 2 for idx in range(int(math.sqrt(c)) + 1)])
        for a in table:
            if c - a in table:
                return True
        return False
