from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        ss = set(s)
        for c in s:
            d[c] += 1
            if d[c] == 2:
                ss.remove(c)
        if len(ss):
            for idx in range(len(s)):
                if s[idx] in ss:
                    return idx
        else:
            return -1