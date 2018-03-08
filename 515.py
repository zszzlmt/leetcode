# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = list()
        res = list()
        queue.append(root)
        while len(queue):
            values = list()
            next_queue = list()
            while len(queue):
                item = queue[0]
                del queue[0]
                values.append(item.val)
                if item.left:
                    next_queue.append(item.left)
                if item.right:
                    next_queue.append(item.right)
            res.append(max(values))
            queue = next_queue
        return res


