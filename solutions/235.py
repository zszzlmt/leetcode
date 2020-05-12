# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy


class Solution(object):

    ppath = None
    qpath = None

    def __traval__(self, node, path, p, q, foundp, foundq):
        if foundp and foundq:
            return
        if node is None:
            return
        if node == p:
            foundp = True
            self.ppath = path + [node]
        if node == q:
            foundq = True
            self.qpath = path + [node]
        self.__traval__(node.left, path + [node], p, q, foundp, foundq)
        self.__traval__(node.right, path + [node], p, q, foundp, foundq)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.__traval__(root, [], p, q, False, False)
        res = None
        for idx in range(min(len(self.ppath), len(self.qpath))):
            if self.ppath[idx] != self.qpath[idx]:
                res = self.ppath[idx - 1]
                break
        else:
            if len(self.ppath) <= len(self.qpath):
                return self.ppath[-1]
            else:
                return self.qpath[-1]
        return res
