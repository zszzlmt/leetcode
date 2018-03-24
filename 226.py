# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __traval__(self, node):
        if not node:
            return None
        base = TreeNode(node.val)
        if node.left:
            base.right = self.__traval__(node.left)
        if node.right:
            base.left = self.__traval__(node.right)
        return base

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.__traval__(root)
