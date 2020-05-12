# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while True:
            m = (l + r) // 2
            rtn = guess(m)
            if not rtn:
                return m
            elif rtn == 1:
                if l != m:
                    l = m
                else:
                    l += 1
            else:
                if r != m:
                    r = m
                else:
                    r -= 1


