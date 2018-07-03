class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        s = set()
        cnt = 0
        for idx in range(len(A)):
            if A[idx] != B[idx]:
                cnt += 1
                if cnt == 1:
                    s.add(A[idx])
                    s.add(B[idx])
                elif cnt == 2:
                    if A[idx] not in s or B[idx] not in s:
                        return False
                else:
                    return False
        if cnt == 2:
            return True
        if cnt == 0:
            from collections import Counter
            c = Counter(A)
            for _, v in c.items():
                if v >= 2:
                    return True
        return False
