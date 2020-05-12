class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        d = dict()
        for idx in range(l):
            if nums[idx] not in d:
                d[nums[idx]] = 0
            else:
                return True
        return False
