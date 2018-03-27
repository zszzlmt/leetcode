class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        elif len(nums) == 1:
            return 1
        dp = list()
        dp.append(1)
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                dp.append(dp[-1] + 1)
            else:
                dp.append(1)
        return max(dp)
