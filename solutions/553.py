class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        if len(nums) <= 2:
            return '/'.join(nums)
        return nums[0] + '/(' + '/'.join(nums[1:]) + ')'
