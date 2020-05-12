import bisect


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = list()
        res = [-1] * len(nums)
        for idx in range(len(nums)) * 2:
            item = nums[idx]
            while stack and item > nums[stack[-1]]:
                res[stack.pop()] = item
            stack.append(idx)
        return res

        # if not nums:
        #     return list()
        # res = ['?'] * len(nums)
        # max_later = None
        # max_all = max(nums)
        # for idx in range(len(nums) - 1, -1, -1):
        #     item = nums[idx]
        #     if item == max_all:
        #         res[idx] = -1
        #         max_later = item
        #         continue
        #     if max_later is None or max_later <= item:
        #         max_later = item
        #         for idxx in range(len(nums)):
        #             if nums[idxx] > item:
        #                 res[idx] = nums[idxx]
        #                 break
        #     else:
        #         for idxx in range(idx + 1, len(nums)):
        #             if nums[idxx] > item:
        #                 res[idx] = nums[idxx]
        #                 break
        # return res

        # if not nums:
        #     return list()
        # res = ['?'] * len(nums)
        # max_value = nums[-1]
        # values_set = set()
        # values_set.add(nums[-1])
        # maximum = max(nums)
        # for idx in range(len(nums) - 1, -1, -1):
        #     item = nums[idx]
        #     if item == maximum:
        #         res[idx] = -1
        #         if item not in values_set:
        #             values_set.add(item)
        #             max_value = item
        #         continue
        #     if item in values_set:
        #         if item != max_value:
        #             for idxx in range(idx + 1, len(nums)):
        #                 if nums[idxx] > item:
        #                     res[idx] = nums[idxx]
        #                     break
        #     else:
        #         values_set.add(item)
        #         if item >= max_value:
        #             max_value = item
        #         else:
        #             for idxx in range(idx + 1, len(nums)):
        #                 if nums[idxx] > item:
        #                     res[idx] = nums[idxx]
        #                     break
        # for idx in range(len(nums)):
        #     if res[idx] == '?':
        #         item = nums[idx]
        #         for idxx in range(idx):
        #             if nums[idxx] > item:
        #                 res[idx] = nums[idxx]
        #                 break
        # return res

        # table = list(set(nums))
        # pos = {table[idx]: idx for idx in range(len(table))}

        # if not nums:
        #     return list()
        # res = list()
        # max_value = max(nums)
        # for idx in range(len(nums)):
        #     item = nums[idx]
        #     if item == max_value:
        #         res.append(-1)
        #         continue
        #     idxx = idx + 1
        #     flag = False
        #     while idxx != idx:
        #         if idxx >= len(nums):
        #             idxx = 0
        #         if nums[idxx] > item:
        #             res.append(nums[idxx])
        #             flag = True
        #             break
        #         idxx += 1
        # return res
