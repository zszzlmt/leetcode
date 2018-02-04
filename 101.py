# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __check__(self, l, r):
        if l == None and r == None:
            return True
        elif (l == None and r != None) or (l != None and r == None):
            return False
        else:
            if l.val != r.val:
                return False
            if not self.__check__(l.left, r.right):
                return False
            if not self.__check__(l.right, r.left):
                return False
            return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.__check__(root.left, root.right)