# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    max_len = None

    def __traval__(self, node, calculating, l, pre):
        if self.max_len is None or l > self.max_len:
            self.max_len = l
        if calculating:
            if node.val == pre:
                if node.left:
                    self.__traval__(node.left, calculating, l + 1, pre)
                if node.right:
                    self.__traval__(ndoe.right, calculating, l + 1, pre)
            else:



    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
