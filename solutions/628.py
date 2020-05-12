class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = list()
        neg = list()
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(abs(num))
        pos_max = 0
        neg_max = 0
        res = 0
        pos.sort(reverse=True)
        neg.sort(reverse=True)
        if len(pos) >= 3:
            pos_max = pos[0] * pos[1] * pos[2]
        if len(neg) >= 2 and len(pos) >= 1:
            neg_max = neg[0] * neg[1] * pos[0]
        if not pos_max and not neg_max:
            if len(neg) >= 3:
                return -(neg[-1] * neg[-2] * neg[-3])
        return max(res, pos_max, neg_max)