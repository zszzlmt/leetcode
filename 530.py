# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    vals = None

    def __traval__(self, node):
        if node is None:
            return
        self.vals.append(node.val)
        self.__traval__(node.left)
        self.__traval__(node.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = list()
        self.__traval__(root)
        self.vals.sort()
        return min([self.vals[idx] - self.vals[idx - 1] for idx in range(1, len(self.vals))])
