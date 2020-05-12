# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    path = None
    
    def __traval__(self, node, t):
        if node.left is None and node.right is None:
            t.append(str(node.val))
            self.path.append('->'.join(t))
            return
        tmp = t + [str(node.val)]
        if node.left is not None:
            self.__traval__(node.left, tmp)
        tmp = t + [str(node.val)]
        if node.right is not None:
            self.__traval__(node.right, tmp)
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return list()
        self.path = list()
        self.__traval__(root, [])
        return self.path