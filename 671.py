# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    values = None

    def __traval__(self, node):
        if node is None:
            return
        self.__traval__(node.left)
        self.__traval__(node.right)
        self.values.add(node.val)
        return

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.values = set()
        self.__traval__(root)
        values = list(self.values)
        values.sort()
        if len(values) < 2:
            return -1
        return values[1]
