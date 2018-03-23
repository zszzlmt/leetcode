class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not len(A):
            return -1
        base = A
        cnt = 1
        if base.find(B) != -1:
            return cnt
        while len(base) < 2 * len(B):
            base += A
            cnt += 1
            if base.find(B) != -1:
                return cnt
        return -1
