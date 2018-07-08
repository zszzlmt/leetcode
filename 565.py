class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        res = 0
        for idx in range(len(nums)):
            val = nums[idx]
            cnt = 0
            if val not in s:
                s.add(val)
                cnt += 1
                while nums[val] not in s:
                    cnt += 1
                    val = nums[val]
                    s.add(val)
                if cnt > res:
                    res = cnt
        return res