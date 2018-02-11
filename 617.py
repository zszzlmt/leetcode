# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __traval__(self, t1, t2):
        if t1 == None and t2 == None:
            return None
        elif t1 == None:
            node = TreeNode(t2.val)
            node_left = self.__traval__(None, t2.left)
            node_right = self.__traval__(None, t2.right)
            node.left = node_left
            node.right = node_right
            return node
        elif t2 == None:
            node = TreeNode(t1.val)
            node_left = self.__traval__(t1.left, None)
            node_right = self.__traval__(t1.right, None)
            node.left = node_left
            node.right = node_right
            return node
        else:
            node = TreeNode(t1.val + t2.val)
            node_left = self.__traval__(t1.left, t2.left)
            node_right = self.__traval__(t1.right, t2.right)
            node.left = node_left
            node.right = node_right
            return node
    
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.__traval__(t1, t2)
        