# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __traval__(self, node):
        if node.left is None and node.right is None:
            if node.val == 1:
                return True
            else:
                return False
        else:
            left_res = False
            right_res = False
            if node.left is not None:
                left_res = self.__traval__(node.left)
            if node.right is not None:
                right_res = self.__traval__(node.right)
            if not left_res:
                node.left = None
            if not right_res:
                node.right = None
            if not node.left and not node.right and node.val == 0:
                return False
            else:
                return True


    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.__traval__(root)
        if not res:
            return None
        else:
            return root
