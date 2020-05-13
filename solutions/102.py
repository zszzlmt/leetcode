# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return list()
        queue = list()
        queue.append(root)
        result = [[root.val]]
        while len(queue) > 0:
            queue_next_level = list()
            result_next_level = list()
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue_next_level.append(node.left)
                    result_next_level.append(node.left.val)
                if node.right is not None:
                    queue_next_level.append(node.right)
                    result_next_level.append(node.right.val)
            if len(result_next_level) != 0:
                result.append(result_next_level)
            queue = queue_next_level

        return result