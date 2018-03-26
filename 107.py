# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = list()
        queue.append(root)
        res = list()
        while len(queue):
            level = list()
            next_queue = list()
            while len(queue):
                node = queue.pop(0)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                level.append(node.val)
            queue = next_queue
            res.append(level)
        return res[::-1]
