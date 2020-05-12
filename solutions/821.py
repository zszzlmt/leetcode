class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [10001 for _ in range(len(S))]
        base_forward = S.find(C)
        base_backward = len(S) - 1 - S[::-1].find(C)

        base = base_forward
        for idx in range(base, len(S)):
            if S[idx] == C:
                res[idx] = 0
                base = idx
            else:
                res[idx] = min(res[idx], idx - base)

        base = base_backward
        for idx in range(base, -1, -1):
            if S[idx] == C:
                res[idx] = 0
                base = idx
            else:
                res[idx] = min(res[idx], base - idx)

        return res
