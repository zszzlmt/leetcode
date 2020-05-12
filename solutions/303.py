class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.t = [0]
        for idx in range(len(nums)):
            self.t.append(self.t[-1] + nums[idx])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.t[j + 1] - self.t[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)