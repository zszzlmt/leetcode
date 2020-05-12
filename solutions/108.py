# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    table = None

    def __traval__(self, l, r):
        if l >= r:
            return None
        m = (l + r) // 2
        node = TreeNode(self.table[m])
        node.left = self.__traval__(l, m)
        node.right = self.__traval__(m + 1, r)
        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if not l:
            return None
        self.table = nums
        return self.__traval__(0, l)
