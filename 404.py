# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    leave_sum = None

    def __traval__(self, n, flag):
        if n is None:
            return
        if n.left is None and n.right is None:
            if flag == 0:
                self.leave_sum += n.val
            return
        if n.left:
            self.__traval__(n.left, 0)
        if n.right:
            self.__traval__(n.right, 1)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.leave_sum = 0
        self.__traval__(root, -1)
        return self.leave_sum