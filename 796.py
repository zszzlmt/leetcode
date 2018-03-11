class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        l1 = len(A)
        l2 = len(B)
        if l1 != l2:
            return False
        tar = A[0]
        flag = False
        for i in range(l2):
            if not flag:
                if tar == B[i]:
                    for j in range(l2):
                        idx = (i + j) % l2
                        if B[idx] != A[j]:
                            break
                        if j == l2 - 1:
                            flag = True
        return flag
