class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = dict()
        while True:
            tmp = n
            val = 0
            while tmp != 0:
                val += (tmp % 10) ** 2
                tmp = tmp // 10
            if val == 1:
                return True
            elif val in d:
                return False
            else:
                d[val] = 0
                n = val