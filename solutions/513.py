# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    depth = -1
    val = None

    def __left_most__(self, n, cnt):
        if n is None:
            return
        self.__left_most__(n.left, cnt + 1)
        self.__left_most__(n.right, cnt + 1)
        if cnt > self.depth:
            self.val = n.val
            self.depth = cnt

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.__left_most__(root, 0)
        return self.val
