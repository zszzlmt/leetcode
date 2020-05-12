# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    max_path = -1

    def __traval__(self, n):
        if n is None:
            return 0
        l = self.__traval__(n.left)
        r = self.__traval__(n.right)
        if l + r > self.max_path:
            self.max_path = l + r
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.max_path = -1
        self.__traval__(root)
        return self.max_path
