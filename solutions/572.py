# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __check__(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val != t.val:
            return False
        left_bool = False
        right_bool = False
        left_bool = self.__check__(s.left, t.left)
        right_bool = self.__check__(s.right, t.right)
        return left_bool and right_bool

    def __traval__(self, s, t, val):
        if s is None:
            return False
        if s.val == val:
            if self.__check__(s, t):
                return True
        left_bool = False
        right_bool = False
        if s.left:
            left_bool = self.__traval__(s.left, t, val)
        if s.right:
            right_bool = self.__traval__(s.right, t, val)
        return left_bool or right_bool


    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.__traval__(s, t, t.val)
