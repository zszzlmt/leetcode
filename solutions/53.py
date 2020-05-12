class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        special_case = max(nums)
        while len(nums) and nums[0] < 0:
            nums.pop(0)
        while len(nums) and nums[-1] < 0:
            nums.pop()
        if not len(nums):
            return special_case
        res = 0
        pre_sum = 0
        for idx in range(len(nums)):
            if pre_sum + nums[idx] > 0:
                pre_sum += nums[idx]
                if pre_sum > res:
                    res = pre_sum
            else:
                pre_sum = 0
        return res