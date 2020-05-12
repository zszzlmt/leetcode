class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            pos = abs(nums[idx]) - 1
            nums[pos] = -abs(nums[pos])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]