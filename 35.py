class Solution(object):

    def __bi_search__(self, t, l, r, target):
        if r == l:
            if target == t[r]:
                return 0
            elif target < t[r]:
                if r == 0:
                    return 0
                else:
                    return r - 1
            else:
                return r + 1
        elif r - l == 1:
            if target == t[l]:
                return l
            elif target == t[r]:
                return r
            elif target > t[r]:
                return r + 1
            elif target < t[l]:
                if l == 0:
                    return 0
                else:
                    return l - 1
            else:
                return r
        else:
            m = (r + l) // 2
            if t[m] == target:
                return m
            elif t[m] > target:
                return self.__bi_search__(t, l, m, target)
            else:
                return self.__bi_search__(t, m, r, target)


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        return self.__bi_search__(nums, 0, l - 1, target)