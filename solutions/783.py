# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    t = None

    def __traval__(self, n):
        if n == None:
            return
        else:
            self.t.append(n.val)
            self.__traval__(n.left)
            self.__traval__(n.right)
            return

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.t = list()
        self.__traval__(root)
        self.t.sort()
        min = None
        for idx in range(len(self.t) - 1):
            if min == None or self.t[idx + 1] - self.t[idx] < min:
                min = self.t[idx + 1] - self.t[idx]
        return min
