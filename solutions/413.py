class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return 0

        diff = [A[idx] - A[idx - 1] for idx in range(1, len(A))]
        part_lengths = list()

        base = 0
        pre_diff = diff[0]
        for idx in range(len(A) - 1):
            if diff[idx] != pre_diff:
                if idx - base >= 2:
                    part_lengths.append(idx - base)
                pre_diff = diff[idx]
                base = idx
        if len(A) - 1 - base >= 2:
            part_lengths.append(len(A) - 1 - base)

        res = 0
        for length in part_lengths:
            res += (length) * (length - 1) // 2

        return res
