import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        divisor = [1]
        for i in range(2, int(math.sqrt(num)) + 1):
            d, m = divmod(num, i)
            if not m:
                divisor.append(i + d)
        return sum(divisor) == num
