# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    sums = None

    def __traval__(self, n):
        if n is None:
            return 0
        left = 0
        right = 0
        if n.left:
            left = self.__traval__(n.left)
        if n.right:
            right = self.__traval__(n.right)
        self.sums += abs(left - right)
        return n.val + left + right

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums = 0
        self.__traval__(root)
        return self.sums
