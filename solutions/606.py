class Solution:

    def construct(self, node):
        if node is None:
            return ""
        else:
            if node.left is None and node.right is None:
                return str(node.val)
            elif node.left is None and node.right is not None:
                return str(node.val) + "()(" + self.construct(node.right) + ")"
            elif node.left is not None and node.right is None:
                return str(node.val) + "(" + self.construct(node.left) + ")"
            else:
                return str(node.val) + "(" + self.construct(node.left) + ")(" + self.construct(node.right) + ")"

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.construct(t)
