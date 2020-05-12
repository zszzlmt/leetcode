class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        pos = [idx for idx in range(len(s) - 1) if s[idx] != s[idx + 1]]
        res = 0
        for idx in pos:
            offset = 0
            while True:
                if idx - offset < 0 or idx + 1 + offset >= len(s):
                    break
                if s[idx - offset] == s[idx] and s[idx - offset] != s[idx + 1 + offset]:
                    res += 1
                    offset += 1
                    continue
                else:
                    break
        return res