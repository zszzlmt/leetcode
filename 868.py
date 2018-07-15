class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        t = [int(item) for item in list(bin(N)[2:])]
        pos = list()
        for idx in range(len(t)):
            if t[idx]:
                pos.append(idx)
        res = [pos[idx] - pos[idx - 1] for idx in range(1, len(pos))]
        if not len(res):
            return 0
        else:
            return max(res)
