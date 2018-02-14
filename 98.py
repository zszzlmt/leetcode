# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    pos_inf = float('inf')
    neg_inf = float('-inf')

    def __check__(self, n, min_value, max_value):
        if n is None:
            return True
        if not min_value < n.val < max_value:
            return False
        else:
            return self.__check__(n.left, min_value, n.val) and self.__check__(n.right, n.val, max_value)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.__check__(root, self.neg_inf, self.pos_inf)


