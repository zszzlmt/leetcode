# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __check__(self, p, q):
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        else:
            if p.val != q.val:
                return False
            if not self.__check__(p.left, q.left):
                return False
            if not self.__check__(p.right, q.right):
                return False
            return True

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.__check__(p, q)