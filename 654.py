# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    table = None
    
    def __generate__(self, left, right):
        if left == right:
            return None
        elif left + 1 == right:
            return TreeNode(self.table[left])
        else:
            max, idx_max = self.__max__(left, right)
            node_left = None
            node_right = None
            if left != idx_max:
                node_left = self.__generate__(left, idx_max)
            if idx_max != right:
                node_right = self.__generate__(idx_max + 1, right)
            node = TreeNode(max)
            node.left = node_left
            node.right = node_right
            return node
    
    def __max__(self, left, right):
        max = None
        idx_max = -1
        for idx in range(left, right):
            if max == None or max < self.table[idx]:
                max = self.table[idx]
                idx_max = idx
        return max, idx_max
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        self.table = nums
        return self.__generate__(0, l)