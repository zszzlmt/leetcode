class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        valid = 0
        for idx in range(len(nums)):
            if nums[idx] != pre:
                pre = nums[idx]
                nums[valid], nums[idx] = nums[idx], nums[valid]
                valid += 1
        return valid
