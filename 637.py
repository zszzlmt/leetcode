# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        res = list()
        queue = list()
        queue_next_level = list()
        queue.append(root)
        level_sum = 0
        level_cnt = 0
        while len(queue):
            node = queue[0]
            del queue[0]
            level_sum += node.val
            level_cnt += 1
            if node.left:
                queue_next_level.append(node.left)
            if node.right:
                queue_next_level.append(node.right)
            if not len(queue):
                queue = queue_next_level
                queue_next_level = list()
                res.append(float(level_sum) / level_cnt)
                level_sum = 0
                level_cnt = 0
        return res