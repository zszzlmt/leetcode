class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = list()
        while S:
            pos = 1
            while set(S[:pos]) & set(S[pos:]):
                pos += 1
            res.append(pos)
            S = S[pos:]
        return res