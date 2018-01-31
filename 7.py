class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        neg = 0
        if x < 0:
            neg = 1
        res = 0
        base = 10
        x = abs(x)
        while x != 0:
            i = int(x % 10)
            x = int(x / 10)
            res *= base
            res += i
        if neg == 1:
            res *= (-1)
        if res > 2 ** 31 - 1 or res < - (2 ** 31):
            return 0
        return res