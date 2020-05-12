class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not len(g) or not len(s):
            return 0
        g.sort()
        s.sort()
        child_idx = 0
        res = 0
        for cake in s:
            if cake >= g[child_idx]:
                res += 1
                child_idx += 1
            if child_idx >= len(g):
                break
        return res
