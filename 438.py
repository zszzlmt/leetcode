from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls = len(s)
        lp = len(p)
        tar = Counter(p)
        count = Counter(s[:lp - 1])
        res = list()
        for idx in range(lp - 1, ls):
            count[s[idx]] += 1
            if count == tar:
                res.append(idx - lp + 1)
            count[s[idx - lp + 1]] -= 1
            if not count[s[idx - lp + 1]]:
                del count[s[idx - lp + 1]]
        return res
