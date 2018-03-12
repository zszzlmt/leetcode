# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return list()
        res = list()
        stack = list()
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not len(stack):
                return res
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
