class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        all = (l - 1) * l // 2 + l
        return all - sum(nums)
