# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    p_path = None
    q_path = None

    def dfs(self, node, p, q, path):
        if node == p:
            self.p_path = path + [node]
        if node == q:
            self.q_path = path + [node]
        if self.p_path is not None and self.q_path is not None:
            return
        if node.left is not None:
            self.dfs(node.left, p, q, path+[node])
        if node.right is not None:
            self.dfs(node.right, p, q, path+[node])
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root, p, q, [])
        shorter, longer = (self.p_path, self.q_path) if len(self.p_path) < len(self.q_path) else (self.q_path, self.p_path)
        for idx in range(len(shorter)-1, -1, -1):
            if shorter[idx] == longer[idx]:
                return shorter[idx]