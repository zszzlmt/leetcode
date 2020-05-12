# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    rec = None

    def __dfs__(self, t, now):
        if t != None:
            now += 1
            if t.left == None and t.right == None:
                if self.rec == None or self.rec > now:
                    self.rec = now
                return
            self.__dfs__(t.left, now)
            self.__dfs__(t.right, now)
        else:
            return

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rec = None
        self.__dfs__(root, 0)
        if self.rec == None:
            return 0
        return self.rec