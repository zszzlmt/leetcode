class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l:
            return -1
        total = sum(nums)
        left = 0
        right = total - nums[0]
        for idx in range(l):
            if left == right:
                return idx
            if idx != l - 1:
                left += nums[idx]
                right -= nums[idx + 1]
        return -1