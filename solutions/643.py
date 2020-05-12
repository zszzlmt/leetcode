class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 1:
            return max(nums)
        slide_sum = sum(nums[:k])
        max_sum = slide_sum
        for idx in range(1, len(nums) - k + 1):
            slide_sum += nums[idx + k - 1] - nums[idx - 1]
            if slide_sum > max_sum:
                max_sum = slide_sum
        return float(max_sum) / k

