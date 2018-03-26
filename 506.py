import copy


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = copy.deepcopy(nums)
        ranks.sort(reverse=True)
        res = list()
        for item in nums:
            rank = ranks.index(item) + 1
            if rank == 1:
                res.append('Gold Medal')
                continue
            elif rank == 2:
                res.append('Silver Medal')
                continue
            elif rank == 3:
                res.append('Bronze Medal')
                continue
            else:
                res.append(str(rank))
                continue
        return res
