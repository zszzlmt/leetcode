class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        sum = 0
        idx = 1
        while True:
            sum += idx
            if sum == num:
                return True
            elif sum > num:
                return False
            else:
                idx += 2