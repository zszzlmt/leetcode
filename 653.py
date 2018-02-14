# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    d = dict()
    k = None

    def __traval__(self, n):
        if n is None:
            return False
        if self.k - n.val in self.d:
            return True
        if n.val not in self.d:
            self.d[n.val] = True
        left_bool = self.__traval__(n.left)
        right_bool = self.__traval__(n.right)
        return left_bool or right_bool

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.d = dict()
        self.k = k
        return self.__traval__(root)
