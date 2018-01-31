class Solution(object):
    res = []

    def generate(self, l, travel, left):
        if left == 0:
            self.res.append(l)
            return
        for idx in range(len(travel)):
            if travel[idx] == 0:
                travel[idx] = 1
                self.generate(l + [self.nums[idx]], travel, left - 1)
                travel[idx] = 0

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l == 0:
            return []
        self.nums = nums
        self.res = []
        travel = [0] * l
        for idx in range(l):
            if travel[idx] == 0:
                travel[idx] = 1
                self.generate([nums[idx]], travel, l - 1)
                travel[idx] = 0
        return self.res