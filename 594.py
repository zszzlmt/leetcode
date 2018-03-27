from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        res = [0]
        for key, value in count.items():
            str_len_1 = value
            str_len_2 = value
            if key - 1 in count:
                str_len_1 += count[key - 1]
            if key + 1 in count:
                str_len_2 += count[key + 1]
            if str_len_1 == str_len_2:
                continue
            res.append(max(str_len_1, str_len_2))
        return max(res)
