# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __traval__(self, node):
        if node is None:
            return [0, 0]
        left = self.__traval__(node.left)
        right = self.__traval__(node.right)
        return [node.val + left[1] + right[1], max(left) + max(right)]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        value = self.__traval__(root)
        return max(value)
