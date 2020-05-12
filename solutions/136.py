class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        res = 0
        for idx in range(l):
            res = res ^ nums[idx]
        return res