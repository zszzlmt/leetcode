class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        t = x
        l = 0
        while t != 0:
            t = int(t / 10)
            l += 1
        t = x
        for idx in range(int(l / 2)):
            a = t % 10
            b = int(t / (10 ** (l - 2 * idx - 1))) % 10
            if a != b:
                return False
            t -= b * (10 ** (l - 2 * idx - 1))
            t = int(t / 10)
        return True