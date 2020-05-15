class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(nums) - 1
        while head < tail:
            sum_ = nums[head] + nums[tail]
            if sum_ < target:
                head += 1
            elif sum_ > target:
                tail -= 1
            else:
                return [nums[head], nums[tail]]
        return []
            