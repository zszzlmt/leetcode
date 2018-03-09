# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    values = None
    sums = None

    def __traval_get__(self, n):
        if n is None:
            return
        self.values.append(n.val)
        if n.left:
            self.__traval_get__(n.left)
        if n.right:
            self.__traval_get__(n.right)

    def __traval_update__(self, n):
        if n is None:
            return
        n.val += self.sums[n.val]
        if n.left:
            self.__traval_update__(n.left)
        if n.right:
            self.__traval_update__(n.right)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return []
        self.values = list()
        self.__traval_get__(root)
        self.values.sort()
        self.sums = {self.values[idx]: sum(self.values[idx + 1:]) for idx in range(len(self.values) - 1)}
        self.sums[self.values[-1]] = 0
        self.__traval_update__(root)
        return root
