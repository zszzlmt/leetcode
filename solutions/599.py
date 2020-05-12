class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set_1 = set(list1)
        set_2 = set(list2)
        res = list()
        min_sum = None
        for idx_1 in range(len(list1)):
            if list1[idx_1] in set_2:
                idx_sum = idx_1 + list2.index(list1[idx_1])
                if min_sum is None:
                    res.append(list1[idx_1])
                    min_sum = idx_sum
                    continue
                elif min_sum == idx_sum:
                    res.append(list1[idx_1])
                    continue
                elif min_sum > idx_sum:
                    min_sum = idx_sum
                    res = list1[idx_1]
                    continue
        return res
