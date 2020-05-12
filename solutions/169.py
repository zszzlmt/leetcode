class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        d = dict()
        max = 0
        max_id = -1
        for idx in range(l):
            if nums[idx] not in d:
                d[nums[idx]] = 1
                if max < 1:
                    max = 1
                    max_id = nums[idx]
            else:
                d[nums[idx]] += 1
                if max < d[nums[idx]]:
                    max = d[nums[idx]]
                    max_id = nums[idx]
        return max_id