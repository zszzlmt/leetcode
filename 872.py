# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __traval__(self, node, leaf):
        if node is None:
            return leaf
        if node.left is None and node.right is None:
            return leaf + [node.val]
        else:
            if node.left:
                leaf = self.__traval__(node.left, leaf)
            if node.right:
                leaf = self.__traval__(node.right, leaf)
        return leaf

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.__traval__(root1, []) == self.__traval__(root2, [])