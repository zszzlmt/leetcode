from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = [value if value % 2 == 0 else value - 1 for _, value in dict(Counter(s)).items()]
        if len(tmp) == 1:
            return len(s)
        for _, value in dict(Counter(s)).items():
            if value % 2 != 0:
                return sum(tmp) + 1
        return sum(tmp)

