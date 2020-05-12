class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = abs(n)
        res = 1
        while n != 0:
            t = n % 2
            n = n // 2
            if t != 0:
                res *= x
            x = x ** 2
        return res
