import copy


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        for item in findNums:
            pos = nums.index(item)
            next_greater = -1
            for idx in range(pos + 1, len(nums)):
                if nums[idx] > item:
                    next_greater = nums[idx]
                    break
            res.append(next_greater)
        return res