class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A') - 1
        res = 0
        for item in s:
            res *= 26
            res += ord(item) - base
        return res
