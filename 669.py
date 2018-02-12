# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    l = None
    r = None

    def __traval__(self, r):
        if r is None:
            return None
        if self.l <= r.val <= self.r:
            r.left = self.__traval__(r.left)
            r.right = self.__traval__(r.right)
            return r
        else:
            left_node = self.__traval__(r.left)
            right_ndoe = self.__traval__(r.right)
            if left_node:
                return left_node
            elif right_ndoe:
                return right_ndoe

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        self.l = L
        self.r = R
        return self.__traval__(root)