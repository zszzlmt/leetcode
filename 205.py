class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)  # same length
        if l == 0:
            return True
        d1 = dict()
        d2 = dict()
        for idx in range(l):
            if s[idx] not in d1:
                d1[s[idx]] = t[idx]
            if t[idx] not in d2:
                d2[t[idx]] = s[idx]
            if d1[s[idx]] != t[idx] or d2[t[idx]] != s[idx]:
                return False
        return True
