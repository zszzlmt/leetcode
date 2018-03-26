class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        max_num = max(nums)
        base = sum([max_num - nums[idx] for idx in range(l)])
        while True:
            if not base % (l - 1):
                return base / (l - 1)
            base += l
