class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d_freq = dict()
        d_idx = dict()
        max_freq = -1
        max_item = list()
        for idx in range(len(nums)):
            item = nums[idx]
            if item not in d_freq:
                d_freq[item] = 1
                d_idx[item] = [idx]
                if d_freq[item] > max_freq:
                    max_freq = d_freq[item]
                    max_item = [item]
                elif d_freq[item] == max_freq:
                    max_item.append(item)
            else:
                d_freq[item] += 1
                d_idx[item].append(idx)
                if d_freq[item] > max_freq:
                    max_freq = d_freq[item]
                    max_item = [item]
                elif d_freq[item] == max_freq:
                    max_item.append(item)
        if max == 1:
            return 1
        min_res = float('inf')
        for idx in range(len(max_item)):
            if max(d_idx[max_item[idx]]) - min(d_idx[max_item[idx]]) + 1 < min_res:
                min_res = max(d_idx[max_item[idx]]) - min(d_idx[max_item[idx]]) + 1
        return min_res
