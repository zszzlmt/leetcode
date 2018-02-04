# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    rec = 0

    def __dfs__(self, t, now):
        if t != None:
            now += 1
        else:
            if now > self.rec:
                self.rec = now
            return
        self.__dfs__(t.left, now)
        self.__dfs__(t.right, now)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rec = 0
        self.__dfs__(root, 0)
        return self.rec
