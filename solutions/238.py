class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        product = 1
        if len(nums) <= 1:
            return nums
        for idx in range(1, len(nums)):
            product *= nums[idx - 1]
            res.append(product)
        product = 1
        for idx in range(len(nums) - 2, -1, -1):
            product *= nums[idx + 1]
            res[idx] *= product
        return res
