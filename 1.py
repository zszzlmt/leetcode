class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        d = dict()
        for i in xrange(len(nums)):
            value = nums[i]
            if target - value in d:
                res.append(d[target - value])
                res.append(i)
                return res
            d[value] = i