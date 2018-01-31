class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = []
        conv = {"I":1, "X":10, "C":100, "M":1000, "V":5, "L":50, "D":500}
        res = 0
        for idx in range(len(s)):
            num.append(conv[s[idx]])
        for idx in range(len(num)):
            val = num[idx]
            if idx == len(num) - 1:
                res += val
            elif val < num[idx + 1]:
                res -= val
            else:
                res += val
        return res