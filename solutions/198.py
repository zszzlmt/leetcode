class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = list()
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for idx in range(2, len(nums)):
            dp.append(max(dp[-2] + nums[idx], dp[-1]))
        return dp[-1]
